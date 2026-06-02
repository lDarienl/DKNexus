"""
DKNumpy: nucleo numerico de DKNexus con memoria CONTIGUA y binding a C (ctypes).

En vez de almacenar matrices como listas de listas, DKNumpy las aplana en un
unico bloque contiguo de `double` y delega el computo pesado a la libreria
dinamica compilada desde ``dknumpy.c`` (``dknumpy.dll`` en Windows /
``libdknumpy.so`` en Linux/Mac).

Acceso al elemento (i, j) de una matriz de ``cols`` columnas:

        indice = i * cols + j

Si la libreria nativa no esta compilada/disponible, se usa un *fallback* puro
en Python (igualmente sobre memoria contigua con ``ctypes``) para que el
interprete siga funcionando. La API publica es identica en ambos modos.
"""

import ctypes
import os
import sys

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def _candidate_lib_paths():
    """Nombres/ubicaciones posibles de la libreria dinamica segun el SO."""
    if sys.platform.startswith("win"):
        names = ["dknumpy.dll"]
    elif sys.platform == "darwin":
        names = ["libdknumpy.dylib", "libdknumpy.so"]
    else:
        names = ["libdknumpy.so"]
    paths = []
    for n in names:
        paths.append(os.path.join(_THIS_DIR, n))
        paths.append(os.path.join(_THIS_DIR, "build", n))
        paths.append(os.path.join(os.getcwd(), n))
    return paths


def _load_native():
    """Intenta cargar la libreria nativa; devuelve el handle o None."""
    for path in _candidate_lib_paths():
        if os.path.exists(path):
            try:
                return ctypes.CDLL(path)
            except OSError:
                continue
    return None


_C_DOUBLE_P = ctypes.POINTER(ctypes.c_double)


def _configure_prototypes(lib):
    """Declara firmas (argtypes/restype) de las funciones de la libreria."""
    lib.dknp_alloc.argtypes = [ctypes.c_long]
    lib.dknp_alloc.restype = _C_DOUBLE_P

    lib.dknp_free.argtypes = [_C_DOUBLE_P]
    lib.dknp_free.restype = None

    lib.dknp_set_block.argtypes = [_C_DOUBLE_P, _C_DOUBLE_P, ctypes.c_long]
    lib.dknp_set_block.restype = None

    lib.dknp_get_block.argtypes = [_C_DOUBLE_P, _C_DOUBLE_P, ctypes.c_long]
    lib.dknp_get_block.restype = None

    lib.dknp_get.argtypes = [_C_DOUBLE_P, ctypes.c_long, ctypes.c_long, ctypes.c_long]
    lib.dknp_get.restype = ctypes.c_double

    lib.dknp_put.argtypes = [
        _C_DOUBLE_P, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_double
    ]
    lib.dknp_put.restype = None

    lib.dknp_matmul.argtypes = [
        _C_DOUBLE_P, _C_DOUBLE_P, _C_DOUBLE_P,
        ctypes.c_long, ctypes.c_long, ctypes.c_long,
    ]
    lib.dknp_matmul.restype = None

    for fn in ("dknp_add", "dknp_sub"):
        f = getattr(lib, fn)
        f.argtypes = [_C_DOUBLE_P, _C_DOUBLE_P, _C_DOUBLE_P, ctypes.c_long]
        f.restype = None

    lib.dknp_scalar_mul.argtypes = [_C_DOUBLE_P, ctypes.c_double, _C_DOUBLE_P, ctypes.c_long]
    lib.dknp_scalar_mul.restype = None

    lib.dknp_transpose.argtypes = [_C_DOUBLE_P, _C_DOUBLE_P, ctypes.c_long, ctypes.c_long]
    lib.dknp_transpose.restype = None

    lib.dknp_update_weights.argtypes = [_C_DOUBLE_P, _C_DOUBLE_P, ctypes.c_double, ctypes.c_long]
    lib.dknp_update_weights.restype = None

    lib.dknp_dot.argtypes = [_C_DOUBLE_P, _C_DOUBLE_P, ctypes.c_long]
    lib.dknp_dot.restype = ctypes.c_double


_LIB = _load_native()
HAS_NATIVE = _LIB is not None
if HAS_NATIVE:
    try:
        _configure_prototypes(_LIB)
    except AttributeError:
        # La libreria existe pero no expone los simbolos esperados: usar fallback.
        _LIB = None
        HAS_NATIVE = False


