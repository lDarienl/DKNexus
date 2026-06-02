# DKNexus DSL

**DKNexus** es un **Lenguaje de Dominio Específico (DSL)** orientado a flujos de trabajo de **Deep Learning y cómputo numérico**, construido con:

- **ANTLR4** para análisis léxico/sintáctico.
- **Python 3** para el intérprete (`Visitor`).
- Librerías matemáticas propias sin dependencias externas de álgebra/cálculo.

Este documento describe la implementación completa hasta el **Segundo Corte**.

---

## Introducción y Propósito

DKNexus nace para ejecutar programas numéricos con:

1. **Semántica controlada** (gramática fija y validación estricta).
2. **Gestión explícita de memoria** (Heap y punteros).
3. **Portabilidad** (cero dependencia de `math`/`numpy` para la base del lenguaje).
4. **Valor educativo** (algoritmos implementados desde cero).

Su objetivo académico es demostrar cómo construir un DSL robusto para problemas cercanos a Deep Learning (operaciones numéricas, álgebra lineal, control de flujo y estructuras de datos) sin delegar toda la complejidad al runtime de Python.

---

## Arquitectura de Memoria (Heap + Punteros)

La capa más fuerte de DKNexus es su modelo de memoria manual:

| Componente | Rol |
|---|---|
| `HeapManager` (`src/heapDKN.py`) | Simula RAM con direcciones hex (`0x001`, `0x002`, ...) |
| `self.scopes` | Pila de ámbitos; cada variable guarda un **puntero** (no el valor directo) |
| `_assign_var` | Reserva en heap, guarda valor, devuelve/actualiza dirección |
| `_lookup_var` | Resuelve nombre -> puntero -> valor en heap |
| `_pop_scope` | Libera automáticamente celdas del ámbito que muere |

### Heap dinámico + bloques contiguos en C (DKNumpy)

Para soportar vectores y matrices grandes de Machine Learning, el heap se rediseñó:

- **Ya no hay límite rígido de 1024 slots.** Por defecto el heap es **dinámico**
  (`max_slots=None`): crece según se necesite. El tope sigue siendo configurable
  para pruebas (`HeapManager(max_slots=...)`).
- Las **matrices ya no se guardan como listas de listas** dentro del heap. Se
  delegan al binding de C (`dknumpyDKN`): se reserva un **bloque CONTIGUO** de
  memoria con `malloc` y el heap **registra el puntero** de ese bloque
  (`self.pointers[addr]`). `dump_memory()` muestra ese puntero como
  `@bloque_C=0x...`.
- La lectura (`read`) reconstruye la lista de listas a partir del bloque contiguo
  para el resto del intérprete (compatibilidad total con el lenguaje).

### ¿Por qué este modelo?

No se delega el control total al recolector de Python. Este enfoque permite:

- comportamiento más **determinista** de recursos,
- trazabilidad de referencias activas,
- validación de presión de memoria por **slots**,
- simulación realista de un runtime de lenguaje.

### Pila de Ámbitos (Scope Stack)

El intérprete mantiene una pila:

```text
scopes = [
  { ... global ... },
  { ... función actual ... },
  ...
]
```

- Al entrar a función: `_push_scope()`
- Al salir: `_pop_scope()`
- La búsqueda de variables es de adentro hacia afuera (resolución léxica anidada).

Esto habilita recursividad y aislamiento local/global.

### Gestión por slots y liberación

El heap reporta el uso en *slots* (peso aproximado de cada celda):

- número/bool/None: `1` slot
- matriz: `filas * columnas` slots
- string/lista: peso derivado del contenido

Por defecto el heap es **dinámico** (no lanza `DKNMemoryError` por tamaño). Si se
fija un tope explícito (`HeapManager(max_slots=N)`) y se excede, se lanza
**`DKNMemoryError`**.

