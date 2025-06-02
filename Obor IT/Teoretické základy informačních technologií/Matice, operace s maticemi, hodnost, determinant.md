### Číselné těleso
- **těleso** ... množina, kde jsou definované 2 binární operace
### Matice
- Nechť $(T; +; \circ)$ je **číselné těleso,** $m, n \in \mathbb{N}$ a dále nechť $a_{ij} \in T$ pro všechny indexy $i = 1, 2, ..., m$ a $j = 1,2,...,n$. Potom **schéma**
  $$
  \begin{pmatrix}
	a_{11} & a_{12} & ... & a_{1n} \\
	a_{21} & a_{22} & ... & a_{2n} \\
	\vdots & \vdots &     & \vdots \\
	a_{m1} & a_{m2} & ... & a_{mn}
  \end{pmatrix}
  =(a_{ij})_{m \times n}
  $$
  se nazývá **matice typu $m \times n$ nad $T$**

- Pro každý prvek $a_{ij}$ je $i$ jeho řádkový index a $j$ jeho sloupcový index.
- Nechť **$r = min\{m,n\}$**, pak prvky $a_{11}, a_{22}, ..., a_{rr}$ tvoří tzv. **hlavní diagonálu matice $A$**.

### Typy matic
- Matice $A = (a_{ij})_{m \times n}$ se nazývá **nulová**, jestliže $a_{ij} = 0$ pro každý index $i, j$.
- Matice $A = (a_{ij})_{m \times n}$ se nazývá **čtvercová** stupně $n$, jestliže $m=n$.
- Čtvercová matice se nazývá **diagonální**, jestliže mimo hlavní diagonálu jsou všechny prvky nulové
- Diagonální matice se nazývá **skalární**, jsou-li si všechny prvky hlavní diagonály rovny.
- Skalární matice se nazývá **jednotková**, pokud má na hlavní diagonále samé jedničky. Značíme ji $E$.

### Rovnost matic
- Dvě matice $A, B \in M_{m \times n}(T)$ jsou si **rovny** (píšeme $A=B$), jestliže $a_{ij} = b_{ij}$ pro každé $i,j$.

### Sčítání matic
- Nechť $A, B \in M_{m \times n}(T)$. **Součtem matic $A$ a $B$** rozumíme matici **$A + B = (c_{ij})_{m \times n}$**, kde $c_{ij} = a_{ij} + b_{ij}$ pro každé $i,j$.
>[!Example] Příklad
>  $$
>  \begin{aligned}
>  \begin{gather}
>  A=
>  \begin{pmatrix}
>  1 & -2 & 0 \\ 
>  -1 & 3 & 1
>  \end{pmatrix}, \ B=
>  \begin{pmatrix}
>  2 & -2 & 1 \\ 
>  0 & -1 & 4
>  \end{pmatrix} \\\\A+B=
>  \begin{pmatrix}
>  3 & -4 & 1 \\
>  -1 & 2 & 5
>  \end{pmatrix}.
>  \end{gather}
>  \end{aligned}
>  $$

### Násobení matice skalárem
- Nechť $(T; +; \cdot)$ je číselné těleso, $A \in M_{m \times n}(T), c \in T$.
- Zavedeme zobrazení "$\cdot$":$\ T \times M_{m \times n}(T) \rightarrow M_{m \times n}(T)$ předpisem $c \cdot A = (b_{ij})_{m \times n},$ kde $b_{ij} = c \cdot a_{ij}$ pro každé $i,j$.
- *(Prvky z $T$ nazýváme skaláry.)*
>[!Example] Příklad
> - Mějme matici $A=\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}$ a skalár $c = 3$.
> - Vynásobíme-li matici skalárem $c$, dostaneme: 
>   $3A=\begin{pmatrix}3 \cdot 1 & 3 \cdot 2 \\ 3 \cdot 3 & 3 \cdot 4\end{pmatrix} =\begin{pmatrix}3 & 6 \\ 9 & 12\end{pmatrix}$
> - Pro libovolné skaláry $c, d \in T$ a libovolné matice $A, B \in M_{m \times n}(T)$ platí
> 	1. $c \cdot (A+B) = c \cdot A + c \cdot B,$
> 	2. $(c+d) \cdot A = c \cdot A + d \cdot A,$
> 	3. $(c \cdot d) \cdot A = c \cdot (d \cdot A),$
> 	4. $1 \cdot A = A.$

