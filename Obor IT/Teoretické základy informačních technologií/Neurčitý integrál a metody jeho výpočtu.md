## Primitivní funkce

- Nechť je $f: \mathbb{R} \rightarrow \mathbb{R}$ definována na intervalu $I$ libovolného druhu.
- Potom máme funkci $F: \mathbb{R} \rightarrow \mathbb{R}$ takovou, že $\forall{x} \in I$ platí $F'(x)=f(x)$
	 - *pokud zderivuji funkci $F$ dostanu funkci $f$
	 -  $F$ nazýváme **primitivní funkcí k $f$ na $I$*

### O primitivní funkci
1. Nechť $F$ je primitivní funkce k $f$ na $I$. Pak také funkce $G$ definovaná předpisem $G(x) = F(x) + c$, $x \in I$, $c \in \mathbb{R}$ je primitivní funkcí k $f$ na $I$.
2. Nechť $F$ a $G$ jsou primitivní funkce k funkci $f$ na $I$, pak funkce $F - G$, $x \in I$ je konstantní.

- Tato nejednoznačnost primitivní funkce k $f$ vede k definici neurčitého integrálu

## Neurčitý integrál funkce $f$ na $I$
- Nechť existuje alespoň jedna primitivní funkce $F$ k funkci $f$ na intervalu $I$.
- Množinu všech primitivních funkcí k funkci $f$ na $I$ pak nazýváme **neurčitý integrál funkce $f$ na $I$** a značíme jej $$\int{f(x)dx}=\{F(x) +c\ |\ c \in \mathbb{R}\}.$$
- Primitivních funkcí $F(x)$ k funkci $f$ je nekonečně mnoho a liší se pouze konstantou $c$
	- jde o tzv. *integrační konstantu
	- to je dáno tím, že při derivaci funkce $F$ se vyloučí veškeré konstanty
- Po integraci funkce $f$ na $F$ je vhodné tuto konstantu pro úplnost doplnit
	- (po získání primitivní funkce k $f$ - *opačná operace k derivaci*)
- Značení:
	- $\int$ - značení integrálu
	- $f(x)$ - integrovaná funkce (integrand)
	- $dx$  - proměnná podle které integrujeme (integrační proměnná)
	- $F(x)$ -  primitivní funkce
	- $c$ - integrační konstanta

>[!Example]- Isibalo - Co nám říká neurčitý integrál
><iframe width="660" height="385" src="https://www.youtube.com/embed/kC9D7iy_16U?si=Lrb78mJEXKhkfTHr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### O existenci primitivní funkce
- Nechť $f : \mathbb{R} \to \mathbb{R}$ je spojitá na intervalu $I \subseteq \mathbb{R}$ libovolného druhu, pak $f$ má na $I$ primitivní funkci.
- Funkce $f$, která není na R spojitá, nemusí mít na R primitivní funkci

### O linearitě primitivní funkce
- Nechť na $(a, b)$ existují primitivní funkce k funkcím $f_1$ a $f_2$ a nechť $k_1, k_2 \in \mathbb{R}$. Pak existuje primitivní funkce k funkci $k_1 f_1 + k_2 f_2$ a platí
$$
\int (k_1 f_1(x) + k_2 f_2(x)) \, dx = k_1 \int f_1(x) \, dx + k_2 \int f_2(x) \, dx.
$$

- Větu o linearitě lze zobecnit na tvar
$$
\int (k_1 f_1(x) + k_2 f_2(x) + \cdots + k_n f_n(x)) \, dx = k_1 \int f_1(x) \, dx + k_2 \int f_2(x) \, dx + \cdots + k_n \int f_n(x) \, dx.
$$
  
## Metody výpočtu neurčitého integrálu
- Na rozdíl od derivace, integrace žádná přesně definovaná pravidla pro počítání složitějších výrazů nemá
- K tomu se využívá různých metod
	- per-partes (typicky pro výrazy obsahující součin)
	- substituce (složené funkce)
- Typicky se snažíme převést integrovaný výraz do ekvivalentní podoby, kterou integrovat umíme

### Přímá integrace
- Převádíme integrál na primitivní funkci pomocí tabulky základních primitivních funkcí, větě o linearitě a vzorečku $\int{f(x)dx}=F(x)+c \Rightarrow [F(x)+c]' = f(x)$
	  1. jednotlivé součty ve výrazu rozdělíme na samostatné integrály
	  2. vytkneme konstanty před integrály
	  3. jednotlivé integrály spočítáme podle pravidel pro primitivní funkce (dle tabulky níže)
		  -  pro složitější výrazy je nutné využít substituce, per partes apod.

![[MacBook-2024-05-21-001282.png| 600]]

  

