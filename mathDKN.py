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

def factorial(n):
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