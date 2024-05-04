### Co je to logika?
- Logika je **věda o správném usuzování**
- Logika *studuje* formy *usuzování* **bez ohledu na obsah**, proto má moderní logika **symbolický charakter**

- *Moderní logika* bývá označována jako **logika formální (symbolická)**
- **Klasická logika** = logika, která používá **dvě pravdivostní hodnoty** (pravda a nepravda) a **klasické logické spojky**
- **Neklasické logika** = logika, která se **zabývá dalšími aspekty**
	- *Modální logika* - používá **neklasické spojky** (*"je možné, že"*, *"je nutné, že"*)
	- *Temporální logika* - zabývá se tvrzeními, ve kterých hraje roli **čas**
	- *Fuzzy logika* - studuje **více pravdivostních hodnot**
- Znalost základů logiky nám umožňuje srozumitelně a jednoznačně se vyjadřovat a argumentovat

### **Výroky a logické spojky**
- **Výrok** je **tvrzení** (výpověď), u kterého **má smysl uvažovat o jeho pravdivosti**
- **Logické spojky** jsou **jazykové výrazy**, kterými **z jednodušších výroků vytváříme výroky složitější**

- Výrok může mít 
	- **Pravdivostní hodnotu 1 ("pravda")**
	- **Pravdivostní hodnotu 0 ("nepravda")**

- *Pravdivostní hodnotu výroku V* označujeme **$||V||_e$**
	- **e = pravdivostní ohodnocení**

- Pravdivostní hodnota výroku <u>se počítá</u> z **pravdivostních hodnot atomických výroků** pomocí **pravdivostních funkcí spojek**

| Název           | Symbol | Pravdivostní funkce | Tabulka pravdivostní funkce             |
| --------------- | ------ | ------------------- | --------------------------------------- |
| **Negace**      | **ㄱ**  | **ㄱ’**              | ![[MacBook-2024-02-28-000750@2x.png]]   |
| **Konjunkce**   | **⋀**  | **⋀’**              | ![[MacBook-2024-02-28-000751@2x.png ]]  |
| **Disjunkce**   | **⋁**  | **⋁'**              | ![[MacBook-2024-02-28-000752@2x.png]]   |
| **Implikace**   | **⟶**  | **⟶'**              | ![[MacBook-2024-02-28-000753@2x.png]]   |
| **Ekvivalence** | **↔**  | **↔'**              | ![[MacBook-2024-02-28-000754@2x.png]]   |
| **Piercova**    | **↓**  | **↓'**              | ![[MacBook-2024-02-28-000755@2x.png]]   |
| Shefferova      | **↑**  | **↑'**              | ![[MacBook-2024-02-28-000756@2x 1.png]] |

### **Výroky s proměnou, kvantifikátory**
- Některé výrazy *přirozeného jazyka* obsahují proměnné
	- Číslo x je větší nebo rovno 3
	-  $x+y \geq z$
- Tyto výrazy **nejsou výroky**. Museli bychom **určit hodnotu proměnných**, které se v těchto výrazech vyskytují.
- Výrazy obsahující *proměnné*, ze kterých se po dosazení hodnot za proměnné stanou výroky, nazýváme **výrokové formy**

- **Výrokové formy** bývají zvykem **označovat písmenem, za kterým jsou v závorce uvedeny všechny proměnné, které forma obsahuje**
	- Číslo x je větší nebo rovno 3 = **V(x)**
	- *$x+y \geq z=U(x,y,z)$*

- **Kvantifikátory** jsou **jazykové výrazy, kterými z výrokových forem vznikají výroky**

### **Obecný kvantifikátor**
- Symbolicky jej značíme $\forall$
- Symbol pochází z němčiny ze slova **allgemein** (obecný)
- *Je pravdivý*, pokud **pro všechny hodnoty z oboru hodnot je výrok pravdivý**
- Použití pro výrokovou formu "x je větší nebo rovno 1":
	- Pro každé *x* platí, že *x* je větší nebo rovno 1
	- ($\forall x$) ($x$ je větší nebo rovno 1)
	- ($\forall x$) ($x\geq 1$)

