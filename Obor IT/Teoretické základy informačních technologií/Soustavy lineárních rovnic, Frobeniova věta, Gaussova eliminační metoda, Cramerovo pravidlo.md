### Lineární rovnice

- Uvažujme číselné těleso $T$ a prvky $a_{1}, \ldots, a_{n}, b \in T$. Úloha určit všechny $n$-tice $\left(x_{1}, \ldots, x_{n}\right) \in T^{n}$, pro něž platí$$\sum_{i=1}^{n} a_{i} x_{i}=a_{1} x_{1} + \cdots + a_{n} x_{n}=b$$se nazývá **lineární rovnice** (LR) o $n$ neznámých nad $T$. **Každá $n$-tice**, pro kterou tato **rovnost nastane**, se nazývá **řešení** této rovnice.

> [!Example]- Isibalo - Lineární rovnice
><iframe width="660" height="385" src="https://www.youtube.com/embed/EtAaMRVTYvw?si=Wbo-i8o7sU1rB211" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Soustava lineárních rovnic

- Nechť $T$ je číselné těleso a $a_{ij}, b_{i} \in T$ pro každé $i=1, \ldots, m$ a každé $j=1, \ldots, n$. Úloha určit všechny $n$-tice $\left(x_{1}, \ldots, x_{n}\right) \in T^{n}$, pro které současně platí $$
(S)\left\{\begin{array}{c}
\sum_{j=1}^{n} a_{1 j} x_{j}=a_{11} x_{1}+\cdots+a_{1 n} x_{n}=b_{1}, \qquad (R_1) \\
\vdots \\
\sum_{j=1}^{n} a_{m j} x_{j}=a_{m 1} x_{1}+\cdots+a_{m n} x_{n}=b_{m}, \qquad (R_m)
\end{array}\right.
$$se nazývá **soustava $m$ lineárních rovnic** (SLR) o $n$ neznámých nad $T$. **Každá $n$-tice** splňující $(S)$ se nazývá **řešení** této soustavy.
---
- Jsou-li $M_{1}, \ldots, M_{m}$ množiny řešení rovnic $\left(R_{1}\right), \ldots,\left(R_{m}\right)$, pak pro množinu řešení soustavy $(S)$ platí $$M=M_{1} \cap \ldots \cap M_{m}$$
- Soustavu $(S)$ můžeme zkráceně zapisovat jako $$\sum_{j=1}^{n} a_{i j} x_{j}=b_{i}, \quad i=1, \ldots, m$$


>[!Example]- Isibalo - Soustava lineárních rovnic
><iframe width="660" height="385" src="https://www.youtube.com/embed/EmJmb_dNJmI?si=2NXmK4okiwrSQM3D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Matice soustavy lineárních rovnic
- Nechť je dána soustava $(S)$ lineárních rovnic. Pak matici  
$$
A=\left(\begin{array}{ccc}
a_{11} & \ldots & a_{1 n} \\
a_{21} & \ldots & a_{2 n} \\
\vdots & & \vdots \\
a_{m 1} & \ldots & a_{m n}
\end{array}\right), \operatorname{resp} \cdot\left(A \mid \vec{b}^{T}\right)=\left(\begin{array}{cccc}
a_{11} & \ldots & a_{1 n} & b_{1} \\
a_{21} & \ldots & a_{2 n} & b_{2} \\
\vdots & & \vdots & \vdots \\
a_{m 1} & \ldots & a_{m n} & b_{m}
\end{array}\right)
$$
nazýváme **matice soustavy** $(S)$, resp. **rozšířená matice soustavy** $(S)$.
### Řešitelnost SLR

- SLR $A \vec{x}^{T}=\vec{b}^{T}$ se nazývá **řešitelná**, jestliže existuje **alespoň jedno její řešení**. Dvě soustavy lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$ a $B \vec{x}^{T}=\vec{c}^{T}$ nazveme **ekvivalentní**, jestliže mají **stejné množiny řešení**.
---
- SLR $A \vec{x}^{T}=\vec{b}^{T}$ je řešitelná právě když je vektor $\vec{b}$ lineární kombinací sloupců matice $A \in \mathcal{M}_{m \times n}(T)$

##### Frobeniova věta
- Nehomogenní soustava lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$ je řešitelná právě tehdy, jeli $\mathrm{h}(A)=\mathrm{h}\left(A \mid \vec{b}^{T}\right)$.
---
- Je-li v této situaci navíc $\mathrm{h}(A)=n$, pak má tato soustava **právě jedno řešení**, pokud $\mathrm{h}(A)<n$, pak má nekonečně mnoho řešení (závislých na $n-\mathrm{h}(A)$ parametrech).
> [!Summary] Frobeniova věta
> Lineární soustava rovnic má řešení, pokud a jen pokud je **hodnost matice koeficientů rovna hodnosti rozšířené matice**. Rozšířená matice zahrnuje jak matici koeficientů, tak sloupec pravých stran rovnic.
> To se dá vyjádřit vztahem: $\mathrm{h}(A)=\mathrm{h}\left(A \mid \vec{b}^{T}\right)$

### Elementární řádkové transformace - EŘT
- **EŘT** matice $A \in \mathcal{M}_{m \times n}(T)$ nazýváme tyto úpravy:
	1. vzájemnou záměnu dvou řádků v $A$
	2. vynásobení některého řádku nenulovým číslem z $T$
	3. přičtení nenulového násobku některého řádku k jinému řádku v $A$

##### Definice řádkové ekvivalence
- Nechť $A, B \in \mathcal{M}_{m \times n}(T)$. Říkáme, že matice $A$ je **řádkově ekvivalentní** s maticí $B$, jestliže můžeme matici $B$ získat z $A$ pomocí konečného počtu EŘT. Pak píšeme $A \sim B$.
---
- **Věta**: Nechť $A, B \in \mathcal{M}_{m \times n}(T)$. Jestliže $A \sim B$, pak matice $A$ i $B$ určují stejné řádkové podprostory. ^09f1b7

>[!Example] Příklad
>Platí $A=\left(\begin{array}{rr}1 & 2 \\ -1 & 0 \\ 3 & 2\end{array}\right) \sim\left(\begin{array}{rr}-6 & -4 \\ -1 & 0 \\ 0 & 2\end{array}\right)=B$, protože $B$ můžeme z $A$ získat takto:
>1. zaměníme $1.$ a $3.$ řádek
>2. $1.$ řádek získané matice vynásobíme $(-2)$
>3. ke $3.$ řádku této matice přičteme její $2.$ řádek.

### Gaussův tvar

>[!Info]- Vedoucí prvek
>- **Vedoucím prvkem řádku** (řádkového vektoru) matice $A \in \mathcal{M}_{m \times n}(T)$ rozumíme **první nenulový prvek zleva** v tomto řádku.

- O matici $A \in \mathcal{M}_{m \times n}(T)$ řekneme, že je v **Gaussově tvaru** (GT), pokud všechny její nulové řádky jsou až za nenulovými a navíc pro každé její dva nenulové řádky $\overrightarrow{a_i}, \overrightarrow{a_j}$ musí být splněno, že pokud $i<j$, pak vedoucí prvek $i$-tého řádku leží ve sloupci, jehož index je menší než index sloupce, ve kterém leží vedoucí prvek $j$-tého řádku.
>[!Example] Příklad
>$$
>A=
>\left(
>\begin{array}{ccccc}
>1 & 2 & -5 & 0 & 1 \\ 
>0 & 0 & 2 & 0 & 5 \\ 
>0 & 0 & 0 & -5 & 4 \\ 
>0 & 0 & 0 & 0 & 0
>\end{array}
>\right)
>\text{je v GT,}
>\ \ \ \ \ \ \ \ \ \ \ \ \ \
>B=
>\left(
>\begin{array}{rrrr}
>0 & 2 & -5 & 0 \\ 
>0 & 0 & 3 & 1 \\ 
>0 & 0 & -2 & 8 \\ 
>0 & 0 & 0 & -8
>\end{array}
>\right)
>\text{není v GT.}
>$$

>[!Tip]
>- **Každá matice $A \in \mathcal{M}_{m \times n}(T)$ je řádkově ekvivalentní s některou maticí v Gaussově tvaru.**

- **Věta:** Je-li $A \sim B$ pro některé matice $A, B \in \mathcal{M}_{m \times n}(T)$, pak nenulové řádky matice $B$ tvoří bázi řádkového podprostoru matice $A$.

### Gaussova eliminační metoda
- Nechť je dána soustava lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$, kde $A \in \mathcal{M}_{m \times n}(T)$.
- Matici $\left(A \mid \vec{b}^{T}\right)$ převedeme pomocí elementárních řádkových transformací na matici $\left(B \mid \vec{c}^{T}\right)$, která je v GT (Gaussově tvaru).
- Pracujeme tedy dál s jinou soustavou, která má ale podle [[Soustavy lineárních rovnic, Frobeniova věta, Gaussova eliminační metoda, Cramerovo pravidlo#^09f1b7|věty]] stejnou množinu řešení jako daná. 
---
- Je-li $\mathrm{h}(A)=\mathrm{h}\left(A \mid \vec{b}^{T}\right)=h<n$, pak
$$
\left
(B \mid \vec{c}^{T}\right)=
\left(
\begin{array}{cccccc|c}
b_{11} & b_{12} & \ldots & b_{1 h} & \ldots & b_{1 n} & c_{1} \\
0 & b_{22} & \ldots & b_{2 h} & \ldots & b_{2 n} & c_{2} \\
\vdots & \vdots & \ddots & \vdots & & \vdots & \vdots \\
0 & 0 & \ldots & b_{h h} & \ldots & b_{h n} & c_{h} \\
0 & & & \ldots & & 0 & 0 \\
\vdots & & & & & \vdots & \vdots \\
0 & & & \ldots & & 0 & 0
\end{array}
\right)
$$
- Přitom se dá vždy zařídit (prohození sloupců), že $b_{i i} \neq 0$ pro každé $i=$ $1,2, \ldots, h$.
---
- Z rovnice $b_{h h} x_{h}+\ldots+b_{h n} x_{n}=c_{h}$, která odpovídá **poslednímu nenulovému řádku matice** $\left(B \mid \vec{c}^{T}\right)$ vypočítáme $x_{h}$ v závislosti na $x_{h+1}, \ldots, x_{n}$.
- Z rovnice, která odpovídá předposlednímu nenulovému řádku vypočítáme v závislosti na $x_{h+1}, \ldots, x_{n}$ neznámou $x_{h-1}$.
$$\vdots$$
- Z rovnice odpovídající prvnímu řádku $\left(B \mid \vec{c}^{T}\right)$ dopočítáme $x_{1}$ v závislosti na $x_{h+1}, \ldots, x_{n}$.
---
- Jestliže $\mathrm{h}(A)=\mathrm{h}\left(A \mid \vec{b}^{T}\right)=n$, pak
$$
\left(B \mid \vec{c}^{T}\right)=\left(\begin{array}{cccc|c}
b_{11} & b_{12} & \ldots & b_{1 n} & c_{1} \\
0 & b_{22} & \ldots & b_{2 n} & c_{2} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \ldots & b_{n n} & c_{n} \\
0 & \ldots & & 0 & 0 \\
\vdots & & & \vdots & \vdots \\
0 & \ldots & & 0 & 0
\end{array}\right).
$$
---
- Z rovnice $b_{n n} x_{n}=c_{n}$, která odpovídá $n$-tému řádku matice $\left(B \mid \vec{c}^{T}\right)$ máme
$$
x_{n}=\frac{1}{b_{n n}} \cdot c_{n}
$$
- Z rovnice, která odpovídá předposlednímu nenulovému řádku vypočítáme

$$
x_{n-1}=\frac{1}{b_{n-1, n-1}} \cdot\left(c_{n-1}-b_{n-1, n} \cdot x_{n}\right)
$$
$$\vdots$$
- Až konečně z rovnice odpovídající prvnímu řádku $\left(B \mid \vec{c}^{T}\right)$ dopočítáme
$$
x_{1}=\frac{1}{b_{11}} \cdot\left(c_{1}-b_{1 n} \cdot x_{n}-b_{1, n-1} \cdot x_{n-1}-\cdots-b_{12} \cdot x_{2}\right)
$$

>[!Example]- Isibalo - Gaussova eliminační metoda
><iframe width="660" height="385" src="https://www.youtube.com/embed/buhdFjMy7PU?si=RCeB41e5YyVfnCjR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

> [!Summary] Gaussova eliminační metoda
> Používá se k vyřešení soustav lineárních rovnic.
> 1) Soustavu rovnic přepíšeme do matice i se sloupcem pravých stran.
> 2) Při aplikování Gaussové eliminační metody tzn. upravuji matici na "trojúhelníkový" (Gaussův) tvar pomocí EŘT.
> 3) Po úpravě na Gaussův tvar pomocí zpětné substituce od posledního řádku postupně dosazujeme známé hodnoty do předchozích rovnic a řešíme zbylé neznámé.

