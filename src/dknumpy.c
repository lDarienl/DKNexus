/*
 * dknumpy.c  -  Nucleo numerico nativo de DKNexus ("DKNumpy").
 *
 * Idea central:
 *   En lugar de representar una matriz como lista de listas en el heap de
 *   Python ([[1,2,3],[4,5,6]]), se aplana en un unico bloque de memoria
 *   CONTIGUA de doubles reservado con malloc.
 *
 *   Una matriz A(filas, columnas) se guarda como un arreglo plano de
 *   (filas * columnas) posiciones. El acceso al elemento (i, j) se resuelve
 *   con aritmetica de punteros mediante la formula:
 *
 *         indice = i * columnas + j
 *
 *   Python (via ctypes) solo envia los PUNTEROS de estos bloques; el computo
 *   pesado (multiplicacion de matrices, ajuste de pesos) se ejecuta aqui, a
 *   velocidad de hardware nativo.
 *
 * Compilacion (genera .dll en Windows / .so en Linux):
 *   Windows (MinGW):  gcc -O2 -shared -o dknumpy.dll dknumpy.c
 *   Windows (MSVC) :  cl /O2 /LD dknumpy.c /Fe:dknumpy.dll
 *   Linux / Mac    :  gcc -O2 -fPIC -shared -o libdknumpy.so dknumpy.c
 */

#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#define DKN_API __declspec(dllexport)
#else
#define DKN_API
#endif

/* ------------------------------------------------------------------ */
/*  Gestion de bloques contiguos (interactua con el HeapManager)       */
/* ------------------------------------------------------------------ */

/*
 * Reserva un bloque CONTIGUO de n doubles con malloc y devuelve su puntero.
 * El bloque se inicializa en cero. Devuelve NULL si n <= 0 o si malloc falla.
 */
DKN_API double *dknp_alloc(long n)
{
    if (n <= 0)
        return NULL;
    double *p = (double *)malloc((size_t)n * sizeof(double));
    if (p != NULL)
        memset(p, 0, (size_t)n * sizeof(double));
    return p;
}

/* Libera un bloque previamente reservado con dknp_alloc (free de C). */
DKN_API void dknp_free(double *p)
{
    if (p != NULL)
        free(p);
}

/* Copia n doubles desde 'src' (arreglo del lado Python) hacia el bloque 'dst'. */
DKN_API void dknp_set_block(double *dst, const double *src, long n)
{
    if (dst != NULL && src != NULL && n > 0)
        memcpy(dst, src, (size_t)n * sizeof(double));
}

/* Copia n doubles desde el bloque 'src' hacia 'dst' (para leer hacia Python). */
DKN_API void dknp_get_block(const double *src, double *dst, long n)
{
    if (dst != NULL && src != NULL && n > 0)
        memcpy(dst, src, (size_t)n * sizeof(double));
}

/* ------------------------------------------------------------------ */
/*  Acceso elemento a elemento por aritmetica de punteros              */
/*       indice = i * columnas + j                                     */
/* ------------------------------------------------------------------ */

DKN_API double dknp_get(const double *p, long cols, long i, long j)
{
    return p[i * cols + j];
}

DKN_API void dknp_put(double *p, long cols, long i, long j, double value)
{
    p[i * cols + j] = value;
}

/* ------------------------------------------------------------------ */
/*  Algebra lineal sobre bloques planos                                */
/* ------------------------------------------------------------------ */

/*
 * Producto matricial:  C(n x p) = A(n x m) * B(m x p).
 * Todos los bloques estan aplanados por filas (row-major).
 */
DKN_API void dknp_matmul(const double *a, const double *b, double *c,
                         long n, long m, long p)
{
    long i, j, k;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < p; j++)
        {
            double s = 0.0;
            for (k = 0; k < m; k++)
                s += a[i * m + k] * b[k * p + j];
            c[i * p + j] = s;
        }
    }
}

/* Suma elemento a elemento: C = A + B (len = filas * columnas). */
DKN_API void dknp_add(const double *a, const double *b, double *c, long len)
{
    long i;
    for (i = 0; i < len; i++)
        c[i] = a[i] + b[i];
}

/* Resta elemento a elemento: C = A - B. */
DKN_API void dknp_sub(const double *a, const double *b, double *c, long len)
{
    long i;
    for (i = 0; i < len; i++)
        c[i] = a[i] - b[i];
}

/* Multiplicacion por escalar: C = A * k. */
DKN_API void dknp_scalar_mul(const double *a, double k, double *c, long len)
{
    long i;
    for (i = 0; i < len; i++)
        c[i] = a[i] * k;
}

/* Transpuesta: C(cols x rows) a partir de A(rows x cols). */
DKN_API void dknp_transpose(const double *a, double *c, long rows, long cols)
{
    long i, j;
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            c[j * rows + i] = a[i * cols + j];
}

/* ------------------------------------------------------------------ */
/*  Machine Learning: ajuste de pesos por descenso de gradiente        */
/*       w = w - lr * grad                                             */
/* ------------------------------------------------------------------ */

DKN_API void dknp_update_weights(double *w, const double *grad,
                                 double lr, long len)
{
    long i;
    for (i = 0; i < len; i++)
        w[i] -= lr * grad[i];
}

/* Producto punto de dos vectores planos (util para capas densas). */
DKN_API double dknp_dot(const double *a, const double *b, long len)
{
    long i;
    double s = 0.0;
    for (i = 0; i < len; i++)
        s += a[i] * b[i];
    return s;
}
