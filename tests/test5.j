square =: *:
square 1 2 3 4

mod2 =: 2 | ]
mod2 i. 4

eq0 =: 0 = ]
parell =: eq0 @: mod2
parell i. 6


square =: *:
square 1 + i. 3  

mod2 =: 2 | ]
eq0 =: 0 = ]

eq0 mod2 i. 6  

parell =: eq0 @: mod2
parell i. 6  

parell =: 0 = ] @: 2 | ]
parell i. 6

inc =: 1 + ]
test =: +/ @: inc @: i.
test 3 
