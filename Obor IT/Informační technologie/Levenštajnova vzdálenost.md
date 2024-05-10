-  Levenštejnova vzdálenost je metrika používaná pro měření rozdílu mezi dvěma řetězci. 
- Udává minimální počet jednoznakových editací (vložení, smazání, substituce), které jsou potřebné k přeměně jednoho řetězce na druhý.

- Vezměme libovolné řetězce $x, y$. Definujeme vzdálenost řetězců $x,y$ následovně:
	1. Pokud je řetězec $y$ prázdný, pak je vzdálenost rovna délce řetězce $x$,
	2. pokud je řetězec $x$ prázdný, pak je vzdálenost rovna délce řetězce y,
	3. začínají-li oba řetězce $x$ i $y$ stejným znakem, pak je vzdálenost rovna vzdálenosti řetězců $x,y$ bez prvních znaků,
	4. pokud oba řetězce **nezačínají** stejným znakem, pak je vzdálenost rovna $1+$ minimum z hodnot:
		(a) vzdálenost řetězce $x$ bez prvního znaku a řetězce $y$,
		(b) vzdálenost řetězce $x$ a řetězce $y$ bez prvního znaku
		(c) a vzdálenost řetězců $x, y$ bez prvních znaků.

- Například:
	- Vzdálenost `""` a `""` je nula.
	- `"ab"`, `"ab"` je nula.
	- `""`, `"a"` je jedna.
	- `"ab"`, `""` je dva.
	- `"a"`, `"ab"` je jedna.
	- `"ba"`, `"aa"` je jedna.


##### Navigace
Předchozí:  [[Výpočet skóre zásahu]]
Následující: [[Unixové operační systémy (UNIX, Linux), uživatelská prostředí a nápovědy]]
Celý okruh: [[2. Informační technologie]]