Al destruir un scope, sus direcciones se liberan en `_pop_scope` (GC básico por
vida de ámbito). Para matrices, esto llama además al `free` de C que libera el
bloque contiguo (`dknp_free`).

---

## DKNumpy: núcleo numérico con binding de C (`ctypes`)

`DKNumpy` (`src/dknumpy.c` + `src/dknumpyDKN.py`) reemplaza el almacenamiento de
matrices como listas de listas por **memoria contigua**:

- Una matriz `A(filas, columnas)` se aplana en un arreglo plano de
  `filas * columnas` posiciones reservado con `malloc` en C.
- El acceso al elemento `(i, j)` se resuelve por aritmética de punteros:

```text
indice = i * columnas + j
```

- Python (vía `ctypes`) solo envía los **punteros** de los bloques; el cómputo
  pesado se ejecuta en C a velocidad nativa:
  - `dknp_matmul` → multiplicación de matrices,
  - `dknp_add` / `dknp_sub` / `dknp_scalar_mul` → operaciones elemento a elemento,
  - `dknp_transpose` → transpuesta,
  - `dknp_update_weights` → **ajuste de pesos** `w = w - lr * grad` (ML),
  - `dknp_dot` → producto punto.

`matrixDKN.py` delega en `DKNumpy` la multiplicación, suma/resta y producto por
escalar (preservando enteros cuando la operación es exacta).

### Compilar la librería nativa

```bash
# Linux / Mac
bash build_dknumpy.sh        # genera src/libdknumpy.so

# Windows (MinGW o MSVC)
build_dknumpy.bat            # genera src/dknumpy.dll
```

> Si no hay compilador de C disponible, `dknumpyDKN.py` usa automáticamente un
> **fallback puro en Python** (también sobre memoria contigua `ctypes`), de modo
> que el intérprete sigue funcionando. `dump_memory()` indica qué backend está
> activo (`C-native` o `python-fallback`).

---

## Librerías Nativas (Cero dependencias externas)

### `mathDKN.py` (sin `import math`)

La librería matemática base se implementa a mano para controlar precisión/errores:

- trigonometría por **Series de Taylor** (`sin`, `cos`, `tan`, `tanh`)
- raíces por **Newton-Raphson** (`sqrt`)
- logaritmos y exponenciales por aproximaciones numéricas (`log`, `log10`, `exp`)
- constantes propias (`PI`, `E`, `INF`)

Se incorporan validaciones de dominio (ej. blindaje de tangente cerca de `PI/2`).

### `matrixDKN.py` (sin NumPy, con binding propio de C)

Álgebra lineal con matrices **dinámicas `n x m`**:

- validación estructural (`matrix_dimensions`, `is_matrix`)
- suma/resta matricial → delegada a **DKNumpy (C)**
- multiplicación matricial y escalar → delegada a **DKNumpy (C)**
- transpuesta → delegada a **DKNumpy (C)** (memoria contigua)
- inversa para matriz cuadrada por **Gauss-Jordan** (en Python)

El cómputo pesado corre sobre memoria contigua en C (`dknumpy.c`); la validación
de dominio y la inversa exacta permanecen en Python.

---

## Resiliencia y Seguridad (Execution Guard)

DKNexus incorpora un guardián de ejecución para proteger la máquina host:

| Mecanismo | Descripción |
|---|---|
| Contador global de instrucciones | Se incrementa por visita/nodo crítico del AST |
| Límite configurable (`instruction_limit`) | Corta ejecución excesiva |
| Excepción de protección | `DKNRuntimeError` con mensaje de timeout/bucle infinito |

Esto evita loops no acotados que saturen CPU, especialmente en `while` y `for`.

### Jerarquía práctica de errores

| Error | Contexto |
|---|---|
| `DKNParseError` | Errores léxicos/sintácticos |
| `DKNRuntimeError` | Errores semánticos o de ejecución |
| `DKNMemoryError` | Heap sin slots / objeto no alojable |

