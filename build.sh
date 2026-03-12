#!/bin/bash
# Automatización para DKNexus usando ANTLR4 y Python3 visitor. Ubuntu 
echo "Generando Lexer y Parser..."
antlr4 -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
echo "Listo. Para ejecutar usa: python3 interpreterDKN.py"