@echo off
REM ==========================================================================
REM  Compila el nucleo numerico nativo DKNumpy (src/dknumpy.c) a dknumpy.dll
REM  El .dll resultante queda en src/ para que dknumpyDKN.py lo cargue por ctypes.
REM ==========================================================================
setlocal
set SRC=src\dknumpy.c
set OUT=src\dknumpy.dll

echo --- Compilando DKNumpy (C) a %OUT% ---

where gcc >nul 2>nul
if %ERRORLEVEL%==0 (
    echo Usando gcc (MinGW)...
    gcc -O2 -shared -o %OUT% %SRC%
    goto done
)

where cl >nul 2>nul
if %ERRORLEVEL%==0 (
    echo Usando cl (MSVC)...
    cl /O2 /LD %SRC% /Fe:%OUT%
    del /q dknumpy.obj 2>nul
    goto done
)

echo ERROR: No se encontro un compilador de C (gcc o cl).
echo Instala MinGW-w64 o las "Build Tools de Visual Studio" y reintenta.
echo (Sin .dll, DKNexus usa automaticamente el fallback en Python.)
exit /b 1

:done
echo Listo. DKNumpy nativo disponible en %OUT%.
endlocal