### Součin matic
- Nechť $A = (a_{ij})_{m \times n}, B = (b_{jk})_{n \times p}$ jsou matice nad tělesem $T$. Součinem matic $A$ a $B$ rozumíme matici $A \cdot B = (c_{ik})_{m \times p}$, kde 
  $$
  c_{ik} = \sum_{j=1}^{n} a_{ij} \cdot b_{jk} = a_{i1} \cdot b_{1k} + a_{i2} \cdot b_{2k} + \ ... \ + a_{in} \cdot b_{nk}
  $$
  pro všechny indexy $i, k$.

- Pro libovolné matice $A = (a_{ij})_{m \times n}, B=(b_{jk})_{n \times p}, C=(c_{kl})_{p \times r}, D=(d_{jk})_{n \times p}$ nad tělesem $T$ platí
	1. $A \cdot (B \cdot C) = (A \cdot B) \cdot C,$
	2. $A \cdot (B + D) = A \cdot B + A \cdot D$
	3. $(B+D) \cdot C = B \cdot C + D \cdot C.$

>[!Example] Příklad
>- Součin matic lze provést, neboť první matice v součinu má stejný počet **sloupců**, jako má druhá matice **řádků**.
>$$ 
>\begin{aligned}
>\begin{gather}
>A \cdot B =
>\begin{pmatrix}
>1 & 2 & 3 \\
>-2 & 2 & -1
>\end{pmatrix}
>\cdot
>\begin{pmatrix}
>0 & 1 & 2 \\
>-2 & -1 & -1 \\
>1 & 0 & 0
>\end{pmatrix}
>= \\ \\ =
>\begin{pmatrix}
>0-4+3 & 1-2+0 & 2-2+0 \\
>0-4-1 & -2-2-0 & -4-2-0
>\end{pmatrix}
>= \\ \\ =
>\begin{pmatrix}
>-1 & -1 & 0 \\
>-5 & -4 & -6
>\end{pmatrix}
>\end{gather}
>\end {aligned}
>$$

  
### Maticová transpozice
- Je-li $A = (a_{ij})_{m \times n}$ matice nad tělesem $T$, pak transponovanou maticí k matici $A$ rozumíme matici $A^{T} = (a_{ij})_{n \times m}$. $A^{T}$ tedy vznikne vzájemnou záměnou odpovídajících řádků a sloupců matice $A$, tedy jakýmsi *překlopením matice $A$ přes hlavní diagonálu*.
>[!Example] Příklad
>$$
>A=
>\begin{pmatrix}
>1 & 2 & 1 & -1 \\
>0 & 2 & 0 & 1 \\
>-1 & 0 & 2 & 1
>\end{pmatrix}
>\Rightarrow A^{T} =
>\begin{pmatrix}
>1 & 0 & -1 \\
>2 & 2 & 0 \\
>1 & 0 & 2 \\
>-1 & 1 & 1
>\end{pmatrix}
>$$

- Pro libovolné matice $A = (a_{ij})_{m \times n}, B = (b_{ij})_{m \times n}, C = (c_{jk})_{n \times p}$ nad tělesem $T$ a libovolný skalár $c \in T$ platí:
	1. $(A + B)^{T} = A^{T} + B^{T},$
	2. $(c \cdot A)^{T} = c \cdot A^{T},$
	3. $(A \cdot C)^{T} = C^{T} \cdot A^{T}.$


