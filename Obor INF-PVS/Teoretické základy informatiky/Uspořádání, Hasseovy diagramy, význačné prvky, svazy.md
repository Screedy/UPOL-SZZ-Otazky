#disk1 #svazy #hasseovy-diagramy #uspořádání
## Uspořádání
- *Uspořádání* je matematický protějšek pojmu **hierarchie**
- Binární relace $U$ na množině $A \neq \varnothing$ se nazývá **uspořádání**, je-li **reflexivní, antisymetrická a tranzitivní.**
>[!tip]
>- **Reflexivní** - Každé $x$ z $X$ je totožné s $x$, tedy $x = x$
> - **Tranzitivní** - Pokud $x \leq y$ a $y \leq z$, pak i $x \leq z$
> - **Antisymetrická** - Pokud $x \leq y$, pak neplatí $y \leq x$, kromě pokud $x = y$
- **kvaziuspořádání** ... reflexivní a tranzitivní binární relace $R$ na $X$
- **uspořádání** ... antisymetrické  kvaziuspořádání
- **ekvivalence** ... symetrické kvaziuspořádání
- **Úplné uspořádání** se nazývá **lineární uspořádání** neboli **řetězec**
- Pokud je relace $R$ uspořádání na množině $X$, pak se $<X,R>$ nazývá se **uspořádaná množina**
- Relaci uspořádání na $X$ obvykle značíme $\leq$ 
	- Místo $<x,y> \in \leq$ píšeme $x \leq y$
- Uspořádání pořád ještě není formálním protějškem "uspořádání" na které jsme zvyklí při porovnání čísel, protože v uspořádané množině **mohou stále existovat prvky**, které jsou nesrovnatelné (značíme **$x \mid \mid y$**)
- V lineárním uspořádání (řetězci) jsou každé dva prvky srovnatelné
	- Můžeme lineární uspořádání chápat jako matematický protějšek pojmu "tradiční srovnání čísel"
- Každá relace identity $id_{x}$ **je uspořádání**, které nazýváme **antiřetězec** (každé dva různé prvky z $X$ jsou nesrovnatelné ($x \mid \mid y$))
	- Antiřetězce jsou nejmenší uspořádání, protože každé uspořádání na $X$ obsahuje $id_{x}$

- Relaci uspořádání "menší rovno" na číselných množinách $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, ...$ nazýváme **přirozené uspořádání čísel** (je reflexivní, antisymetrické, tranzitivní a úplné), (nejedná se o jediné přirozené uspořádání čísel na číselných množinách)
- Když $\leq$ je uspořádání na $X$, pak $\leq^{-1}$ (inverzní) je uspořádání na $X$, které označujeme $\geq$
>[!info] Princip duality
> V praxi to znamená, že pokud řeknu tvrzení pro nejmenší prvek v uspořádané množině $<X,R>$, tak PLATÍ i pro největší prvek v uspořádaní množině $<X,R^{-1}>$
### Znázornění uspořádání a pokrytí
- Konečnou relaci uspořádání můžeme znázornit maticí, nebo orientovaným grafem, ale díky speciálním vlastnostem je můžeme znázorňovat mnohem přehledněji pomocí speciálních diagramů

- Ke každému uspořádání $\leq$ na $X$ lze uvažovat odvozenou **relaci** $\prec$ definovanou předpisem
	- **$x \prec y$, právě když $x < y$ a pro každé $z \in X$ platí: $x \leq z \leq y$ pak $z \in \{x,y\}$**
	- Znamená že $x < y$ a zároveň neexistuje žádný prvek $z \in X$, který by se nacházel "mezi $x$ a $y$." (bezprostřední pokrytí prvků)
