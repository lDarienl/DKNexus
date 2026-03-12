grammar grammarDKN;

// Definiciones del lenguaje

program: statement+;

statement
    : 'print' '(' expr ')' ';'                                      # PrintCommand
    | 'return' expr ';'                                             # ReturnStmt
    | 'return' ';'                                                  # ReturnVoid
    | expr ';'                                                      # PrintExpr
    | VARIABLE '=' expr ';'                                         # Asignacion
    | 'if' '(' expr ')' '{' statement+ '}'                          # IfStmt
    | 'for' '(' expr ';' expr ';' expr ')' '{' statement+ '}'       # ForStmt
    | 'while' '(' expr ')' '{' statement+ '}'                       # WhileStmt
    ;

// expr: primera alternativa = menor prioridad, última = mayor.
// Orden: suma/resta < mult/div < potencia.
expr
    // NOTA ANTLR: en recursión izquierda, el orden aquí define la precedencia.
    // Para que ^ tenga más prioridad que * y que +, se coloca primero.
    : expr '^' expr                     # Potencia
    | expr op=('*'|'/'|'%') expr        # MulDivMod
    | expr op=('+'|'-') expr            # SumaResta
    | '(' expr ')'                      # Parens
    | 'sin' '(' expr ')'                # SinFunc
    | 'cos' '(' expr ')'                # CosFunc
    | 'tan' '(' expr ')'                # TanFunc
    | NUMBER                            # Num
    | VARIABLE                          # Var
    ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
// Identificadores: deben empezar con letra o '_' y luego pueden tener letras, dígitos o '_'.
// Ej: x, y2, _tmp, radio10.  NO permitido: 1nombre
INVALID_ID: [0-9]+ [a-zA-Z_][a-zA-Z0-9_]*;
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