### **Existenční kvantifikátor**
- Symbolicky jej značíme $\exists$
- Symbol pochází z němčiny ze slova **existentiell** (existenční)
- *Je pravdivý*, pokud **pro alespoň jednu hodnotu z oboru hodnot je výrok pravdivý**
- Použití pro výraz "x je větší nebo rovno 1":
	- Existuje $x$ tak, že $x$ je větší nebo rovno 1
	- $(\exists x)$ ($x$ je větší nebo rovno 1)
	- $(\exists x)$ $(x\geq 1)$

### **Základy výrokové logiky**
- Výroková logika **je nejjednodušším formálním systémem logiky**
- Ve výrokové logice nepracujeme s výroky samotnými, ale **pracujeme s formami výroků**
- Formy výroků se nazývají **formule** a jsou to **přesně definované řetězce symbolů**
- *Konkrétní výroky dostaneme nahrazením výrokových symbolů atomickými výroky*
- *Formule jsou jisté posloupnosti symbolů jazyka, samy o sobě nemají žádný význam*

- Jazyk výrokové logiky se skládá z:
	- **výrokových symbolů** - p, q, r, ...
	- **symbolů výrokových spojek** - ㄱ, ∧, ∨, ⟶, ↔
	- **pomocných symbolů** - různé druhy závorek

- Formule daného jazyka výrokové logiky je definovaná následovně:
	- **každý výrokový symbol je formule** (tzv. atomické)
	- jsou-li φ (phi) a 𝜓 (psi) formule, jsou i formule (tzv. složené) i výrazy:
		- ㄱφ
		- (φ ∧ 𝜓)
		- (φ ∨ 𝜓)
		- (φ ⟶ 𝜓)
		- (φ ↔ 𝜓)

- **Pravdivostní ohodnocení** je libovolné zobrazení $e$ výrokových symbolů daného jazyka výrokové logiky do množiny $\{0, 1\}$
- **0** a **1** reprezentují **nepravda** a **pravda**
- *Pravdivostní hodnota formule* φ při ohodnocení $e$, označujeme ji $\mid\mid\phi\mid\mid_e$, je definována:
	- Je-li $\phi$ *výrokovým symbolem p*, pak 
		- $\mid\mid p\mid\mid_e$ = e(p)
	- Je-li $\phi$ složená formule, pak
		- $\mid\mid\neg\psi\mid\mid_e$ = $\neg'\mid\mid \psi\mid\mid_{e}$
		- $\mid\mid \psi \ \land \  \theta\mid\mid_{e}\ = \  \mid\mid \psi\mid\mid_{e} \ \land' \mid \mid \theta \mid\mid_{e}$
		- $\mid\mid\phi\lor\theta\mid\mid_{e} \ =\ \mid\mid\phi\mid\mid_{e}\ \lor' \  \mid\mid\theta\mid\mid_{e}$
		- $\mid\mid\phi\rightarrow\theta\mid\mid _{e} \ =\ \mid\mid\phi\mid\mid_{e}\ \rightarrow' \  \mid\mid\theta\mid\mid_{e}$
		- $\mid\mid\phi\leftrightarrow\theta\mid\mid_{e} \ =\ \mid\mid\phi\mid\mid_{e}\ \leftrightarrow' \  \mid\mid\theta\mid\mid_{e}$

- **Tautologie** = je-li formule při **každém ohodnocení pravdivá**
- **Kontradikce** = je-li formule při **každém ohodnocení nepravdivá**
- **Splnitelná** = je-li formule **alespoň při jednom ohodnocení pravdivá**

- **Formule $\psi$ sémanticky plyne z formule $\phi$**, značíme $\phi \models \psi$, jestliže $\psi$ je pravdivá při každém ohodnocení, při kterém je pravdivá $\phi$
- Pokud $\psi$ sémanticky plyne z $\phi$ a naopak, říkáme, že $\psi$ a $\phi$ jsou sémanticky ekvivalentní $\phi \equiv \psi$

##### Navigace
Předchozí: Je první hehe
Následující: [[Booleovské funkce, funkčně úplné systémy]]
Celý okruh: [[1. Teoretické základy informačních technologií]]