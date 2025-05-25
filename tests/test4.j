NB. Test para operaciones especiales

NB. 1 Funcion identidad
] 5

] 1 2 3 4

] _5

NB. 2 Concatenacion
1 , 2 3

(1 2 3) , (4 5 6)

5 , _7 _8

NB. 3 Longitud unaria
# 1 2 3 4 5

# 7

# (1 2) , (3 4 5)

NB. 4 Filtro binario
1 0 1 0 # 1 2 3 4

1 1 0 0 1 # 5 6 7 8 9

1 1 1 # 7 8 9

NB. 5 Acceso por indice 
0 2 { 2 3 4

1 { 5 6 7 8

0 1 0 { 9 8 7

NB. 6 Secuencia
i. 4

i. 1

i. 0

a =: 5
i. a

NB. 7 Operaciones sobre el mismo elemento
+: 1 2 3

*: 2 3 4

^: 2 3

NB. 8 Reduccion 
+ / 1 2 3

* / 1 2 3 4

^ / 2 2 2

- / 10 3 2

NB. 9 Flip
7 | ~ 2

3 - ~ 10

5 ^ ~ 2

NB. 10 Combinaciones de operaciones
# ] 1 2 3 4

+ / i. 5

1 0 1 # ] 3 4 5

1 | ~ + / 1 2 3
