#### Okolí bodu
- Nechť $a \in \mathbb{R}$ a je dáno $\delta \in \mathbb{R}, \delta > 0$, pak interval
  $$U_{\delta}(a) = (a - \delta, a + \delta)$$
  nazýváme **$\delta$-okolím bodu** $a$.
- Interval $U_{\delta}^{-}(a) = \langle a - \delta, a)$ nazýváme **levým $\delta$-okolím bodu $a$**
- Interval $U_{\delta}^{+} = (a, a + \delta \rangle$ nazýváme **pravým $\delta$-okolím bodu** $a$
#### Prstencové okolí bodu
- Prstencovým $\delta$-okolím bodu $a$ rozumíme množinu
  $$P_{\delta}(a) = U_{\delta}(a) \setminus \{a\} = (a - \delta, a) \cup (a, a + \delta)$$
- Levé a pravé prstencové $\delta$-okolí:
  $$P_{\delta}^{-} = U_{\delta}^{-} \setminus \{a\} = (a - \delta, a)$$
  $$P_{\delta}^{+} = U_{\delta}^{+} \setminus \{a\} = (a, a + \delta)$$
#### Okolí na rozšířené reálné ose

- Nechť je dáno číslo $k \in \mathbb{R}$. Okolím bodu $\infty$ rozumíme interval
  $$P_{k}(\infty) = U_{k}(\infty) = (k, \infty),$$
- Okolím bodu $-\infty$ rozumíme interval
  $$P_{k}(-\infty) = U_{k}(-\infty) = (-\infty, k)$$
## Limita funkce
- Nechť $f : \mathbb{R} \rightarrow \mathbb{R}$. Říkáme, že $f$ má v bodě $a \in \mathbb{R}^*$ limitu $A \in \mathbb{R}^*$, právě když platí podmínka
  $$\forall U(A) \; \exists P(a) \; \forall x \in \mathbb{R} : (x \in P(a) \Rightarrow f(x) \in U(A))$$

- Píšeme $\lim_{x \to a} f(x) = A$.
- Pro $a \in \mathbb{R}$ jde o limitu ve vlastním bodě, zatímco pro $a \in \{-\infty, \infty\}$ jde o limitu v nevlastním bodě
- Je-li $A \in \mathbb{R}$, říkáme, že $f$ má vlastní limitu, zatímco je-li $A \in \{-\infty, \infty\}$, říkáme, že $f$ má nevlastní limitu.
#### Jednostranné limity
- Často je třeba rozlišit, zda se zajímáme o hodnoty funkce $f$ v blízkosti bodu $a \in \mathbb{R}$ pro $x < a$ nebo $x > a$, je tak vhodné zavést pojem jednostranné limity
- Nechť $f : \mathbb{R} \to \mathbb{R}$. Říkáme, že $f$ má v bodě $a \in \mathbb{R}$ limitu $A \in \mathbb{R}^*$ zprava, právě když platí podmínka $$\forall U(A) \; \exists P^+(a) \; \forall x \in \mathbb{R} \; : \; (x \in P^+(a) \Rightarrow f(x) \in U(A))$$
- Píšeme $\lim_{x \to a^+} f(x) = A$
- Podobně lze popsat limitu zleva, kde píšeme $P^-(a)$ místo $P^+(a)$ a $\lim_{x \to a^-} f(x) = A$
- Funkce $f$ má v bodě $a$ limitu $A$, právě když existují obě jednostranné limity (limity zprava a zleva) a jsou si rovny
  - např. $f(x) = sgn(x)$ v bodě 0 limitu nemá, protože:
    - $\lim_{x \to 0^-} sgn(x) = -1$
    - $\lim_{x \to 0^+} sgn(x) = 1$
## Typy limit funkce
- Rozlišujeme $4$ typy limit podle toho, jestli $a$, $A$ nabývá reálných nebo hodnot $\pm \infty$
>[!Example]- Isibalo - Typy limit funkce
><iframe width="660" height="385" src="https://www.youtube.com/embed/W-0s1lMRwkc?si=90SZ0ZKKwQHyTcBs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

>[!Example]- Vlastní limita ve vlastním bodě
>![[Pasted image 20240627200335.png | 200]]
>pro $a, A \in \mathbb{R}$
>- Jdeme k nějaké konkrétní hodnotě a vyjde nám konkrétní výsledek.
>- např. $\lim_{x \rightarrow  1}(\frac{x^{2}-1}{x-1})=2$
>
> <iframe width="660" height="385" src="https://www.youtube.com/embed/R4y0NXiNVRo?si=1ejRy1dAKI8fTKI4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

>[!Example]- Vlastní limita v nevlastním bodě
>![[Pasted image 20240627203837.png | 200]]
>- pro $a \in \mathbb{\pm \infty} \land A\in\mathbb{R}$
>- pro hodně vzdálené body $x$ se funkční hodnoty přibližují k nějaké reálné funkční hodnotě $A$
>- např. $\lim_{x \rightarrow \infty}(\frac{x+1}{x})=1$
>
><iframe width="660" height="385" src="https://www.youtube.com/embed/jV09c5KLRAs?si=-J47ilfs4NWHpVAh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

>[!Example]- Nevlastní limita ve vlastním bodě 
>![[Pasted image 20240627200435.png | 200]]
>- pro $a \in \mathbb{R} \land A\in\mathbb{\pm \infty}$
>- např. $\lim_{x \rightarrow 0}(\frac{1}{x^{2}})=+\infty$
>
><iframe width="660" height="385" src="https://www.youtube.com/embed/pTRjPKIu2w8?si=xPBt7HKUQcXSpxT9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

>[!Example]- Nevlastní limita v nevlastním bodě
>![[Pasted image 20240627203755.png | 200]]
>- pro $a, A \in \mathbb{\pm \infty}$
>- funkční hodnoty vzdálených $x$ konverguje k $\pm \infty$
>- např. $\lim_{x \rightarrow \infty}(x+2) = \infty$
>
><iframe width="660" height="385" src="https://www.youtube.com/embed/e79gAkmqJZA?si=F8ufqbjIwvbwGDPC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
## Použití limity funkce
1. Vyšetření průběhu funkcí
   - **Určení asymptot**: Limity umožňují nalézt asymptoty funkce
     - (přímky, ke kterým se funkce nekonečně přibližuje)
   - **Chování v nekonečnu**: Limity určují, jak se funkce chová, když se argument blíží k $\pm \infty$
2. Spojitost funkcí
   - **Definice spojitosti**
     - Funkce je spojitá v bodě, pokud se limita funkce v tomto bodě rovná funkční hodnotě v tomto bodě.
3. Derivace
   - **Definice derivace**
     - Derivace funkce v bodě je definována jako limita rozdílového podílu pro $h$ blížící se k nule.
   - **Aplikace derivací**:
     - Derivace se používají k určení rychlosti změny, nalezení maxima a minima funkcí, a v mnoha fyzikálních a technických aplikacích.
4. Integrály
   - **Definice integrálu**
     - limita Riemannových součtů je definována počtem dělení intervalu $n$, pro $n$ jdoucí k nekonečnu.
   - **Aplikace integrálů**: Integrály se používají k výpočtu obsahu plochy vymezené danými funkcemi, objemu rotačních těles, délky křivky, ...
## Vlastnosti limity funkce
- Zápis $\lim_{x \to a} f(x) = A$ znamená, že limita v bodě $a$ existuje a je rovna $A$.
#### 1) Lokální vlastnost limity
- Nechť $f : \mathbb{R} \to \mathbb{R}$ a $g : \mathbb{R} \to \mathbb{R}$. Nechť dále existuje $P(a)$ takové, že $\forall x \in P(a)$ platí $f(x) = g(x)$. Pak $\lim_{x \to a} f(x) = A$, právě když $\lim_{x \to a} g(x) = A$.
#### 2) O jednoznačnosti limity
- Pro $f : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}^*$ existuje nejvýše jedna limita $f$ v $a$.
  - stejně tak pro limitu zleva, resp. zprava
