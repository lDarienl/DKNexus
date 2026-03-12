grammar grammarDKN;

// Definiciones del lenguaje

program: statement+;

statement
    : expr ';'                                                      # PrintExpr
    | VARIABLE '=' expr ';'                                         # Asignacion
    | 'if' '(' expr ')' '{' statement+ '}'                          # IfStmt
    | 'for' '(' expr ';' expr ';' expr ')' '{' statement+ '}'       # ForStmt
    | 'while' '(' expr ')' '{' statement+ '}'                       # WhileStmt
    ;

// expr: primera alternativa = menor prioridad, última = mayor.
// Orden: suma/resta < mult/div < potencia.
expr
    : expr op=('+'|'-') expr            # SumaResta
    | expr op=('*'|'/'|'%') expr        # MulDivMod
    | expr '^' expr                     # Potencia
    | '(' expr ')'                      # Parens
    | 'sin' '(' expr ')'                # SinFunc
    | 'cos' '(' expr ')'                # CosFunc
    | 'tan' '(' expr ')'                # TanFunc
    | NUMBER                            # Num
    | VARIABLE                          # Var
    ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
VARIABLE: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
