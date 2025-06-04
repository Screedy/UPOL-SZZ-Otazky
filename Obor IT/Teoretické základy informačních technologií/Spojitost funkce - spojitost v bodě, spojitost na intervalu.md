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

