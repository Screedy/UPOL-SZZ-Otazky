
### Skalární součin
##### Definice
Nechť $V=(V ;+, \mathbf{R},\,\cdot\,)$ je VP nad tělesem reálných čísel. Skalárním součinem na $V$ nazveme každé zobrazení $\circ: V \times V \rightarrow \mathbf{R}$, které pro každé $\vec{u}, \vec{v}, \vec{w} \in V$ a pro každé $c \in \mathbf{R}$ splňuje:
1. $\vec{u} \circ \vec{v}=\vec{v} \circ \vec{u}$   =(komutativita)
2. $\vec{u} \circ(\vec{v}+\vec{w})=\vec{u} \circ \vec{v}+\vec{u} \circ \vec{w}$  =(distributivita)
3. $(c \cdot \vec{u}) \circ \vec{v}=c \cdot(\vec{u} \circ \vec{v})$  =(asociativita)
4. $\vec{u} \circ \vec{u} \geq 0$, rovnost nastane právě když $\vec{u}=\vec{o}$.

### EVP - definice
Eukleidovským vektorovým prostorem rozumíme každý vektorový prostor, na kterém je zaveden skalární součin.

### Délka(norma) vektoru
##### Definice
Nechť $V$ je EVP, $\vec{u} \in V$. Číslo $\|\vec{u}\|=\sqrt{\vec{u} \circ \vec{u}}$ nazveme délka vektoru $\vec{u}$.

Pokud $\vec{u}=\left(u_1, u_2, \ldots, u_n\right)$, tak velikost vektoru $\vec{u}$ vypočítáme vztahem:
$$
\|\vec{u}\|=\sqrt{\vec{u} \circ \vec{u}}=\sqrt{u_1^2+u_2^2+\ldots+u_n^2}
$$
Nechť $V$ je EVP, $\vec{u}, \vec{v} \in V, c \in \mathbb{R}$. Platí
1. $\|c \cdot \vec{u}\|=|c| \cdot\|\vec{u}\|$,
2. $\|\vec{o}\|=0$ a pro $\vec{u} \neq \vec{o}$ pak $\|\vec{u}\|>0$.
3. $|\vec{u} \circ \vec{v}| \leq\|\vec{u}\| \cdot\|\vec{v}\|$  =(**Schwarzova nerovnost**).

### Úhel vektorů
Definice $5.14$
Nechť $V$ je EVP, $\vec{u} \vec{v} \in V, \vec{u} \neq \vec{o} \neq \vec{v}$. Úhlem vektorů $\vec{u}$ a $\vec{v}$ rozumíme číslo
$$
\varphi(\vec{u}, \vec{v})=\arccos \frac{\vec{u} \circ \vec{v}}{\|\vec{u}\| \cdot\|\vec{v}\|} .
$$
- Ze Schwarzovy nerovnosti plyne, že úhel $\varphi$ je určen korektně.
- Platí, že $\cos \varphi(\vec{u}, \vec{v})=\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \cdot\|\vec{v}\|}$, kde $0 \leq \varphi \leq \pi$.

### Ortogonální(kolmé) vektory
Vektory u a v jsou navzájem ortogonální, pokud je jejich skalární součin roven nule, tj. pokud $u \cdot v=0$. Píšeme $u \perp v$. To zřejmě nastane pokud je jeden z těchto vektorů nulový vektor $0 \in R^n$ nebo pokud svírají tyto vektory pravý úhel, tj. $\cos \varphi=0$ neboli $\varphi(\vec{u}, \vec{v})=\frac{\pi}{2}$

Nechť $V$ je EVP, $\vec{u}, \overrightarrow{v_1}, \overrightarrow{v_2}, \ldots, \overrightarrow{v_n} \in V$ a nechť platí $\vec{u} \perp \overrightarrow{v_i}$ pro každé $i=$ $1,2, \ldots, n$. Pak $\vec{u} \perp \vec{w}$ pro každý $\vec{w} \in\left[\left\{\overrightarrow{v_1}, \overrightarrow{v_2}, \ldots, \overrightarrow{v_n}\right\}\right]$.

##### Definice
Nechť $V$ je EVP. Vektory $\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n} \in V$ nazveme **vzájemně ortogonální**, platí-li $\overrightarrow{u_i} \perp \overrightarrow{u_j}$ pro každé $i \neq j$, kde $i, j=1,2, \ldots, n$.

