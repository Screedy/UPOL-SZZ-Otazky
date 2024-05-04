### Ekvivalence
- Ekvivalence jsou matematickým protějškem k pojmu nerozlišitelnost
- Binární relace $E$ na množině $A \neq \varnothing$ se nazývá **ekvivalence**, je-li **reflexivní, symetrická a tranzitivní**.

- Vlastnosti:
	- **Reflexivní**
		- Každé $x$ z $X$ je totožné s $x$, tedy $x$ nelze rozlišit od $x$
	- **Symetrická**
		- Pokud $x$ nelze rozlišit od $y$, pak i $y$ nelze rozlišit od $x$
	- **Tranzitivní**
		- Pokud $x$ nelze rozlišit od $y$ a $y$ od $z$, pak i $x$ nelze rozlišit od $z$

- Reflexivní a symetrická relace se nazývá *tolerance*
- *Tranzitivní tolerance* se nazývá *ekvivalence*

- Pro ekvivalenci $E$ na množině $X$ definujeme pro každý $x \in X$ množinu
	- $[x]_{E} = \{y \in X \mid <x,y> \in E \}$ = třída ekvivalence prvku $x$
	- $[x]_{E}$ je množina těch prvků $y \in X$, které jsou E-ekvivalentní $x$

- $<x,y> \in E$ čteme jako "*$x$ a $y$ jsou E-ekvivalentní*"

- Relace *identity* $id_{x}$ je *nejmenší* ekvivalence na $X$
	- $id_{x} = \{<a,a>,<b,b>,<c,c>\}$
- Relace *kartézského součinu* $\iota_{X}$ je největší ekvivalence na $X$

### Rozklad
- Rozklad na množině je matematický protějšek shluků nerozlišitelných prvků

- Nechť **$X \neq \varnothing$** je množina. Systém množin $\Pi \subseteq 2^{X}$ splňují
	- **$Y \neq \varnothing$ pro každou $Y \in \Pi$**
		- Rozklad $\Pi$ na $X$ je systém neprázdných podmnožin $Y$
	- **Pro každé $Y_{1}, Y_{2} \in \Pi$ platí: pokud $Y_{1} \cap Y_{2} \neq \varnothing$, pak $Y_{1} = Y_{2}$**
		- Požadujeme, aby dvě různé třídy rozkladu $\Pi$ byly disjunktní
	- $\cup \, \Pi = X$
		- Sjednocení všech tříd rozkladu $\Pi$ bylo rovno množině $X$ se nazývá **rozklad na množině $X$**. 
		- Množiny $Y \in \Pi$ nazýváme **třídy rozkladu $\Pi$**. Pro prvek $x \in X$ označíme $[x]_{\Pi}$ tu třídu rozkladu $\Pi$, která obsahuje $x$.

- Na množině $X$ existují dva mezní rozklady:
	- $[x]_{\Pi} = \{x\}$
		- Všechny třídy rozkladu $\Pi$ jsou jednoprvkové
	- $[x]_{\Pi} = X$
		- Máme jen jednu třídu rozkladu $\Pi$, která je rovna celé $X$

- Všechny rozklady pro $X = \{a,b,c,d\}$:
	$$
	\begin{aligned}
	\{\{a\},\{b\},\{c\},\{d\}\} &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\\
	\{\{a,b\}, \{c\}, \{d\}\} \\
	\{\{b\},\{a,c\},\{d\}\} \\
	\{\{b\}, \{c\}, \{a,d\}\, \\
	\{\{a\},\{b,c\},\{d\}\} \\
	\{\{a,b,c\},\{d\}\} \\
	\set{\set{b,c},\set{a,d}} \\
	\set{\set{a},\set{c}, \set{b,d}} \\
	\set{\set{a,c},\set{b,d}} \\
	\set{\set{c}, \set{a,b,d}} \\
	\set{\set{a},\set{b},\set{c,d}} \\
	\set{\set{a,b},\set{c,d}} \\
	\set{\set{b},\set{a,c,d}} \\
	\set{\set{a}, \set{b,c,d}} \\
	\set{\set{a,b,c,d}}
	\end{aligned}
	$$

### Rozklad a Ekvivalence
- Nechť **$\Pi$ je rozklad na $X$**. Pak **binární relace $E_{\Pi}$ na $X$** definovaná
	- $<x,y> \in E_{\Pi}$, právě když $[x]_{\Pi} = [y]_{\Pi}$
	je ekvivalence příslušná rozkladu $\Pi$

 - Nechť **$E$ je ekvivalence na $X$**. Pak **systém množin $\Pi_{E} \subseteq 2^{X}$** definovaný
	 - $\Pi_{E} = \{[x]_{E} \mid x \in X \}$
	je rozklad příslušný ekvivalenci $E$

- Pro ekvivalenci $E$ na $X$ a pro rozklad $\Pi$ na $X$ máme **$E_{\Pi_E} = E, \, \Pi_{E_\Pi} = \Pi$**

### Přirozené zobrazení
- Rozklad na množině $X$ příslušný ekvivalenci $E$ označujeme běžně $X/E$ místo $\Pi_{E}$ a někdy jej nazýváme faktorová množina $X$ podle $E$
- Jelikož $[x]_{E} = [x]_{\Pi E}$, říkáme, že $[x]_{E}$ je třída rozkladu množiny $X$ podle $E$

- Uvažujeme-li o vztahu množiny $X$ a rozkladu $X/E$, pak víme, že každému $x \in X$ přísluší třída rozkladu $[x]_{E}$, pro kterou $x \in [x]_{E}$

- Pro **ekvivalenci E na X** tedy můžeme uvažovat zobrazení **$f_{E}:X \rightarrow X/E$**,
	- kde $f_{E}(x) = [x]_{E}$ pro každý $x \in X$,
	a nazýváme jej přirozené (kanonické) zobrazení.

- Platí, že každé přirození zobrazení $f_{E}$ je surjektivní
- $f_{E}$ je i injektivní, právě když $[x]_{E} = \{x\}$ pro každé $x \in X$, což je právě když $E = id_{x}$

##### Navigace
Předchozí:  [[Binární relace na množině a jejich vlastnosti]]
Následující: [[Uspořádání, Hasseovy diagramy]]
Celý okruh: [[1. Teoretické základy informačních technologií]]