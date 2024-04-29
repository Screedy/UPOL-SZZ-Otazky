### Kartézský součin
- Kartézský součin n množin je **množina všech uspořádaných n-tic prvků z těchto množin $X_{1} \times ... \times X_{n} = \{ <x_{1}, ..., x_{n}> \mid x_{1} \in X_{1}, ..., x_{n} \in X_{n} \}$**
- Je-li $X_{1} = ... = X_{n} = X$, pak píšeme $X^{n}$ a říkáme **n-tá kartézská mocnina množiny X**
- Velikost $\mid A \times B \mid$ je $\mid A \mid \times \mid B \mid$
- **Relace mezi $X_{1}, ..., X_{n}$** je **libovolná podmnožina kartézského součinu $X_{1} \times ... \times X_{n}$**

### Pojem relace
- **Relace je množina uspořádaných n-tic prvků**
- Relace je určena:
	- **Aritou vztahu** = **číslo udávající počet objektů**, které do relace vstupují
	- **Množiny**, jejichž **prvky** do relace vstupují
- Relace je matematickým protějškem pojmu **vztah**

- Označuje se **$R = \{<x_{1}, ..., x_{n}>\}$**
- Číslu n říkáme **arita** relace R, R se nazývá **n-ární** (unární, binární, ternární, ...)
- **$<x_{1}, ..., x_{n}> = <y_{1}, ..., y_{m}>$**, právě když **$n = m$** a $x_{1} = y_{1}, ..., x_{n} = y_{m}$

### Vztah a operace s relacemi
- Relace jsou speciální množiny (relace podmožina kartézskáho součinu) $\rightarrow$ lze s nimi provádět **množinové operace a vztahy**

- **Rovnost** (vztah)
	- Označujeme symbolem "$=$"
	- **Pro každé $x$ platí: $x \in A$, právě když $x \in B$**
	- Dvě množiny obsahují stejné prvky
	- Když $A=B$ říkáme, že množina A se rovná množině B
	- $A=B$ platí, právě když platí zároveň $A \subseteq B$ a $B \subseteq A$
- **Inkluze** (vztah)
	- Označujeme symbolem "$\subseteq$"
	- **Pro každé $x$ platí: jestliže $x \in A$, pak $x \in B$**
	- Všechny prvky množiny $A$ jsou také prvky množiny $B$
	- Když $A \subseteq B$ říkáme, že množna $A$ je podmnožinou množiny $B$

- **Průnik** (operace)
	- Označujeme symbolem "$\cap$"
	- **$A \cap B = \{ x \mid x \in A$ a $x \in B\}$**
	- Prvek $x$ patří do $A \cap B$, **právě když patří do A a zároveň do B**
	- Společné prvky
	- Množiny $A$ a $B$ se nazývají **navzájem disjunktní**, právě když **$A \cap B = \varnothing$**
- **Sjednocení** (operace)
	- Označujeme symbolem "$\cup$"
	- **$A \cup B = \{ x \mid x \in A$ nebo $x \in B \}$**
	- Prvek $x$ patří do $A \cup B$, právě když patří do **A nebo do B**
	- Spojení všech prvků v množinách
- **Rozdíl** (operace)
	- Označujeme symbolem "$-$"
		- **$A - B = \{ x \mid x \in A$ a $x \notin B\}$**
		- Prvek $x$ patří do $A-B$, právě když patří do $A$, ale nepatří do $B$
- **Inverze** (operace)
	- Inverzní relací k relaci **$R \subseteq X \times Y$** je relace $R^{-1} \subseteq Y \times X$
		- **$R^{-1} = \{<y, x> | <x, y> \in R\}$**
	- "Pořadí v relaci se převrátí"