### Cramerovo pravidlo
- Další možnost jak řešit SLR.
- Nelze použít vždy.
- Pouze když soustava obsahuje tolik **rovnic jako neznámých** a navíc **hodnost** její matice je **plná**.
### Věta (Cramerovo pravidlo):
- Je dána soustava $n$ lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$ o $n$ neznámých nad $T$ taková, že platí $\operatorname{det}(A) \neq 0$. Pak tato soustava má právě jedno řešení $\vec{x}=\left(x_{1}, \ldots, x_{n}\right)$, pro něž platí
$$
x_{j}=\frac{\operatorname{det}\left(A_{j}\right)}{\operatorname{det}(A)} \quad \forall j=1, \ldots, n
$$
- Přitom matice $A_{j}$ je matice, kterou získáme nahrazením $j$-tého sloupcového vektoru matice $A$, tedy $\vec{a_{j}}^{T}$, vektorem $\vec{b}^{T}$.

>[!Example] Příklad
>- Určete druhou složku vektoru řešení soustavy:
>$$
>\begin{aligned}
>x_{1}+2 x_{2}+5 x_{3} & =-9 \\
>x_{1}-x_{2}+3 x_{3} & =2 \\
>3 x_{1}-6 x_{2}-x_{3} & =25
>\end{aligned}
>$$
>- Řešení:
>Podle Cramerova pravidla je $x_{2}=\frac{\left|A_{2}\right|}{|A|}$, kde:
>$$
>|A|=\left|\begin{array}{rrr}
>1 & 2 & 5 \\
>1 & -1 & 3 \\
>3 & -6 & -1
>\end{array}\right|=20 \quad \text { a }
>\quad\left|A_{2}\right|=\left|\begin{array}{rrr}
>1 & -9 & 5 \\
>1 & 2 & 3 \\
>3 & 25 & -1
>\end{array}\right|=-60
>$$ 
>tedy $x_{2}=-3$.

>[!Example]- Isibalo - Cramerovo pravidlo
><iframe width="660" height="385" src="https://www.youtube.com/embed/nyi42cJ8olM?si=C4gvMeMQDubkSvlB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
##### Navigace
Předchozí: [[Eukleidovské vektorové prostory, ortogonální a ortonormální báze, Schwarzova nerovnost, Schmidtova ortogonalizační metoda]]
Následující: [[Lineární zobrazení a transformace a jejich matice]]
Celý okruh: [[1. Teoretické základy informačních technologií]]