---

## Componentes del Lenguaje

### 1) Lógica

- Operadores lógicos: `and`, `or`, `not`
- Cortocircuito en `and`/`or`
- Truthiness estilo Python (`0`, vacío y `None` son falso; resto verdadero)

### 2) Control de flujo

- `if (...) { ... }`
- `while (...) { ... }`
- `for (init; cond; update) { ... }`

> Nota: el núcleo actual implementa `if`; los flujos tipo `if/else` se modelan con composición de condiciones y bloques.

### 3) Estructuras de datos

- **Pilas (LIFO)**: `push`, `pop`
- **Colas (FIFO)**: `enqueue`, `dequeue`
- **Listas** y **matrices** como literales
- **Diccionarios** (tablas hash clave-valor): literal `{ }`, acceso/asignación `d[clave]`

#### Diccionarios nativos (tablas hash)

Implementados en la **gramática** (regla `DictLiteral` + `dictEntry`) y en el
**Visitor** (`visitDictLiteral`). Permiten búsqueda en tiempo O(1) sin recorrer
listas. Las claves admitidas son strings o números.

```dkn
persona = {"nombre": "Ada", "edad": 36};
print(persona["nombre"]);   // Ada
persona["edad"] = 37;        // actualizar
persona["lenguaje"] = "DKN"; // insertar
```

Utilidades sobre diccionarios:

| Función | Descripción |
|---|---|
| `dict()` | crea un diccionario vacío |
| `len(d)` | número de pares clave-valor |
| `keys(d)` | lista de claves |
| `values(d)` | lista de valores |
| `has(d, clave)` | `True`/`False` si la clave existe |
| `del(d, clave)` | elimina la clave y devuelve su valor |
| `type(d)` | `"dict"` |

### 3.1) Persistencia ultra-liviana (Redis + fallback a disco)

`persistDKN.py` guarda estado clave-valor en **RAM** mediante **Redis** (cliente
nativo de Python). Ideal para guardar el estado de los pesos de un modelo de ML:

```dkn
redis_set("modelo_pesos", [0.5, -0.2, 0.13]);
redis_set("hiperparams", {"lr": 0.01, "epochs": 100});

pesos = redis_get("modelo_pesos");   // [0.5, -0.2, 0.13] (con su tipo original)
print(redis_keys());                 // claves almacenadas
print(redis_exists("modelo_pesos")); // True
redis_del("modelo_pesos");
```

| Función | Descripción |
|---|---|
| `redis_set(clave, valor)` | guarda un valor (serializado en JSON) |
| `redis_get(clave)` | recupera el valor con su tipo original (o `None`) |
| `redis_del(clave)` | elimina la clave (`True` si existía) |
| `redis_exists(clave)` | `True`/`False` |
| `redis_keys()` | lista de claves |
| `store_backend()` | backend activo: `"redis"` o `"disk"` |

> Si la librería `redis` no está instalada o no hay servidor escuchando en
> `127.0.0.1:6379`, DKNexus usa automáticamente un **fallback a disco** (un único
> archivo `.dknexus_store.json`). Configurable con las variables de entorno
> `DKN_REDIS_HOST` / `DKN_REDIS_PORT`.

### 4) I/O y utilidades nativas

- Archivos: `read(ruta)`, `write(ruta, contenido)`
- Introspección/runtime:
  - `len(x)`
  - `type(x)`
  - `dump_memory()`
  - `id(x)`
  - `isinstance(x, tipo)`
  - `dir(x)`
  - `help(x)`
  - `repr(x)`
  - `str(x)`
  - `print(x)`

### 5) Funciones de usuario

Definición:

```dkn
function nombre(p1, p2) {
    // statements
    return p1 + p2;
}
```

Llamada:

```dkn
print(nombre(10, 20));
```

---

## Justificación Técnica

DKNexus es sólido para el Segundo Corte por tres razones:

