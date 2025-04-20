- Makro je nástroj na vytváření nových operátorů
	- Jinými slovy umožňuje abstrakci na úrovni zdrojového kódu (např. `(impl a b) --> (if a b t)`)
- Proces nazýváme **expanze makra**
	- Funkce, která proces vykoná se jmenuje **expanzní funkce makra**
- Onen expandovaný výraz se opětovně předloží vyhodnocovacímu procesu
```lisp
(defmacro impl (ant-expr cons-expr)
	(list 'if ant-expr cons-expr 't))
```
- Při definici sdělujeme 3 údaje: *název makra, $\lambda$-seznam expanzní funkce, tělo expanzní funkce*
- Při definici děláme 2 nárocně věci naráz:
	1) vymýšlíme co má být expanzí daného makro výrazu
	2) píšeme funkce, která výraz na expanzi převádí
