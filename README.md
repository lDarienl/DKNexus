# DKNexus

Lenguaje de dominio específico (DSL) implementado con **ANTLR v4** y un **intérprete en Python** usando el patrón **Visitor**.  
Este repo está configurado para trabajar **solo con el target Python3** (sin Flex/Bison, sin Java como runtime).

---

## Qué soporta el DSL (estado actual)

- **Aritmética**: `+ - * / % ^` con precedencia correcta (`^` > `* / %` > `+ -`) y paréntesis.
- **Trigonometría**: `sin(x)`, `cos(x)`, `tan(x)` usando la librería propia `mathDKN.py`.
- **Variables**: asignación `x = expr;` y lectura `x`.
- **Impresión**: `print(expr);`
- **Return**:
  - `return expr;` detiene el programa y guarda el valor retornado.
  - `return;` detiene el programa sin valor.
- **Control de flujo**:
  - `if (expr) { ... }`
  - `while (expr) { ... }`
  - `for (init; cond; update) { ... }`

---

## Sintaxis rápida (ejemplos)

> Todas las sentencias terminan en `;`.

```text
x = 1;
y = 2;
print(x + y);

z = (10 + 2) * 5;
print(z);

print(sin(0));
print(cos(0));
print(tan(0));

i = 0;
while (5 - i) { i = i + 1; }
print(i);

return x ^ 2;
```

---

## Reglas de identificadores (variables)

- **Permitido**: `x`, `y2`, `radio10`, `_tmp`, `a1b2`
- **No permitido**: `1nombre` (un identificador no puede empezar con número)

Si escribes `1nombre`, el intérprete reporta un error con línea/columna.

---

## Manejo de errores (resiliencia)

- **Error matemático**:
  - `a / 0` → `Error: Imposible dividir entre 0.`
  - `a % 0` → `Error: Imposible calcular módulo entre 0.`
- **Errores léxicos/sintácticos**:
  - Se recolectan y se muestran con `L<linea>:<columna> ...`
  - En REPL no crashea: imprime el error y permite seguir.

---

## Cómo correr el lenguaje (Ubuntu)

### 1) Dependencias del sistema

```bash
sudo apt update
sudo apt install default-jre python3-pip python3-venv
```

- **default-jre**: necesario para ejecutar el generador ANTLR (el JAR).
- **python3-venv**: obligatorio en Ubuntu 24.04+ para evitar `externally-managed-environment` (PEP 668).

### 2) Instalar ANTLR4 (JAR) y comando `antlr4`

```bash
cd /tmp
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
sudo mv antlr-4.13.2-complete.jar /usr/local/lib/
echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.13.2-complete.jar"' >> ~/.bashrc
source ~/.bashrc
```

### 3) Crear el entorno virtual e instalar dependencias Python

```bash
cd /ruta/a/DKNexus
rm -rf venv
python3 -m venv venv
source venv/bin/activate
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 4) Generar lexer/parser/visitor (Python)

Cada vez que cambies `grammarDKN.g4`:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
```

Esto genera (regenerables):
- `grammarDKNLexer.py`
- `grammarDKNParser.py`
- `grammarDKNVisitor.py`
- `grammarDKNBaseVisitor.py`

### 5) Ejecutar el intérprete

```bash
source venv/bin/activate
python3 interpreterDKN.py
```

El programa pregunta:
- Ruta de un archivo `.dkn`, o Enter para abrir la consola (REPL).

---

## Estructura del proyecto

### Archivos que editas

- `grammarDKN.g4`: gramática ANTLR (léxico + sintaxis).
- `interpreterDKN.py`: intérprete (Visitor) + REPL + manejo de errores.
- `mathDKN.py`: librería matemática propia (π, factorial, sin, cos, tan).
- `requirements.txt`: dependencias Python (runtime de ANTLR).

### Archivos generados por ANTLR (no editar)

- `grammarDKNLexer.py`, `grammarDKNParser.py`, `grammarDKNVisitor.py`, `grammarDKNBaseVisitor.py`
- `*.interp`, `*.tokens` (metadatos)

Si los borras, se regeneran ejecutando:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
```

### Limpieza / cosas que NO se usan

- `*.java`, `*.class` y archivos de gramáticas antiguas (por ejemplo `DeepLearning*`) **no se usan** en este enfoque.
- `.gitignore` ya incluye reglas para ignorar `venv/`, `__pycache__/`, `*.pyc`, `*.java`, `*.class`, etc.
