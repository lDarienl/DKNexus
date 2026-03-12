@echo off
echo Generando Lexer y Parser para Windows...
java -jar /usr/local/lib/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener grammarDKN.g4
echo Listo. Ejecuta: python interpreterDKN.py
pause