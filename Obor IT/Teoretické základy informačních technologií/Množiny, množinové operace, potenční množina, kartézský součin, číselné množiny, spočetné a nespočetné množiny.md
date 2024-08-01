### Pojem množina
- Množina je objekt, který se <u>skládá</u> z **jiných objektů**, tzv. **prvků množiny**
- **Množina je jednoznačně daná prvky, které obsahuje** - <u>nemá tedy smysl hovořit o pořadí</u> prvků v množině, nebo <u>kolikrát</u> je daný prvek v množině
- Množina je matematickým protějškem k pojmům **soubor, seskupení, ...**

- **Množiny** označujeme **velkými písmeny** a jejich **prvky malými**
	- $x\in A$ znamená, že $x$ je prvkem množiny $A$

- Zápis množin lze těmito základními způsoby:
	- **Výčtem prvků** $A=\{a_{1},\ ...\ a_{n}\}$, množina $A$ obsahuje právě prvky $a_{1},\ ...\ ,a_{n}$
	- **Charakteristická vlastnost** $A=\{x\mid\psi(x)\}$, množina obsahuje prvky $x$ splňující vlastnost $\psi(x)$
- **Systém množin** = množina, jejíž prvky jsou znovu množiny

### Vztahy mezi množinami
1. **Rovnost**
	- Označujeme symbolem "$=$"
	- **Pro každé $x$ platí: $x\in A$, právě když $x \in B$**
	- Dvě množiny obsahují stejné prvky
	- Když $A=B$ říkáme, že množina $A$ se rovná množině $B$
	- **$A=B$** platí, právě když platí zároveň $A \subseteq B$ a $B \subseteq A$  
2. **Inkluze**
	- Označujeme symbolem "$\subseteq$"
	- **Pro káždé $x$ platí: jestliže $x \in A$, pak $x \in B$**
	- Všechny prvky množiny $A$ jsou také prvky množiny $B$
	- Když $A \subseteq B$ říkáme, že množina $A$ je podmnožinou množiny $B$
	- Někdy je výhodné psát $A \subset B$, abychom označili, že $A \subseteq B$ a $A \neq B$

### Operace s množinami
- Mezi základní operace s množinami patří **průnik, stejnocení a rozdíl**

1. **Průnik**
	- Označujeme symbolem "$\cap$"
	- **$A \cap B = \{x \mid x \in A$ a $x \in B\}$**
	- Prvek $x$ patří do $A \cap B$, **právě když patří do $A$ a zároveň do $B$**
	- Společné prvky
	- Množiny A a B se nazývají **navzájem disjunktní** právě když $A \cap B = \varnothing$ 
2. **Sjednocení**
	- Označujeme symbolem "$\cup$"
	- **$A \cup B = \{ x \mid x \in A$ nebo $x \in B\}$**
	- Prvek $x$ patří do $A \cup B$, **právě když patří do $A$ nebo do $B$**
	- Spojení všech prvků v množinách
3. Rozdíl
	- Označujeme symbolem "$-$"
	- **$A - B = \{ x \mid x \in A$ a $x \notin B \}$**
	- Prvek $x$ patří do $A - B$, **právě když patří do $A$, ale nepatří do $B$**

### Vennovy diagramy
- Lze na nich **ilustrovat základní operace a vztahy mezi množinami**
- Umožňují názornou představu

### Potenční množina
- **$2^{X} = \{ A \mid A \subseteq X\}$**
- Množina, jejímiž prvky jsou **právě všechny podmnožiny dané množiny X**
- Značí se $2^{X}$
- Je-li $X$ konečná, pak $\mid 2^{X} \mid = 2^{\mid X \mid}$
- **Vždy obsahuje prázdnou množinu** ($\varnothing$), protože ta je podmnožinou každé množiny
>[!Example] Příklad
>- $X = \set{a,b} \rightarrow 2^{X}=\set{\varnothing, \set{a}, \set{b}, \set{a,b}}$
>- $X = \varnothing \rightarrow 2^{X} = \set{\varnothing}$