- **Skládání** (operace)
	- Je-li $R \subseteq X \times Y$ a $S \subseteq Y \times Z$, pak **složením relací** je relace **$R \circ S \subseteq X \times Z$**
		- $R \circ S = \{<x, z> \mid$ existuje $y \in Y: <x,y> \in R$ a $<y,z> \in S$
	- "Přes společný prvek (tzv. prostředníka) spojím relace do jedné"

### Binární relace a jejich reprezentace
- Základní způsoby reprezentace binárních relací je:
	- **Maticí, Grafem, Seznamem seznamů**

- **Reprezentace maticí (tabulkou)**
	- Tabulky a matice představují **základní způsob reprezentace binárních relací**
	- Máme relaci **$R \subseteq X \times Y$**, kde **$X = \{x_{1}, ..., x_{m}\}$** a **$Y = \{y_{1}, ..., y_{n}\}$**. Relaci R repzentujeme maticí/tabulkou, ve které se na místě odpovídající řádku $i$ a sloupci $j$ nachází hodnota, která určuje, **zda dvojici $<x_{i},y_{j}> \in R$**, nebo $<x_{i},y_{j}> \notin R$
	- $M_{R}$ se nazývá matice relace $R$
	- **Výhodou je přehlednost, nevýhodou je paměťová náročnost**
	- Pro relaci $R = \{<a,1>,<a,2>,<a,4>,<b,2>,<b,4>,<c,1>\}$
	  ![[MacBook-2024-02-29-000762@2x.png | 400]]

- **Reprezentace orientovaným grafem**
	- Graf binární relace $R \subseteq X \times X$ dostaneme tak
		- Každý prvek $x \in X$ znázorníme v rovině jako **kroužek** s označením daného prvku
		- Pokud $<x,y> \in R$, nakreslíme z **kroužku odpovídajícího $x$ do kroužku odpovídajícího $y$ orientovanou čáru s šipkou**.
	- Pro relaci $R=\{<a,b>,<a,d>,<b,d>,<c,a>\}$
	  ![[MacBook-2024-02-29-000763@2x.png | 150]]

- **Reprezentace seznamem seznamů**
	- **Je vhodný pro uložení** binární relace $R$ na množině $X$
	- Reprezentaci tvoří **hlavní (spojový) seznam**, ve kterém jsou uloženy **všechny prvky množiny X.**
	- Z každého prvku $x \in X$ hlavního seznamu vede seznam obsahující právě **ty $y \in X$, pro každé $<x,y> \in R$**
	- Reprezentace seznamem seznamů je **paměťové úsporná** a je vhodná pro počítačové zpracování
	-  Pro relaci $R=\{<a,b>,<a,d>,<b,d>,<c,a>\}$
	  ![[MacBook-2024-02-29-000764@2x.png | 400]]

### Mocnina relace
- N-tou mocninu relace zavádíme pomocí *skládání relací*
	- $R^{1} = R$
	- $R^{n} = R \circ R^{n-1}$
		- $R^{2} = R \circ R$
		- $R^{3} = R \circ R^{2} = R \circ R \circ R$
	- Obecně **neplatí** $R^{n} \subseteq R^{n+1}$

- Nechť $R, S, T$ jsou binární relace na $X$, kde $S \subseteq T$
	- $S^{-1} \subseteq T^{-1}$
	- $R \circ S \subseteq R \circ T$ a $S \circ R \subseteq T \circ R$
	- Pokud $R$ je **tranzitivní, pak $R^{n} \subseteq R$** pro každé $n \in N$
	- $R^{m} \circ R^{n} = R^{m+n} = R^{n} \circ R^{m}$ pro každé $n \in N$
	- Pokud je $X$ konečná a $<x,y> \in R^{i}$ pro každé $i > \mid X \mid$, pak $<x,y> \in R^{m}$ pro nějaké $m \leq \mid X \mid$

### Uzávěry relací
- Pro binární relaci $R$ na $X$ definujeme binární relace:
	- $Ref(R)$ = reflexivní uzávěr relace $R$
		- $Ref(R) = R \cup id_{x}$
		- K relaci přidám relaci identity
	- $Sym(R)$ = symetrický uzávěr relace $R$
		- $Sym(R) = R \cap R^{-1}$
		- K relaci přidám inverzní relaci
	- $Tra(R)$ = tranzitivní uzávěr relace R
		- $Tra(R)$ = $\cup^{\infty}_{n=1} R^{n}$
		- Sjednocení nekonečně mnoho relací $R^{1} \cup ,... , \cup R^{n}$, pokud ale je R definována na konečné množině $X$, kde $\mid X \mid = n$, pak $Tra(R) = \cup^{n}_{i=1} R^{i}$
- ![[MacBook-2024-02-29-000765@2x.png | 500]]

##### Navigace
Předchozí:  [[Množiny, množinové operace, potenční množina, kartézský součin, číselné množiny, spočetné a nespočetné množiny]]
Následující: [[Funkce (zobrazení) a jejich vlastnosti]]
Celý okruh: [[1. Teoretické základy informačních technologií]]