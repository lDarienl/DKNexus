grammar grammarDKN;

// Definiciones del lenguaje

program: statement+;

statement
    : 'print' '(' expr ')' ';'                                      # PrintCommand
    | 'return' expr ';'                                             # ReturnStmt
    | 'return' ';'                                                  # ReturnVoid
    | 'push' '(' VARIABLE ',' expr ')' ';'                          # StackPushStmt
    | 'enqueue' '(' VARIABLE ',' expr ')' ';'                       # QueueEnqueueStmt
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
    | '-' expr                          # UnaryMinus
    | '(' expr ')'                      # Parens
    | 'sin' '(' expr ')'                # SinFunc
    | 'cos' '(' expr ')'                # CosFunc
    | 'tan' '(' expr ')'                # TanFunc
    | 'tanh' '(' expr ')'               # TanhFunc
    | 'sqrt' '(' expr ')'               # SqrtFunc
    | 'root' '(' expr ',' expr ')'      # RootFunc
    | 'log' '(' expr ')'                # LogFunc
    | 'log10' '(' expr ')'              # Log10Func
    | 'abs' '(' expr ')'                # AbsFunc
    | 'floor' '(' expr ')'              # FloorFunc
    | 'ceil' '(' expr ')'               # CeilFunc
    | 'trans' '(' expr ')'              # MatrixTrans
    | 'inv' '(' expr ')'                # MatrixInv
    | 'pop' '(' VARIABLE ')'            # StackPop
    | 'dequeue' '(' VARIABLE ')'        # QueueDequeue
    | '[' (expr (',' expr)*)? ']'       # ListLiteral
    | PI                                # PiConst
    | EULER                             # EConst
    | INF                               # InfConst
    | NUMBER                            # Num
    | STRING                            # StringLiteral
    | VARIABLE                          # Var
    ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
// Strings: comillas dobles, dentro se puede escapar " con \"
STRING: '"' ( '\\"' | ~["\r\n] )* '"';
// Identificadores: deben empezar con letra o '_' y luego pueden tener letras, dígitos o '_'.
// Ej: x, y2, _tmp, radio10.  NO permitido: 1nombre
INVALID_ID: [0-9]+ [a-zA-Z_][a-zA-Z0-9_]*;

// Comentarios de línea: se ignoran completamente
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Constantes reservadas (case-insensitive)
PI: [pP][iI];
EULER: [eE];
INF: [iI][nN][fF];

VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
