# DKNexus

Lenguaje de dominio específico (DSL) para experimentos de **Deep Learning / cálculo numérico**, implementado con:

- **ANTLR v4** para la gramática y el parser.
- **Python 3** para el intérprete, usando el patrón **Visitor**.
- Librerías propias: `mathDKN.py` (math), `matrixDKN.py` (matrices).

El proyecto está configurado para trabajar **solo con el target Python3** (sin Flex/Bison, sin NumPy, sin librerías externas de terceros).

---

## 1. Estructura del proyecto

Después de organizarlo, la estructura recomendada es:

```text
DKNexus/
  README.md
  requirements.txt
  build.sh
  build.bat
  .gitignore

  grammar/
    grammarDKN.g4

  src/
    __init__.py           (puede estar vacío)
    interpreterDKN.py
    mathDKN.py
    matrixDKN.py
    grammarDKNLexer.py
    grammarDKNParser.py
    grammarDKNVisitor.py
    grammarDKNBaseVisitor.py

  tests/
    ejemplos_basicos.dkn
    matrices.dkn
    pilas_colas.dkn
    errores.dkn
    ...
```

- **`grammar/`**: gramática ANTLR (`grammarDKN.g4`).
- **`src/`**: todo el código Python del lenguaje (intérprete + librerías + archivos generados por ANTLR).
- **`tests/`**: programas de prueba escritos en el DSL (`*.dkn`).

> Nota: Si los `.py` generados por ANTLR (`grammarDKN*.py`) están en la raíz, muévelos a `src/` después de correr `build.sh`/`build.bat`.

---

## 2. Qué soporta el DSL

### 2.1. Aritmética y constantes

- **Operadores**: `+ - * / % ^` con precedencia:
  - `^` (potencia) > `* / %` > `+ -`
- **Paréntesis**: `(expr)`
- **Menos unario**: `-expr`
- **Constantes** (case-insensitive):
  - `PI`, `Pi`, `pi`, etc. → constante π
  - `E`, `e` → constante e
  - `INF`, `Inf`, `inf` → infinito

Ejemplos:

```text
print(10 + 2 * 5);     // 20
print((10 + 2) * 5);   // 60
print(2 ^ 3 + 4);      // 12
print(PI * 2);
print(E);
```

### 2.2. Funciones matemáticas (`mathDKN.py`)

- Trigonometría: `sin(x)`, `cos(x)`, `tan(x)`, `tanh(x)`
- Raíces y potencias:
  - `sqrt(x)` – raíz cuadrada
  - `root(x, y)` – raíz y-ésima de x
  - `^` – potencia
- Logaritmos:
  - `log(x)` – log natural
  - `log10(x)` – log base 10
- Misceláneo:
  - `abs(x)`, `floor(x)`, `ceil(x)`

> Todas implementadas **sin `math` ni NumPy**, usando series / Newton-Raphson / transformaciones.

### 2.3. Variables y control de flujo

- Asignación: `x = expr;`
- Lectura: `x` en expresiones.
- Estructuras:

```text
if (condicion) { ... }

while (condicion) { ... }

for (init; cond; update) { ... }
```

Ejemplo:

```text
x = 10;
if (x - 5) { x = 42; }
print(x);      // 42

i = 0;
while (5 - i) { i = i + 1; }
print(i);      // 5
```

### 2.4. Return y programa

- `return expr;` – detiene la ejecución y guarda el valor retornado.
- `return;` – detiene la ejecución sin valor.

En REPL o al ejecutar un archivo, si hay `return expr;` se imprime ese valor al final del bloque/archivo.

### 2.5. Strings

- Literales de string con comillas dobles:

```text
mensaje = "Hola mundo";
print(mensaje);

cola = [];
enqueue(cola, "Primero");
enqueue(cola, "Segundo");
print(dequeue(cola));    // "Primero"
```

Se soporta `\"` dentro de strings para escribir comillas.

### 2.6. Comentarios

- Comentarios de una línea:

```text
// Comentario de línea
x = 3; // comentario al final
```

---

## 3. Pilas, colas y listas

Las listas se representan con corchetes:

```text
lista = [1, 2, 3];
matriz = [[0.5, 0.2], [0.1, 0.8]];
```

### 3.1. Pilas (stack)

- `push(nombre, expr);` → inserta al final (LIFO).
- `pop(nombre)` → devuelve y elimina el último elemento.

```text
historial = [];
push(historial, 0.95);
push(historial, 0.82);
ultimo = pop(historial);
print(ultimo);
```

### 3.2. Colas (queue)

- `enqueue(nombre, expr);` → inserta al final (FIFO).
- `dequeue(nombre)` → devuelve y elimina el primer elemento.

```text
cola = [];
enqueue(cola, "Primero");
enqueue(cola, "Segundo");
print(dequeue(cola));   // "Primero"
print(dequeue(cola));   // "Segundo"
```

Errores:
- Pop/dequeue sobre estructura vacía → error claro.
- Usar `push/enqueue` sobre variable no lista → error semántico.

---

## 4. Matrices 2x2 (`matrixDKN.py`)

Soporte básico de matrices 2x2 (sin NumPy):

- Literales:

```text
W = [[0.5, 0.2], [0.1, 0.8]];
I = [[1, 0], [0, 1]];
```

- Operaciones:
  - `trans(m)` – transpuesta.
  - `inv(m)` – inversa (Gauss-Jordan 2x2 cerrada).
  - `A + B`, `A - B` – suma/resta entre 2x2.
  - `A * B` – multiplicación de matrices 2x2.
  - `A * escalar`, `escalar * A` – multiplicación escalar.

