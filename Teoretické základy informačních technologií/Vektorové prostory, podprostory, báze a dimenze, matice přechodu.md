### Vektorový prostor

- Čtveřici $(V ;+, T, \cdot)$ nazýváme vektorový prostor, jestliže
	1. $(V ;+)$ je abelovská grupa $s$ jednotkou $\vec{o}$ (nulový vektor);
	2. $T$ je číselné těleso;
	3. $\cdot : T \times V \rightarrow V$ je levá vnější operace nad $T$ a $V$;
	4. Pro všechny $\vec{u}, \vec{v} \in V$ a všechny $c, d \in T$ platí
		- $c \cdot(\vec{u}+\vec{v})=c \cdot \vec{u}+c \cdot \vec{v}$,
		- $(c+d) \cdot \vec{u}=c \cdot \vec{u}+d \cdot \vec{u}$,
		- $(c \cdot d) \cdot \vec{u}=c \cdot(d \cdot \vec{u})$,
		- $1 \cdot \vec{u}=\vec{u}$.
- Pole *vektorového prostoru* ... množina $V$
- *Vektory* ... prvky pole $V$
- *Skaláry* ... prvky tělesa $T$
---
- vektorový prostor $V$ (prvky jsou vektory) nad tělesem $T$ (prvky jsou skaláry). Platí, že " + ": $V \times V \rightarrow V$ a " $\cdot$ ": $T \times V \rightarrow V$ (tzn. když **násobím vektor jiným vektorem** tak výsledek bude zase **v tom samém vektorovém prostoru** a když **násobím vektor skalárem** tak výsledek bude **taktéž v tom samém vektorovém prostoru**)
- operace musí být **uzavřené** (např. po násobení **nesmím** dostat něco co **není** ve vektorovém prostoru $V$)

>[!Tip] Levá vnější operace
>- Nechť' $A \neq \emptyset \neq B$. 
>- **Levou vnější operaci** nad $A$ a $B$ nazýváme každé zobrazení " . " $: A \times B \rightarrow B$.

### Lineární kombinace vektorů
- Nechť $V$ je vektorový prostor nad tělesem $T$, nechť $\vec{v}, \overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n} \in V$. Říkáme, že vektor $\vec{v}$ je lineární kombinací vektoru $\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n}$, jestliže existují skaláry $c_1, c_2, \ldots, c_n \in T$ tak, že
$$
\vec{v}=\sum_{i=1}^n c_i \overrightarrow{u_i}=c_1 \overrightarrow{u_1}+c_2 \overrightarrow{u_2}+\cdots+c_n \overrightarrow{u_n} .
$$
>[!Example] Příklad $5.3$
>- Nulový vektor $\vec{o} \in V$ je lineární kombinací libovolných vektorů z $V$


### Lineární závislost a nezávislost vektorů - definice
- Nechť $V$ je vektorový prostor nad tělesem $T$. Vektory $\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n} \in V$ nazýváme **lineárně závislé**, jestliže existují skaláry $c_1, c_2, \ldots, c_n \in T$ tak, že
$$
\vec{o}=\sum_{i=1}^n c_i \overrightarrow{u_i}=c_1 \overrightarrow{u_1}+c_2 \overrightarrow{u_2}+\cdots+c_n \overrightarrow{u_n},
$$
a přitom **alespoň jedno z čísel** mezi $c_1, c_2, \ldots, c_n$ je nenulové.
V opačném případě, tedy pokud
$$
\vec{o}=\sum_{i=1}^n c_i \overrightarrow{u_i}=c_1 \overrightarrow{u_1}+c_2 \overrightarrow{u_2}+\cdots+c_n \overrightarrow{u_n},
$$
pouze v případě, že $c_1=c_2=\ldots=c_n=0$, se vektory $\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n} \in V$ nazývají **lineárně nezávislé**.

### Báze vektorového prostoru $V$
- je to **množina lineárně nezávislých vektorů**, které **"generují" prostor** $V$
- generují znamená, že pomocí této množiny jsme schopni vyjádřit libovolný vektor prostoru $V$
- (kdybychom nějaký vektor z této množiny odebrali, už bychom nedokázali vyjádřit celý prostor $V$)

