# Pràctica LP: Compilador de G

David Berrocal Fidalgo (Grup: 11)

En aquest document es descriu el compilador/intèrpret del llenguatge G desenvolupat com a pràctica de Llenguatges de Programació. G és una versió simplificada de J (derivat d'APL) que treballa principalment amb operacions vectoritzades i té una sintaxi concisa.

## 1. Compilació

Per compilar el projecte, s'utilitza el Makefile proporcionat:

```bash
# Genera els arxius Python necessaris a partir de la gramàtica g.g4
make

# O també:
make generate
```

Aquest procés utilitza ANTLR4 per generar els arxius Python necessaris per a l'intèrpret a partir de la gramàtica g.g4.

## 2. Execució

Hi ha diverses formes d'executar l'intèrpret:

### Executar un programa des d'un fitxer

```bash
python3 g.py programa.j
```

### Executar un programa i redirigir la sortida a un fitxer

```bash
python3 g.py programa.j > sortida.txt
```

### Executar l'intèrpret en mode interactiu

```bash
python3 g.py
```

En aquest mode, l'intèrpret espera una línia d'entrada precedida pel símbol `?`.

### 2.1 Proves

El Makefile proporciona eines per executar jocs de proves automàticament:

```bash
# Executa tots els programes de prova (.j) del directori tests/
# i guarda les sortides en fitxers .out
make test

# Compara els resultats generats (.out) amb els resultats esperats (.res)
make diff
```

Per crear un nou joc de proves:
1. Crear un fitxer `nom_test.j` en el directori `tests/`
2. Opcionalment, crear un fitxer `nom_test.res` amb la sortida esperada
3. Executar `make test` per generar el fitxer `nom_test.out`
4. Utilitzar `make diff` per comparar el resultat obtingut amb l'esperat

## 3. Funcionalitats del llenguatge

El llenguatge G implementa un subconjunt del llenguatge J, amb les següents funcionalitats:

### Tipus de dades
- El tipus principal són les llistes d'enters, escrites amb elements separats per espais: `1 2 3`
- Els nombres negatius s'indiquen amb prefix `_`: `_1 _2 _3`

### Operadors aritmètics
- Suma: `+` (ex: `1 + 2 3` resulta en `3 4`)
- Resta: `-` (ex: `5 - 2` resulta en `3`)
- Multiplicació: `*` (ex: `1 2 * 3 3` resulta en `3 6`)
- Divisió entera: `%` (ex: `7 % 2` resulta en `3`)
- Potència: `^` (ex: `2 ^ 3` resulta en `8`)
- Mòdul: `|` (ex: `2 | 7` resulta en `1`) - Nota: els operands van al revés

### Operadors de comparació
- Igualtat: `=` (ex: `1 = 1` resulta en `1`)
- Desigualtat: `<>` (ex: `1 <> 2` resulta en `1`)
- Menor que: `<` (ex: `1 < 2` resulta en `1`)
- Major que: `>` (ex: `2 > 1` resulta en `1`)
- Menor o igual: `<=` (ex: `1 <= 1` resulta en `1`)
- Major o igual: `>=` (ex: `1 >= 1` resulta en `1`)

### Operadors de llistes
- Concatenació: `,` (ex: `1 , 2 3` resulta en `1 2 3`)
- Filtratge: `#` (ex: `1 0 1 # 2 3 4` resulta en `2 4`)
- Indexació: `{` (ex: `0 2 { 2 3 4` resulta en `2 4`)

### Operadors unaris
- Identitat: `]` (ex: `] 1 2 3` resulta en `1 2 3`)
- Longitud: `#` (ex: `# 1 2 3` resulta en `3`)
- Interval: `i.` (ex: `i. 4` resulta en `0 1 2 3`)

### Combinadors d'operadors
- Self-apply: `:` (ex: `+: 1 2 3` resulta en `2 4 6`, equivalent a `1 2 3 + 1 2 3`)
- Fold: `/` (ex: `+/ 1 2 3` resulta en `6`, suma tots els elements) - Nota: només es pot aplicar a operadors aritmètics.
- Flip: `~` (ex: `7 |~ 2` resulta en `1`, inverteix els operands)

### Variables i assignacions
- Assignació: `=:` (ex: `x =: 1 2 3`)
- Accés a variables: `x` (accedeix al valor assignat a x)

### Definició i composició de funcions
- Definició de funció: `nom =: expressió` (ex: `square =: *:`)
- Composició de funcions: `@:` (ex: `parell =: eq0 @: mod2`)
- Exemple complet: 
  ```j
  mod2 =: 2 | ]
  eq0 =: 0 = ]
  parell =: eq0 @: mod2
  parell i. 6    NB. resultat: 1 0 1 0 1 0
  ```

### Gestió d'errors

L'intèrpret implementa diversos mecanismes per gestionar els errors:

#### Errors sintàctics
- Es detecten a la funció `main()` utilitzant `parser.getNumberOfSyntaxErrors()`.
- Si es troba algun error sintàctic, es mostra el nombre d'errors i es finalitza l'execució.
- S'eliminen els listeners d'errors predeterminats amb `parser.removeErrorListeners()` per evitar missatges detallats del parser d'ANTLR.

#### Errors d'execució
- Al mètode `visitArrel`, s'implementa un bloc try-except per capturar les excepcions que puguin sorgir durant l'avaluació.
- Quan es detecta un error, es mostra un missatge amb el prefix "Error:" i es deté el processament del node actual.

#### Errors específics
L'intèrpret també gestiona errors específics del llenguatge G:
- Errors de longitud quan s'operen llistes de diferents mides
- Errors quan els operands no són del tipus esperat (per exemple, no són llistes)
- Errors quan s'intenta utilitzar variables o funcions no definides
- Errors quan s'intenta aplicar operadors no suportats o combinacions invàlides

### Altres característiques
- Avaluació de dreta a esquerra (menys quan s'usen parèntesis)
- Vectorització automàtica (si un operand és escalar i l'altre llista)
- Comentaris: comencen amb `NB.` i van fins al final de la línia
- Prioritat uniforme d'operadors (tots tenen la mateixa prioritat)

Per netejar els arxius generats pel compilador:

```bash
make clean
```
