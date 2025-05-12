- **Lexikální rozsah proměnné** ... rozsah je určen oblastí ve zdrojovém kódu
- V Lispu jinak nejsou proměnné omezeny (časově)
- Přístupnost vazeb a symbolů je dána pomocí 2 podmínek
	1) za jakých okolností jsou vidět (*viditelnost* = *scope*)
	2) po jaký čas od vzniku existují (*životnost* = *extent*)


> [!info]
> **lexikální vazby** ... mají lexikální viditelnost a neomezenou životnost (ty jsou v Lispu)
> 
> **dynamické vazby** ... mají neomezenou viditelnost, ale omezenou životnost (starší typ)

- **Dynamická proměnná** ... její vazby jsou vždy dynamické
	- Definice makrem `defvar`
	- V Lispu mají název ohraničený hvězdičkami (`*dynamic-var*`)

> [!tip]
> Funkční vazby symbolů u lokálních funkcí jsou vždy lexikální.
