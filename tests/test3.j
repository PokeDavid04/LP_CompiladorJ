NB. Test para operaciones relacionales

NB. 1 Pruebas numero con numero
5 = 5

5 <> 5

5 < 10

10 > 5

5 <= 5

5 >= 10

NB. 2 Pruebas con variables
a =: 5

b =: 10

a = b

a <> b

a < b

a > b

a <= b

a >= b

NB. 3 Pruebas numero con lista
5 = (3 5 7)

5 <> (3 5 7)

5 < (3 5 7)

5 > (3 5 7)

5 <= (3 5 7)

5 >= (3 5 7)

NB. 4 Pruebas lista con lista
(1 5 9) = (1 5 8)

(1 5 9) <> (1 5 8)

(1 5 9) < (2 5 10)

(1 5 9) > (0 5 8)

(1 5 9) <= (1 5 9)

(1 5 9) >= (1 6 8)

NB. 5 Pruebas con asignacion
c =: 3 = 3

c

d =: (1 2 3) = (1 2 4)

d

e =: a < (4 5 6)

e

NB. 6 Casos especiales
_5 = _5

_5 <> 5

(1 _2 3) > (_2 _3 _4)
