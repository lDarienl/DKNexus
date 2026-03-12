grammar grammarDKN;

// Definiciones del lenguaje

program: statement+;

statement
    : expr ';'                                                      # print expresion
    | VARIABLE '=' expr ';'                                         # asignacion
    | 'if' '(' expr ')' '{' statement+ '}'                          # if
    | 'for' '(' expr ';' expr ';' expr ')' '{' statement+ '}'       # for
    | 'while' '(' expr ')' '{' statement+ '}'                       # while
    ;

// expr: primera alternativa = menor prioridad, última = mayor.
// Orden: suma/resta < mult/div < potencia.
expr
    | expr op=('+'|'-') expr            # suma y resta (menor prioridad)
    | expr op=('*'|'/'|'%') expr        # multiplicacion y division
    | expr '^' expr                     # potencia (mayor prioridad)
    | '(' expr ')'                      # parentesis
    | 'sin' '(' expr ')'                # funcion seno
    | 'cos' '(' expr ')'                # funcion coseno
    | 'tan' '(' expr ')'                # funcion tangente
    | NUMBER                            # int
    | VARIABLE                          # id
    ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
VARIABLE: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