Ejemplo:

```text
W = [[0.5, 0.2], [0.1, 0.8]];
I = [[1, 0], [0, 1]];

W_T = trans(W);
H = W * I;
H_inv = inv(H);

print(H_inv);
```

Errores:
- Dimensiones incorrectas → error de dominio.
- Matriz no 2x2 o singular → error de dominio.

---

## 5. Reglas de identificadores

- **Permitido**: `x`, `y2`, `radio10`, `_tmp`, `a1b2`
- **No permitido**: `1nombre` (un identificador no puede empezar con número).

Si usas algo como `1nombre`, se lanza:

```text
Error: Identificador inválido '1nombre' en Lx:y. Un identificador no puede empezar con número.
```

---

## 6. Manejo de errores

### 6.1. Matemáticos

- División/módulo:
  - `a / 0` → `Error: Imposible dividir entre 0.`
  - `a % 0` → `Error: Imposible calcular módulo entre 0.`
- Potencias:
  - `0 ^ 0` → `Error matemático: 0 ^ 0 es indeterminado.`
  - `0 ^ -n` → `Error matemático: 0 elevado a exponente negativo (división por cero).`
  - Overflow en `^` → `Error de Desbordamiento: El resultado es demasiado grande para ser procesado.`
- `sqrt(x)` con `x < 0`:
  - `Error de Dominio: No se puede calcular la raíz cuadrada de un número negativo.`
- `log(x)` / `log10(x)` con `x <= 0`:
  - `Error de Dominio: El logaritmo solo está definido para números positivos.`
- `root(x, y)` con `x < 0` y `y` par/no-impar-entero:
  - `Error de Dominio: Raíz par de un número negativo produce un número complejo.`
- `tan(x)` con cos(x) ≈ 0:
  - `Error de dominio: Tangente indefinida (división por cero en coseno).`
- Cualquier operación que produzca `NaN` (por ejemplo con `INF`):
  - `Operación inválida: El resultado es un valor indeterminado (NaN).`

### 6.2. Variables

- Usar variable no definida:

```text
print(z);
```

→ `Error Semántico: La variable 'z' no ha sido declarada.`

### 6.3. Sintaxis / Léxico

- Mensajes con formato: `L<linea>:<columna> ...`
- Casos comunes:
  - `missing ';'` → `Falta ';' al final de la instrucción.`
  - `token recognition error at:` → `Token inválido: ...`
  - `mismatched input ',' expecting ')'` → `Llamada a función mal formada: cantidad de argumentos incorrecta.`
  - `no viable alternative` → `Error de sintaxis: expresión/instrucción mal formada.`

En REPL el intérprete **no se cae**: imprime el error y te deja seguir escribiendo.

---

## 7. Cómo correr el lenguaje (Ubuntu)

### 7.1. Dependencias del sistema

```bash
sudo apt update
sudo apt install default-jre python3-pip python3-venv
```

- **default-jre**: necesario para ejecutar el generador ANTLR (JAR).
- **python3-venv**: obligatorio en Ubuntu 24.04+ para evitar `externally-managed-environment` (PEP 668).

### 7.2. Instalar ANTLR4 (JAR) y comando `antlr4`

```bash
cd /tmp
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
sudo mv antlr-4.13.2-complete.jar /usr/local/lib/
echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.13.2-complete.jar"' >> ~/.bashrc
source ~/.bashrc
```

### 7.3. Entorno virtual e instalación

```bash
cd /ruta/a/DKNexus
rm -rf venv
python3 -m venv venv
source venv/bin/activate
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 7.4. Generar lexer/parser/visitor (Python)

Cada vez que cambies `grammar/grammarDKN.g4`:

```bash
./build.sh     # o: antlr4 -Dlanguage=Python3 -visitor -no-listener grammar/grammarDKN.g4
```

`build.sh`:
- Genera `grammarDKNLexer.py`, `grammarDKNParser.py`, `grammarDKNVisitor.py`, `grammarDKNBaseVisitor.py`.
- Los mueve a `src/`.

### 7.5. Ejecutar el intérprete

Con el venv activado:

```bash
cd /ruta/a/DKNexus
python3 src/interpreterDKN.py
```

Luego:

- Para ejecutar un archivo:
  - Escribe la ruta, por ejemplo: `tests/ejemplos_basicos.dkn`
- Para entrar al REPL:
  - Presiona Enter sin escribir ruta.

En REPL:
- Escribes varias líneas.
- Dejas una línea vacía para ejecutar el bloque.
- Se muestra `>>> Ejecutado.` al terminar el bloque.

---

## 8. Archivos clave (resumen)

- **`grammar/grammarDKN.g4`**: gramática del lenguaje.
- **`src/interpreterDKN.py`**: intérprete principal, REPL, manejo de errores.
- **`src/mathDKN.py`**: librería matemática propia.
- **`src/matrixDKN.py`**: operaciones de matrices 2x2.
- **`src/grammarDKN*.py`**: archivos generados por ANTLR (no editar a mano).
- **`tests/*.dkn`**: programas de ejemplo / pruebas.

Limpieza:
- `*.java`, `*.class` y restos de gramáticas antiguas no se usan.
- `.gitignore` ya ignora `venv/`, `__pycache__/`, `*.pyc`, `*.java`, `*.class`, etc.