### Hodnost matice
- **Řádkovým podprostorem** matice $A \in M_{m \times n}(T)$ rozumíme *podprostor v aritmetickém vektorovém prostoru $T^{n}$*, který **je generovaný řádkovými vektory matice $A$.**
>[!Example] Příklad
>  Řádkovým podprostorem matice
>    $$
>  A=
>  \begin{pmatrix}
>  2 & -1 & 3,1 & 5 \\
>  -3 & 1,8 & -2 & 4 \\
>  0 & 0 & 4,5 & 0
>  \end{pmatrix} \in M_{3 \times 4}(R)
>  $$
>  je tedy prostor $[\{(2; -1; 3,1;5), (-3; 1,8; -2; 4), (0; 0; 4,5; 0)\}] \subseteq R^{4}.$
  
- **Hodností matice** $A \in M_{m \times n}(T)$ rozumíme **dimenzi řádkového podprostoru** matice $A$ a značíme ji $h(A)$.
	- **$h(A)$ se musí rovnat počtu lineárně nezávislých řádků** matice $A \in M_{m \times n}(T)$, tedy $h(A) \leq m.$
	- Jestliže $A \sim B$, pak $h(A) = h(B).$
	- **$h(A)$ je rovna počtu nenulových řádků** libovolné matice $B$ v $GT$ takové, že $A \sim B$.

>[!Example] Příklad
>$$
>A_{5 \times 4} = 
>\begin{pmatrix}
>\times & \times & \times & \times \\
>0 & \times & \times & \times \\
>0 & 0 & \times & \times \\
>0 & 0 & 0 & \times \\
>0 & 0 & 0 & 0
>\end{pmatrix}
>\Rightarrow h(A) = 4,
>\ \ \ \ 
>B_{3 \times 3} =
>\begin{pmatrix}
>\times & \times & \times \\
>0 & 0 & \times \\
>0 & 0 & 0
>\end{pmatrix}
>\Rightarrow h(B) = 2.
>$$

> [!Tip] 
> Hodnost Ize určit pomocí Gaussové eliminační metody tzn. upravuji na "trojúhelníkový" (Gaussův) tvar - *upravuji matici pomocí EŘT (Elementárních Řádkových Transformací).*
>
> **Hodnost matice je tedy počet nenulových řádků v Gaussově tvaru**

### Permutace na množině
- Dána konečná množina $A = \{a_{1}, a_{2}, ..., a_{n}\}.$ **Pořadím $\Pi$** množiny $A$ nazveme každou $n$-tici $\Pi = (a_{k1}, a_{k2}, ..., a_{kn}) \in A^{n}$ takovou, že **každý prvek z $A$ je v ní zastoupen přávě jednou.**

- **Permutací $P$** na množině $A = \{a_{1}, a_{2}, ..., a_{n}\}$ rozumíme **každou bijekci $P: A \rightarrow A$.**
- Permutaci $P$ množiny $A$ můžeme zapisovat ve tvaru 
  $$ P = 
  \begin{pmatrix}
  a_{1} & a_{2} & ... & a_{n} \\
  a_{\pi(1)} & a_{\pi(2)} & ... & a_{\pi(n)}
  \end{pmatrix}
  $$
  kde $\pi$ je některé pořadí indexové množiny $\{1,2,...,n\}$

- Pro každou $n$-prvkovou $(n \geq 1)$ množinu $A = \{a_{1}, a_{2}, ..., a_{n}\}$ je počet permutací na ní stejný jako počet pořadí této možiny, a je **roven číslu $n!$**.

- Protože nezáleží na povaze prvků $a_{1}, a_{2}, ..., a_{n}$ množiny $A$, můžeme dále pracovat přímo s množinou prvních $n$ přirozených čísel, tedy $\{1, 2, ..., n\}$.
- Základním pořadím množiny $A$ přitom rozumíme $n$-tici $\Pi_{0} = \{1, 2, ..., n\}$.

