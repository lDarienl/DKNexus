# DKNexus DSL

**DKNexus** es un **Lenguaje de Dominio Específico (DSL)** orientado a flujos de
trabajo de **Machine Learning y Deep Learning**, construido **desde cero** y con
**cero librerías externas de cálculo** (sin `numpy`, sin `scikit-learn`, sin
`matplotlib`, sin `math`).

| Capa | Tecnología |
|---|---|
| Análisis léxico / sintáctico | **ANTLR 4** (`-Dlanguage=Python3 -visitor`) |
| Intérprete | **Python 3** (patrón *Visitor* sobre el AST) |
| Núcleo numérico | **C** (`dknumpy.c`) con *binding* `ctypes` + *fallback* en Python |
| Álgebra / matemática | Librerías propias (`mathDKN`, `matrixDKN`) |
| Persistencia | **Redis** con *fallback* a disco (`persistDKN`) |
| Memoria | Heap simulado con punteros y *scopes* (`heapDKN`) |

> Referencias de diseño: la API de alto nivel imita a **scikit-learn**
> (`fit` / `predict`), el núcleo numérico imita a **NumPy** (memoria contigua), y
> la regresión / backprop siguen el enfoque del libro **Grokking** (gradiente
> descendente iterativo).

---

## Índice

1. [¿Qué es DKNexus y para qué sirve?](#1-qué-es-dknexus-y-para-qué-sirve)
2. [Cumplimiento por cortes](#2-cumplimiento-por-cortes)
3. [Arquitectura general (pipeline)](#3-arquitectura-general-pipeline)
4. [Instalación y uso](#4-instalación-y-uso)
5. [Referencia del lenguaje (sintaxis)](#5-referencia-del-lenguaje-sintaxis)
6. [Librería estándar (built-ins)](#6-librería-estándar-built-ins)
7. [DKNumpy: núcleo numérico en C](#7-dknumpy-núcleo-numérico-en-c)
8. [Gestión de memoria y seguridad](#8-gestión-de-memoria-y-seguridad)
9. [Machine Learning y Deep Learning](#9-machine-learning-y-deep-learning)
10. [Estructura del proyecto](#10-estructura-del-proyecto)
11. [Tests incluidos](#11-tests-incluidos)
12. [Qué puede y qué NO puede hacer (límites)](#12-qué-puede-y-qué-no-puede-hacer-límites)
13. [Pendientes / Roadmap](#13-pendientes--roadmap)
14. [Referencias y licencia](#14-referencias-y-licencia)

---

## 1. ¿Qué es DKNexus y para qué sirve?

DKNexus es un lenguaje de programación pequeño pero completo, diseñado con un
objetivo académico: **demostrar cómo se construye un lenguaje y su runtime**, y
**cómo se implementan los algoritmos de ML/DL por dentro**, sin esconder la
complejidad detrás de librerías de terceros.

**Filosofía (por qué se hace así):**

- **Cero dependencias de cálculo.** Trigonometría, exponenciales, logaritmos,
  álgebra de matrices y los algoritmos de ML/DL están escritos a mano. Esto
  tiene valor educativo y hace el proyecto autocontenido.
- **Eficiencia donde importa.** El cómputo pesado de matrices se delega a un
  núcleo en **C** (`dknumpy.c`) mediante *binding* `ctypes`, igual que NumPy usa
  C/Fortran por debajo. Si no hay compilador, hay *fallback* en Python.
- **Runtime controlado.** Memoria manual (heap + punteros), aislamiento de
  ámbitos y un *execution guard* contra bucles infinitos.

**Sirve para:** escribir programas numéricos, manipular vectores/matrices,
entrenar modelos de regresión y clasificación, y montar una red neuronal
multicapa (MLP) para problemas no lineales como el XOR, todo con una sintaxis
sencilla tipo C/Python.

---

## 2. Cumplimiento por cortes

### Primer corte — Diseño del lenguaje

| Tema esperado | Estado | Dónde |
|---|---|---|
| Diseño del lenguaje (qué puede hacer el DSL) | ✅ | Este README + gramática |
| Gramática | ✅ | `grammar/grammarDKN.g4` |
| Parte léxica (tokens, palabras reservadas, operadores) | ✅ | reglas léxicas del `.g4` |
| Parte semántica (validación de tipos / sentido) | ✅ | `EvalVisitor` (`_require_number`, `_matches_type`, etc.) |
| Parte sintáctica (estructura válida de programas) | ✅ | reglas `program`/`statement`/`expr` |
| Primeros programas ejecutables | ✅ | `tests/*.dkn` |
| ANTLR básico (v4) | ✅ | lexer/parser/visitor generados en `src/` |

### Segundo corte — Lenguaje de propósito general

| Tema esperado | Estado | Dónde |
|---|---|---|
| Ciclos `for` / `while` | ✅ | `visitForStmt`, `visitWhileStmt` |
| Funciones (declaración, parámetros, retorno) | ✅ | `function ... { ... retornar x; }` |
| Variables (asignación, tipos, alcance) | ✅ | heap + *scopes* (`heapDKN`) |
| Archivos (lectura/escritura) | ✅ | `read`, `write`, `load_csv` |
| Recursividad | ✅ | `tests/euclides_recursivo.dkn`, `recursividad_scoop.dkn` |
| Consola / interfaz (terminal) | ✅ | REPL + ejecución de archivo (`main()`) |
| Visitor (recorrido completo del árbol) | ✅ | `EvalVisitor` |

### Tercer corte — Machine Learning y Deep Learning

| Tema esperado | Estado | Dónde |
|---|---|---|
| Regresión lineal (entrenamiento + predicción) | ✅ | `tests/regresion_lineal.dkn` + `update_weights` |
| Regresión logística (clasificación) | ✅ | `tests/clasificacion_binaria.dkn` + `sigmoid` |
| Perceptrón (clasificador lineal) | ✅ | `escalon` + `tests/clasificacion_binaria.dkn` |
| Perceptrón multicapa (MLP) | ✅ | `mlp_init` / `mlp_fit` / `mlp_predict` + `tests/mlp_xor.dkn` |
| Red neuronal: **predicción** | ✅ | regresión lineal / MLP |
| Red neuronal: **clasificación** | ✅ | logística / perceptrón / MLP (XOR) |
| Red neuronal: **agrupamiento (clustering / k-vecinos)** | ✅ | `kmeans` (no supervisado) + `knn` |
| Optimizador (gradiente descendente) | ✅ | `dknp_update_weights` (C) + backprop en `mlp_fit` |
| Métricas (exactitud / matriz de confusión / MSE) | ✅ | `mse`, `exactitud`, `matriz_confusion` |
| Métrica de **precisión** explícita | ✅ | `precision` (`TP / (TP + FP)`) |
| Gráficos (visualización de resultados) | ✅ | `graficar_dispersion`, `graficar_linea` (canvas ASCII) |
| Propio NumPy (vectores/matrices + binding C) | ✅ | `dknumpy.c` + `dknumpyDKN.py` |
| Estructuras clave-valor propias | ✅ | diccionarios nativos (tabla hash) |
| Persistencia (Redis / disco) | ✅ | `persistDKN.py` |

**Resumen:** los **tres cortes están completos**. El corte 3 cubre los tres
pilares: **predicción** (regresión lineal), **clasificación** (regresión
logística, perceptrón, MLP/XOR) y **agrupamiento** (`kmeans` no supervisado y
`knn`), además de optimizador, métricas (incluida `precision`) y gráficos.

---

## 3. Arquitectura general (pipeline)

```text
  programa.dkn
      │
      ▼
┌───────────────┐   tokens    ┌────────────────┐   AST    ┌─────────────────────┐
│  Lexer ANTLR  │ ──────────► │  Parser ANTLR  │ ───────► │  EvalVisitor (Py)   │
│ grammarDKNLexer│            │ grammarDKNParser│         │  interpreterDKN.py   │
└───────────────┘             └────────────────┘          └──────────┬──────────┘
                                                                      │ usa
        ┌─────────────────────────────────────────────────────────────┼───────────────┐
        ▼                         ▼                      ▼              ▼               ▼
  ┌───────────┐           ┌──────────────┐       ┌────────────┐  ┌────────────┐  ┌────────────┐
  │ heapDKN   │           │  matrixDKN   │       │  mathDKN   │  │ persistDKN │  │ dataDKN    │
  │ (memoria) │           │ (álgebra)    │       │ (cálculo)  │  │ (Redis)    │  │ (CSV)      │
  └───────────┘           └──────┬───────┘       └────────────┘  └────────────┘  └────────────┘
                                 │ cómputo pesado
                                 ▼
                         ┌────────────────┐  ctypes  ┌──────────────┐
                         │  dknumpyDKN.py │ ───────► │  dknumpy.c   │  (C nativo / .dll / .so)
                         │  (binding)     │          │  (malloc)    │
                         └────────────────┘          └──────────────┘
```

1. El `.dkn` se convierte en **tokens** (lexer) y luego en un **árbol sintáctico**
   (parser), ambos generados por ANTLR.
2. El **`EvalVisitor`** recorre el árbol y ejecuta cada nodo.
3. Las variables viven en un **heap simulado** con punteros; las matrices se
   almacenan como **bloques contiguos en C**.
4. El cálculo pesado de matrices baja a **C** (o a un *fallback* en Python).

---

## 4. Instalación y uso

### 4.1 Requisitos

- **Python 3.10+**
- **Java Runtime** (solo si vas a regenerar el parser con ANTLR)
- **Compilador de C** opcional (GCC/MinGW/MSVC) para el núcleo nativo
- **Redis** opcional (si no está, se usa disco automáticamente)

### 4.2 Dependencias

```bash
python -m venv venv
# Windows: venv\Scripts\activate    |  Linux/Mac: source venv/bin/activate
python -m pip install -r requirements.txt
```

> El núcleo del lenguaje no necesita paquetes externos. `requirements.txt`
> incluye `antlr4-python3-runtime` (runtime del parser) y, opcionalmente,
> `redis` (persistencia).

### 4.3 Compilar el núcleo en C (opcional pero recomendado)

```bash
# Windows (MinGW o MSVC)
build_dknumpy.bat        # genera src/dknumpy.dll

# Linux / Mac
bash build_dknumpy.sh    # genera src/libdknumpy.so
```

Si no compilas, todo sigue funcionando con el *fallback* en Python.
`dump_memory()` indica el backend activo (`C-native` o `python-fallback`).

### 4.4 Regenerar el parser (solo si cambias la gramática)

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener -o src grammar/grammarDKN.g4
```

### 4.5 Ejecutar

```bash
python src/interpreterDKN.py
```

- Escribe la ruta de un `.dkn` (p. ej. `../tests/regresion_lineal.dkn`) para
  ejecutarlo.
- O presiona **Enter** para entrar al **REPL** interactivo.

---

## 5. Referencia del lenguaje (sintaxis)

DKNexus usa sintaxis tipo C: **bloques con llaves `{ }`** y **sentencias
terminadas en `;`**.

### 5.1 Comentarios

```dkn
// Comentario de una línea
```

### 5.2 Variables y tipos

No se declara el tipo; se infiere del valor. Tipos: `int`, `float`, `bool`,
`str`, `list`, `matrix`, `dict`, `none`.

```dkn
x = 10;              // int
pi_aprox = 3.1416;   // float
nombre = "Ada";      // str
activo = 1 == 1;     // bool
v = [1, 2, 3];       // list (vector)
m = [[1, 2], [3, 4]]; // matrix
d = {"lr": 0.01};    // dict
```

### 5.3 Operadores

| Categoría | Operadores |
|---|---|
| Aritméticos | `+`  `-`  `*`  `/`  `%`  `^` (potencia) |
| Comparación | `==`  `!=`  `<`  `>`  `<=`  `>=` |
| Lógicos | `and`  `or`  `not` (con cortocircuito) |
| Unario | `-` (negación) |

### 5.4 Control de flujo

```dkn
if (x > 0) {
    print("positivo");
}

while (i < 10) {
    i = i + 1;
}

for (k = 0; k < 5; k = k + 1) {
    print(k);
}
```

> Nota: el núcleo implementa `if` (sin `else`). El patrón `if/else` se modela con
> dos `if` de condiciones complementarias (`>= 0.5` y `< 0.5`), como en los
> tests de clasificación.

### 5.5 Funciones (parámetros y retorno)

La palabra clave de retorno es **`retornar`** (no `return`).

```dkn
function suma(a, b) {
    retornar a + b;
}

print(suma(10, 20));   // 30
```

Soporta **recursividad** y aislamiento de ámbito (cada llamada tiene su scope):

```dkn
function factorial(n) {
    if (n <= 1) { retornar 1; }
    retornar n * factorial(n - 1);
}
```

### 5.6 Estructuras de datos

```dkn
// Listas y matrices
v = [10, 20, 30];
print(v[0]);            // acceso
v[1] = 99;              // asignación por índice

// Pilas (LIFO)
push(pila, 1); push(pila, 2);
print(pop(pila));       // 2

// Colas (FIFO)
enqueue(cola, "A"); enqueue(cola, "B");
print(dequeue(cola));   // "A"

// Diccionarios (tabla hash propia)
persona = {"nombre": "Ada", "edad": 36};
print(persona["nombre"]);
persona["edad"] = 37;
print(has(persona, "edad"));   // True
```

---

## 6. Librería estándar (built-ins)

### 6.1 Matemática (vía `mathDKN`, sin `import math`)

Disponibles como expresiones del lenguaje:

| Función | Descripción | Implementación |
|---|---|---|
| `sin(x)` `cos(x)` `tan(x)` | trigonometría | Series de Taylor |
| `tanh(x)` | tangente hiperbólica | vía `exp` |
| `sqrt(x)` | raíz cuadrada | Newton-Raphson |
| `root(x, y)` | raíz y-ésima | `exp(log(x)/y)` |
| `log(x)` `log10(x)` | logaritmos | serie de `ln` |
| `abs(x)` `floor(x)` `ceil(x)` | utilidades | a mano |
| `PI` `E` `INF` | constantes | series propias |

### 6.2 Estadística y datos

| Función | Descripción |
|---|---|
| `sum(x)` `mean(x)` `min(x)` `max(x)` | reducciones sobre lista o matriz |
| `normalize(v)` | normalización min-max a `[0, 1]` |
| `load_csv(ruta)` | carga un CSV **solo numérico** (sin encabezado ni texto) como matriz |
| `read_csv(ruta)` | CSV real con **comillas, encabezado y columnas mixtas** → dict `{header, rows, n_rows, n_cols}` |
| `csv_col(tabla, j)` | columna `j` (texto o número) de una tabla `read_csv` |
| `csv_col_num(tabla, j)` | columna `j` solo valores numéricos (para ML/estadística) |
| `get_col(m, j)` / `set_col(m, j, v)` | columnas de una matriz |

### 6.3 Álgebra de matrices (vía `matrixDKN` → C)

| Operación | Cómo |
|---|---|
| Suma / resta | `a + b`, `a - b` (matrices del mismo tamaño) |
| Producto matricial | `a * b` |
| Escalar | `a * k` |
| Transpuesta | `trans(m)` |
| Inversa | `inv(m)` (Gauss-Jordan) |

### 6.4 I/O e introspección

| Función | Descripción |
|---|---|
| `print(x)` | imprime un valor |
| `input_prompt(mensaje)` | lee una línea de texto desde la consola |
| `input_num(mensaje)` | lee un número desde la consola |
| `read(ruta)` / `write(ruta, txt)` | archivos de texto |
| `len(x)` `type(x)` `str(x)` `repr(x)` | utilidades de tipo |
| `isinstance(x, "tipo")` | chequeo de tipo |
| `id(x)` `dir(x)` `help(x)` | introspección |
| `dump_memory()` | imprime el estado del heap |

### 6.5 Persistencia (vía `persistDKN`: Redis o disco)

| Función | Descripción |
|---|---|
| `redis_set(clave, valor)` | guarda (serializado en JSON) |
| `redis_get(clave)` | recupera con su tipo original |
| `redis_del(clave)` `redis_exists(clave)` `redis_keys()` | gestión |
| `store_backend()` | `"redis"` o `"disk"` |

> Si no hay servidor Redis en `127.0.0.1:6379`, se usa un único archivo
> `.dknexus_store.json`. Configurable con `DKN_REDIS_HOST` / `DKN_REDIS_PORT`.

---

## 7. DKNumpy: núcleo numérico en C

`dknumpy.c` + `dknumpyDKN.py` reemplazan el almacenamiento de matrices como
listas de listas por **memoria contigua** (igual que NumPy):

- Una matriz `A(filas, columnas)` se aplana en un bloque de `filas * columnas`
  `double` reservado con `malloc`. El elemento `(i, j)` se ubica en
  `indice = i * columnas + j`.
- Python (vía `ctypes`) solo envía **punteros**; el cómputo corre en C:

| Símbolo C | Operación |
|---|---|
| `dknp_matmul` | multiplicación de matrices |
| `dknp_add` / `dknp_sub` | suma / resta elemento a elemento |
| `dknp_scalar_mul` | producto por escalar |
| `dknp_transpose` | transpuesta |
| `dknp_update_weights` | **`w = w - lr * grad`** (descenso de gradiente) |
| `dknp_dot` | producto punto |

**Ejemplo de dimensiones** (`mat A(2,3) * mat B(3,4) = C(2,4)`): la validación de
dominio está en `matrixDKN.matrix_mul` (verifica que columnas de A == filas de B)
y el cómputo baja a `dknp_matmul`.

> Si la librería nativa no está compilada, `dknumpyDKN.py` usa un **fallback
> puro en Python** (también sobre memoria contigua con `ctypes`). La API es
> idéntica en ambos modos.

---

## 8. Gestión de memoria y seguridad

### 8.1 Heap + punteros + scopes

| Componente | Rol |
|---|---|
| `HeapManager` (`heapDKN.py`) | RAM simulada: direcciones `0x001`, `0x002`, … |
| `self.scopes` | pila de ámbitos; cada variable guarda un **puntero**, no el valor |
| `_assign_var` / `_lookup_var` | reservar / resolver nombre → puntero → valor |
| `_push_scope` / `_pop_scope` | entrar/salir de función; libera celdas del ámbito muerto |

- El heap es **dinámico** por defecto (sin tope rígido), apto para vectores y
  matrices grandes. Se puede fijar un tope (`HeapManager(max_slots=N)`) para
  pruebas; al excederlo lanza `DKNMemoryError`.
- Las matrices se guardan como **bloques contiguos en C** y el heap registra su
  puntero; al liberar el ámbito se llama al `free` de C.

### 8.2 Execution Guard (anti bucles infinitos)

- Un **contador global de instrucciones** (`_bump_instruction`) se incrementa en
  cada nodo crítico y en los bucles matemáticos.
- Al superar `instruction_limit` (1.000.000 por defecto) se lanza
  `DKNRuntimeError` con mensaje de *timeout / bucle infinito*.

### 8.3 Jerarquía de errores

| Error | Contexto |
|---|---|
| `DKNParseError` | errores léxicos / sintácticos |
| `DKNRuntimeError` | errores semánticos / de ejecución |
| `DKNMemoryError` | heap sin capacidad |

---

## 9. Machine Learning y Deep Learning

Todo el ML/DL está implementado **a mano**, sin numpy ni scikit-learn. La API de
alto nivel imita a scikit-learn (`fit`/`predict`) y el entrenamiento usa el
optimizador de **descenso de gradiente** del núcleo en C.

### 9.1 Optimizador

| Función | Descripción |
|---|---|
| `update_weights(w, grad, lr)` | actualiza pesos `w = w - lr * grad` (nativo en C) |
| `dot(a, b)` | producto punto de dos vectores 1D |

### 9.2 Activaciones

| Función | Descripción |
|---|---|
| `sigmoid(z)` | `1 / (1 + e^-z)`, con saturación anti-overflow (regresión logística / MLP) |
| `escalon(z)` | salto de Heaviside: `1.0` si `z >= 0`, si no `0.0` (perceptrón clásico) |

### 9.3 Métricas

| Función | Descripción |
|---|---|
| `mse(y_real, y_pred)` | error cuadrático medio (regresión) |
| `exactitud(y_real, y_pred)` | accuracy en clasificación binaria |
| `precision(y_real, y_pred)` | precisión `TP / (TP + FP)` (0.0 si no hay positivos predichos) |
| `matriz_confusion(y_real, y_pred)` | imprime TN/FP/FN/TP |

### 9.4 Gráficos (canvas ASCII)

| Función | Descripción |
|---|---|
| `graficar_dispersion(X, Y)` | nube de puntos en texto (~40×15) |
| `graficar_linea(X, Y, W)` | dispersión + recta `y = W[0] + W[1]·x` |

### 9.5 Red Neuronal Multicapa (MLP, estilo scikit-learn)

| Función | Descripción |
|---|---|
| `mlp_init([n_in, n_hid, n_out])` | crea la red `{W1, b1, W2, b2}` con pesos aleatorios pequeños |
| `mlp_fit(red, X, Y, lr, epochs)` | entrena con **backpropagation** (forward + regla de la cadena) |
| `mlp_predict(red, X)` | forward pass; devuelve predicciones binarias (`>= 0.5 → 1`) |

El backprop usa la derivada de la sigmoide `A·(1−A)` y todo el álgebra
(`matmul`, `transpose`, suma de bias por *broadcast*, sigmoide elemento a
elemento) está escrita en Python puro y protegida por el *execution guard*.

### 9.6 Agrupamiento y vecindad

| Función | Descripción |
|---|---|
| `knn(X_train, Y_train, x_query, k)` | clasificación supervisada por **k-vecinos** más cercanos (distancia euclídea + voto mayoritario) |
| `kmeans(X, k, iters)` | **agrupamiento no supervisado**: asigna cada punto al centroide más cercano y recalcula centroides; devuelve un vector con la etiqueta de cluster de cada punto |

`kmeans` usa **inicialización determinista** (los primeros `k` puntos de `X`, sin
`random`) para que los tests sean reproducibles. Ambos calculan distancias con
`mathDKN.sqrt` y operaciones nativas, sin librerías externas.

### 9.7 Modelos implementados ↔ referencias

| Modelo DKNexus | Equivalente | Test |
|---|---|---|
| Regresión lineal (gradiente descendente) | `SGDRegressor` / Grokking | `tests/regresion_lineal.dkn` |
| Perceptrón clásico (escalón, online) | `Perceptron` | `tests/clasificacion_binaria.dkn` |
| Regresión logística (sigmoide, batch GD) | `LogisticRegression` | `tests/clasificacion_binaria.dkn` |
| MLP para XOR (1 capa oculta) | `MLPClassifier` | `tests/mlp_xor.dkn` |
| k-vecinos (clasificación) | `KNeighborsClassifier` | `tests/clustering_knn.dkn` |
| k-means (agrupamiento) | `KMeans` | `tests/clustering_knn.dkn` |

### 9.8 Ejemplo mínimo (regresión lineal)

```dkn
print("--- Entrenando Regresion Lineal ---");
X = [1.0, 2.0, 3.0, 4.0];
Y = [2.0, 4.0, 6.0, 8.0];   // y = 2x
W = [0.0, 0.0];             // W[0]=bias, W[1]=pendiente
lr = 0.01;

for (epoca = 0; epoca < 50; epoca = epoca + 1) {
    grad = [0.0, 0.0];
    for (i = 0; i < len(X); i = i + 1) {
        pred = W[0] + W[1] * X[i];
        error = pred - Y[i];
        grad[0] = grad[0] + error;
        grad[1] = grad[1] + error * X[i];
    }
    W = update_weights(W, grad, lr);
}
print(W);
graficar_linea(X, Y, W);
```

### 9.9 Ejemplo mínimo (MLP / XOR)

```dkn
X = [[0.0,0.0],[0.0,1.0],[1.0,0.0],[1.0,1.0]];
Y = [[0.0],[1.0],[1.0],[0.0]];
red = mlp_init([2, 4, 1]);
red = mlp_fit(red, X, Y, 0.5, 5000);
print(mlp_predict(red, X));    // [0.0, 1.0, 1.0, 0.0]
```

### 9.10 Ejemplo mínimo (KNN y K-Means)

```dkn
// k-vecinos (clasificación supervisada)
X_train = [[1.0,1.0],[1.5,1.0],[8.0,8.0],[9.0,8.0]];
Y_train = [0.0, 0.0, 1.0, 1.0];
print(knn(X_train, Y_train, [8.5, 8.5], 3));   // 1.0

// k-means (agrupamiento no supervisado)
X_cluster = [[1.0],[2.0],[10.0],[11.0]];
print(kmeans(X_cluster, 2, 10));               // [0.0, 0.0, 1.0, 1.0]
```

---

## 10. Estructura del proyecto

```text
DKNexus/
├─ grammar/
│  └─ grammarDKN.g4              # gramática ANTLR (léxico + sintaxis)
├─ src/
│  ├─ interpreterDKN.py          # intérprete (EvalVisitor) + REPL
│  ├─ heapDKN.py                 # heap dinámico + punteros + scopes
│  ├─ mathDKN.py                 # matemática propia (sin import math)
│  ├─ matrixDKN.py               # álgebra de matrices (delega a C)
│  ├─ dknumpy.c                  # núcleo numérico nativo (C)
│  ├─ dknumpyDKN.py              # binding ctypes + fallback Python
│  ├─ persistDKN.py              # persistencia Redis / disco
│  ├─ dataDKN.py                 # carga de CSV
│  └─ grammarDKN*.py             # lexer/parser/visitor generados por ANTLR
├─ tests/                        # programas .dkn de ejemplo
├─ build_dknumpy.sh / .bat       # compilan la librería nativa
├─ requirements.txt
└─ README.md
```

---

## 11. Tests incluidos

| Categoría | Archivos |
|---|---|
| **ML / DL (básico)** | `regresion_lineal.dkn`, `clasificacion_binaria.dkn`, `mlp_xor.dkn`, `clustering_knn.dkn`, `test_ml_metricas.dkn` |
| **ML / DL (integral + estrés + errores)** | `test_dl_completo.dkn` (pipeline completo con gráficos), `test_dl_estres.dkn` (datasets grandes, MLP de 8 ocultas, 3 clusters), `test_dl_errores.dkn` (catálogo de errores forzados) |
| **Datos reales (CSV)** | `test_data_csv.dkn`, `regresion_ingresos_data.dkn` + `data.csv` (~10 280 filas; regresión 80/20 edad+sexo+escolaridad → ingreso) |
| Control de flujo / lógica | `flujo_y_logica.dkn`, `test_logica.dkn`, `print_1_a_100.dkn`, `print_impares_1_a_100.dkn` |
| Funciones / recursividad | `euclides.dkn`, `euclides_iterativo.dkn`, `euclides_recursivo.dkn`, `recursividad_scoop.dkn`, `burbuja.dkn` |
| Matrices / estructuras | `test_matrices.dkn`, `matrices_y_estructuras.dkn`, `test_matriz_singular.dkn`, `test_diccionarios.dkn`, `test_pilas_colas.dkn` |
| Datos / archivos | `archivos.dkn`, `test_files.dkn`, `procesamiento_datos.dkn`, `test_csv_resiliencia.dkn` |
| Matemática / límites | `taylor.dkn`, `tan_pi_sobre_2.dkn`, `test_limites_math.dkn`, `test_infinito.dkn`, `aritmetica_y_errores.dkn` |
| Memoria / persistencia | `test_heap_stress.dkn`, `test_persistencia.dkn` |

Ejecutar uno (desde `src/`):

```bash
python -c "import interpreterDKN as I; I.run(open(r'../tests/mlp_xor.dkn',encoding='utf-8').read())"
```

---

## 12. Qué puede y qué NO puede hacer (límites)

**Puede:**

- Aritmética, lógica, control de flujo, funciones y recursividad.
- Vectores, matrices `n×m`, diccionarios, pilas y colas.
- Álgebra lineal acelerada en C; matemática por series propias.
- Entrenar regresión lineal, regresión logística, perceptrón y un MLP.
- Agrupamiento (`kmeans`) y clasificación por vecindad (`knn`).
- Métricas (incl. `precision`), gráficos ASCII, persistencia y carga de CSV.

**No puede (por diseño / aún no):**

- **`if/else` nativo** (se modela con dos `if`).
- Activaciones distintas a sigmoide/escalón (ReLU, softmax) — *no incluidas*.
- Más de una capa oculta en el MLP (arquitectura fija `[in, hidden, out]`).
- `string` como clave numérica mixta avanzada, slicing de listas, `break`/`continue`.
- Cualquier librería externa de cálculo (es una restricción intencional).

---

## 13. Pendientes / Roadmap

Los tres cortes están **completos** (predicción, clasificación y agrupamiento).
Posibles extensiones futuras (no requeridas):

1. **Más activaciones** (ReLU, softmax) y MLP con número de capas variable.
2. **k-means con inicialización k-means++** (hoy es determinista por simplicidad).
3. **Métricas adicionales** (recall, F1) a partir de la matriz de confusión.
4. **`if/else` nativo** en la gramática.

---

## 14. Referencias y licencia

**Referencias de diseño:**

- **NumPy** — modelo de memoria contigua para vectores/matrices (núcleo en C).
- **scikit-learn** — API `fit` / `predict` y los modelos
  (`SGDRegressor`, `Perceptron`, `LogisticRegression`, `MLPClassifier`).
- **Grokking** — regresión y backpropagation por gradiente descendente iterativo.
- **ANTLR 4** — generación de lexer/parser y patrón Visitor.
- **Redis** — almacén clave-valor en memoria para persistencia ligera.

**Licencia:** proyecto académico para la asignatura de Lenguajes de Programación
y Transducción, enfocado en diseño de DSL, análisis sintáctico, construcción de
runtimes controlados e implementación de ML/DL desde cero.
