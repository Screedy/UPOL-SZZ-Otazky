- Jedná se o programovací paradigma založené na *formální logice*
- Programy tedy nejsou posloupnosti příkazů, nýbrž soubor *logický pravidel a vztahů* z nichž odvozujeme závěry
- Nejznámějším jazykem je **Prolog**
## Pravidla
- Definuje vztah mezi objekty a umožní odvození nových znalostí
```lisp
; Prolog pravidlo
head :- body

; Lisp pravidlo
(<- head body)
(<- alarm-on locked room-danger)
```
- Zápis slovy "hlava platí, pokud platí tělo"
- *Hlava* je hodnota a *tělo* je seznam hodnot
- **program** ... seznam pravidel
	- záleží na jejich pořadí (přidáváme nakonec)
- Aplikací pravidel na cíl vzniká stromová struktura nazývaná *strom úsudků* (viz dále)
## Cíl substituce
- V logickém programování se jedná o *otázku*, na kterou chceme najít odpověď
```lisp
; Cíl
(goal)
(? subgoal1 subgoal2 ...)
(? alarm-on police-on way)
```
- *Substitucí* se myslí proces, kde se jedná o dosazení konkrétní hodnoty za proměnnou
- **proměnná** ... symbol začínající otazníkem ... např: `?x, ?a`
- Substituce se rovnají pokud obsahují stejné páry
## Unifikace (výrazů)
- Substituci nazveme unifikátorem výrazu pokud po aplikaci na dané výrazy, dostanu stejné výrazy
- Např: substituce `(sub (?x . a) (?y . b)))` je unifikátor výrazů `(?x ?y)` a `(?x b)`
- Existuje algoritmus, který dokáže zjistit zda jous výrazy unifikovatelné a případně vrátí jejich *nejobecnější unifikátor*
	- ![[Pasted image 20250314161440.png]]
- **nejobecnější unifikátor** ... unifikuje pouze jen to opravdu potřebné
	- Pokud jde výrazy unifikovat, existuje i nejobecnější unifikátor
## Úsudek
- Jde o proces odvozování nových informací z existujících pravidel
- V procesu jde o dokázání cíle pomocí rozložení na *podcíle* a následném nalézání shody s existujícími pravidly
- Při vytváření těchto úsudků vzniká strom, který může být **nekonečný**
#### Strom úsudků
- Vizualizace procesu *usuzování*
#### Nekonečný strom úsudků
- Řešení 2 způsoby
	 1) líné stromy
	 2) průchod do šířky - hůře předvídatelné pořadí odpovědí; v konečném čase dorazíme ke každé odpovědi