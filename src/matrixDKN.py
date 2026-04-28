"""
Librería de matrices para DKNexus.
Soporta matrices de dimensión dinámica n x m (sin dependencias externas).
"""


def _is_number(x):
    return isinstance(x, (int, float))


def matrix_dimensions(m):
    """Devuelve (filas, columnas) si m es matriz válida, si no None."""
    if not isinstance(m, list) or not m:
        return None
    if not all(isinstance(row, list) for row in m):
        return None
    cols = len(m[0])
    if cols == 0:
        return None
    if not all(len(row) == cols for row in m):
        return None
    if not all(_is_number(v) for row in m for v in row):
        return None
    return (len(m), cols)


def is_matrix(m):
    return matrix_dimensions(m) is not None


def is_matrix_2x2(m):
    dims = matrix_dimensions(m)
    return dims == (2, 2)


def matrix_transpose(m):
    """Transpuesta de una matriz n x m."""
    dims = matrix_dimensions(m)
    if dims is None:
        raise ValueError("Error de Dominio: trans(m) requiere una matriz válida.")
    rows, cols = dims
    return [[m[i][j] for i in range(rows)] for j in range(cols)]


def matrix_add(a, b):
    """Suma elemento a elemento de matrices del mismo tamaño."""
    da = matrix_dimensions(a)
    db = matrix_dimensions(b)
    if da is None or db is None or da != db:
        raise ValueError("Error de Dominio: suma/resta requiere matrices con la misma dimensión.")
    rows, cols = da
    return [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]


def matrix_sub(a, b):
    """Resta elemento a elemento de matrices del mismo tamaño."""
    da = matrix_dimensions(a)
    db = matrix_dimensions(b)
    if da is None or db is None or da != db:
        raise ValueError("Error de Dominio: suma/resta requiere matrices con la misma dimensión.")
    rows, cols = da
    return [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]


def matrix_scalar_mul(m, k):
    """Multiplicación de una matriz n x m por un escalar."""
    dims = matrix_dimensions(m)
    if dims is None or not _is_number(k):
        raise ValueError("Error de Dominio: multiplicación escalar requiere matriz válida y escalar.")
    rows, cols = dims
    return [[m[i][j] * k for j in range(cols)] for i in range(rows)]


def matrix_mul(a, b):
    """Producto matricial: (n x m) * (m x p) = (n x p)."""
    da = matrix_dimensions(a)
    db = matrix_dimensions(b)
    if da is None or db is None:
        raise ValueError("Error de Dominio: multiplicación requiere matrices válidas.")
    ra, ca = da
    rb, cb = db
    if ca != rb:
        raise ValueError("Error de Dominio: dimensiones incompatibles para multiplicación de matrices.")
    out = []
    for i in range(ra):
        row = []
        for j in range(cb):
            s = 0
            for k in range(ca):
                s += a[i][k] * b[k][j]
            row.append(s)
        out.append(row)
    return out


def matrix_inv(m):
    """Inversa de matriz cuadrada mediante Gauss-Jordan."""
    dims = matrix_dimensions(m)
    if dims is None:
        raise ValueError("Error de Dominio: inv(m) requiere una matriz válida.")
    n, c = dims
    if n != c:
        raise ValueError("Error de Dominio: inv(m) requiere una matriz cuadrada.")

    # Matriz aumentada [A | I]
    aug = []
    for i in range(n):
        left = [float(m[i][j]) for j in range(n)]
        right = [1.0 if i == j else 0.0 for j in range(n)]
        aug.append(left + right)

    for col in range(n):
        # Buscar pivote
        pivot = col
        while pivot < n and abs(aug[pivot][col]) < 1e-12:
            pivot += 1
        if pivot == n:
            raise ValueError("Error de Dominio: Matriz singular (determinante = 0), no tiene inversa.")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]

        # Normalizar fila pivote
        piv = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= piv

        # Eliminar columna en otras filas
        for i in range(n):
            if i == col:
                continue
            factor = aug[i][col]
            if factor == 0:
                continue
            for j in range(2 * n):
                aug[i][j] -= factor * aug[col][j]

    return [row[n:] for row in aug]


# Compatibilidad retroactiva con nombres previos 2x2
def matrix_transpose_2x2(m):
    return matrix_transpose(m)


def matrix_add_2x2(a, b):
    return matrix_add(a, b)


def matrix_sub_2x2(a, b):
    return matrix_sub(a, b)


def matrix_scalar_mul_2x2(m, k):
    return matrix_scalar_mul(m, k)


def matrix_mul_2x2(a, b):
    return matrix_mul(a, b)


def matrix_inv_2x2(m):
    return matrix_inv(m)
