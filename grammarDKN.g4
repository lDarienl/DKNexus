grammar grammarDKN;

// Definiciones del lenguaje

program: statement+;

statement
    : expr ';'
    | 'if' '(' expr ')' '{' statement+ '}'
    | 'for' '(' expr ';' expr ';' expr ')' '{' statement+ '}'
    | 'while' '(' expr ')' '{' statement+ '}'
    ;

expr
    : expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | expr '%' expr
    | expr '^' expr
    | 'sin' '(' expr ')'
    | 'cos' '(' expr ')'
    | 'tan' '(' expr ')'
    | NUMBER
    | VARIABLE
    | '(' expr ')'
    ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
VARIABLE: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