#### 3) O jednostranných limitách
- Nechť $f : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}$. Pak $\lim_{x \to a} f(x) = A \in \mathbb{R}^*$, právě když $\lim_{x \to a^+} f(x) = \lim_{x \to a^-} f(x) = A$.
  - obě jednostranné limity musí být rovny
#### 4) O omezenosti
- Nechť $f : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}^*$ a nechť $\lim_{x \to a} f(x) = A \in \mathbb{R}$. Pak existuje $P(a) \subset D(f)$ takové, že $f$ je na $P(a)$ omezená.
  - to znamená, že existuje takové $K > 0$ takové, že pro $x \in P(a)$ platí $|f(x)| \leq K$
  - $x\in{U(a)} \to x\in\mathbb{R}$
#### 5) O limitě absolutní hodnoty
- Nechť $f : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}^*$. Jestliže $\lim_{x \to a} f(x) = A \in \mathbb{R}^*$, pak $\lim_{x \to a} |f(x)| = |A|$.
#### 6) O aritmetických operacích s limitami
- Nechť $f, g : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}^*$, $\lim_{x \to a} f(x) = A$, $\lim_{x \to a} g(x) = B$ a $A,B \in \mathbb{R}^*$. Potom:
1. Je-li součet $A+B$ definován, je $\lim_{x \to a}(f(x)+g(x)) = A+B$
   - limita součtu je součet limit
