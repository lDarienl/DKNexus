#!/usr/bin/env zsh
set -e

# Forzamos a cargar tu entorno de Zsh para que reconozca el comando antlr4
source ~/.zshrc 2>/dev/null || true

echo "--- Generando Lexer y Parser directo en src/ ---"
antlr4 -Dlanguage=Python3 -visitor -no-listener -o src grammar/grammarDKN.g4

echo "--- Limpiando archivos de control temporales ---"
rm -f src/grammarDKN*.tokens src/grammarDKN*.interp

echo "Listo. Para ejecutar usa: cd src && python3 interpreterDKN.py"
