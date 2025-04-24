- Makro je nástroj na vytváření nových operátorů
	- Jinými slovy umožňuje abstrakci na úrovni zdrojového kódu
	- př. `(impl a b)` $\longrightarrow$ `(if a b t)`
- Proces nazýváme **expanze makra**
	- Funkce, která proces vykoná se jmenuje **expanzní funkce makra**
- Onen expandovaný výraz se opětovně předloží vyhodnocovacímu procesu
```lisp
(defmacro impl (ant-expr cons-expr)
	(list 'if ant-expr cons-expr 't))
```
- ![[Pasted image 20250421172052.png]]
- Při definici sdělujeme 3 údaje: *název makra, $\lambda$-seznam expanzní funkce, tělo expanzní funkce*
- Při definici děláme 2 nárocně věci naráz:
	1) vymýšlíme co má být expanzí daného makro výrazu
	2) píšeme funkce, která výraz na expanzi převádí
- Definicí makra si rozšiřujeme programovací jazyk
- Můžeme využít zpětný apostrof pro lepší čitelnost v definici makra (potlačí vyhodnocení)
	- Opětovné vyhodnocení vyvoláme čárkou
```lisp
(list'if a b 't)

`(if ,a ,b t)

;; čárka na zpětné vyhodnocení
CL-USER 4 > `((+ 1 1) ,(+ 1 1))
((+ 1 1) 2)

;; rozbalení seznamu zavináčem
CL-USER 13 > `((list 1 2) ,(list 1 2) ,@(list 1 2))
((LIST 1 2) (1 2) 1 2)
```
#### Problém vícenásobného vyhodnocování
```lisp
(defmacro whenv (condition &body body)
	`(when ,condition
		,@body
		,condition))

;; expandovaný výraz
(when (cdr '(1 2))
	(print "Ano")
	(cdr '(1 2))))

;; zkouška v Listeneru
CL-USER 3 > (whenv (cdr (print'(1 2)))
				(print "Ano"))

(1 2)
"Ano"
(1 2)
(2)
;; (1 2) by se mělo správně vytisknout jen jednou
```
- Můžeme vyřešit vytvořením nové vazby
```lisp
(defmacro whenv (condition &body body)
	`(let ((result ,condition))
		(when result
			,@body
			result)))
```
- Vznikne tím ale nový problém **zabrání symbolu**
#### Problém zabrání symbolu
- Může k němu dojít pokud v expanzi makra vytvoříme nové prostředí, které zastiňuje prostředí vytvořené uživatelem
- Tím nám vzniknou nové neočekávané vazby
- **Řešení**: generování unikátního symbolu (funkce `gensym`)
```lisp
;; opravená verze
(defmacro whenv (condition &body body)
	(let ((res-symbol (gensym)))
		`(let ((,res-symbol ,condition))
			(when ,res-symbol
				,@body
				,res-symbol))))

(LET ((#:G1151 (CDR RESULT)))
	(WHEN #:G1151
		(PRINT "Neprázdné cdr v seznamu:")
		(PRINT RESULT)
		#:G1151))
```
- Jde řešit i napsáním pomocné funkce místo použití `gensym`
	- **pravidlo co nejrychlejšího úniku z makra do funkce**

## Rekurze v makrech
- Ve své expanzi obsahují sami sebe
- Při kompilaci (převodu programu z Lispu do jiného jazyka) se všechna makra expandují $\longrightarrow$ může dojít k zacyklení
- **Řešení:** uniknout z makra do pomocné funkce