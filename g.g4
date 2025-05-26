grammar g;

root : (statement? comment? '\n')* EOF # arrel
     ;

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

funcion : <assoc=right> funcion_atom ('@:' (funcion_atom | ID))* # f_comp
        ;

funcion_atom : operador_un # f_un
             | expr operador_bin ']' # f_bin
             | operador_bin operador_un_comb # f_comb_un
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

comment : 'NB.' (ID | NUM | NUM_NEG | SIMB)* # comentario
        ;

ID  : [a-zA-Z][a-zA-Z0-9]* ;
NUM : [0-9]+ ;
NUM_NEG : '_' NUM ;

SIMB : ('+'|'-'|'*'|'%'|'^'|'|'|'='|'<>'|'<'|'>'|'<='|'>='|','|'#'|'{' | ']'|'i.'|':'|'/'|'~'|'@:'|'.'|'-'|'_') ;

WS  : [ \t\r]+ -> skip ; // Espacios en blanco