def backend_name():
    """'C-native' si se cargo el .dll/.so; 'python-fallback' en caso contrario."""
    return "C-native" if HAS_NATIVE else "python-fallback"


class DKNFlatBlock:
    """
    Bloque de memoria CONTIGUA de ``n`` doubles.

    - Modo nativo: el bloque se reserva en C con ``malloc`` (``dknp_alloc``) y se
      guarda el puntero crudo. Python solo manipula ese puntero.
    - Modo fallback: se usa un arreglo ``ctypes`` ``(c_double * n)`` que tambien
      vive en memoria contigua y expone un puntero compatible.
    """

    __slots__ = ("n", "_native", "_ptr", "_buf", "_freed")

    def __init__(self, n):
        self.n = int(n)
        self._freed = False
        if self.n < 0:
            raise ValueError("DKNFlatBlock: tamano negativo.")
        if HAS_NATIVE and self.n > 0:
            self._native = True
            self._buf = None
            self._ptr = _LIB.dknp_alloc(ctypes.c_long(self.n))
            if not self._ptr:
                raise MemoryError("dknp_alloc devolvio NULL (malloc fallo).")
        else:
            # Fallback (o bloque de tamano 0): memoria contigua del lado Python.
            self._native = False
            self._buf = (ctypes.c_double * max(self.n, 1))()
            self._ptr = ctypes.cast(self._buf, _C_DOUBLE_P)

    @property
    def ptr(self):
        """Puntero ctypes al bloque (lo que se envia a C)."""
        if self._freed:
            raise RuntimeError("Bloque ya liberado.")
        return self._ptr

    def ptr_address(self):
        """Direccion entera (numerica) del bloque; util para registrar el puntero."""
        if self._freed or not self._ptr:
            return 0
        return ctypes.cast(self._ptr, ctypes.c_void_p).value or 0

    def write(self, flat_values):
        """Escribe una secuencia de numeros en el bloque (indice plano)."""
        if self._freed:
            raise RuntimeError("Bloque ya liberado.")
        for i, v in enumerate(flat_values):
            if i >= self.n:
                break
            self._ptr[i] = float(v)

    def read(self):
        """Devuelve la lista plana de doubles del bloque."""
        if self._freed:
            raise RuntimeError("Bloque ya liberado.")
        return [self._ptr[i] for i in range(self.n)]

    def get(self, index):
        return self._ptr[index]

    def set(self, index, value):
        self._ptr[index] = float(value)

    def free(self):
        """Libera el bloque (free de C en modo nativo)."""
        if self._freed:
            return
        if self._native and self._ptr:
            _LIB.dknp_free(self._ptr)
        self._ptr = None
        self._buf = None
        self._freed = True


class DKNMatrix:
    """
    Matriz aplanada en un ``DKNFlatBlock`` contiguo (row-major).

    El elemento (i, j) se ubica en ``i * cols + j``.
    """

    __slots__ = ("rows", "cols", "block", "integral")

    def __init__(self, rows, cols, block=None, integral=False):
        self.rows = int(rows)
        self.cols = int(cols)
        self.block = block if block is not None else DKNFlatBlock(self.rows * self.cols)
        # Si la matriz se construyo solo con enteros, se recuerda para que la
        # lectura no muestre floats artificiales (p.ej. 1.0 en vez de 1).
        self.integral = integral

    @classmethod
    def from_list(cls, mat):
        """Construye una matriz contigua a partir de una lista de listas."""
        rows = len(mat)
        cols = len(mat[0]) if rows else 0
        integral = all(
            isinstance(v, int) and not isinstance(v, bool)
            for row in mat for v in row
        )
        m = cls(rows, cols, integral=integral)
        flat = []
        for i in range(rows):
            for j in range(cols):
                flat.append(float(mat[i][j]))
        m.block.write(flat)
        return m

    def to_list(self):
        """Reconstruye la lista de listas a partir del bloque contiguo."""
        flat = self.block.read()
        cols = self.cols
        if self.integral:
            return [
                [int(flat[i * cols + j]) if float(flat[i * cols + j]).is_integer()
                 else flat[i * cols + j] for j in range(cols)]
                for i in range(self.rows)
            ]
        return [[flat[i * cols + j] for j in range(cols)] for i in range(self.rows)]

    def get(self, i, j):
        return self.block.get(i * self.cols + j)

    def set(self, i, j, value):
        self.block.set(i * self.cols + j, value)

    def free(self):
        self.block.free()


