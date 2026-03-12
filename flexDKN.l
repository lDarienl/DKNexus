%{
#include "grammarDKN.tab.h"
%}

%%
[0-9]+       { yylval.num = atoi(yytext); return NUMBER; }
[+\-*/%^]    { return yytext[0]; }
"if"         { return IF; }
"for"        { return FOR; }
"while"      { return WHILE; }
[ \t\n\r]+   { /* ignore whitespace */ }
[a-zA-Z]+    { yylval.str = strdup(yytext); return VARIABLE; }
%%
