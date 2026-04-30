"""
Carga y parsing de datos tabulares para DKNexus (CSV simple, sin dependencias).
"""


def _parse_cell(raw: str):
    """Convierte texto de celda a int o float; rechaza vacíos y no numéricos."""
    s = raw.strip()
    if s == "":
        raise ValueError("celda vacía")
    try:
        return int(s, 10)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError as e:
        raise ValueError(f"valor no numérico: {s!r}") from e


def load_csv_matrix(path: str, bump_cell) -> list[list]:
    """
    Lee un CSV separado por comas (sin comillas complejas).
    Todas las filas deben tener el mismo número de columnas que la primera fila de datos.
    `bump_cell` se invoca por cada celda parseada (Execution Guard).
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            text = f.read()
    except OSError as e:
        raise ValueError(f"No se pudo abrir el archivo: {e}") from e

    lines = [ln.strip() for ln in text.splitlines() if ln.strip() != ""]
    if not lines:
        raise ValueError("CSV vacío o sin filas de datos.")

    matrix: list[list] = []
    expected_cols: int | None = None

    for row_idx, line in enumerate(lines, start=1):
        parts = [p.strip() for p in line.split(",")]
        if expected_cols is None:
            expected_cols = len(parts)
            if expected_cols == 0:
                raise ValueError("La primera fila no contiene columnas.")
        elif len(parts) != expected_cols:
            raise ValueError(
                f"Fila malformada {row_idx}: se esperaban {expected_cols} columnas, "
                f"se encontraron {len(parts)}."
            )
        row: list = []
        for cell in parts:
            bump_cell()
            try:
                row.append(_parse_cell(cell))
            except ValueError as e:
                raise ValueError(f"Fila {row_idx}, celda inválida: {e}") from e
        matrix.append(row)

    return matrix
