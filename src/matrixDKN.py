"""
Librería de matrices para DKNexus.
Soporta matrices de dimensión dinámica n x m.

El computo pesado (multiplicacion, suma/resta, escalar) se DELEGA al nucleo
numerico ``dknumpyDKN``, que aplana las matrices en memoria contigua y, cuando
hay libreria nativa compilada, ejecuta las operaciones en C. Validacion de
dominio y casos exactos (transpuesta, inversa) se mantienen aqui.
"""

import dknumpyDKN as _dknp


def _is_number(x):
    return isinstance(x, (int, float))


def _all_integral_matrix(m):
    """True si todos los elementos son enteros (no bool)."""
    return all(isinstance(v, int) and not isinstance(v, bool) for row in m for v in row)


def _intify(out, integral):
    """
    DKNumpy devuelve floats. Si la operacion fue puramente entera, se vuelve a
    enteros cuando el resultado es exacto (preserva la semantica previa).
    """
    if not integral:
        return out
    res = []
    for row in out:
        new_row = []
        for v in row:
            fv = float(v)
            new_row.append(int(fv) if fv.is_integer() else fv)
        res.append(new_row)
    return res


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
    """Transpuesta de una matriz n x m (sobre bloque contiguo de DKNumpy)."""
    dims = matrix_dimensions(m)
    if dims is None:
        raise ValueError("Error de Dominio: trans(m) requiere una matriz válida.")
    return _intify(_dknp.transpose_lists(m), _all_integral_matrix(m))


def matrix_add(a, b):
    """Suma elemento a elemento de matrices del mismo tamaño (delegada a C)."""
    da = matrix_dimensions(a)
    db = matrix_dimensions(b)
    if da is None or db is None or da != db:
        raise ValueError("Error de Dominio: suma/resta requiere matrices con la misma dimensión.")
    integral = _all_integral_matrix(a) and _all_integral_matrix(b)
    return _intify(_dknp.add_lists(a, b), integral)


def matrix_sub(a, b):
    """Resta elemento a elemento de matrices del mismo tamaño (delegada a C)."""
    da = matrix_dimensions(a)
    db = matrix_dimensions(b)
    if da is None or db is None or da != db:
        raise ValueError("Error de Dominio: suma/resta requiere matrices con la misma dimensión.")
    integral = _all_integral_matrix(a) and _all_integral_matrix(b)
    return _intify(_dknp.sub_lists(a, b), integral)


def matrix_scalar_mul(m, k):
    """Multiplicación de una matriz n x m por un escalar (delegada a C)."""
    dims = matrix_dimensions(m)
    if dims is None or not _is_number(k):
        raise ValueError("Error de Dominio: multiplicación escalar requiere matriz válida y escalar.")
    integral = _all_integral_matrix(m) and isinstance(k, int) and not isinstance(k, bool)
    return _intify(_dknp.scalar_mul_lists(m, k), integral)


def matrix_mul(a, b):
    """
    Producto matricial: (n x m) * (m x p) = (n x p).

    El computo se delega a ``dknumpyDKN`` (memoria contigua + C nativo cuando
    esta disponible); aqui solo validamos dominio y preservamos enteros.
    """
    da = matrix_dimensions(a)
    db = matrix_dimensions(b)
    if da is None or db is None:
        raise ValueError("Error de Dominio: multiplicación requiere matrices válidas.")
    ra, ca = da
    rb, cb = db
    if ca != rb:
        raise ValueError("Error de Dominio: dimensiones incompatibles para multiplicación de matrices.")
    integral = _all_integral_matrix(a) and _all_integral_matrix(b)
    return _intify(_dknp.matmul_lists(a, b), integral)


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


def get_column(m, col_index):
    """Extrae la columna `col_index` (0-based) como lista de longitud nfilas."""
    dims = matrix_dimensions(m)
    if dims is None:
        raise ValueError("get_col: se requiere una matriz válida (n x m, numérica).")
    rows, cols = dims
    if not isinstance(col_index, int) or isinstance(col_index, bool):
        raise ValueError("get_col: el índice de columna debe ser un entero.")
    if col_index < 0 or col_index >= cols:
        raise ValueError(
            f"get_col: índice de columna fuera de rango: {col_index} (válido 0..{cols - 1})."
        )
    return [m[i][col_index] for i in range(rows)]


def set_column(m, col_index, vector):
    """
    Devuelve una **nueva** matriz con la columna `col_index` reemplazada por `vector`.
    `vector` debe tener longitud nfilas.
    """
    dims = matrix_dimensions(m)
    if dims is None:
        raise ValueError("set_col: se requiere una matriz válida (n x m, numérica).")
    rows, cols = dims
    if not isinstance(col_index, int) or isinstance(col_index, bool):
        raise ValueError("set_col: el índice de columna debe ser un entero.")
    if col_index < 0 or col_index >= cols:
        raise ValueError(
            f"set_col: índice de columna fuera de rango: {col_index} (válido 0..{cols - 1})."
        )
    if not isinstance(vector, list) or matrix_dimensions(vector) is not None:
        raise ValueError("set_col: el tercer argumento debe ser un vector (lista 1D), no una matriz.")
    if len(vector) != rows:
        raise ValueError(
            f"set_col: el vector tiene longitud {len(vector)}, se esperaban {rows} filas."
        )
    if not all(_is_number(v) for v in vector):
        raise ValueError("set_col: el vector debe contener solo valores numéricos.")
    out = [[m[i][k] for k in range(cols)] for i in range(rows)]
    for i in range(rows):
        out[i][col_index] = vector[i]
    return out
