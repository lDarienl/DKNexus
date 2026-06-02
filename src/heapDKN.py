"""
Simulacion de memoria manual (heap + direcciones) para el interprete DKNexus.

Rediseno para Machine Learning / arreglos grandes:

- El heap YA NO esta limitado rigidamente a 1024 slots. Por defecto es DINAMICO
  (``max_slots=None``): crece segun se necesite para soportar vectores y
  matrices grandes. Aun asi se puede fijar un tope opcional para pruebas.

- Las matrices ya no se guardan como listas de listas dentro del heap, sino que
  se delegan al binding de C (``dknumpyDKN``): se reserva un BLOQUE CONTIGUO de
  memoria con ``malloc`` y el heap REGISTRA el puntero de ese bloque. La lectura
  reconstruye la lista de listas para el resto del interprete.
"""

import matrixDKN
import dknumpyDKN


class DKNMemoryError(Exception):
    """El heap no puede alojar mas datos (tope opcional de slots agotado)."""


class HeapManager:
    """
    Memoria RAM simulada: direcciones hexadecimales -> valor / bloque contiguo.

    - Escalares, strings y listas genericas viven en ``self.ram``.
    - Matrices viven en ``self.blocks`` como bloques contiguos en C
      (``dknumpyDKN.DKNMatrix``), y su puntero se registra en ``self.pointers``.
    """

    def __init__(self, max_slots: int | None = None):
        # max_slots=None => heap dinamico (sin limite rigido). Un entero fija un tope.
        self.max_slots = max_slots
        self.used_slots = 0
        self.ram: dict[str, object] = {}
        self.blocks: dict[str, "dknumpyDKN.DKNMatrix"] = {}
        self.pointers: dict[str, int] = {}
        self.cell_weight: dict[str, int] = {}
        self._next_id = 0

    def weight(self, value: object, depth: int = 0) -> int:
        """Peso en slots: escalar = 1, listas/matrices = suma recursiva de elementos."""
        if depth > 32:
            return 1
        if value is None or isinstance(value, (bool, int, float)):
            return 1
        if isinstance(value, str):
            return max(1, len(value))
        if isinstance(value, list):
            if not value:
                return 1
            total_weight = 0
            for element in value:
                total_weight += self.weight(element, depth + 1)
            return max(1, total_weight)
        if isinstance(value, dict):
            if not value:
                return 1
            total_weight = 0
            for k, v in value.items():
                total_weight += self.weight(k, depth + 1) + self.weight(v, depth + 1)
            return max(1, total_weight)
        return 1

    def _clone_for_store(self, value: object) -> object:
        """Copia superficial para que mutaciones externas no corrompan el heap."""
        if isinstance(value, list):
            return [x for x in value]
        if isinstance(value, dict):
            return {k: v for k, v in value.items()}
        return value

    def _check_capacity(self, w: int) -> None:
        """Solo aplica si hay un tope explicito (max_slots no es None)."""
        if self.max_slots is None:
            return
        if w > self.max_slots:
            raise DKNMemoryError(
                f"Objeto demasiado grande ({w} slots) para el tope del heap ({self.max_slots})."
            )
        if self.used_slots + w > self.max_slots:
            raise DKNMemoryError(
                f"Heap lleno: se requieren {w} slots libres pero solo quedan "
                f"{self.max_slots - self.used_slots} de {self.max_slots}."
            )

    def allocate(self, value: object) -> str:
        """Reserva memoria y devuelve la direccion (puntero)."""
        w = self.weight(value)
        self._check_capacity(w)

        self._next_id += 1
        addr = f"0x{self._next_id:03X}"

        if matrixDKN.is_matrix(value):
            # Bloque CONTIGUO en C (malloc) + registro del puntero.
            matrix = dknumpyDKN.DKNMatrix.from_list(value)
            self.blocks[addr] = matrix
            self.pointers[addr] = matrix.block.ptr_address()
        else:
            self.ram[addr] = self._clone_for_store(value)

        self.cell_weight[addr] = w
        self.used_slots += w
        return addr

    def read(self, addr: str) -> object:
        if addr in self.blocks:
            # Reconstruye la lista de listas desde el bloque contiguo.
            return self.blocks[addr].to_list()
        if addr in self.ram:
            return self.ram[addr]
        raise KeyError(addr)

    def free(self, addr: str | None) -> None:
        """Libera la celda asociada a una direccion (GC basico por ambito)."""
        if addr is None:
            return
        if addr in self.blocks:
            self.blocks[addr].free()  # free() de C en modo nativo
            self.blocks.pop(addr, None)
            self.pointers.pop(addr, None)
        elif addr in self.ram:
            self.ram.pop(addr, None)
        else:
            return
        w = self.cell_weight.pop(addr, 0)
        self.used_slots -= w

    def dump_state(self) -> str:
        """Representacion amigable del estado del heap."""
        limite = "dinamico (malloc)" if self.max_slots is None else f"{self.max_slots} slots"
        lines = [
            f"Backend numerico: {dknumpyDKN.backend_name()}",
            f"Heap usage: {self.used_slots} slots usados | limite: {limite}",
            f"Cells: {len(self.ram) + len(self.blocks)} "
            f"(escalares/listas: {len(self.ram)}, bloques contiguos: {len(self.blocks)})",
        ]
        all_addrs = sorted(set(self.ram) | set(self.blocks))
        for addr in all_addrs:
            w = self.cell_weight.get(addr, 0)
            if addr in self.blocks:
                mat = self.blocks[addr]
                ptr = self.pointers.get(addr, 0)
                lines.append(
                    f"{addr} [w={w}] -> matriz {mat.rows}x{mat.cols} "
                    f"@bloque_C=0x{ptr:X} -> {repr(mat.to_list())}"
                )
            else:
                lines.append(f"{addr} [w={w}] -> {repr(self.ram[addr])}")
        return "\n".join(lines)