Nenulové vzájemně ortogonální vektory $\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n}$ z EVP $V$ jsou **lineárně nezávislé**.

Jsou-li vektory $\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n}$ vzájemně ortogonální v EVP $V$ a platí-li $V=$ $\left[\left\{\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n}\right\}\right]$, pak množina $\left\{\overrightarrow{u_1}, \overrightarrow{u_2}, \ldots, \overrightarrow{u_n}\right\}$ je báze VP $V$, tzv. **ortogonální báze**.

### Gram - Schmidtova ortogonalizační metoda

Metoda, která z **báze** vektorového prostoru vytvoří **ortogonální bázi**.

*Mám 3 (bázové) vektory, které neleží v jedné rovině. Chci z nich udělat navzájem kolmé vektory. A pak je chci ortonormalizovat - aby byly všechny stejně dlouhé.*

Vektorový prostor, který je generovaný bází $V=\left[\left\{\vec{u}_1, \vec{u}_2, \vec{u}_3\right\}\right]$ budeme chtít převést na $V=\left[\left\{\vec{w}_1, \vec{w}_2, \vec{w}_3\right\}\right]$ tak abychom věděli, že $v_i \perp v_j$ pro $\forall i, j \in\{1,2,3\}$ kde $i \neq j$ 

**Kroky:**
1. Zvolíme si výchozí vektor $\vec{w}_1$ : je jedno který si vezmu, klidně $u_1$ tzn. $\vec{w}_1=\vec{u}_1$
2. Najdu $\vec{w}_2=\vec{u}_2+k \cdot \vec{w}_1$ (Najdu $w_2$ jako lineární kombinaci vektoru $u_2$ a k násobku $\left.w_1\right): \vec{w}_2=\vec{u}_2-\frac{\vec{u}_2 \circ \vec{w}_1}{\vec{w}_1 \circ \vec{w}_1} \cdot \vec{w}_1$
3. Najdu $\vec{w}_3$ jako lineární kombinaci předchozích vektorů - ty co už mám $\left(\vec{w}_1\right.$ a $\left.\vec{w}_2\right)$ - tzn. $\vec{w}_1=\vec{u}_3+r \cdot \vec{w}_1+s \cdot \vec{w}_2$ kde r a s jsou nějaké násobky. Po úpravě dostaneme: $\vec{w}_3=\vec{u}_3-\frac{\vec{u}_3 \circ \vec{w}_1}{\vec{w}_1 \circ \vec{w}_1} \cdot \vec{w}_1-\frac{\vec{u}_3 \circ \vec{w}_2}{\vec{w}_2 \circ \vec{w}_2} \cdot \vec{w}_2$

Když získám všechny vektory ortogonální báze tak je pak zapíšu jako množinu $B_{\perp(V)}=\left\{\vec{w}_1, \vec{w}_2, \vec{w}_3\right\}$

*Tohle je ortogonalizační metoda "jen" pro tři vektory. Pokud bych jich bylo více, pokračovali bychom ve stejném duchu dále.*

### Ortonormalizace ortogonální báze
Musíme zajistit aby měli všechny vektory délku jedna (jednotkové prvky).
Ortonormalizace vektoru:
1. Spočítáme délku vektoru - pomoci skalárního součinu: $\|\vec{w}\|=\sqrt{\vec{w} \circ \vec{w}}$
2. Vydělíme původní vektor délkou vektoru: $\vec{n}=\frac{\vec{w}}{\|\vec{w}\|}$
3. Dostaneme vektor, který má délku jedna

Tohle udělámé pro všechny ortogonální vektory a pak dostaneme ortonormální bázi 

###### Příklad ortonormalizace jednoho vektoru.
$\vec{w}_1=(1,-2,2,0)$
1. $\left\|\vec{w}_1\right\|=\sqrt{\vec{w}_1 \circ \vec{w}_1}=\sqrt{9}=3$
2. Vydělíme každou složku vektoru délkou vektoru
3. Dostaneme: $\vec{n}_1=\left(\frac{1}{3},-\frac{2}{3}, \frac{2}{3}, 0\right)$

##### Navigace
Předchozí:  [[Vektorové prostory, podprostory, báze a dimenze, matice přechodu]]
Následující: [[Soustavy lineárních rovnic, Frobeniova věta, Gaussova eliminační metoda, Cramerovo pravidlo]]
Celý okruh: [[1. Teoretické základy informačních technologií]]