NB. 1. Definiciones básicas de funciones
square =: *:
square 1 2 3 4

NB. 2. Funciones de identidad con modificaciones
add5 =: 5 + ]
add5 i. 5

NB. 3. Operaciones con módulo
mod2 =: 2 | ]
mod2 i. 6

mod4 =: 4 | ]
mod4 i. 8

NB. 4. Funciones de comparación
isZero =: 0 = ]
isZero 0 1 0 2 0

greaterThan3 =: 3 < ]
greaterThan3 2 3 4 5

NB. 5. Composición simple de funciones
eq0 =: 0 = ]
div3 =: 3 | ]
div3Test =: eq0 @: div3
div3Test i. 9

NB. 6. Composición múltiple y funciones aritméticas
inc =: 1 + ]
double =: 2 * ]
incDouble =: double @: inc
incDouble 5 10 15

NB. 7. Funciones con fold
sumRange =: +/ @: i.
sumRange 5

prodRange =: */ @: 1 + ] @: i.
prodRange 5

NB. 8. Operaciones con filtros
nums =: 1 2 3 4 5 6
mask =: 1 0 1 0 1 0
mask # nums

NB. 9. Operaciones con índices
getSecond =: 1 { ]
getSecond 10 20 30 40

NB. 10. Definición alternativa para números pares
parell =: 0 = ] @: 2 | ]
parell i. 6

NB. 11. Potencia como operación
cube =: 3 ^ ]
cube 2 3 4

NB. 12. Tamaño y rangos
createAndCount =: # @: i.
createAndCount 7

NB. 13. Operaciones complejas encadenadas
complexChain =: +/ @: *: @: inc @: i.
complexChain 4

NB. 14. Operador de duplicación con 
double2 =: +:
double2 5 10 15
