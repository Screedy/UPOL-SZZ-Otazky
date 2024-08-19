## Spojitost funkce v bodě

- Říkáme, že $f : \mathbb{R} \to \mathbb{R}$ je spojitá v bodě $a \in \mathbb{R}$, právě když $$\lim_{x \to a} f(x) = f(a)$$
	- slovy: limita v bodě $a$ funkce $f$ je definována a je rovna funkční hodnotě v tomto bodě 
- Alternativní definice (**$\epsilon-\delta$ formulace spojitosti**):
	- Funkce $f$ definovaná na okolí bodu $a \in D_f$ je spojitá v bodě $a \in D_f$, právě když pro každé $\epsilon > 0$ existuje $\delta > 0$ tak, že pro každé $x \in \mathbb{R}$ splňující $|x - a| < \delta$ platí $|f(x) - f(a)| < \epsilon$.
- Analogicky jako u limity říkáme, že $f$ je spojitá zprava resp. zleva, právě když $\lim_{x \to a^+} f(x) = f(a)$, resp. $\lim_{x \to a^-} f(x) = f(a)$.
- Na rozdíl od limity:
	- musí být funkce $f$ v bodě $a$ definována
	- limita $\lim_{x \to a} f(x)$ musí být rovna funkční hodnotě v bodě $a$
- ![[Pasted image 20240628132136.png | 300]]

>[!Example]- Isibalo - Spojitost v bodě a na intervalu
><iframe width="660" height="385" src="https://www.youtube.com/embed/hLNV7Rzl8HI?si=2VaNekZ1HbTNDlwv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Základní vlastnosti spojitosti
- Nechť $f, g : \mathbb{R} \to \mathbb{R}$. Pak:
	1)  $f$ je spojitá v bodě $a$, právě když je v $a$ spojitá zprava i zleva
	2)  Jestliže je $f$ spojitá v $a$, pak existuje $U(a)$ takové, že $f$ je omezená na $U(a)$
	3)  Jsou-li $f, g$ spojité v $a$, pak $|f|$, $f + g$, $f \cdot g$ jsou také v $a$ spojité. Pokud $g(a) \neq 0$, je v $a$ spojitá i $\frac{f}{g}$
		- Jsou-li funkce $f$ a $g$ spojité v bodě $a$, pak můžeme o součtu, rozdílu, součinu a podílu těchto funkcí prohlásit, že se **jedná o funkci spojitou** v bodě $a$.
	4) Nechť $f$ je spojitá v $a$ a $g$ spojitá v $A = f(a)$. Pak je také $g \circ f$ spojitá v $a$

### O limitě složené funkce
Nechť $f, g : \mathbb{R} \to \mathbb{R}$ a nechť:
- $\lim_{x \to a} f(x) = A \in \mathbb{R}$,
- $g$ je spojitá v $A$.
Pak $\lim_{x \to a} g(f(x)) = g(A)$.

### O spojitosti elementárních funkcí
- Nechť $f : \mathbb{R} \to \mathbb{R}$, $x \in D(f)$ je elementární. Pak v každém bodě $x \in D(f)$ je $f$ spojitá.


## Spojitost na intervalu (množině)
Nechť $f : \mathbb{R} \to \mathbb{R}$ je definována na intervalu $(a, b)$.
1. Říkáme, že $f$ je spojitá na $(a, b)$, je-li spojitá v každém bodě tohoto intervalu.
2. Říkáme, že $f$ je spojitá na $\langle a, b \rangle$, je-li spojitá na $(a, b)$, v bodě $a$ je spojitá zprava a v bodě $b$ je spojitá zleva.

##### Navigace

Předchozí: [[Limita funkce včetně nevlastních, jednostranné limity]]
Následující: [[Vlastnosti spojitých funkcí, spojitost složené a inverzní funkce]]
Celý okruh: [[1. Teoretické základy informačních technologií]]

---
# Další věci k tomuto tématu

## Důsledky spojitosti funkce
- Spojitost funkce na intervalu má zajímavé důsledky důležité pro vyšetření průběhu funkce
### O omezenosti a minimu (Weierstrassova věta)
- Nechť $f : \mathbb{R} \to \mathbb{R}$ je spojitá na uzavřeném intervalu $\langle a, b \rangle$. Pak:
1. **O omezenosti**: $f$ je omezená na $\langle a, b \rangle$.
2. **O maximu a minimu:** $f$ nabývá na $\langle a, b \rangle$ svého (lokálního) maxima a minima. 
	- To znamená, že existují $c, d \in \langle a, b \rangle$ takové, že $f(c) = \min_{x \in \langle a, b \rangle} f(x)$ a $f(d) = \max_{x \in \langle a, b \rangle} f(x)$
	- Což také znamená, že pro všechna $x \in \langle a, b \rangle$ je $f(c) \leq f(x) \leq f(d)$.
	- Zjednodušeně, je-li funkce f spojitá v uzavřeném intervalu ⟨a,b⟩, pak nabývá v alespoň jednom bodě svého lokálního maxima a v alespoň jednom bodě svého minima.
	- Tato věta nám dává jistotu v existenci lokálního maxima a minima, neříká však nic o jejich vyhledání
	