### Dimenze
 - **Dimenze** vektorového prostoru $V$ je rovna **počtu prvků báze** tohoto vektorového prostoru. 
 - Pokud je báze nekonečná, je i dimenze nekonečná.

### Podprostor
- Nechť $(V ;+, T, \cdot)$ je vektorový prostor nad tělesem $T$ a nechť $\emptyset \neq W \subseteq V$. Pak $(W ;+, T, \cdot)$ nazveme **podprostor vektorového prostoru** $V$, jestliže
	1. $\forall \vec{u}, \vec{v} \in W: \quad \vec{u}+\vec{v} \in W$,
	2. $\forall \vec{u} \in W, \forall c \in T: \quad c \cdot \vec{u} \in W$.

>[!Tip]
>Musí být tedy uzavřené na sčítání vektorů a na násobení skalárem.
### Transformace souřadnic vektoru vzhledem k bázi
- Nechť $V$ je vektorový prostor nad $T$ takový, že $\operatorname{dim} V=n$ (má $n$ bázových vektorů). Jeli $B=\left\{\vec{u}_1, \ldots, \vec{u}_n\right\}$ báze prostoru $V$ a $\vec{u}=\sum_{i=1}^n c_i \vec{u}_i$ vektor z $V$, potom koeficienty $c_1, \ldots, c_n$ (skaláry z $T$) nazýváme souřadnice vektoru $\vec{u}$ vzhledem k bázi $B$ a píšeme $\{\vec{u}\}_B=\left(c_1, \ldots, c_n\right)$
>[!Tip]
>- Transformace souřadnic využívá **matice přechodu** od **jedné báze k druhé bázi**. 
>- Pokud budeme znát souřadnice vektoru v jedné bázi tak **pomocí jeho násobení maticí** **přechodu dostaneme souřadnice vektoru v nové bázi**.

### Matice přechodu

- Nechť $B=\left\{\vec{u}_1, \vec{u}_2, \ldots, \vec{u}_n\right\}$ a $B^{\prime}=\left\{\vec{u}_1^{\prime}, \vec{u}_2^{\prime}, \ldots, \vec{u}_n^{\prime}\right\}$ jsou báze VP $V$ a nechť $\left\{\vec{u}_i^{\prime}\right\}_B=\left(a_{i 1}, a_{i 2}, \ldots, a_{i n}\right), i \in\{1,2, \ldots, n\}$. Potom matici $A= ||a_{i j}||$ nazýváme maticí přechodů od báze $B$ k bázi $B^{\prime}$.

>[!Tip]
>- Matice přechodu bude vypadat tak, že v řádcích bude mít zapsané vektory nové báze popsané pomocí staré báze.
>- První řádek:
>	- Vezmeme si první vektor nové báze a zapíšeme jej jako lineární kombinaci vektorů staré báze (zapisuji zde jen koeficienty). 
>	- Takhle uděláme všechny řádky a dostaneme matici přechodu.

Věta:
Nechť $B=\left\{\vec{u}_1, \vec{u}_2, \ldots, \vec{u}_n\right\}$ a $B^{\prime}=\left\{\vec{u}_1^{\prime}, \vec{u}_2^{\prime}, \ldots, \vec{u}_n^{\prime}\right\}$ jsou báze VP $V$ a nechť $A$ je matice přechodu od báze $B$ k bázi $B^{\prime}$. Potom každý vektor $\vec{u} \in V$ můžeme vyjádřit:
$$
\{\vec{u}\}_B=\{\vec{u}\}_B^{\prime} \cdot A
$$
**Do řádku zapsané koeficienty lineárních kombinací kdy vyjadřujeme bázové vektory nové báze pomocí bázových vektorů staré báze.**


## Něco navíc - Podprostory:
--- 
### Vlastnosti
Věta 5.5
Neprázdná podmnožina $W$ pole vektorového prostoru $(V ;+, T$, * ) je polem podprostoru ve $V$ právĕ když s každými prvky $\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n}$ obsahuje také každou jejich lineární kombinaci.

### Průnik
Průnik $W_1 \cap W_2$ dvou podprostorů $W_1$ a $W_2$ ve $V P(V ;+, T, \cdot)$ je obecně opět podprostor ve $V$. Je to "největší" (vzhledem k $\subseteq$ ) podprostor ve $V$, který je obsažen současně ve $W_1$ a $W_2$.