2. Je-li součin $A \cdot B$ definován, je $\lim_{x \to a}(f(x) \cdot g(x)) = A \cdot B$
   - limita součinu je součin limit
3. Je-li podíl $\frac{A}{B}$ definován, je $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{A}{B}$
   - limita podílu je podíl limit
#### 7) O limitě složené funkce
- Nechť $f, g : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}^*$. Nechť dále současně platí podmínky:
1. $\lim_{x \to a} f(x) = A \in \mathbb{R}^*$,
2. $\lim_{y \to A} g(y) = B \in \mathbb{R}^*$,
3. existuje $P(a)$ takové, že $\forall x \in \mathbb{R}$ platí: je-li $x \in P(a)$ pak $f(x) \neq A$. - (pro $x$ dostatečně blízká k $a$, tak že $f(x) \neq A$)
   Pak $\lim_{x \to a} (g \circ f)(x) = \lim_{x \to a} g(f(x)) = B$.
#### 8) O limitním přechodu v nerovnost
- Nechť $f, g : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}^*$. Nechť dále $\lim_{x \to a} f(x) = A \in \mathbb{R}^*$ a $\lim_{x \to a} g(x) = B \in \mathbb{R}^*$.
1. Jestliže $A < B$, pak existuje $P(a)$ takové, že pro $x \in P(a)$ je $f(x) < g(x)$.
2. Jestliže existuje $P(a)$ tak, že pro $x \in P(a)$ je $f(x) \leq g(x)$, pak $A \leq B$.
#### 9) O důsledcích věty o limitním přechodu v nerovnost
Nechť $f, g : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}^*$.
1. Je-li $\lim_{x \to a} f(x) = 0$ a existuje okolí $P(a)$ tak, že $g$ je omezená na $P(a)$. Pak $\lim_{x \to a} f(x) \cdot g(x) = 0$.
2. Je-li $\lim_{x \to a} f(x) = A > 0$, pak existuje okolí $P(a)$ takové, že pro $x \in P(a)$ je $f(x) > 0$.
#### 10) O sevření nebo o křídlech
Nechť $a \in \mathbb{R}^*$, $f, g, h : \mathbb{R} \to \mathbb{R}$. Nechť dále:
1. existuje $P(a)$ takové, že pro $x \in P(a)$ platí $h(x) \leq f(x) \leq g(x)$,
2. $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = A \in \mathbb{R}^*$.
Pak také $\lim_{x \to a} f(x) = A$.
---
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
#### Základní vlastnosti spojitosti
- Nechť $f, g : \mathbb{R} \to \mathbb{R}$. Pak:
	1)  $f$ je spojitá v bodě $a$, právě když je v $a$ spojitá zprava i zleva
	2)  Jestliže je $f$ spojitá v $a$, pak existuje $U(a)$ takové, že $f$ je omezená na $U(a)$
	3)  Jsou-li $f, g$ spojité v $a$, pak $|f|$, $f + g$, $f \cdot g$ jsou také v $a$ spojité. Pokud $g(a) \neq 0$, je v $a$ spojitá i $\frac{f}{g}$
		- Jsou-li funkce $f$ a $g$ spojité v bodě $a$, pak můžeme o součtu, rozdílu, součinu a podílu těchto funkcí prohlásit, že se **jedná o funkci spojitou** v bodě $a$.
	4) Nechť $f$ je spojitá v $a$ a $g$ spojitá v $A = f(a)$. Pak je také $g \circ f$ spojitá v $a$