1. **Control explícito de recursos**  
   El runtime administra su heap con punteros y cuotas de memoria.

2. **Seguridad de ejecución**  
   El guardián de instrucciones previene bucles infinitos y abuso de CPU.

3. **Profundidad educativa**  
   Algoritmos matemáticos y matriciales implementados manualmente facilitan comprender la mecánica real detrás de bibliotecas de alto nivel.

---

## Arquitectura del Proyecto

```text
DKNexus/
├─ grammar/
│  └─ grammarDKN.g4
├─ src/
│  ├─ interpreterDKN.py
│  ├─ heapDKN.py                # heap dinámico + bloques contiguos
│  ├─ mathDKN.py
│  ├─ matrixDKN.py             # delega cómputo pesado a DKNumpy
│  ├─ dknumpy.c                # núcleo numérico nativo (C)
│  ├─ dknumpyDKN.py            # binding ctypes + fallback Python
│  ├─ persistDKN.py            # persistencia Redis + fallback a disco
│  ├─ grammarDKNLexer.py        # generado por ANTLR
│  ├─ grammarDKNParser.py       # generado por ANTLR
│  └─ grammarDKNVisitor.py      # generado por ANTLR
├─ build_dknumpy.sh            # compila libdknumpy.so
├─ build_dknumpy.bat           # compila dknumpy.dll
├─ tests/
│  └─ *.dkn
└─ README.md
```

---

## Instrucciones de Uso

## 1) Requisitos

- Java Runtime (para ANTLR4)
- Python 3.10+ (recomendado)
- entorno virtual (`venv`)

## 2) Instalar dependencias

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 3) Generar parser/lexer con ANTLR4

Desde la raíz del proyecto (con el alias `antlr4` o con el jar completo):

```bash
# Opción A: alias antlr4
antlr4 -Dlanguage=Python3 -visitor -no-listener -o src grammar/grammarDKN.g4

# Opción B: jar completo + Java (necesario para regenerar tras cambios en la gramática)
java -jar tools/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener -o gen_tmp grammar/grammarDKN.g4
# luego copiar gen_tmp/grammar/grammarDKN*.py a src/
```

> Cada cambio en `grammar/grammarDKN.g4` (p. ej. el literal de diccionarios
> `DictLiteral`) requiere regenerar los archivos ANTLR.

## 4) Ejecutar intérprete

```bash
python3 src/interpreterDKN.py
```

Al iniciar:

- Ingresa ruta de archivo `.dkn` para ejecución directa.
- O presiona Enter para entrar a modo interactivo (REPL).

---

## Ejemplos rápidos

### Lógica y control

```dkn
i = 1;
while (i <= 5 and not (i == 3)) {
    print(i);
    i = i + 1;
}
```

### Matrices dinámicas

```dkn
a = [[1,2,3],[4,5,6]];
print(trans(a));
```

### Estado del heap

```dkn
x = [[1,0],[0,1]];
dump_memory();
```

---

## Estado de Entrega (Segundo Corte)

| Ítem | Estado |
|---|---|
| Gramática ANTLR4 + Visitor Python | Completado |
| Heap + punteros + scopes | Completado |
| Execution Guard | Completado |
| Math nativa sin `math` | Completado |
| Matriz dinámica sin NumPy | Completado |
| DKNumpy: memoria contigua + binding de C (`ctypes`) | Completado |
| Heap dinámico con bloques `malloc` y registro de punteros | Completado |
| Diccionarios nativos (tablas hash) en gramática + Visitor | Completado |
| Persistencia ligera Redis con fallback a disco | Completado |
| Lógica (`and`, `or`, `not`) | Completado |
| I/O y built-ins de introspección | Completado |

---

## Licencia y uso académico

Proyecto desarrollado con fines académicos para la asignatura de Lenguajes, enfocado en diseño de DSL, análisis sintáctico y construcción de runtimes controlados.