Nechť navíc $f(a) < f(b)$. Pak:
3. **O nabývání mezihodnot (Bolzanova-Weierstrassova věta):** $f$ nabývá v intervalu $(a, b)$ všech hodnot mezi $f(a)$ a $f(b)$. 
	- To znamená, že pro libovolné číslo $d \in (f(a), f(b))$ existuje číslo $c \in (a, b)$ takové, že $f(c) = d$.
### Bolzanova věta 
- Nechť $f : \mathbb{R} \to \mathbb{R}$ je spojitá na uzavřeném intervalu $\langle a, b \rangle$ taková, že $f(a) \cdot f(b) < 0$. Pak existuje $c \in \mathbb{R}$ takové, že $c \in (a, b)$ a $f(c) = 0$.
	-  její graf v alespoň jednom vnitřním bodě tohoto intervalu protíná osu x
- Jedná se o postačující podmínku, který je přímým důsledkem **Bolzano-Weierstrassovy** věty
	- zajišťuje nám existenci nulového bodu
	- nulový bod lze nalézt **metodou půlení intervalu**
- ![[Pasted image 20240628134849.png]]

### O hodnotách spojité funkce
  - Funkce $f$ je spojitá na uzavřeném intervalu $\langle a, b \rangle$ a v $(a, b)$ nemá žádné nulové body, pak na $(a, b)$ je buď $f(x) > 0$ nebo $f(x) < 0$ pro všechny $x \in (a, b)$.

### O spojitosti inverzní funkce
  - Nechť $f$ je spojitá a ryze monotónní na intervalu $I$. Pak inverzní funkce $f^{-1}$ je také spojitá na $f(I)$.

### O spojitosti složených funkcí
- Je-li funkce $g$ spojitá v bodě $a$ a funkce $f$ spojitá v bodě $g(a)$, pak je složená funkce $f \circ g$ spojitá v bodě $a$.
	- složením spojitých funkcí získáme opět spojitou funkci.

## Jednostranná spojitost a body nespojitosti
- Mějme funkci $f : A \to \mathbb{R}$. 
- Jestliže v jistém levém, resp. pravém okolí bodu $a$ není funkce $f$ definována, pak mluvíme o jednostranné spojitosti v bodě $a$ zprava, resp. zleva.
- Např. funkce $f : y = \sqrt{x}$ jde v bodě 0 o spojitost zprava (funkce není definována pro $x < 0$). 
- Pojem jednostranné spojitosti však zavádíme i v případě, že máme definováno okolí bodu $a$ zprava i zleva.

### Jednostranná spojitost
Říkáme, že funkce $f : A \to \mathbb{R}$ je spojitá zprava (zleva) v bodě $a \in A$, jestliže platí:
- $\lim_{x \to a^+} f(x) = f(a)$
- resp. $\lim_{x \to a^-} f(x) = f(a)$

### Body nespojitosti
- Body definičního oboru funkce $f$, v nichž není funkce spojitá, nazýváme body nespojitosti funkce $f$. Tyto body můžeme roztřídit do tří skupin

#### Body odstranitelné nespojitosti
- Existuje konečná limita $\lim_{x \to a} f(x) = b$, ale $b \neq f(a)$. 
- Stačí funkci $f$ v bodě $a$ předefinovat tak, že položíme $f(a) = b$ a funkce se stane spojitou. 
- K bodům odstranitelné nespojitosti patří také body, v nichž je funkce $f$ nedefinovaná, ale existuje v něm limita $\lim_{x \to a} f(x) = b$. 
	- V takovém případě postačí funkci $f$ v bodě $a$ dodefinovat tak, že položíme $f(a) = b$. Funkci $f$ tak rozšíříme na $D(f) \cup \{a\}$.
- Např. Funkce $f(x) = \frac{\sin x}{x}$ není definována v bodě $x = 0$.
	- ![[Pasted image 20240628133523.png]]

#### Nespojitost prvního druhu
- Existují konečné jednostranné limity, ale nejsou si rovny:
$$
\lim_{x \to a^+} f(x) \neq \lim_{x \to a^-} f(x)
$$
-  tomto případě nazveme bod $a$ nespojitostí prvního druhu a číslo
$$
s(a) = \lim_{x \to a^+} f(x) - \lim_{x \to a^-} f(x)
$$
nazýváme **skokem funkce v bodě $a$.**
- Např. funkce $f(x) = \text{sgn} x$ má v bodě 0 nespojitost prvního druhu.
	- ![[Pasted image 20240628133546.png]]

#### Nespojitost druhého druhu
- Jestliže alespoň jedna z jednostranných limit neexistuje nebo je nevlastní $\lim_{x \to a^+} f(x) = \infty$, pak bod $a$ nazveme bodem nespojitosti druhého druhu.
- Např. funkce $f(x) = \frac{1}{x}$ má v bodě 0 nespojitost druhého druhu.
	- Tvrzení nám dokáže opět jednostranné limity:
$$
\lim_{x \to 0^+} \frac{1}{x} = \infty, \quad \text{resp.} \quad \lim_{x \to 0^-} \frac{1}{x} = -\infty
$$

- ![[Pasted image 20240628133619.png]]