### Znaménko pořadí
- Nechť $\Pi = (k_{1}, k_{2}, ..., k_{n})$ je pořadí množiny $A = \{a_{1}, a_{2}, ..., a_{n}\}$. Říkáme, že **prvky $k_{i}$ a $k_{j}$ tvoří inverzi v $\Pi$**, jestliže $i<j$, přestože $k_{i} > k_{j}$.

- **Znaménkem pořadí $\Pi$** nazveme číslo $sgn(\Pi) = (-1)^{[\Pi]}$, přitom $[\Pi]$ značí počet inverzí v pořadí $\Pi$.
- Je-li $sgn(\Pi) = 1$, nazveme pořadí $\Pi$ sudé (nebo naopak **počet inverzí je sudý** => 1)
- Je-li $sgn(\Pi) = -1$, nazveme pořadí $\Pi$ liché. (nebo naopak **počet inverzí je lichý** => -1)
> [!Example] Příklad
> *V pořadí  $\pi = (2, 1, 4, 5, 3)$ množiny $A$ jsou inverze    $2,1$ ;  $4,3$ ; $5,3$* tedy $sgn(\pi) = (-1)^{3} = -1$, tedy $\pi$ je liché.

### Znaménko permutace
- Nechť $P = \begin{pmatrix} \pi_{1} \\ \pi_{2} \end{pmatrix}$ je permuatace množiny $A$.
- **Znaménkem permutace $P$** nazveme číslo $1$, **jestliže $sgn(\Pi_{1}) = sgn(\Pi_{2})$**, číslo $-1$, pokud $sgn(\Pi_{1}) \neq sgn(\Pi_{2})$.
- Je-li $sgn(P) = 1$ nazývá se permutace $P$ sudá.
- Je-li $sgn(P) = -1$, říkáme, že $P$ je lichá.
> [!Example] Příklad
> Je dána permutace:
>   $$
>   P=
>   \begin{pmatrix}
>   2 & 1 & 3 & 5 & 4 \\
>   3 & 1 & 2 & 4 & 5
>   \end{pmatrix}
>   =
>   \begin{pmatrix}
>   \pi_{1} \\ \pi_{2}
>   \end{pmatrix}.
>   $$ 
>   Pak $sgn(\pi_{1}) = (-1)^{2} = 1$ a $sgn(\pi_{2}) = (-1)^{2} = 1$, tedy $P$ je sudá permutace.
### Transpozice na množině
- **Transpozicí na $A = \{1, 2, ..., n\}$** rozumíme permutaci $P$ na $A$ takovou, že existují $i, j \in A$ tak, že $P(i) = j, P(j) = i, P(k) = k$ pro všechny $k \in A \text{\\} \{i,j\}$.
- *Slovy*: zamění 2 prvky a ostatní ponechá stejně
> [!Example] Příklad
>  na $A = \{1,2,3,4,5,6\}$ platí: 
>  $$
>  T(1,4)=
>  \begin{pmatrix}
>  1 & 2 & 3 & 4 & 5 & 6 \\
>  4 & 2 & 3 & 1 & 5 & 6
>  \end{pmatrix}.
>  $$

### Determinant
- Nechť $A = (a_{ij}) \in M_{n}(T)$ je **čtvercová** matice stupně $n$ nad číselným tělesem $T$. **Determinantem matice $A$** rozumíme číslo $\det(A)$ z tělesa $T$ takové, že $\det(A) = \sum_{P} sgn(P) \cdot a_{1k_{1}} \cdot a_{2k_{2}} \cdot ... \cdot a_{nk_{n}}$, kde **sčítáme přes všechny permutace** $P = \begin{pmatrix} 1 & 2 & ... & n \\ k_{1} & k_{2} & ... & k_{n} \end{pmatrix}$ na indexové množině $\{1, 2, ..., n\}$. 
  Každý ze součinů $a_{1k_{1}} \cdot a_{2k_{2}} \cdot ... \cdot a_{nk_{n}}$ přitom nazýváme člen determinantu $\det(A)$.

