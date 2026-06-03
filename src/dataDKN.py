"""
Carga y parsing de datos tabulares para DKNexus (CSV simple, sin dependencias).

- ``load_csv_matrix``: solo valores numéricos (CSV simple).
- ``read_csv_table``: CSV con comillas, encabezado y celdas texto/número (p. ej. data.csv).
"""


def _strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1]
    return s


def _split_csv_line(line: str) -> list[str]:
    """Divide una línea CSV respetando campos entre comillas dobles."""
    fields: list[str] = []
    cur: list[str] = []
    in_quotes = False
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if in_quotes:
            if ch == '"':
                if i + 1 < n and line[i + 1] == '"':
                    cur.append('"')
                    i += 2
                    continue
                in_quotes = False
                i += 1
                continue
            cur.append(ch)
            i += 1
            continue
        if ch == '"':
            in_quotes = True
            i += 1
            continue
        if ch == ",":
            fields.append("".join(cur).strip())
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    fields.append("".join(cur).strip())
    return fields


def _parse_cell_mixed(raw: str):
    """Celda mixta: número si es posible, si no string (sin comillas externas)."""
    s = _strip_quotes(raw.strip())
    if s == "":
        return ""
    try:
        return int(s, 10)
    except ValueError:
        pass
    try:
        fv = float(s)
        if "." not in s and "e" not in s.lower() and "E" not in s:
            if float(int(fv)) == fv:
                return int(fv)
        return fv
    except ValueError:
        return s


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


def read_csv_table(path: str, bump_cell) -> dict:
    """
    Lee un CSV con encabezado, comillas y columnas mixtas (texto y números).

    Devuelve un diccionario:
      - ``header``: lista de nombres de columna (strings)
      - ``rows``: lista de filas (cada fila es lista de valores)
      - ``n_rows``, ``n_cols``: dimensiones de la tabla de datos
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            text = f.read()
    except OSError as e:
        raise ValueError(f"No se pudo abrir el archivo: {e}") from e

    lines = [ln.strip() for ln in text.splitlines() if ln.strip() != ""]
    if not lines:
        raise ValueError("CSV vacío o sin filas.")

    header_parts = _split_csv_line(lines[0])
    header = [_strip_quotes(h) for h in header_parts]
    n_cols = len(header)
    if n_cols == 0:
        raise ValueError("El encabezado no tiene columnas.")

    rows: list[list] = []
    for row_idx, line in enumerate(lines[1:], start=2):
        parts = _split_csv_line(line)
        if len(parts) != n_cols:
            raise ValueError(
                f"Fila {row_idx}: se esperaban {n_cols} columnas, se encontraron {len(parts)}."
            )
        row: list = []
        for cell in parts:
            bump_cell()
            row.append(_parse_cell_mixed(cell))
        rows.append(row)

    return {
        "header": header,
        "rows": rows,
        "n_rows": len(rows),
        "n_cols": n_cols,
    }


def csv_column(table: dict, col_index: int) -> list:
    """Extrae la columna ``col_index`` (0-based) de una tabla devuelta por ``read_csv``."""
    if not isinstance(table, dict) or "rows" not in table:
        raise ValueError("csv_col: el primer argumento debe ser una tabla de read_csv.")
    rows = table["rows"]
    if not isinstance(col_index, int) or isinstance(col_index, bool):
        raise ValueError("csv_col: el índice de columna debe ser un entero.")
    if not rows:
        return []
    n_cols = len(rows[0])
    if col_index < 0 or col_index >= n_cols:
        raise ValueError(
            f"csv_col: índice {col_index} fuera de rango (0..{n_cols - 1})."
        )
    return [row[col_index] for row in rows]


def csv_column_numeric(table: dict, col_index: int, bump_cell) -> list:
    """Columna solo con valores numéricos (float); omite strings no convertibles."""
    raw = csv_column(table, col_index)
    out: list = []
    for v in raw:
        bump_cell()
        if isinstance(v, bool):
            continue
        if isinstance(v, (int, float)):
            out.append(float(v))
        elif isinstance(v, str):
            try:
                out.append(float(v))
            except ValueError:
                continue
    return out