#### O limitě složené funkce
Nechť $f, g : \mathbb{R} \to \mathbb{R}$ a nechť:
- $\lim_{x \to a} f(x) = A \in \mathbb{R}$,
- $g$ je spojitá v $A$.
- pak $\lim_{x \to a} g(f(x)) = g(A)$.
#### O spojitosti elementárních funkcí
- Nechť $f : \mathbb{R} \to \mathbb{R}$, $x \in D(f)$ je elementární. Pak v každém bodě $x \in D(f)$ je $f$ spojitá.
#### Spojitost na intervalu (množině)
Nechť $f : \mathbb{R} \to \mathbb{R}$ je definována na intervalu $(a, b)$.
1. Říkáme, že $f$ je spojitá na $(a, b)$, je-li spojitá v každém bodě tohoto intervalu.
2. Říkáme, že $f$ je spojitá na $\langle a, b \rangle$, je-li spojitá na $(a, b)$, v bodě $a$ je spojitá zprava a v bodě $b$ je spojitá zleva.
#### O omezenosti a minimu (Weierstrassova věta)
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
>[!tip] Bolzanova věta
>- Nechť $f : \mathbb{R} \to \mathbb{R}$ je spojitá na uzavřeném intervalu $\langle a, b \rangle$ taková, že $f(a) \cdot f(b) < 0$. Pak existuje $c \in \mathbb{R}$ takové, že $c \in (a, b)$ a $f(c) = 0$.
>> -  její graf v alespoň jednom vnitřním bodě tohoto intervalu protíná osu x
> - Jedná se o postačující podmínku, který je přímým důsledkem **Bolzano-Weierstrassovy** věty
	>> - zajišťuje nám existenci nulového bodu
	>> - nulový bod lze nalézt **metodou půlení intervalu**
> ![[Pasted image 20240628134849.png]]

#### O hodnotách spojité funkce
  - Funkce $f$ je spojitá na uzavřeném intervalu $\langle a, b \rangle$ a v $(a, b)$ nemá žádné nulové body, pak na $(a, b)$ je buď $f(x) > 0$ nebo $f(x) < 0$ pro všechny $x \in (a, b)$.
#### O spojitosti inverzní funkce
- Funkce $f$ je spojitá a ryze monotónní na intervalu $I$. Pak $f^{-1}$ je také spojitá.
## Jednostranná spojitost a body nespojitosti
- Mějme funkci $f : A \to \mathbb{R}$. 
- Jestliže v jistém levém, resp. pravém okolí bodu $a$ není funkce $f$ definována, pak mluvíme o jednostranné spojitosti v bodě $a$ zprava, resp. zleva.
- Např. funkce $f : y = \sqrt{x}$ jde v bodě 0 o spojitost zprava (funkce není definována pro $x < 0$). 
- Pojem jednostranné spojitosti však zavádíme i v případě, že máme definováno okolí bodu $a$ zprava i zleva.
#### Jednostranná spojitost
Říkáme, že funkce $f : A \to \mathbb{R}$ je spojitá zprava (zleva) v bodě $a \in A$, jestliže platí:
- $\lim_{x \to a^+} f(x) = f(a)$
- resp. $\lim_{x \to a^-} f(x) = f(a)$
#### Body nespojitosti
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