### Metoda per partes ("po částech")
- Nechť funkce $f, g : \mathbb{R} \to \mathbb{R}$ jsou definovány na $(a, b)$ a nechť $F' = f$ a $G' = g$ na $(a, b)$.
- Nechť dále existuje $\int f(x)G(x) \, dx$ na $(a, b)$. Pak také existuje $\int F(x)g(x) \, dx$ na $(a, b)$ a platí
$$
\int F(x)g(x) \, dx = F(x)G(x) - \int f(x)G(x) \, dx.
$$
- Tvrzení věty si budeme lépe pamatovat ve tvaru
$$
\int F G' = F G - \int F' G.
$$
- Možná čitelnější zápis: $$\int u v' = u v - \int u' v.$$
- Odvozeno z pravidla pro derivaci součinu funkcí
	  - $(uv)^{'} = u^{'}v + uv^{'}$ - obě strany zintegrujeme
	  - $uv = \int u^{'}v + \int uv^{'}$  
	  - tedy $\int u^{'}v = uv - \int uv^{'}$ nebo  $\int uv^{'} = uv - \int u^{'}v$
- Tato metoda je vhodná, když je jedna funkce v součinu snadno diferencovatelná a druhá integrovatelná

>[!Example]- Isibalo - Metoda per partes
><iframe width="660" height="385" src="https://www.youtube.com/embed/gZvICMtNbeQ?si=rVZruKSuiIALJ36j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

  
### Substituční metoda
- Převádíme složenou funkci, kterou neumíme integrovat do jednoduššího tvaru tak, aby šla integrovat přímo
- Volba vhodné substituce není snadná a vyžaduje nějakou zkušenost

>[!Example]- Isibalo - Substituční metoda
><iframe width="660" height="385" src="https://www.youtube.com/embed/Qx_NnL2iSGM?si=Bbrt-ChkMwX4s4q3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### První věta o substituci
1. Nechť funkce $t = \varphi(x)$ zobrazuje interval $(a, b)$ do intervalu $(\beta, \gamma)$ a nechť na $(a, b)$ existuje vlastní $\varphi'$.
2. Nechť funkce $f$ má na intervalu $(\beta, \gamma)$ primitivní funkci $F$, tj. platí $F(t) = \int f(t) \, dt$, $t \in (\beta, \gamma)$. Pak na $(a, b)$ existuje primitivní funkce k funkci $(f \circ \varphi) \varphi'$ a platí
$$
\int (f \circ \varphi)(x) \varphi'(x) \, dx = (F \circ \varphi)(x), \, x \in (a, b)
$$
neboli

$$
\int f(\varphi(x)) \varphi'(x) \, dx = F(\varphi(x)).
$$

  

- Postup výpočtu neurčitého integrálu pomocí první věty o substituci:
1. Hledáme integrál tvaru $\int f(\varphi(x)) \varphi'(x) \, dx$.
2. Pokud funkce $f$ a $\varphi$ splňují podmínky první věty o substituci, pak:
    a) Položíme $\varphi(x) = t$, $x \in (a, b)$, $t \in (\beta, \gamma)$.
       $\varphi'(x) \, dx = dt$.
    b) Vypočítáme integrál $\int f(t) \, dt = F(t)$, $t \in (\beta, \gamma)$
	- doufáme, že je výraz jednodušší než původní integrál v zadání a umíme ho spočítat
1. Vrátíme se k proměnné $x$ a hledaný neurčitý integrál má tvar $F(\varphi(x))$, $x \in (a, b)$.

- Stručněji: 
$$\int f(\varphi(x)) \cdot \varphi'(x) dx = \left| \begin{array}{c} \varphi(x) = t \\ \varphi'(x) dx = dt \end{array} \right| = \int f(t) dt.$$

#### Druhá věta o substituci
1. Nechť funkce $x = \varphi(t)$ zobrazuje interval $(\beta, \gamma)$ na interval $(a, b)$ a nechť na $(\beta, \gamma)$ existuje vlastní $\varphi' > 0$ (nebo $\varphi' < 0$).
2. Nechť $G$ je primitivní funkce k funkci $(f \circ \varphi) \varphi'$ na intervalu $(\beta, \gamma)$, tj. platí $G(t) = \int (f \circ \varphi)(t) \varphi'(t) \, dt$, $t \in (\beta, \gamma)$. Pak na $(a, b)$ existuje primitivní funkce k funkci $f$ a platí
$$\int f(x) \, dx = (G \circ \varphi^{-1})(x), \, x \in (a, b)$$
neboli
$$\int f(x) \, dx = G(\varphi^{-1}(x)).$$
- Postup výpočtu neurčitého integrálu pomocí druhé věty o substituci:
1. Hledáme integrál tvaru
$$\int f(x) \, dx.$$
2. Zvolíme nějakou vhodnou funkci $\varphi$ a pokud funkce $f$ a $\varphi$ splňují podmínky druhé věty o substituci, pak
   a) položíme $x = \varphi(t)$, $t \in (\beta, \gamma)$, $x \in (a, b)$,
