### Binární relace na množině
- Nechť $A, B$ jsou neprázné množiny. **Kartézský součin množin $A$ a $B$ ($A \times B$)** je množina všech **uspořádaných** dvojic **$<a,b>$, kde $a \in A, b \in B$**.
- Každou podmnožinu $R \subseteq A \times B$ nazveme **binární relace mezi množinami $A$ a $B$**. **Je-li $A = B$, pak $R \subseteq A \times A$** nazveme **binární relace na množině $A$**

- Binární relace na množině $X$ jsou relace $R \subseteq X \times Y$, kde $X=Y$
- Speciální relace:
	- $\varnothing$ (**Prázdná relace**) - symetrická, antisymetrická, tranzitivní, irreflexivní, asymetrická
	- **Relace identity**, $id_{x} = \{<x,y> \mid x \in X \}$ - reflexivní, symetrická, antisymetrická, tranzitivní (a úplná, když je $\mid X \mid = 1$)
	- **Kartézský součin (plná relace) $X \times X$** - reflexivní, symetrická, tranzitivní a úplná (antisymetrická pro $\mid X \mid = 1$)

### Vlastnosti binární relace
- Nechť $R$ je relace na množině $X$:

- **Reflexivní**
	- Pokud **pro každé $x \in X$ platí $<x,x> \in R$**
	- Každé prvek z $X$ je v relaci sám se sebou
	- Na matici to poznáme pomocí diagonály jedniček
	- V orientovaném grafu je u každého vrcholu smyška
- **Symetrická**
	- Pokud **pro každé $x,y \in X$ platí $(<x,y> \in R) \rightarrow (<y,x> \in R)$**
	- Každé relace $<x,y> \in R$ se objeví i v převrácené formě, tedy $<y,x> \in R$
	- Na matici to poznáme, že je symetrická podle diagonály
	- V orientovaném grafu se projevuje tak, že buď jsou mezi body dvě hrany, nebo žádná
- **Antisymetrická**
	- Pokud **pro každé $x,y \in X$ platí  $(<x,y> \in R \wedge <y,x> \in R) \rightarrow (x + y)$**
	- Vyjadřuje, že pro každé dva různé prvky z $X$ neplatí zároveň $<x,y> \in R$ a $<y,x> \in R$
	- Každá dvě různá pole v matice, které jsou souměrné podle diagonály, neobsahují dvě jedničky
	- V orientovaném grafu mezi dvěma vrcholy vede jedna nebo žádná hrana
- **Tranzitivní**
	- Pokud **pro každé $x,y \in X$ platí $(<x,y> \in R \wedge <y,z> \in R) \rightarrow (<x,z> \in R)$**
	- Pokud $<x,y> \in R$ a $<y,z> \in R$, pak také $<x,z> \in R$
	- V orientovaním grafu, když vede **šipka** z **$k$** do **$l$** a z **$l$** do **$m$**, tak musí vést **šipka** i z **$k$** do **$m$**
- Irreflexivní
	- Pokud **pro každé $x \in X$ platí $<x,x> \notin R$**
- Asymetrická
	- Pokud **pro každé $x,y \in X$ platí $(<x,y> \in R) \rightarrow (<y,x> \notin R)$**
- Úplná
	- Pokud pro každé $x,y \in X$ platí $(x<y> \in R) \vee (<y,x> \in R)$
