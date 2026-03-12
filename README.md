# DKNexus

DSL para procesos de Deep Learning (ANTLR v4, enfoque funcional, lenguaje objetivo Python).  
Proyecto usando **solo ANTLR4** (lexer + parser + Visitor en Python).

---

## Comandos en Ubuntu

### 1. Instalar ANTLR4 y el runtime de Python

```bash
# Java (necesario para el generador antlr4)
sudo apt update
sudo apt install default-jre

# ANTLR4 (JAR y alias)
cd /tmp
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
sudo mv antlr-4.13.2-complete.jar /usr/local/lib/
echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.13.2-complete.jar"' >> ~/.bashrc
source ~/.bashrc

# Runtime de Python para ANTLR
pip install antlr4-python3-runtime==4.13.2
# o, con venv:
# python3 -m venv venv && source venv/bin/activate
# pip install -r requirements.txt
```

### 2. Clonar / entrar al proyecto

```bash
cd /ruta/a/DKNexus
```

### 3. Generar lexer, parser y visitor en Python

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
```

Se generan: `grammarDKNLexer.py`, `grammarDKNParser.py`, `grammarDKNVisitor.py`, `grammarDKNBaseVisitor.py`.

### 4. Ejecutar el intérprete

**Modo interactivo** (consola):

```bash
python3 interpreterDKN.py
```

**Archivo**:

```bash
python3 interpreterDKN.py ejemplo.dkn
```

---

## Resumen de comandos (sin reinstalar)

```bash
cd /ruta/a/DKNexus
antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
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