Příklad
Uvažujme množiny
$$
M^{+}=\left\{\left(\begin{array}{ll}
a & 0 \\
0 & b
\end{array}\right): a, b \in \mathbf{R}\right\}, M^{-}=\left\{\left(\begin{array}{ll}
0 & c \\
d & 0
\end{array}\right): c, d \in \mathbf{R}\right\}
$$
Pak $\left(M^{+} ;+, \mathbf{R}, \cdot\right)$ a $\left(M^{-} ;+, \mathbf{R}, \cdot\right)$ jsou podprostory ve $\operatorname{VP}\left(\mathcal{M}_2(\mathbf{R}) ;+, \mathbf{R}, \cdot\right)$ a platí
$$
M^{+} \cap M^{-}=\left\{\left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right)\right\}=\{\vec{o}\} .
$$

### Sjednocení
Přitom $M^{+} \cup M^{-}$ není polem podprostoru $\operatorname{VP}\left(\mathcal{M}_2(\mathbf{R}) ;+, \mathbf{R}, \cdot\right)$, protože např.
$$
(-1) \cdot \underbrace{\left(\begin{array}{rr}
-2 & 0 \\
0 & 1
\end{array}\right)}_{\in M^{+}}+3 \cdot \underbrace{\left(\begin{array}{rr}
0 & 1,5 \\
-1 & 0
\end{array}\right)}_{\in M^{-}}=\left(\begin{array}{rr}
2 & 4,5 \\
-3 & -1
\end{array}\right),
$$
což není prvek ani z $M^{+}$, ani z $M^{-}$, tedy ani z $M^{+} \cup M^{-}$.
Obecně, jsou-li $W_1$ a $W_2$ dva podprostory VP $V$, pak nejmenší podprostor ve $V$ obsahující současnẽ jak $W_1$, tak i $W_2$ je podprostor $\left[W_1 \cup W_2\right]$.
### Součet
Vĕta $5.7$
Jsou-li $W_1$ a $W_2$ podprostory $\mathrm{VP}(V ;+, T, \cdot)$, pak polem nejmenšího podprostoru obsahujícího současně $W_1$ a $W_2$ je množina
$$
W_1+W_2=\left\{\vec{w} \in V: \vec{w}=\overrightarrow{w_1}+\vec{w}_2, \overrightarrow{w_1} \in W_1, \overrightarrow{w_2} \in W_2\right\} .
$$
Definice $5.7$
Necht $(V ;+, T, \cdot)$ je VP a $W_1$ a $W_2$ jeho podprostory. Podprostor $W_1+W_2$ nazveme součet podprostorů $W_1, W_2$.
Věta $5.14$
Necht $W_1$ a $W_2$ jsou podprostory VP $V$ konečné dimenze. Pak $\operatorname{dim}\left(W_1+W_2\right)=$ $\operatorname{dim}\left(W_1\right)+\operatorname{dim}\left(W_2\right)-\operatorname{dim}\left(W_1 \cap W_2\right)$

### Přímý součet
Definice $5.8$
Necht $(V ;+, T, \cdot)$ je VP a $W_1$ a $W_2$ jeho podprostory. Je-li $W_1 \cap W_2=\{\vec{o}\}$, pak platí $V=W_1+W_2$, říkáme, že $V$ je přimý součet podprostorů $W_1, W_2$ a píseme $V=W_1 \oplus W_2$.

Je-li VP $(V ;+, T, \cdot)$ prrímým součtem podprostorů $W_1$ a $W_2$, pak každý vektor $\vec{v} \in V$ lze psát právě jedním způsobem ve tvaru $\vec{v}=\vec{w}_1+\overrightarrow{w_2}$, kde $\overrightarrow{w_1} \in W_1$, $\vec{w}_2 \in W_2$.

---

##### Navigace
Předchozí:  [[Matice, operace s maticemi, hodnost, determinant]]
Následující: [[Eukleidovské vektorové prostory, ortogonální a ortonormální báze, Schwarzova nerovnost, Schmidtova ortogonalizační metoda]]
Celý okruh: [[1. Teoretické základy informačních technologií]]