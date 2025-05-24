grammar g;

root : (statement? comment? '\n')* EOF # arrel
     ;
/* 
function : 'function' ID '(' paramlist? ')' statement+ 'end' # funcio
         ;

paramlist : ID (',' ID)* # llista_parametres
          ;

main : 'main' statement+ 'end' # programa_principal
     ;
*/

statement : ID '=:' expr # asignacion
          | expr # expresion
          ;

expr : '(' expr ')' # parentesis
     | <assoc=right> expr ('+'|'-'|'*'|'%'|'^'|'|') expr # operacion
     | operand+ # operando
     | ID # variable
     ;

operand : NUM # numero
        | NUM_NEG # numero_negativo
        ;

comment : 'NB.' (ID)+ # comentario
        ;

ID  : [a-zA-Z]+ ;
NUM : [0-9]+ ;
NUM_NEG : '_' NUM ;
         

WS  : [ \t\r]+ -> skip ; // Espacios en blanco