$$dx = \varphi'(t) \, dt,$$
   b) vypočítáme integrál
$$\int f(\varphi(t)) \varphi'(t) \, dt = G(t), \quad t \in (\beta, \gamma)$$
   - opět doufáme, že nový výraz je jednodušší než původní integrál v zadání a umíme ho spočítat
3. Vrátíme se k proměnné $x$ a hledaný neurčitý integrál má tvar
$$G(\varphi^{-1}(x)), \quad x \in (a, b).$$
Stručněji:
$$\int f(x) dx = \left| \begin{array}{c} x = \varphi(t) \\ dx = \varphi'(t) dt \end{array} \right| = \int f(\varphi(t)) \cdot \varphi'(t) dt.$$

### Integrace racionálních funkcí
- Je třeba umět integrovat následující čtyři typy zlomků:
1. $\frac{A}{x - a}$,
2. $\frac{A}{(x - a)^k}$,
3. $\frac{Ax + B}{x^2 + px + q}$,
4. $\frac{Ax + B}{(x^2 + px + q)^k}$,

kde $A, B, a, p, q \in \mathbb{R}$, $k \in \mathbb{N}$ a $p^2 - 4q < 0$. 

- Výpočet jednotlivých případů:
1.
$$\int \frac{A}{x - a} dx = \left| x - a = t \atop dx = dt \right| = A \int \frac{1}{t} dt = A \ln |t| + c = A \ln |x - a| + c.$$

2. pro $k > 1$ pak
$$\int \frac{A}{(x - a)^k} dx = \left| x - a = t \atop dx = dt \right| = A \int \frac{1}{t^k} dt = \frac{A}{(1 - k)t^{1 - k}} + c = \frac{A}{(1 - k)(x - a)^{1 - k}} + c.$$

3. Je-li $A = 2$ a $B = p$ (čitatel je tak derivací jmenovatele), pak máme obecně
$$\int \frac{Ax + B}{x^2 + px + q} dx = \int \frac{2x + p}{x^2 + px + q} dx = \left| x^2 + px + q = t \atop (2x + p) dx = dt \right| = \int \frac{1}{t} dt = \ln |t| + c = \ln |x^2 + px + q| + c.$$

- Pokud máme obecně $x^2 + px + q$ a $p^2 - 4q < 0$, pak $$ x^2 + px + q = \left( x + \frac{p}{2} \right)^2 - \frac{p^2}{4} + q = \left( x + \frac{p}{2} \right)^2 + \left( q - \frac{p^2}{4} \right) = \left( q - \frac{p^2}{4} \right) \left( \left( \frac{x + \frac{p}{2}}{\sqrt{q - \frac{p^2}{4}}} \right)^2 + 1 \right). $$
  - Potom je
$$\int \frac{1}{x^2 + px + q} dx = \int \frac{1}{(q - \frac{p^2}{4}) \left( \left( \frac{x + \frac{p}{2}}{\sqrt{q - \frac{p^2}{4}}} \right)^2 + 1 \right)} dx = \left| \frac{x + \frac{p}{2}}{\sqrt{q - \frac{p^2}{4}}} = t \atop dx = \frac{1}{\sqrt{q - \frac{p^2}{4}}} dt \right|$$
$$= \frac{1}{\sqrt{q - \frac{p^2}{4}}} \int \frac{1}{t^2 + 1} dt = \frac{1}{\sqrt{q - \frac{p^2}{4}}} \arctan{t + c} = \frac{1}{\sqrt{q - \frac{p^2}{4}}} \arctan \frac{x + \frac{p}{2}}{\sqrt{q - \frac{p^2}{4}}} + c.$$

- Nakonec vyřešíme nejobecnější případ třetího typu zlomku. Při výpočtu tohoto integrálu použijeme to, co již známe ze speciálních tvarů v předchozích dvou příkladech.
- Obecně vypadá úprava a postup takto:
$$\int \frac{Ax + B}{x^2 + px + q} dx = \frac{A}{2} \int \frac{2x + \frac{2B}{A} + p - p}{x^2 + px + q} dx =$$
$$= \frac{A}{2} \int \frac{2x + p}{x^2 + px + q} dx + \left( B - \frac{pA}{2} \right) \int \frac{1}{x^2 + px + q} dx.$$

- Tyto integrály jsme však postupně vyřešili výše.

4. Pomocí substituce

##### Navigace

Předchozí: [[Průběh funkce - základní věty diferenciálního počtu, extrémy funkce, konvexní a konkávní křivky, asymptoty]]
Následující: [[Riemannův určitý integrál - definice, základní věta integrálního počtu, metody výpočtu]]
Celý okruh: [[1. Teoretické základy informačních technologií]]
