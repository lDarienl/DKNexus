import matrixDKN as _matrixDKN


def compute_pi(iterations=2000):
    """
    Aproximación de pi por la serie de Nilakantha:
    π = 3 + 4/(2·3·4) - 4/(4·5·6) + 4/(6·7·8) - ...
    """
    pi = 3.0
    sign = 1
    for i in range(1, iterations + 1):
        n = i * 2
        pi += sign * (4 / (n * (n + 1) * (n + 2)))
        sign *= -1
    return pi

PI = compute_pi(2000)

def compute_e(iterations=20):
    """
    Calcula la constante e usando la serie de Taylor:
    e = 1/0! + 1/1! + 1/2! + 1/3! + ...
    """
    e_val = 1.0
    fact = 1.0
    for i in range(1, iterations):
        fact *= i  # Esto calcula el factorial de forma acumulativa
        e_val += 1.0 / fact
    return e_val

E = compute_e(20)

# Infinito (sin usar librerías): float('inf') es built-in, pero usamos 1e309.
INF = 1e309

def factorial(n):
    # Solo para enteros no negativos
    if int(n) != n or n < 0:
        raise ValueError("Error de Argumento: El factorial solo se define para enteros no negativos.")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def sin(x):
    # Convertir a rango -PI a PI para precisión
    x = x % (2 * PI)
    # Serie de Taylor para sin(x)
    term = 0
    for n in range(10):  # 10 iteraciones dan buena precisión
        term += ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
    return term

def cos(x):
    x = x % (2 * PI)
    term = 0
    for n in range(10):
        term += ((-1)**n * x**(2*n)) / factorial(2*n)
    return term

def tan(x):
    """Tangente con blindaje para PI/2."""
    # Normalizamos el ángulo al rango [0, PI] para detectar múltiplos de PI/2
    x_norm = x % PI
    if abs(x_norm - (PI / 2)) < 1e-10:
        raise ValueError("Error de dominio: Tangente indefinida en múltiplos de PI/2.")

    c = cos(x)
    if abs(c) < 1e-12:  # Blindaje extra por si falla lo anterior
        raise ValueError("Error de dominio: División por cero en coseno.")
    return sin(x) / c


def abs(x):
    return -x if x < 0 else x


def floor(x):
    i = int(x)
    return i if i <= x else i - 1


def ceil(x):
    i = int(x)
    return i if i >= x else i + 1


def sqrt(x, iterations=30):
    if x < 0:
        raise ValueError("Error de Dominio: No se puede calcular la raíz cuadrada de un número negativo.")
    if x == 0:
        return 0.0
    # Newton-Raphson
    g = x if x >= 1 else 1.0
    for _ in range(iterations):
        g = 0.5 * (g + x / g)
    return g


def exp(x, terms=40):
    # Reducción simple: exp(x) = (exp(x/n))^n
    if x == 0:
        return 1.0
    n = 1
    ax = abs(x)
    while ax > 1:
        ax /= 2
        n *= 2
    y = x / n
    # Serie de Taylor
    s = 1.0
    term = 1.0
    for k in range(1, terms):
        term *= y / k
        s += term
    # elevar por cuadrados repetidos
    for _ in range(int(n).bit_length() - 1):
        s *= s
    return s


def _ln_series(x):
    # ln(x) = 2 * ( y + y^3/3 + y^5/5 + ... ), y=(x-1)/(x+1), x>0
    y = (x - 1) / (x + 1)
    y2 = y * y
    term = y
    s = 0.0
    k = 1
    for _ in range(40):
        s += term / k
        term *= y2
        k += 2
    return 2 * s


def log(x):
    if x <= 0:
        raise ValueError("Error de Dominio: El logaritmo solo está definido para números positivos.")
    # Escalar x a [0.5, 2] usando potencias de 2
    k = 0
    while x > 2:
        x /= 2
        k += 1
    while x < 0.5:
        x *= 2
        k -= 1
    ln2 = _ln_series(2.0)
    return _ln_series(x) + k * ln2


def log10(x):
    return log(x) / log(10.0)


def root(x, y):
    # raíz y-ésima: x^(1/y)
    if y == 0:
        raise ValueError("Error de dominio: root(x, y) requiere y != 0.")
    # Si x < 0, solo permitir y entero impar (aprox)
    if x < 0:
        yi = int(y)
        if abs(y - yi) > 1e-12 or yi % 2 == 0:
            raise ValueError("Error de Dominio: Raíz par de un número negativo produce un número complejo.")
        return -root(-x, y)
    return exp(log(x) / y)


def tanh(x):
    ex = exp(x)
    enx = exp(-x)
    denom = ex + enx
    if denom == 0:
        return 0.0
    return (ex - enx) / denom


# --- Estadística descriptiva y normalización (sin librerías externas) ---


def _is_real_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _iter_flat_numeric(data, bump):
    """
    Recorre elementos de una lista 1D o de una matriz (por filas).
    Exige tipos numéricos; `bump` se invoca por cada elemento visitado.
    """
    if _matrixDKN.is_matrix(data):
        for row in data:
            for v in row:
                bump()
                if not _is_real_number(v):
                    raise ValueError(
                        "Operación estadística: todos los elementos deben ser numéricos (no strings ni bool)."
                    )
                yield v
        return
    if isinstance(data, list):
        for v in data:
            bump()
            if not _is_real_number(v):
                raise ValueError(
                    "Operación estadística: todos los elementos deben ser numéricos (no strings ni bool)."
                )
            yield v
        return
    raise ValueError("Operación estadística: se esperaba una lista o una matriz.")


def dk_sum(data, bump=lambda: None):
    s = 0
    for v in _iter_flat_numeric(data, bump):
        s += v
    return s


def dk_mean(data, bump=lambda: None):
    total = 0.0
    n = 0
    for v in _iter_flat_numeric(data, bump):
        total += float(v)
        n += 1
    if n == 0:
        raise ValueError("mean: la colección está vacía.")
    return total / n


def dk_min(data, bump=lambda: None):
    it = _iter_flat_numeric(data, bump)
    try:
        m = next(it)
    except StopIteration:
        raise ValueError("min: la colección está vacía.") from None
    for v in it:
        m = v if v < m else m
    return m


def dk_max(data, bump=lambda: None):
    it = _iter_flat_numeric(data, bump)
    try:
        m = next(it)
    except StopIteration:
        raise ValueError("max: la colección está vacía.") from None
    for v in it:
        m = v if v > m else m
    return m


def normalize_vector(vec, bump=lambda: None):
    """
    Normalización min-max a [0, 1]: (x - min) / (max - min).
    Solo vectores (lista 1D numérica); no matrices.
    """
    if not isinstance(vec, list) or _matrixDKN.is_matrix(vec):
        raise ValueError("normalize: se esperaba un vector (lista 1D numérica).")
    if not vec:
        raise ValueError("normalize: el vector está vacío.")
    vals = []
    for v in vec:
        bump()
        if not _is_real_number(v):
            raise ValueError("normalize: todos los elementos deben ser numéricos.")
        vals.append(float(v))
    lo = vals[0]
    hi = vals[0]
    for x in vals[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    span = hi - lo
    if span == 0:
        return [0.0 for _ in vals]
    return [(x - lo) / span for x in vals]
