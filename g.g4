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
          | ID '=:' funcion # asignacion_funcion
          ;

expr : '(' expr ')' # parentesis
     | <assoc=right> expr operador_bin expr # operacion_binaria
     | <assoc=right> operador_un expr # operacion_unaria
     | <assoc=right> expr operador_bin operador_bin_comb expr # operacion_binaria_combinada
     | <assoc=right> operador_bin operador_un_comb expr # operacion_unaria_combinada
     | <assoc=right> ID expr # llamada_funcion
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

operador_comp : ('@:') # operador_composicion
              ;


funcion_simple : <assoc=right> expr operador_bin # f1
               | <assoc=right> operador_un # f2
               | <assoc=right> expr operador_bin operador_bin_comb # f3
               | <assoc=right> operador_bin operador_un_comb # f4
               | ID # funcion_id
               ;

funcion : funcion_simple (operador_un)* (operador_comp funcion)? # composicion
        ;

operand : NUM # numero
        | NUM_NEG # numero_negativo
        ;

comment : 'NB.' (ID | NUM | NUM_NEG)* # comentario
        ;

ID  : [a-zA-Z][a-zA-Z0-9]* ;
NUM : [0-9]+ ;
NUM_NEG : '_' NUM ;

WS  : [ \t\r]+ -> skip ; // Espacios en blanco