- Jinými slovy:
	- Determinant čtvercové matice je číslo z $T$, které **se rovná součtu $n!$ součinů prvků** matice $A$, přičemž v každém z těchto součinů $a_{1k_{1}} \cdot a_{2k_{2}} \cdot ... \cdot a_{nk_{n}}$ je každý řádek a sloupec matice zastoupen **právě jedním prvkem**.
	- Tento **součin ale musíme doplnit znaménkem** stejným jako *je znaménko permutace* určené řádkovými a sloupcovými indexy prvků zastoupených v tomto součinu

> [!Example] Příklad
> Určete determinant matice $A=\begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix} \in M_{2}(T)$:
> 
> Členy determinantu budou součiny $a_{11}\ \cdot\ a_{22}$, který odpovídá permutaci $$P_{1}=\begin{vmatrix}1&2\\1&2\end{vmatrix},$$jejíž znaménko je $1$, a také $a_{12}\ \cdot\ a_{21}$, který odpovídá permutaci $$P_{2}=\begin{vmatrix}1&2\\2&1\end{vmatrix},$$ jejíž znaménko je $-1$. Celkem tedy dostáváme $$det(A)=a_{11}\ \cdot\ a_{22}\ -\ a_{12}\ \cdot\ a_{21}.$$

>[!Example]- Isibalo - Definice determinantu
><iframe width="660" height="385" src="https://www.youtube.com/embed/Km0rb7-M8aU?si=MPA0jamRC_BpJraX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

>[!Tip] Sarrusovo pravidlo
>- Vyjádření determinantů matic $2.$ a $3.$ stupně lze znázornit i schematicky:
>- Pokud šipka jde zleva doprava, pak výsledek přičítám, pokud zprava doleva, pak ho odečítám
>- Pro $n=2:$
>![[MacBook-2024-03-10-000819.png| 150]]
>- Pro $n=3:$
>![[MacBook-2024-03-10-000820.png| 150]]

### Determinanty matic ve speciálních tvarech
- Pro každou matici $A \in M_{n}(T)$, kde $T$ je číselné těleso, platí $det(A^{T}) = det(A)$.
- Má-li matice $A \in M_{n}(T)$ v některém řádku (sloupci) samé nuly, platí $det(A) = 0$.
- Má-li matice $A \in M_{n}(T)$ pod (nad) hlavní diagonálou samé nuly, platí $det(A) = \prod_{i=1}^{n} a_{ii} = a_{11} \cdot a_{22} \cdot ... \cdot a_{nn}$
- Vznikne-li matice $B \in M_{n}(T)$ dva stejné řádky (sloupce), pak $det(A) = 0$.

### Submatice, subdeterminant
- Nechť $A = (a_{ij}) \in M_{m \times n}(T)$. Pak každou matici, která vznikne z $A$ **vynecháním** některých jejích řádků a sloupců, nazýváme **submatice** (nebo *dílčí matice*) **matice $A$**
- Je-li submatice čtvercová, pak její determinant nazýváme **subdeterminant matice $A$**
> [!Example] Příklad
> $$
> \begin{pmatrix}
> 2 & -1 & 0 \\
> 1 & 4  & 1 \\
> -2 & 0 & -3
> \end{pmatrix}
> \rightarrow
> \begin{pmatrix}
> 2 & 0 \\
> -2 & -3
> \end{pmatrix}
> $$
### Algebraický doplněk prvku ve čtvercové matici
- Nechť $A = (a_{ij}) \in M_{n}(T)$. Potom **subdeterminant dílčí matice**, která vznikne z $A$ vynecháním $i$-tého řádku a $j$-tého sloupce, budeme **nazývat minor matice $A$ příslušný k prvku $a_{ij}$**. značíme $M_{ij}$.
- **Algebraickým doplňkem prvku $a_{ij}$** matice $A$ rozumíme číslo $$A_{ij} = (-1)^{i+j} \cdot M_{ij}.$$
> [!Example] Příklad
> $$
> A = 
> \begin{pmatrix}
> 2 & -1 & 0 \\
> 1 & 4 & 1 \\
> -2 & 0 & -3
> \end{pmatrix}
> \rightarrow
> A_{32} = (-1)^{3+2} \cdot
> \begin{vmatrix}
> 2 & 0 \\
> 1 & 1 \\
> \end{vmatrix}
> = -2
> $$

