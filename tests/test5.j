NB. Pruebas adicionales de funciones y composiciones

square =: *:
square 1 2 3 4

mod =: 2 | ]
mod i. 4

eq =: 0 = ]
parell =: eq @: mod
parell i. 6

square 1 + i. 3
eq =: 0 = ]

eq mod i. 6

parell =: eq @: mod
parell i. 6 

parell =: 0 = ] @: 2 | ]
parell i. 6

inc =: 1 + ]
test =: +/ @: inc @: i.
test 3 

NB. Pruebas con doble composicion
double =: 2 * ]
triple =: 3 * ]
sextupl =: double @: triple
sextupl 7

NB. Combinacion de operadores binarios y unarios
sub1 =: _1 + ]
dism =: sub1 @: *:
dism 5

NB. Filtros y selecciones
nums =: 1 2 3 4 5 6 7 8
filtro =: 1 0 1 0 1 0 1 0
filtro # nums

NB. Operaciones con rangos
rango3 =: i. 3
+ / rango3

NB. Operacion dual con mismo elemento
cuad =: *:
cuad 4
*: 4

NB. Combinacion de reduccion y operadores
sum3 =: + / @: i.
sum3 4

NB. Operacion en cascada
inc2 =: 2 + ]
cascade =: inc2 @: *: @: inc2
cascade 3

NB. Manipulacion de listas
head =: 0 { ]
tail =: 1 + ] @: i. @: # @: ]
lista =: 5 6 7 8 9
head lista
tail lista

NB. Operadores multiples en composicion
comp1 =: *: @: +/ @: i.
comp1 5
