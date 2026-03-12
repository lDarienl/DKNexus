"""
Librería de matrices para DKNexus (equivalente conceptual a NumPy para Python).
Operaciones 2x2 implementadas sin dependencias externas.
"""


def _is_number(x):
    return isinstance(x, (int, float))


def is_matrix_2x2(m):
    """Comprueba si el valor es una matriz 2x2 de números."""
    if not isinstance(m, list) or len(m) != 2:
        return False
    if not all(isinstance(row, list) and len(row) == 2 for row in m):
        return False
    return all(_is_number(m[i][j]) for i in range(2) for j in range(2))


def matrix_transpose_2x2(m):
    """Transpuesta de una matriz 2x2."""
    if not is_matrix_2x2(m):
        raise ValueError("Error de Dominio: trans(m) requiere una matriz 2x2.")
    return [[m[0][0], m[1][0]], [m[0][1], m[1][1]]]


def matrix_add_2x2(a, b):
    """Suma elemento a elemento de matrices 2x2."""
    if not (is_matrix_2x2(a) and is_matrix_2x2(b)):
        raise ValueError("Error de Dominio: suma/resta requiere matrices 2x2.")
    return [
        [a[0][0] + b[0][0], a[0][1] + b[0][1]],
        [a[1][0] + b[1][0], a[1][1] + b[1][1]],
    ]


def matrix_sub_2x2(a, b):
    """Resta elemento a elemento de matrices 2x2."""
    if not (is_matrix_2x2(a) and is_matrix_2x2(b)):
        raise ValueError("Error de Dominio: suma/resta requiere matrices 2x2.")
    return [
        [a[0][0] - b[0][0], a[0][1] - b[0][1]],
        [a[1][0] - b[1][0], a[1][1] - b[1][1]],
    ]


def matrix_scalar_mul_2x2(m, k):
    """Multiplicación de una matriz 2x2 por un escalar."""
    if not is_matrix_2x2(m) or not _is_number(k):
        raise ValueError("Error de Dominio: multiplicación escalar requiere matriz 2x2 y escalar.")
    return [
        [m[0][0] * k, m[0][1] * k],
        [m[1][0] * k, m[1][1] * k],
    ]


def matrix_mul_2x2(a, b):
    """Producto de matrices 2x2 (filas por columnas)."""
    if not (is_matrix_2x2(a) and is_matrix_2x2(b)):
        raise ValueError("Error de Dominio: multiplicación requiere matrices 2x2.")
    return [
        [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
        [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]],
    ]


def matrix_inv_2x2(m):
    """Inversa de una matriz 2x2. Falla si es singular (det = 0)."""
    if not is_matrix_2x2(m):
        raise ValueError("Error de Dominio: inv(m) requiere una matriz 2x2.")
    a, b = m[0][0], m[0][1]
    c, d = m[1][0], m[1][1]
    det = a * d - b * c
    if det == 0:
        raise ValueError("Error de Dominio: Matriz singular (determinante = 0), no tiene inversa.")
    inv_det = 1.0 / det
    return [
        [ d * inv_det, -b * inv_det],
        [-c * inv_det,  a * inv_det],
    ]