#### Adjungovaná matice
- Transponovaná matice algebraických doplňků
- Používá se k sestavení inverzní matice
- Postup
	1. Udělám algebraický doplněk pro všechny prvky
	2. Matici transponuju
### Inverzní matice
- **Pouze ke čtvercovým maticím**
- Pro matici $A$ existuje právě 1 inverzní matice $A^{-1}$
- Platí: $\ A \cdot A^{-1} = A^{-1} \cdot A = E$ ($E$ ... jednotková matice)
- **Postup**
	1. sestavíme $adj(A)$
	2. spočítáme $det(A)$
	3. inverzní matice je $A^{-1} = \frac{1}{det(A)} \cdot adj(A)$

### Laplaceův rozvoj determinantu
- Nechť $A = (a_{ij}) \in M_{n}(T)$. Pak pro každý řádkový index $i = 1, 2, ..., n$ platí
  $$
  det(A)=\sum_{j=1}^{n} a_{ij} \cdot A_{ij} = a_{i1} \cdot A_{i1} + ...+ a_{in} \cdot A_{in},
  $$
  resp. pro každý sloupcový index $j = 1, 2, ..., n$ platí
  $$
  det(A)=\sum_{i=1}^{n} a_{ij} \cdot A_{ij} = a_{1j} \cdot A_{1j} + ...+ a_{nj} \cdot A_{nj},
  $$