>[!info]
>Relaci $\prec$ nazýváme **pokrytí příslušné $\leq$**
- $x \prec y$ čteme "x je pokryt y" nebo "y pokrývá x"
- $\prec \subseteq \leq$, tedy relace $\prec$ je obsažena v uspořádání $\leq$
- Relace pokrytí je: ireflexivní, asymetrická a NENÍ tranzitivní
## Hasseův diagram
- Znázorňují konečné uspořádané množiny
- Složen z uzlů (prvky množiny $X$) a hran (vyznačující relaci pokrytí $\prec$)
- Pravidla:
	- Je-li $x \leq y$, nakreslíme uzel $x$ níže než uzel $y$
	- Je-li $x \prec y$, propojíme uzel $x$ a $y$ úsečkou
- Je vhodné, aby se hrany nekřížili

>[!Example] Příklad hasseova diagramu
>![[MacBook-2024-03-05-000783.png| 700]]
## Význačné prvky v uspořádaných množinách a jejich vztahy
- Nechť $<X, \leq >$ je uspořádaná množina. Prvek $x \in X$ se nazývá:
	- **minimální**, jestliže pro každý $y \in X$ platí: pokud $y \leq x$, pak $x = y$
	- **nejmenší**, jestliže $x \leq y$ pro každý $y \in X$ (je pouze jeden)
	- **maximální**, jestliže pro každý $y \in X$ platí: pokud $x \leq y$, pak $x = y$
	- **největší**, jestliže $y \leq x$ pro každý $y \in X$ (je pouze jeden)
- Pokud je $x$ nejmenší, pak bude i minimální (obráceně neplatí)
- Pokud je $x$ největší, pak bude i maximální (obráceně neplatí)

- Nechť $<X, \leq>$ je uspořádaná množina. Pak platí:
	- V $<X, \leq >$ existuje nejvýše **jeden největší** a **jeden nejmenší** prvek
	- Je-li $x \in X$ **největší (nejmenší)** prvek, pak je také **maximální (minimální)** a žádné další maximální (minimální) prvky se v $X$ nevyskytují
	- Pokud je $\leq$ **lineární uspořádání**, pak je $x \in X$ **největší (nejmenší)** prvek, **právě když** je **maximální (minimální)**
#### Horní a dolní mez
- Nechť $<X, \leq >$ je uspořádaná množina a $Y \subseteq X$. Definujeme množiny
	- **$L(Y) = \{ x \in X \mid x \leq y$ platí pro každé $y \in Y \}$**
		- Nazývá se **dolní kužel** množiny $Y$ v $<X, \leq >$
		- Vznikne uspořádaná množina $<L(Y), \leq_{L(Y)}>$
	- **$U(Y) = \{x \in X \mid x \geq y$ platí pro každé $y \in Y\}$**
		- Nazývá se **horní kužel** množiny $Y$ v $<X, \leq>$
		- Vznikne uspořádaná množina $<U(Y), \leq_{U(Y)}>$

- V horním/dolním kuželu můžeme najít, pokud existuje, nejmenší (největší) prvek.
- Nechť $<X, \leq>$ je uspořádaná množina a $Y \subseteq X$
	- Pokud má $L(Y)$ největší prvek, pak se nazývá **infimum $Y$** a označuje se $inf(Y)$
	- Pokud má $U(Y)$ nejmenší prvek, pak se nazývá **supremum $Y$** a označuje se $sup(Y)$
## Svazy
- Na základě existence *infima* či *suprema* ke každým dvěma prvkům definujeme speciální uspořádané množiny zvané *polosvazy* a *svazy*
- Nechť $<X, \leq>$ je uspořádaná množina.
	- Pokud pro každé $x, y \in X$ existuje $inf(x,y)$, pak $<X \leq>$ nazveme **průsekový polosvaz**
	- Pokud pro každé $x,y \in X$ existuje $sup(x,y)$, pak $<X, \leq>$ nazveme **spojový polosvaz**
	- Je-li $<X, \leq>$ průsekový i spojový polosvaz, pak $<X, \leq>$ nazveme **svaz**
- **Svaz** ... pro každé dva prvky existuje *supremum* i *infimum*
- Každý konečný svaz má největší a nejmenší prvek