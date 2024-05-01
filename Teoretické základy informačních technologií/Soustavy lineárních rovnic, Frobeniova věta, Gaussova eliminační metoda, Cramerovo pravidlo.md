### Lineární rovnice
##### Definice
Uvažujme číselné těleso $T$ a prvky $a_{1}, \ldots, a_{n}, b \in T$. Úloha určit všechny $n$-tice $\left(x_{1}, \ldots, x_{n}\right) \in T^{n}$, pro něž platí

$$
\sum_{i=1}^{n} a_{i} x_{i}=a_{1} x_{1} + \cdots + a_{n} x_{n}=b
$$

se nazývá **lineární rovnice** (LR) o $n$ neznámých nad $T$.

**Každá $n$-tice**, pro kterou tato **rovnost nastane**, se nazývá **řešení** této rovnice.

### Soustava lineárních rovnic
##### Definice
Nechť $T$ je číselné těleso a $a_{ij}, b_{i} \in T$ pro každé $i=1, \ldots, m$ a každé $j=1, \ldots, n$. 
Úloha určit všechny $n$-tice $\left(x_{1}, \ldots, x_{n}\right) \in T^{n}$, pro které současně platí

$$
(S)\left\{\begin{array}{c}
\sum_{j=1}^{n} a_{1 j} x_{j}=a_{11} x_{1}+\cdots+a_{1 n} x_{n}=b_{1}, \qquad (R_1) \\
\vdots \\
\sum_{j=1}^{n} a_{m j} x_{j}=a_{m 1} x_{1}+\cdots+a_{m n} x_{n}=b_{m}, \qquad (R_m)
\end{array}\right.
$$

se nazývá **soustava $m$ lineárních rovnic** (SLR) o $n$ neznámých nad $T$.

**Každá $n$-tice** splňující $(S)$ se nazývá **řešení** této soustavy.
### Soustava lineárních rovnic
- Jsou-li $M_{1}, \ldots, M_{m}$ množiny řešení rovnic $\left(R_{1}\right), \ldots,\left(R_{m}\right)$, pak pro množinu řešení soustavy $(S)$ platí

$$
M=M_{1} \cap \ldots \cap M_{m}
$$

- Soustavu $(S)$ můžeme zkráceně zapisovat jako

$$
\sum_{j=1}^{n} a_{i j} x_{j}=b_{i}, \quad i=1, \ldots, m
$$

### Matice soustavy lineárních rovnic
##### Definice
Dána SLR $(S)$. Pak matici

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

nazýváme **matice soustavy** $(S)$, resp. **rozšířená matice soustavy** $(S)$,
### Matice soustavy lineárních rovnic

- Dána $\operatorname{SLR}(S), A \in \mathcal{M}_{m \times n}(T)$ nechť je její matice.
- Označme $\vec{x}^{T}=\left(\begin{array}{c}x_{1} \\ \vdots \\ x_{n}\end{array}\right), \vec{b}^{T}=\left(\begin{array}{c}b_{1} \\ \vdots \\ b_{n}\end{array}\right)$.
- Soustavu $(S)$ pak můžeme psát v tzv. **maticovém tvaru**

$$
A \vec{x}^{T}=\vec{b}^{T}
$$
### Řešitelnost SLR
##### Definice
SLR $A \vec{x}^{T}=\vec{b}^{T}$ se nazývá **řešitelná**, jestliže existuje **alespoň jedno její řešení**. Dvě soustavy lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$ a $B \vec{x}^{T}=\vec{c}^{T}$ nazveme **ekvivalentní**, jestliže mají **stejné množiny řešení**.

- SLR $A \vec{x}^{T}=\vec{b}^{T}$ je řešitelná právě když je vektor $\vec{b}$ lineární kombinací sloupců matice $A \in \mathcal{M}_{m \times n}(T)$

- Dány soustavy $A \vec{x}^{T}=\vec{b}^{T}$ a $B \vec{x}^{T}=\vec{c}^{T} m$ LR o $n$ neznámých nad $T$. Je-li $\left(A \mid \vec{b}^{T}\right) \sim\left(B \mid \vec{c}^{T}\right)$, pak jsou tyto dvě soustavy ekvivalentní ^09f1b7

### Řešitelnost SLR
##### Věta (Frobeniova nebo Kroneckerova - Cappeliova)
Soustava lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$ je řešitelná právě když $\mathrm{h}(A)=\mathrm{h}\left(A \mid \vec{b}^{T}\right)$.

Je-li v této situaci navíc $\mathrm{h}(A)=n$, pak má tato soustava právě jedno řešení, pokud $\mathrm{h}(A)<n$, pak má nekonečně mnoho řešení (závislých na $n-\mathrm{h}(A)$ parametrech).

### Gaussova eliminační metoda
- Dána soustava lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$, kde $A \in \mathcal{M}_{m \times n}(T)$.
- Matici $\left(A \mid \vec{b}^{T}\right)$ převedeme pomocí EŘT (elementární řádkové transformace) na matici $\left(B \mid \vec{c}^{T}\right)$, která je v GT (Gaussově tvaru).
- Pracujeme tedy dál s jinou soustavou, která má ale podle [[Soustavy lineárních rovnic, Frobeniova věta, Gaussova eliminační metoda, Cramerovo pravidlo#^09f1b7|věty]] stejnou množinu řešení jako daná. 

- Je-li $\mathrm{h}(A)=\mathrm{h}\left(A \mid \vec{b}^{T}\right)=h<n$, pak

$$
\left(B \mid \vec{c}^{T}\right)=\left(\begin{array}{cccccc|c}
b_{11} & b_{12} & \ldots & b_{1 h} & \ldots & b_{1 n} & c_{1} \\
0 & b_{22} & \ldots & b_{2 h} & \ldots & b_{2 n} & c_{2} \\
\vdots & \vdots & \ddots & \vdots & & \vdots & \vdots \\
0 & 0 & \ldots & b_{h h} & \ldots & b_{h n} & c_{h} \\
0 & & & \ldots & & 0 & 0 \\
\vdots & & & & \vdots & \vdots \\
0 & & & \ldots & & 0 & 0
\end{array}\right)
$$

- Přitom se dá vždy zařídit (prohození sloupců), že $b_{i i} \neq 0$ pro každé $i=$ $1,2, \ldots, h$.


## Gaussova eliminační metoda

- Z rovnice $b_{h h} x_{h}+\ldots+b_{h n} x_{n}=c_{h}$, která odpovídá poslednímu nenulovému rádku matice $\left(B \mid \vec{c}^{T}\right)$ vypočítáme $x_{h}$ v závislosti na $x_{h+1}, \ldots, x_{n}$.
- Z rovnice, která odpovídá předposlednímu nenulovému rádku vypočítáme v závislosti na $x_{h+1}, \ldots, x_{n}$ neznámou $x_{h-1}$.
- Z rovnice odpovídající prvnímu řádku $\left(B \mid \vec{c}^{T}\right)$ dopočítáme $x_{1} \mathrm{v}$ závislosti na $x_{h+1}, \ldots, x_{n}$.


## Gaussova eliminační metoda

- Jestliže $\mathrm{h}(A)=\mathrm{h}\left(A \mid \vec{b}^{T}\right)=n$, pak

$$
\left(B \mid \vec{c}^{T}\right)=\left(\begin{array}{cccc|c}
b_{11} & b_{12} & \ldots & b_{1 n} & c_{1} \\
0 & b_{22} & \ldots & b_{2 n} & c_{2} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \ldots & b_{n n} & c_{n} \\
0 & \ldots & 0 & 0 \\
\vdots & & \vdots & \vdots \\
0 & \ldots & 0 & 0
\end{array}\right)
$$

## Gaussova eliminační metoda

- Z rovnice $b_{n n} x_{n}=c_{n}$, která odpovídá $n$-tému řádku matice $\left(B \mid \vec{c}^{T}\right)$ máme

$$
x_{n}=\frac{1}{b_{n n}} \cdot c_{n}
$$

- Z rovnice, která odpovídá předposlednímu nenulovému řádku vypočítáme

$$
x_{n-1}=\frac{1}{b_{n-1, n-1}} \cdot\left(c_{n-1}-b_{n-1, n} \cdot x_{n}\right)
$$

- Až konečně z rovnice odpovídající prvnímu řádku $\left(B \mid \vec{c}^{T}\right)$ dopočítáme

$$
x_{1}=\frac{1}{b_{11}} \cdot\left(c_{1}-b_{1 n} \cdot x_{n}-b_{1, n-1} \cdot x_{n-1}-\cdots-b_{12} \cdot x_{2}\right)
$$

## Cramerovo pravidlo

- Další možnost jak řešit SLR.
- Nelze použít vždy.
- Pouze když soustava obsahuje tolik rovnic jako neznámých a navíc hodnost její matice je plná.


## Věta 7.9 (Cramerovo pravidlo)

Dána soustava $n$ lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$ o $n$ neznámých nad $T$ taková, že platí $\operatorname{det}(A) \neq 0$. Pak tato soustava má právě jedno řešení $\vec{x}=\left(x_{1}, \ldots, x_{n}\right)$, pro něž platí

$$
x_{j}=\frac{\operatorname{det}\left(A_{j}\right)}{\operatorname{det}(A)} \quad \forall j=1, \ldots, n
$$

Přitom matice $A_{j}$ je matice, kterou získáme nahrazením $j$-tého sloupcového vektoru matice $A$, tedy ${\overrightarrow{a_{j}}}^{T}$, vektorem $\vec{b}^{T}$.

## Cramerovo pravidlo

Přiklad 7.5

Určete druhou složku vektoru řešení soustavy

$$
\begin{aligned}
x_{1}+2 x_{2}+5 x_{3} & =-9 \\
x_{1}-x_{2}+3 x_{3} & =2 \\
3 x_{1}-6 x_{2}-x_{3} & =25
\end{aligned}
$$

Řešení: Podle Cramerova pravidla je $x_{2}=\frac{\left|A_{2}\right|}{|A|}$, kde

$$
|A|=\left|\begin{array}{rrr}
1 & 2 & 5 \\
1 & -1 & 3 \\
3 & -6 & -1
\end{array}\right|=20 \quad \text { a } \quad\left|A_{2}\right|=\left|\begin{array}{rrr}
1 & -9 & 5 \\
1 & 2 & 3 \\
3 & 25 & -1
\end{array}\right|=-60
$$

tedy $x_{2}=-3$.

## 3 Homogenní soustavy lineárních rovnic

## Obsah

## Obsah

## Homogenní SLR

Definice 7.11

Soustava lineárních rovnic $A \vec{x}^{T}=\vec{b}^{T}$ se nazývá homogenní, jestliže $\vec{b}=\vec{o}$. V opačném případě se nazývá nehomogenní.

Věta 7.10

Necht $A \vec{x}^{T}=\vec{o}^{T}$ je homogenní SLR nad $T$ taková, že $A \in \mathcal{M}_{m \times n}(T)$ a $\mathrm{h}(A)=$ $h$. Pak všechna řešení této soustavy tvoří podprostor v AVP $T^{n}$ (prostor řešeni této soustavy). Jeho dimenze je přitom rovna $n-h$.

## Fundamentální systém řešení homogenní SLR

Definice 7.12

Fundamentálním systémem řešení (FSŘ) homogenní SLR $A \vec{x}^{T}=\vec{o}^{T}$ rozumíme každou bázi prostoru řešení této soustavy.

- Podle definice je zrejmé, že FSŘ jsou určena všechna řešení této soustavy (báze je množina generátorů).
- Pokud je matice soustavy $A \vec{x}^{T}=\vec{o}^{T}$ čtvercová, má tato soustava právě jedno řešení právě když $\operatorname{det}(A) \neq 0$.
- Jediným řešením je přitom $\vec{o}$ (tzv. triviální řešení).
- Dimenze prostoru řešení takovéto soustavy je potom 0 , a nemá smysl mluvit o jejím FSŘ.


## Fundamentální systém řešení homogenní SLR

Přiklad 7.6

Určete FSŘ soustavy

$$
\begin{aligned}
x_{1}+2 x_{2}-x_{3}+3 x_{4}-2 x_{5} & =0 \\
2 x_{1}+x_{2}+x_{4}-3 x_{5} & =0 \\
5 x_{1}+4 x_{2}-x_{3}+5 x_{4}-8 x_{5} & =0 \\
3 x_{2}-2 x_{3}+5 x_{4}-x_{5} & =0
\end{aligned}
$$

Řešení: Matici soustavy převedeme na GT, tedy

$$
\left(\begin{array}{rrrrr}
1 & 2 & -1 & 3 & -2 \\
2 & 1 & 0 & 1 & -3 \\
5 & 4 & -1 & 5 & -8 \\
0 & 3 & -2 & 5 & -1
\end{array}\right) \sim \cdots \sim\left(\begin{array}{rrrrr}
1 & 2 & -1 & 3 & -2 \\
0 & -3 & 2 & -5 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{array}\right)
$$

Fundamentální systém řešení homogenní SLR

Přiklad 7. 6

Řešení:

- Tedy $\mathrm{h}(A)=2$, a soustava má proto nekonečně mnoho řešení, která budou záviset na 3 parametrech.
- Za parametry zvolíme např. $x_{2}, x_{3}, x_{4}$.
- Pak ze dvou nenulových řádků nalezené matice v GT získáme tzv. obecné rešení soustavy: $\left(4 x_{2}-3 x_{3}-7 x_{4}, x_{2}, x_{3}, x_{4}, 3 x_{2}-2 x_{3}+5 x_{4}\right)$.
- FSŘ získáme tak, že trojici $\left(x_{2}, x_{3}, x_{4}\right)$ volíme $\mathrm{v}$ obecném řešení postupně jako jednotlivé prvky kanonické báze v AVP $T^{3}$, tzn.

| $x_{2}$ | $x_{3}$ | $x_{4}$ |  | FSŘ je tedy trojice: |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 |  | $\overrightarrow{u_{1}}=(4,1,0,0,3)$ |
| 0 | 1 | 0 | $=$ | $\overrightarrow{u_{2}}=(-3,0,1,0,-2)$ |
| 0 | 0 | 1 |  | $\overrightarrow{u_{3}}=(-7,0,0,1,5)$ |

## Vztah řešení homogenní SLR a nehomogenní SLR

## Definice 7.13

Necht $A \vec{x}^{T}=\vec{b}^{T}$ je nehomogenní SLR nad $T$. Pak homogenní soustava $A \vec{x}^{T}=$ $\vec{o}^{T}$ se nazývá soustava přiřazená $\mathrm{k} A \vec{x}^{T}=\vec{b}^{T}$.

Věta 7.11

Necht $A \vec{x}^{T}=\vec{b}^{T}$ je nehomogenní SLR $\left(A \in \mathcal{M}_{m \times n}(T)\right)$ nad $T$ a necht $\vec{u}$ je některé její řešení. Pak množina všech řešení této soustavy je tvořena právě všemi vektory $\vec{u}+\vec{v} \in T^{n}$, kde $\vec{v}$ je libovolné řešení přiřazené homogenní soustavy.