> [!Example] Příklad
> $$
> \begin{aligned}
> \begin{gather}
> \begin{vmatrix}
> A
> \end{vmatrix}
> =
> \begin{vmatrix}
> 2 & -1 & 0 \\
> 1 & 4 & 1 \\
> -2 & 0 & -3 \\
> \end{vmatrix}
> =\\\\=
> (-1) \cdot (-1)^{1+2} \cdot 
> \begin{vmatrix}
> 1 & 1 \\
> -2 & -3 \\
> \end{vmatrix}
> + 4 \cdot (-1)^{2+2} \cdot
> \begin{vmatrix}
> 2 & 0 \\
> -2 & -3 \\
> \end{vmatrix}
> + 0 \cdot (-1)^{3+2} \cdot
> \begin{vmatrix}
> 2 & 0 \\
> 1 & 1 \\
> \end{vmatrix}
> =\\\\ = -1 + (-24) + 0 = -25
> \end{gather}
> \end{aligned}
> $$

  ### Řádkové a sloupcové vektory
  - Nechť $A = (a_{ij}) \in M_{m \times n}(T)$.
  - $n$-tici $a_{i}^{\rightarrow} = (a_{i1}, a_{i2}, ..., a_{in})$ budeme nazývat **$i$-tý řádkový vektor matice $A$** pro každý index $i = 1, 2, ..., m$.
  - $m$-tici $a_{j}^{\rightarrow T} = \begin{pmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{mj} \end{pmatrix}$ budeme nazývat $j$-tý sloupcový vektor matice $A$ pro každý index $j = 1, 2, ..., n$.

### Úpravy matice při výpočtu determinantu
- Vznikne-li matice $B \in M_{n}(T)$ z matice $A \in M_{n}(T)$ vynásobením $i$-tého řádku (sloupce) číslem $c \in T$, pak $det(B) = c \cdot det(A)$
- **Přičteme-li** k některému řádku (sloupci) matice $A \in M_{n}(T)$ některou **lineární kombinaci** ostatních řádků, pak získáme matici $B \in M_{n}(T)$, pro kterou platí **$det(B) = det(A)$**
- Jsou-li řádkové (sloupcové) vektory matice $A \in M_{n}(T)$ lineární závislé, pak platí **$det(A) = 0$**.
- Nechť $A, B \in M_{n}(T)$. Pak **$det(A \cdot B) = det(A) \cdot det(B)$**.
> [!Example] Příklad
> $$
> \begin{aligned}
> \begin{gather}
> \begin{vmatrix}
> 2 & 5 & -3 & -1 & 0 & 4 \\
> 3 & -1 & 2 & 2 & -2 & 6 \\
> 1 & -5 & -3 & 4 & 2 & -2 \\
> 0 & 2 & -1 & 2 & 1 & -3 \\
> -1 & 1 & -2 & -3 & 0 & 1 \\
> 1 & 2 & -2 & 2 & 3 & -9 
> \end{vmatrix}
> =
> \begin{vmatrix}
> 2 & 5 & -3 & -1 & 0 & 4 \\
> 3 & 3 & 0 & 6 & 0 & 0 \\
> 1 & -9 & -1 & 0 & 0 & 4 \\
> 0 & 2 & -1 & 2 & 1 & -3 \\
> -1 & 1 & -2 & -3 & 0 & 1 \\
> 1 & -4 & 1 & -4 & 0 & 0 
> \end{vmatrix}
> \\\\=(-1)
> \begin{vmatrix}
> 2 & 5 & -3 & -1 & 4 \\
> 3 & 3 & 0 & 6 & 0 \\
> 1 & -9 & -1 & 0 & 4 \\
> -1 & 1 & -2 & -3 & 1 \\
> 1 & -4 & 1 & -4 & 0
> \end{vmatrix}
> = (-3)
> \begin{vmatrix}
> 2 & 5 & -3 & -1 & 4 \\
> 1 & 1 & 0 & 2 & 0 \\
> 1 & -9 & -1 & 0 & 4 \\
> -1 & 1 & -2 & -3 & 1 \\
> 1 & -4 & 1 & -4 & 0
> \end{vmatrix}
> \\\\=(-3)
> \begin{vmatrix}
> 2 & 3 & -3 & -5 & 4 \\
> 1 & 0 & 0 & 0 & 0 \\
> 1 & -10 & -1 & -2 & 4 \\
> -1 & 2 & -2 & -1 & 1 \\
> 1 & -5 & 1 & -6 & 0
> \end{vmatrix}
> = 3
> \begin{vmatrix}
> 3 & -3 & -5 & 4 \\
> -10 & -1 & -2 & 4 \\
> 2 & -2 & -1 & 1 \\
> -5 & 1 & -6 & 0
> \end{vmatrix}
> \\\\
> = 3
> \begin{vmatrix}
> -5 & 5 & -1 & 0 \\
> -18 & 7 & 2 & 0 \\
> 2 & -2 & -1 & 1 \\
> -5 & 1 & -6 & 0
> \end{vmatrix}
> =(-3)
> \begin{vmatrix}
> -5 & 5 & -1 \\
> -18 & 7 & 2 \\
> -5 & 1 & -6
> \end{vmatrix}
> =(-3)
> \begin{vmatrix}
> 0 & 0 & -1 \\
> -28 & 17 & 2 \\
> 25 & -29 & -6
> \end{vmatrix}
> \\\\
> = 3
> \begin{vmatrix}
> -28 & 17 \\
> 25 & -29
> \end{vmatrix}
> = 3 \cdot 387 = 1161.
> \end{gather}
> \end{aligned}
> $$

##### Navigace
Předchozí:  [[Stromy, kořenové stromy, vztahy mezi výškou, počtem vrcholů, počtem listů]]
Následující: [[Vektorové prostory, podprostory, báze a dimenze, matice přechodu]]
Celý okruh: [[1. Teoretické základy informačních technologií]]