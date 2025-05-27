NB. llista bàsica
1 2 3 4 5

NB. operacions sobre llistes
1 2 3 - 6 7 5 NB. retorna _5 _5 _2
3 + 3 + 5
3 4 % 2 4  

NB. Operacions sobre llistes però un dels operands és un escalar
1 2 3 + 6   NB. retorna 7 8 9
6 + 1 2 3   NB. retorna 7 8 9
_4 _2 2 ^ 2

NB. Operacions sobre llistes de diferent longitud (ha de donar error)
NB. 1 2 3 + 6 7

NB. Tots els operadors tenen la mateixa prioritat TODO CANVIAR NUMEROS
5 + 2 * 3 NB. 5 + (2 * 3) = 11
5 * 2 + 3 NB. (5 + 2) * 3 = 25
2 * 4 + 5 
2 * 4 + 5
2 ^ 2 * 3
2 * 3 ^ 2
1 | 2 ^ 2 * 5

NB. Ús de parèntesis per controlar prioritat
(5 + 2) * 3 NB. (5 + 2) * 3 = 21
(2 + 4) * (4 + 5)
(_2 + 4) * (4 + _5)

NB. Treballar amb nombres negatius
_4 * 3 5 6 NB. _4 * 3 5 6 = _12 _20 _24
_32 - _3

NB. Divisió entera
5 % 2       NB. retorna 2
9 10 % 3    NB. retorna 3 3

NB. Residu 
2 | 5       NB. retorna 1
3 | 9 10    NB. retorna 0 1

NB.  Funcions de comparació 
1 2 3 < 4 5 6 NB. retorna 1 1 1
1 2 3 < 2 1 4 NB. retorna 1 0 1

1 = 1          NB.  retorna 1
1 = 2          NB.  retorna 0
1 <> 2         NB.  retorna 1
2 > 1          NB.  retorna 1
1 < 2          NB.  retorna 1
2 >= 2         NB.  retorna 1
1 <= 0         NB.  retorna 0
_1 <= _2       NB.  retorna 0
_1 <> 1        NB.  retorna 1
1 _1 3 > _4 _1 _1   NB. retorna 1 0 1

i =: 3
j =: 5

i = j         NB. retorna 0
i <> j        NB. retorna 1
i < j         NB. retorna 1
i > j         NB. retorna 0
i <= j        NB. retorna 1
i >= j        NB. retorna 0

k =: 1 = 2
k             NB. retorna 0

l =: (1 23 4) = (1 2 3)
l             NB. retorna 1 0 0

NB. ALTRES FUNCIONS
NB. Funció identitat
] 2 NB. retorna 2
] 1 _2 3 NB. retorna 1 _2 3

NB. Concanetació
1 3 5 , 2 4 6 NB. retorna 1 3 5 2 4 6
1 2 , 4 NB. retorna 1 2 4
1 2 , _2 _3 NB. retorna 1 2 _2 _3

NB. # unari, retorna la longitud d'un vector
# 1 2 3 NB. retorna 3

NB. # binari, fa un filtre amb una màscara
0 1 1 0 # 1 5 7 3 NB. retorna 5 7

NB. { per accedir a elements per índex
1 3 { 1 2 3 4       NB. retorna 2 4
1 2 1 3 { 1 2 3 4   NB. retorna 2 3 2 4

NB. i. per obtenir un vector amb els n primers números naturals
i. 4           NB. retorna 0 1 2 3
i. 0           NB. no retorna res
i. 3           NB. retorna 0 1 2

NB. Operador flip
7 | ~ 2        NB. retorna 1
2 - ~ 5        NB. retorna 3

NB. Operador fold
+ / 3 2 4      NB. retorna 9
* / 2 3 4      NB. retorna 24
^ / 2 3 2      NB. retorna 512
| / 2 5 7      NB. retorna 0

NB. Operador ':'
+: 1 2 3 4          NB. retorna 2 4 6 8
*: 4 5 7 8          NB. retorna 16 25 49 64

NB. Combinació de funcions
# 12 2, 3 4 2       NB. retorna 5
* / i. 3            NB. retorna 6
2 % ~ * / 1 2 3     NB. retorna 3
+: (1 + 2)          NB. retorna 3
+/ *: 1 2 3         NB. retorna 14
+: 1 2 3 + 4 5 6    NB. retorna 10 14 18
*: ] i. 5           NB. retorna 0 1 4 9 16

NB. assignació de variables
x =: 1 2 3 4 5      NB. assigna a x el valor 1 2 3 4 5
y =: 6 + 3          NB. assigna a y el valor 9

x                   NB. retorna 1 2 3 4 5
y                   NB. retorna 9

NB. Operacions amb variables
1 + x               NB. retorna 2 3 4 5 6
x * 2 3 4 5 6       NB. retorna 2 6 12 20 30 TODO no la fa be
x + y * 4           NB. retorna 37 38 39 40 41
x ^ 2               NB. retorna 1 4 9 16 25
x | 2               NB. retorna 1 0 1 0 1
x % 2               NB. retorna 0 1 1 2 2
x + (3 4 5 5 6)     NB. retorna 4 6 8 9 11
i. y                NB. retorna 0 1 2 3 4 5 6 7 8

NB. DEFINICIÓ DE FUNCIONS
NB. Assignació
square =: *:
square 1 2 3 4      NB. retorna 1 4 9 16
square 1 + i. 3     NB. resultat: 1 4 9

NB. Funció Identitat
mod2 =: 2 | ]
mod2 i. 4           NB. retorna 0 1 0 1

NB. Composició de funcions
eq0 =: 0 = ]
eq0 mod2 i. 6       NB. retorna 1 0 1 0 1 0 

parell =: eq0 @: mod2
parell i. 6         NB. retorna 1 0 1 0 1 0

parell =: 0 = ] @: 2 | ]
parell i. 6         NB. retorna 1 0 1 0 1 0

inc =: 1 + ]
test =: +/ @: inc @: i.
test 3              NB. resultat: 6

quad =: *:
NB. mitjana =: +/ % #   NB. suma total dividit per mida
NB. mitjana 1 2 3       NB. retorna 2

NB. quad_mitjana =: *: @: mitjana
NB. quad_mitjana 1 2 3  NB. retorna 4

mascara =: 1 0 1 0
valors =: 10 20 30 40
mascara # valors    NB. retorna 10 30

triplica =: 3 * ]
triplica 2 4        NB. retorna 6 12

primer =: 0 { ]
segon  =: 1 { ]
primer 100 200 300       NB. 100
segon 100 200 300        NB. 200





