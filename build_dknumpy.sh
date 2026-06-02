#!/bin/bash
# ===========================================================================
#  Compila el nucleo numerico nativo DKNumpy (src/dknumpy.c) a libdknumpy.so
#  El .so resultante queda en src/ para que dknumpyDKN.py lo cargue por ctypes.
# ===========================================================================
set -e

SRC="src/dknumpy.c"
OUT="src/libdknumpy.so"

echo "--- Compilando DKNumpy (C) a ${OUT} ---"

if command -v gcc >/dev/null 2>&1; then
    CC=gcc
elif command -v clang >/dev/null 2>&1; then
    CC=clang
else
    echo "ERROR: No se encontro gcc ni clang."
    echo "(Sin .so, DKNexus usa automaticamente el fallback en Python.)"
    exit 1
fi

"${CC}" -O2 -fPIC -shared -o "${OUT}" "${SRC}"
echo "Listo. DKNumpy nativo disponible en ${OUT} (compilador: ${CC})."
