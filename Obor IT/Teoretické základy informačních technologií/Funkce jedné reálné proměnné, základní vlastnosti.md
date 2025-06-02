- Zobrazení $f$ se nazývá **reálná funkce**, jestliže $H(f) \subset \mathbb{R}$
- Reálná funkce $f$ se nazývá
  1.  **funkce jedné reálné proměnné**, jestliže $D(f) \subset \mathbb{R}$, tedy $f:\mathbb{R} \rightarrow \mathbb{R}$
  2.  **posloupnost**, jestliže $D(f) = \mathbb{N}$, tedy $f: \mathbb{N} \rightarrow \mathbb{R}$
  3.  **funkce $n$ reálných proměnných**, jestliže $D(f) \subset \mathbb{R}^{n}$, kde $n \in \mathbb{N}$, tedy $f:\mathbb{R}^{n} \rightarrow \mathbb{R}$

## Funkce jedné reálné proměnné
- Funkce jedné reálné proměnné
  - Každé zobrazení $f$ z $\mathbb{R}$ do $\mathbb{R}$ nazýváme **reálná funkce jedné reálné proměnné.**
  - Je-li $(x,y) \in f$, píšeme $y = f(x)$
    - $x$ se nazývá **nezávislá proměnná, y závislá proměnná**
- S pojmem funkce jsou spjaty _dvě významné množiny_:
  - **Definiční obor funkce:** $D(f) = \set{x \in \mathbb{R}; \exists(x,y) \in f}$
    - Prvky definičního oboru nazýváme vzory
  - **Funkční obor (obor hodnot):** $H(f) = \set{y \in \mathbb{R}; \exists(x,y) \in f}$
    - Prvky funkčního oboru nazýváme obrazy

### Způsoby definice funkce
- Zadat (definovat) funkci $f$ znamená **určit její definiční obor $D(f)$ a jisté pravidlo $V(x,y)$**, jehož oborem pravdivosti je $f$ a které stanovuje, jak k zadanému $x \in D(f)$ najít hodnotu $f(x)$.
- Podle toho, jak je toto pravidlo formulováno, rozlišujeme tato zadání funkce:
  1.  **rovnicí (předpisem):** $$
	   \begin{gather}
	   f=\set{(x,y) \in \mathbb{R} \times \mathbb{R}; y=x^{2}-1}\\
	   f: y=x^{2}-1
	   \end{gather}$$
  2.  **tabulkou:**
      ```sql
      |  x  | -2  | -1  | 0   | 1   | 2   | 3   |
      | --- | --- | --- | --- | --- | --- | --- |
      |  y  | 3   | 0   | -1  | 0   | 3   | 8   |
      ```
  3.  **grafem:**![[MacBook-2024-05-06-001204.png]]
  4.  **po částech:**
      $$
      \begin{aligned}
      \chi(x)=\cases{0& \text{pro $x$ iracionální} \\1 & \text{pro $x$ racionální}} \\
      sgn\ x = \cases{-1 & pro x < 0 \\ \ \ \ 0 & pro x = 0 \\ \ \ \ 1 & pro x > 0}&&&&&&&&&&&&&&&&
      \end{aligned}
      $$
  5.  implicitní rovnic (nejsou explicitně odděleny závislé a nezávislé proměnné): $$x^{2}+y^{2}=25$$
  6.  parametricky: $$x=4 \cdot \cos{t}, y=\sin{t}, t\in <0, \pi>$$
  7.  jinak: např. pomocí výrokové formy $V(x,y)=$ "$y$ je největší celé číslo, které není větší než $x$", ...

## Vlastnosti funkcí
- **Omezenost:**
  - Nechť $f: \mathbb{R} \rightarrow \mathbb{R}$ a $M \in D(f)$. Říkáme, že $f$ je na množině $M$
    1. **omezená shora,** právě když $$\exists K \in \mathbb{R}, \forall{x}\in M: f(x) \leq K$$
    2. **omezená zdola,** právě když $$\exists{k} \in \mathbb{R}, \forall{x} \in M: f(x) \geq k$$
  - Pokud je funkce omezená zdola i shora, říkáme, že je na množině $M$ **omezená**
  - Dále říkáme, že $f$ má v bodě $a \in M$
    1. **maximum na množině $M$,** právě když $$\forall{x} \in M: f(x) \leq f(a) \text{ a píšeme } f(a)=\max_{x\in M}{f(x)}$$
    2. **minimum na množině $M$**, právě když $$\forall{x} \in M: f(x) \geq f(a) \text{ a píšeme } f(a)=\min_{x \in M}{f(x)}$$
- **Monotónnost:**
  - Nechť $f: \mathbb{R} \rightarrow \mathbb{R}$ a $M \subset D(f).$ Říkáme, že funkce $f$ je na množině $M$
    1. **rostoucí,** právě když $$\forall{x_{1},x_{2}} \in M: (x_{1} < x_{2} \Rightarrow f(x_{1}) < f(x_{2}))$$
    2. **neklesající,** právě když $$\forall{x_{1},x_{2}} \in M: (x_{1} < x_{2} \Rightarrow f(x_{1}) \leq f(x_{2}))$$
    3. **klesající,** právě když $$\forall{x_{1},x_{2}} \in M: (x_{1} < x_{2} \Rightarrow f(x_{1}) > f(x_{2}))$$
    4. **nerostoucí,** právě když $$\forall{x_{1},x_{2}} \in M:(x_{1}<x_{2} \Rightarrow f(x_{1}) \geq f(x_{2}))$$
  - Pokud má funkce některou z těchto vlastností, říkáme, že je **monotonní na $M$**.
  - Je-li funkce rostoucí nebo klesající, říkáme, že je **ryze monotonní na $M$**.
- **Parita a periodičnost:**
  - Nechť $f: \mathbb{R} \rightarrow \mathbb{R}$ a $M \subset D(f)$. Říkáme, že funkce $f$ je
    1. **sudá na množině $M$** (symetrická podle $y$), právě když $$\forall{x} \in M: (-x) \in M \land f(x) = f(-x)$$
    2. **lichá na množině $M$** (symetrická podle $x$), právě když $$\forall{x} \in M:(-x) \in M \land f(-x) = -f(x)$$
    3. **$p$-periodická na množině $M$** s periodou $p \in \mathbb{R}$ $$\forall{x} \in M: x + p \in M \land x-p \in M \land f(x+p)=f(x-p)=f(x)$$

### Funkce injektivní, surjektivní, bijektivní
- Funkce $f: X \rightarrow Y$ se nazývá:
  - **Prostá (injektivní),** právě když
    - pro každé $x_{1}, x_{2} \in X$ platí, jestliže $x_{1} \neq x_{2}$, pak $f(x_{1}) \neq f(x_{2})$
    - _tedy neopakují se $y$ pro dvě různá $x$_
    - např. lineární funkce
  - **Funkce množiny $X$ na množinu $Y$ (surjektivní),** právě když
    - pro každé $y \in Y$ existuje $x \in X$ tak, že $f(x) = y$
    - _tedy musí být použity všechny prvky z $Y$_
  - Vzájemně jednoznačná (**bijektivní**), právě když **je injektivní a surjektivní**

##### Navigace

Předchozí: [[Lineární zobrazení a transformace a jejich matice]]
Následující: [[Posloupnosti a jejich limity, limes superior, limes inferior]]
Celý okruh: [[1. Teoretické základy informačních technologií]]