### Kartézský součin
- Kartézský součin $n$ množin je **množina všech uspořádaných $n$-tic prvků z těchto množin**
- $X_{1} \times ... \times X_{n} = \{ <x_{1}, ... x_{n}> \mid x_{1} \in X_{1}, ..., x_{n} \in X_{n}\}$
- Je-li $X_{1} = ... = X_{n} = X$, pak píšeme $X^{n}$ a říkáme **$n$-tá kartézská mocnina množiny $X$**
- Velikost $\mid A \times B \mid$ je $\mid A \mid \times \mid B \mid$

### Speciální množiny
- Speciální množinou je tzv. **prázdná množina**, označující se $\varnothing$. Tato **množina neobsahuje žádný prvek**, tedy pro **každý prvek $x$ platí: $x \notin \varnothing$**

### Význačné číselné množiny
1. Přirozená čísla - $\mathbb{N}$
	- $1, 2, 3, 4, ...$
	- Jsou používána pro počítání a pořadí.
2. Celá čísla - $\mathbb{Z}$
	- $..., -3, -2, -1, 0, 1, 2, 3, ...$
	- Zahrnují přirozená čísla, jejich záporné protějšky a nulu.
3. Racionální čísla - $\mathbb{Q}$
	- Čísla, která lze vyjádřit jako podíl dvou celých čísel ($\frac{p}{q}$, kde $p \in \mathbb{Z}$ a $q \in \mathbb{Z} \\ \set{0}$).
	- Mohou být zlomky nebo celá čísla.
4. Iracionální čísla
	- Zahrnuje čísla, která nelze vyjádřit jako podíl dvou celých čísel.
	- $\pi, e, \sqrt{2}$
5. Reální čísla - $\mathbb{R}$
	- Všechna racionální a iracionální čísla.
	- Zahrnují všechny možné délky na číselné ose.

![[ciselneMnoziny.png | 350]]

### Množiny konečné/nekonečné a spočetné/nespočetné
- Množiny se dělí na:
	- **Konečné**
		- **Existuje přirozené číslo $n$** tak, že **prvky v množině lze jednoznačně očíslovat**
		- Číslo $n$ určuje počet prvků v množině (velikost množiny)
		- Značení **$\mid A \mid \ =\ n$**
	- **Nekonečné**
		- Není-li konečná
		- Značení **$\mid A \mid \ =\ \infty$**

- Množiny se dále dělí na:
	- **Spočetné**
		- Pokud je **konečná** nebo **existuje bijekce $f: N \rightarrow A$**
			- Jinými slovy, množina je spočetná, pokud její prvky lze jednoznačně přiřadit k prvkům množiny přirozených čísel. Tedy pokud existuje bijekce mezi touto množinou a podmnožinou $\mathbb{N}$
		- Značení $\mid A \mid = n$
	- **Nespočetné**
		- Není-li spočetná
		- Nespočetné množiny jsou vždy nekonečné
		- **Důkaz** nespočetnosti lze například pomocí **Cantorovy diagonální metody**

>[!Example] Příklad spočetné a nespočetné množiny
>- Množina celých čísel $\mathbb{Z} = \set{..., -2, -1, 0, 1, 2, ...}$ je nekonečná, ale je **spočetná**, protože můžeme zkonstruovat bijekci s množinou $\mathbb{N}$.
>- Množina reálných čísel $\mathbb{R}$ je nespočetná. To lze dokázat pomocí Cantorova diagonálního argumentu, který ukazuje, že žádná bijekce mezi $\mathbb{N}$ a $\mathbb{R}$ neexistuje.


##### Navigace
Předchozí:  [[Úplné konjunktivní a disjunktivní normální formy]]
Následující: [[Relace, binární relace a jejich reprezentace, operace s relacemi]]
Celý okruh: [[1. Teoretické základy informačních technologií]]