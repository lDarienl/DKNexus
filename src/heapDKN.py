"""
Simulación de memoria manual (heap + direcciones) para el intérprete DKNexus.
"""

import matrixDKN

class DKNMemoryError(Exception):
    """El heap no puede alojar más datos (slots agotados)."""


class HeapManager:
    """
    Memoria RAM simulada: direcciones hexadecimales -> valor.
    Cada reserva consume un número de slots según el tipo/tamaño del objeto.
    """

    def __init__(self, max_slots: int = 1024):
        self.max_slots = max_slots
        self.used_slots = 0
        self.ram: dict[str, object] = {}
        self.cell_weight: dict[str, int] = {}
        self._next_id = 0

    def weight(self, value: object, depth: int = 0) -> int:
        """Peso en slots: escalar = 1, listas = suma recursiva de elementos."""
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
        return 1

    def _clone_for_store(self, value: object) -> object:
        """Copia superficial para que mutaciones externas no corrompan el heap."""
        if isinstance(value, list):
            if matrixDKN.is_matrix(value):
                return [[elem for elem in row] for row in value]
            return [x for x in value]
        return value

    def allocate(self, value: object) -> str:
        """Reserva memoria y devuelve la dirección (puntero)."""
        stored = self._clone_for_store(value)
        w = self.weight(stored)
        if w > self.max_slots:
            raise DKNMemoryError(
                f"Objeto demasiado grande ({w} slots) para el límite del heap ({self.max_slots})."
            )
        if self.used_slots + w > self.max_slots:
            raise DKNMemoryError(
                f"Heap lleno: se requieren {w} slots libres pero solo quedan "
                f"{self.max_slots - self.used_slots} de {self.max_slots}."
            )
        self._next_id += 1
        addr = f"0x{self._next_id:03X}"
        self.ram[addr] = stored
        self.cell_weight[addr] = w
        self.used_slots += w
        return addr

    def read(self, addr: str) -> object:
        if addr not in self.ram:
            raise KeyError(addr)
        return self.ram[addr]

    def free(self, addr: str | None) -> None:
        """Libera la celda asociada a una dirección (GC básico por ámbito)."""
        if addr is None or addr not in self.ram:
            return
        w = self.cell_weight.pop(addr, 0)
        self.ram.pop(addr, None)
        self.used_slots -= w

    def dump_state(self) -> str:
        """Representación amigable del estado del heap."""
        lines = [
            f"Heap usage: {self.used_slots}/{self.max_slots} slots",
            f"Cells: {len(self.ram)}",
        ]
        for addr in sorted(self.ram.keys()):
            w = self.cell_weight.get(addr, 0)
            lines.append(f"{addr} [w={w}] -> {repr(self.ram[addr])}")
        return "\n".join(lines)
