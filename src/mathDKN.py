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
    """Tangente = seno / coseno. Indefinida cuando cos(x) = 0."""
    c = cos(x)
    # Umbral para evitar problemas numéricos cerca de 0
    if -1e-12 < c < 1e-12:
        raise ValueError("Error de dominio: Tangente indefinida (división por cero en coseno).")
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
