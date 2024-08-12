### Pojem funkce
- Nechť $X, Y$ jsou neprázdné množiny a $R$ je binární relace mezi množinami $X$ a $Y$.
- Relace $R$ se nazývá **zobrazení $X$ do $Y$**, má-li tyto vlastnosti:
	- **pro každé $x \in X$ existuje $y \in Y$ tak, že $<x,y> \in R$**
	- **pro každé $x \in X$ a $y_{1}, y_{2} \in Y$ platí, že $<x,y_{1}> \in R$ a $<x,y_{2}> \in R \rightarrow y_{1} = y_{2}$**
- Funkce je matematickým protějškem k pojmu přiřazení
- **Parciální** (částečná) **funkce - může existovat $x \in X$ ke kterému neexistuje $y$**

- Je-li $R \subseteq X \times Y$ funkce, píšeme $R: X \rightarrow Y$
- Používáme spíš $f, g$ ... než $R, S$

- Je-li $f: X \rightarrow Y$ funkce a $x \in X$, pak $y \in Y$, pro který je $<x,y> \in f$, označujeme $f(x)$, píšeme také $x \mapsto y$ ($x \mapsto f(x)$).
- V tom případě říkáme, že $f$ zobrazuje prvek $x$ na prvek $y$

- Prvek $y$ nazveme **obraz prvku** $x$, prvek $x$ nazveme **vzor prvku** $y$.
- Množinu $f(X) = \{ f(x)\ |\  x \in A \}$ nazveme **úplný obraz množiny $X$**

### Vlastnosti funkcí
- Funkce $f: X \rightarrow Y$ se nazývá:
	- **Prostá (injektivní),** právě když:
		- pro **každé $x_{1}, x_{2} \in X$ platí, jestliže $x_{1} \neq x_{2}$ pak $f(x_{1}) \neq f(x_{2})$**
		- tedy neopakují se $y$ pro dvě různá $x$
	- **Funkce množiny $X$ na množinu $Y$ (surjektivní)**, právě když
		- pro **každé $y \in Y$ existuje $x \in X$ tak, že $f(x) = y$**
		- tedy musí být použita všechny prvky z $Y$
	- **Vzájemně jednoznačná (bijektivní)**, právě když 
		- **je prostá a je to funkce na množinu $Y$**
		- tedy *injektivní* a *surjektivní* zároveň

##### Navigace
Předchozí:  [[Relace, binární relace a jejich reprezentace, operace s relacemi]]
Následující: [[Binární relace na množině a jejich vlastnosti]]
Celý okruh: [[1. Teoretické základy informačních technologií]]