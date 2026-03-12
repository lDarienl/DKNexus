# DKNexus

DSL para procesos de Deep Learning (ANTLR v4, enfoque funcional, lenguaje objetivo Python).  
Proyecto usando **solo ANTLR4** (lexer + parser + Visitor en Python).

---

## Comandos en Ubuntu

### 1. Dependencias del sistema

```bash
sudo apt update
sudo apt install default-jre python3-pip python3-venv
```

- **default-jre**: para ejecutar el generador ANTLR (Java).
- **python3-venv**: para crear el entorno virtual y evitar el error *externally-managed-environment* (PEP 668).

### 2. ANTLR4 (generador de lexer/parser)

```bash
cd /tmp
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
sudo mv antlr-4.13.2-complete.jar /usr/local/lib/
echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.13.2-complete.jar"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Entorno virtual (recomendado en Ubuntu)

En Ubuntu 24.04+ no se pueden instalar paquetes con `pip` a nivel de sistema; hay que usar un **entorno virtual**:

```bash
cd /ruta/a/DKNexus
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Cada vez que abras una nueva terminal en el proyecto, activa el venv:

```bash
cd /ruta/a/DKNexus
source venv/bin/activate
```

### 4. Generar lexer, parser y visitor

Con el venv activado (o con `antlr4` en el PATH):

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
```

**Importante:** Si cambias la gramática (`grammarDKN.g4`), vuelve a ejecutar este comando para regenerar el parser y que el intérprete use las etiquetas (# asignacion, # potencia, etc.).

Se generan: `grammarDKNLexer.py`, `grammarDKNParser.py`, `grammarDKNVisitor.py`, `grammarDKNBaseVisitor.py`.

### 5. Ejecutar el intérprete

Con el venv activado:

**Modo interactivo:**

```bash
python3 interpreterDKN.py
```

**Ejecutar un archivo:**

```bash
python3 interpreterDKN.py ejemplo.dkn
```

---

## Resumen rápido (con venv ya creado)

```bash
cd /ruta/a/DKNexus
source venv/bin/activate
antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4   # solo si cambiaste la gramática
python3 interpreterDKN.py
```

---

## Ejemplo de código DSL

```
3 + 5 ;
sin(0) ;
2 ^ 10 ;
if ( 1 ) { 42 ; }
```

Cada expresión debe terminar en `;`.

Archivos del proyecto: Los que editas son grammarDKN.g4, interpreterDKN.py y mathDKN.py. Los grammarDKN*.py se generan con antlr4. DeepLearning* y los .java/.class eran sobras (no corruptos); ya se eliminaron y están en .gitignore. Para regenerar: antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
