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
     | <assoc=right> expr operador_bin expr # operacion_binaria
     | <assoc=right> operador_un expr # operacion_unaria
     | <assoc=right> expr operador_bin operador_bin_comb expr # operacion_binaria_combinada
     | <assoc=right> operador_bin operador_un_comb expr # operacion_unaria_combinada
     | operand+ # operando
     | ID # variable
     ;

operador_bin : ('+'|'-'|'*'|'%'|'^'|'|'|'='|'<>'|'<'|'>'|'<='|'>='|','|'#'|'{') # operador_binario
            ;

operador_un : (']'|'#'|'i.') # operador_unario
            ;

operador_bin_comb : ('~') # operador_binario_combinacion
                  ;

operador_un_comb : (':'|'/') # operador_unario_combinacion
                 ;

operand : NUM # numero
        | NUM_NEG # numero_negativo
        ;

comment : 'NB.' (ID | NUM | NUM_NEG)* # comentario
        ;

ID  : [a-zA-Z]+ ;
NUM : [0-9]+ ;
NUM_NEG : '_' NUM ;

WS  : [ \t\r]+ -> skip ; // Espacios en blanco
