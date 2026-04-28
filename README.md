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

El heap tiene límite configurable (por defecto 1024 slots):

- número/bool/None: `1` slot
- matriz: `filas * columnas` slots
- string/lista: peso derivado del contenido

Si no hay espacio, se lanza **`DKNMemoryError`**.

Al destruir un scope, sus direcciones se liberan en `_pop_scope` (GC básico por vida de ámbito).

---

## Librerías Nativas (Cero dependencias externas)

### `mathDKN.py` (sin `import math`)

La librería matemática base se implementa a mano para controlar precisión/errores:

- trigonometría por **Series de Taylor** (`sin`, `cos`, `tan`, `tanh`)
- raíces por **Newton-Raphson** (`sqrt`)
- logaritmos y exponenciales por aproximaciones numéricas (`log`, `log10`, `exp`)
- constantes propias (`PI`, `E`, `INF`)

Se incorporan validaciones de dominio (ej. blindaje de tangente cerca de `PI/2`).

### `matrixDKN.py` (sin NumPy)

Álgebra lineal implementada desde cero con matrices **dinámicas `n x m`**:

- validación estructural (`matrix_dimensions`, `is_matrix`)
- suma/resta matricial
- multiplicación matricial y escalar
- transpuesta
- inversa para matriz cuadrada por **Gauss-Jordan**

Este enfoque es clave para comprender cómo se propagan tensores/matrices sin abstracciones externas.

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
│  ├─ heapDKN.py
│  ├─ mathDKN.py
│  ├─ matrixDKN.py
│  ├─ grammarDKNLexer.py        # generado por ANTLR
│  ├─ grammarDKNParser.py       # generado por ANTLR
│  └─ grammarDKNVisitor.py      # generado por ANTLR
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

Desde la raíz del proyecto:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener -o src grammar/grammarDKN.g4
```

> Cada cambio en `grammar/grammarDKN.g4` requiere regenerar archivos ANTLR.

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
| Lógica (`and`, `or`, `not`) | Completado |
| I/O y built-ins de introspección | Completado |

---

## Licencia y uso académico

Proyecto desarrollado con fines académicos para la asignatura de Lenguajes, enfocado en diseño de DSL, análisis sintáctico y construcción de runtimes controlados.