# --------------------------------------------------------------------------
#  Operaciones de alto nivel sobre listas de listas.
#  Aplanan -> delegan a C (o fallback) -> devuelven listas de listas (float).
# --------------------------------------------------------------------------


def matmul_lists(a, b):
    """Producto matricial A(n x m) * B(m x p). Delega en C si esta disponible."""
    ma = DKNMatrix.from_list(a)
    mb = DKNMatrix.from_list(b)
    if ma.cols != mb.rows:
        raise ValueError("matmul: dimensiones incompatibles.")
    out = DKNMatrix(ma.rows, mb.cols)
    if HAS_NATIVE:
        _LIB.dknp_matmul(
            ma.block.ptr, mb.block.ptr, out.block.ptr,
            ma.rows, ma.cols, mb.cols,
        )
    else:
        _fallback_matmul(ma, mb, out)
    result = out.to_list()
    ma.free(); mb.free(); out.free()
    return result


def add_lists(a, b):
    """Suma elemento a elemento de dos matrices del mismo tamano."""
    return _elementwise(a, b, "dknp_add", _fallback_add)


def sub_lists(a, b):
    """Resta elemento a elemento de dos matrices del mismo tamano."""
    return _elementwise(a, b, "dknp_sub", _fallback_sub)


def scalar_mul_lists(mat, k):
    """Multiplica una matriz por un escalar."""
    m = DKNMatrix.from_list(mat)
    out = DKNMatrix(m.rows, m.cols)
    length = m.rows * m.cols
    if HAS_NATIVE:
        _LIB.dknp_scalar_mul(m.block.ptr, ctypes.c_double(float(k)), out.block.ptr, length)
    else:
        for idx in range(length):
            out.block.set(idx, m.block.get(idx) * float(k))
    result = out.to_list()
    m.free(); out.free()
    return result


def transpose_lists(mat):
    """Transpuesta de una matriz n x m usando el bloque contiguo."""
    m = DKNMatrix.from_list(mat)
    out = DKNMatrix(m.cols, m.rows)
    if HAS_NATIVE:
        _LIB.dknp_transpose(m.block.ptr, out.block.ptr, m.rows, m.cols)
    else:
        for i in range(m.rows):
            for j in range(m.cols):
                out.block.set(j * m.rows + i, m.block.get(i * m.cols + j))
    result = out.to_list()
    m.free(); out.free()
    return result


def update_weights_lists(weights, grad, lr):
    """Ajuste de pesos por descenso de gradiente: w = w - lr * grad (vectores)."""
    w = DKNFlatBlock(len(weights))
    g = DKNFlatBlock(len(grad))
    w.write([float(x) for x in weights])
    g.write([float(x) for x in grad])
    length = len(weights)
    if HAS_NATIVE:
        _LIB.dknp_update_weights(w.ptr, g.ptr, ctypes.c_double(float(lr)), length)
    else:
        for i in range(length):
            w.set(i, w.get(i) - float(lr) * g.get(i))
    result = w.read()
    w.free(); g.free()
    return result


def _elementwise(a, b, native_fn, py_fn):
    ma = DKNMatrix.from_list(a)
    mb = DKNMatrix.from_list(b)
    if (ma.rows, ma.cols) != (mb.rows, mb.cols):
        raise ValueError("operacion elemento a elemento: dimensiones distintas.")
    out = DKNMatrix(ma.rows, ma.cols)
    length = ma.rows * ma.cols
    if HAS_NATIVE:
        getattr(_LIB, native_fn)(ma.block.ptr, mb.block.ptr, out.block.ptr, length)
    else:
        py_fn(ma, mb, out, length)
    result = out.to_list()
    ma.free(); mb.free(); out.free()
    return result


def _fallback_matmul(ma, mb, out):
    n, m, p = ma.rows, ma.cols, mb.cols
    for i in range(n):
        for j in range(p):
            s = 0.0
            for k in range(m):
                s += ma.block.get(i * m + k) * mb.block.get(k * p + j)
            out.block.set(i * p + j, s)


def _fallback_add(ma, mb, out, length):
    for idx in range(length):
        out.block.set(idx, ma.block.get(idx) + mb.block.get(idx))


def _fallback_sub(ma, mb, out, length):
    for idx in range(length):
        out.block.set(idx, ma.block.get(idx) - mb.block.get(idx))
