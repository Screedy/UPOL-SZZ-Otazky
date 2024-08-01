## Spojitost funkce v bodě
- Intuitivně si můžeme spojitost funkce v bodě představit jako, že "velmi malé" změně hodnoty proměnné z definičního oboru odpovídá "velmi malá" změna funkční hodnoty
- Velký význam poznatků spojitosti při vyšetřování průběhu funkce 
### Formální definice
- Říkáme, že $f : \mathbb{R} \to \mathbb{R}$ je spojitá v bodě $a \in \mathbb{R}$, právě když $$\lim_{x \to a} f(x) = f(a)$$
- Alternativní definice (**$\epsilon-\delta$ formulace spojitosti**):
	- Funkce $f$ definovaná na okolí bodu $a \in D_f$ je spojitá v bodě $a \in D_f$, právě když pro každé $\epsilon > 0$ existuje $\delta > 0$ tak, že pro každé $x \in \mathbb{R}$ splňující $|x - a| < \delta$ platí $|f(x) - f(a)| < \epsilon$.

- Analogicky říkáme, že $f$ je spojitá zprava resp. zleva, právě když $\lim_{x \to a^+} f(x) = f(a)$, resp. $\lim_{x \to a^-} f(x) = f(a)$.
- Na rozdíl od limity:
	- musí být funkce $f$ v bodě $a$ definována 
	- limita $\lim_{x \to a} f(x)$ musí být rovna funkční hodnotě v bodě $a$
- ![[Pasted image 20240628132136.png]]
### 1) Základní vlastnosti spojitosti
- z definice plyne několik podmínek pro splnění spojitosti
- Nechť $f, g : \mathbb{R} \to \mathbb{R}$. Pak:
1)  $f$ je spojitá v bodě $a$, právě když je v $a$ spojitá zprava i zleva
2)  Jestliže je $f$ spojitá v $a$, pak existuje $U(a)$ takové, že $f$ je omezená na $U(a)$
3)  Jsou-li $f, g$ spojité v $a$, pak $|f|$, $f + g$, $f \cdot g$ jsou také v $a$ spojité. Pokud $g(a) \neq 0$, je v $a$ spojitá i $\frac{f}{g}$
4) Nechť $f$ je spojitá v $a$ a $g$ spojitá v $A = f(a)$. Pak je také $g \circ f$ spojitá v $a$

### 2) O limitě složené funkce
Nechť $f, g : \mathbb{R} \to \mathbb{R}$ a nechť:
- $\lim_{x \to a} f(x) = A \in \mathbb{R}$,
- $g$ je spojitá v $A$.
Pak $\lim_{x \to a} g(f(x)) = g(A)$.

### 3) O spojitosti elementárních funkcí
- Nechť $f : \mathbb{R} \to \mathbb{R}$, $x \in D(f)$ je elementární. Pak v každém bodě $x \in D(f)$ je $f$ spojitá.

### 4) O spojitosti inverzní funkce
  - Nechť $f$ je spojitá a ryze monotónní na intervalu $I$. Pak inverzní funkce $f^{-1}$ je také spojitá na $f(I)$.
### 5) O spojitosti složených funkcí
- Je-li funkce $g$ spojitá v bodě $a$ a funkce $f$ spojitá v bodě $g(a)$, pak je složená funkce $f \circ g$ spojitá v bodě $a$.


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

##### Navigace

Předchozí: [[Spojitost funkce - spojitost v bodě, spojitost na intervalu]]
Následující: [[Derivace funkce a její geometrický význam - Pravidla pro derivování funkcí, derivace složené funkce, derivace inverzní funkce, derivace elementárních funkcí]]
Celý okruh: [[1. Teoretické základy informačních technologií]]
