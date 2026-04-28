#!/bin/bash
echo "--- Generando Lexer y Parser desde grammar/ ---"
# Ejecutar ANTLR apuntando a la carpeta grammar
antlr4 -Dlanguage=Python3 -visitor -no-listener grammar/grammarDKN.g4

# Mover los archivos generados automáticamente a src/
mv grammar/grammarDKN*.py src/ 2>/dev/null || mv grammarDKN*.py src/

echo "--- Limpiando archivos temporales ---"
rm -f grammar/*.tokens grammar/*.interp *.tokens *.interp

echo "Listo. Para ejecutar usa: cd src && python3 interpreterDKN.py"
