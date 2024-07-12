
## Určitý integrál
- Existuje několik definic určitého integrálu:
	- Cauchyův
	- Newtonův,
	- **Riemannův** (nejčastější) - zobecnění Cachyuova integrálu,
	- Lebesgueův...
- Definice se liší množinou funkcí, pro které platí
- Na rozdíl od neurčitého integrálu, kde výsledkem je množina primitivních funkcí, je výsledkem určitého integrálu **číslo**, které můžeme interpretovat jako obsah plochy pod křivkou grafu funkce $f$ na intervalu $\langle a, b \rangle$ 
	- určitý integrál uvažujeme na uzavřeném intervalu, na níž je funkce $f$ omezena
	- říkáme **určitý integrál $f$ od $a$ do $b$**
- Využití pro výpočet:
	- obsahu plochy pod křivkou grafu (rovinného útvaru),
	- délky křivek,
	- objemy rotačních těles, pláště těles,...
	- jiné aplikace ve fyzice, chemii

>[!Tip] Poznámka
> **Idea výpočtu** obsahu plochy pro vymezený úsek grafu:
> -  Úsek grafu rozdělíme na $n$ podintervalů stejné délky
> 	- (obecně stejné délky mít nemusí)
> -  Pro každý interval můžeme uvažovat obdélník, jehož základna je dána dělením a výška je dána některou funkční hodnotou na daném podintervalu
> 	- např. lokální maximum/minimum
> - Odhad (aproximace) obsahu celé plochy spočítáme jako součet obsahů ploch jednotlivých obdélníků
> - Je přitom zřejmé že, pokud vezmeme jako výšky jednotlivých obdélníků lokální maxima/minima, je tento odhad nepřesný
> 	- Přesnější odhad získáme jemnějším rozdělením na více podintervalů (užších obdélníků)

## Dělení intervalu
- Mějme uzavřený interval $\langle a, b \rangle$, dělením tohoto intervalu pak rozumíme konečnou množinu bodů $D = \{x_0, x_1,..., x_{n}\}$, která splňuje $a = x_1 < x_2 < ... < x_{n} =b$ 
	- prvky množiny $D$ nazýváme **dělící body intervalu** $\langle a, b \rangle$ 
	- interval $\langle x_{i-1}, x_{i}\rangle$, $i \in \{1, 2, ..., n\}$ nazýváme *i-tý interval dělení* 
- Množina $D^{'}$ nazýváme **zjemnění dělení** $D$, je-li $D \subset D^{'}$  
	- každý dělící bod dělení $D$ je tak dělícím bodem dělení $D^{'}$

## Horní a dolní součet
- Nechť funkce $f$ je omezená na intervalu $\langle a, b \rangle$ a množina $D$ je dělení intervalu $\langle a, b \rangle$
- **Horní součet funkce $f$** vzhledem k intervalu dělení $D$ je číslo $$\overline S(f, D) = \sum_{i=1}^{n} M_i(x_{i}-x_{i-1})$$ kde
$$M_i = \sup \{ f(x) \mid x_{i-1} \leq x \leq x_i \}$$
- s rostoucím se $n$ se horní součet funkce $f$ zmenšuje


- **Dolní součet funkce $f$** vzhledem k intervalu dělení $D$ je číslo
$$
\underline S(f,D) = \sum_{i=1}^n m_i (x_i - x_{i-1}),
$$
kde
$$
m_i = \inf \{ f(x) \mid x_{i-1} \leq x \leq x_i \}.
$$
- s rostoucím se $n$ se dolní součet funkce $f$ zvětšuje 

![[Pasted image 20240704120120.png]]

- Je zřejmé, že $\underline S(f,D) \leq S(f,D) \leq \overline S(f,D)$
	- kde $S(f, D)$ je skutečný obsah plochy pod grafem
- Zjemňováním dělení $D$ tak, že $n \to \infty$, dojde u horního součtu ke zmenšování, u dolního součtu ke zvětšování
	- v obou případech se součty přiblíží k $S(f, D)$ (splynou v jednu hodnotu)
- $\lim_{n\to \infty} \sum_{i=1}^{n}m_i(x_i-x_{i-1}) = S(f,D) = lim_{n\to \infty} \sum_{i=1}^{n} M_i(x_i-x_{i-1})$    
- Této společné hodnotě $S(f, D)$, jestliže existuje, říkáme **Riemannův integrál funkce $f$ od $a$ do $b$**

## Horní a dolní integrál funkce
- Existuje mnoho dělení intervalů na množině $\langle a, b \rangle$ a můžeme uvažovat množinu všech horních součtů vzhledem k příslušným dělením  $$U = \{ \overline{S}(f,D) \mid D \text{ je dělení } \langle a, b \rangle \}$$
- Zřejmě platí
$$\overline{S}(f,D) \geq m \sum_{i=1}^{n} (x_i - x_{i-1}) = m(b - a),$$
- $m$ je dolní závora funkce $f$ omezené na $\langle a, b \rangle$
	-  minimum z funkčních hodnot na intervalu
- To znamená, že množina horních součtů je zdola omezená a existuje největší dolní mez těchto součtů. Číslo
$$\overline{S} = \inf U$$
budeme nazývat *horní Riemannův integrál funkce $f$*. 
 

- Dále můžeme podobně uvažovat množinu všech dolních součtů vzhledem k příslušným
dělením intervalu $\langle a, b \rangle$, kterou označíme
$$L = \{ \underline{S}(f,D) \mid D \text{ je dělení } \langle a, b \rangle \}$$
- Zřejmě platí
$$\underline{S}(f,D) \leq M \sum_{i=1}^{n} (x_i - x_{i-1}) = M(b - a),$$
- $M$ je nějaká horní závora omezené funkce $f$ na $\langle a, b \rangle$.
	- maximum z funkčních hodnot na intervalu
- To znamená, že množina dolních součtů je shora omezená a existuje nejmenší horní
mez těchto součtů. Číslo
$$\underline{S} = \sup L$$
budeme nazývat dolní Riemannův integrál funkce $f$.

### Riemannův integrál
- Říkáme, že $f : \mathbb{R} \to \mathbb{R}$ definovaná a **omezená** na intervalu $\langle a, b \rangle$ je *Riemannovsky integrovatelná* na $\langle a, b \rangle$ právě tehdy, když
$$\overline{S} = \underline{S}$$
	- horní a dolní Riemannovy integrály funkce $f$ jsou si rovny (dolní mez horních součtů a horní mez dolních součtů jsou si rovny)
- Krátce to budeme zapisovat jako $f(x) \in \mathcal{R}(a, b)$
- Společná hodnota se pak nazývá **Riemannův integrál** a značí se
$$(R) \int_{a}^{b} f(x) \, dx,$$
což budeme jednoduše zkracovat jako
$$\int_{a}^{b} f(x) \, dx,$$
- číslo $a$ je nazývá dolní mez, $b$ pak horní mez (jedná se *integrační meze*)

### Věty
-  První věty jsou zjevné z toho, že zjemňováním se horní součet zmenšuje, dolní se naopak zvětšuje
- Horní součty jsou omezeny zdola a dolní shora, tyto meze jsou přitom rovny

1. Nechť $f : \mathbb{R} \to \mathbb{R}$ je omezená na $\langle a, b \rangle$ a $D_0$ je zjemnění
dělení $D$ daného intervalu, pak
$$\underline{S}(f,D) \leq \underline{S}(f,D_0) \leq \overline{S}(f,D_0) \leq \overline{S}(f,D).$$
	
2. Je-li $f : \mathbb{R} \to \mathbb{R}$ omezená na $\langle a, b \rangle$ a jsou-li $D_1$ a $D_2$ libovolná
dělení intervalu $\langle a, b \rangle$ platí
$$\underline{S}(f,D_1) \leq \overline{S}(f,D_2).$$
	
3. Je-li $f : \mathbb{R} \to \mathbb{R}$ definovaná a omezená na $\langle a, b \rangle$, pak $\underline{S} \leq \overline{S}$.

4. Nechť $f : \mathbb{R} \to \mathbb{R}$ je definovaná a omezená na $\langle a, b \rangle$. Pak $f \in \mathcal{R}(a, b)$ právě tehdy, když pro libovolné $\epsilon > 0$ existuje dělení $D_\epsilon$ intervalu $\langle a, b \rangle$ takové, že
$$\overline{S}(f,D_\epsilon) - \underline{S}(f,D_\epsilon) < \epsilon.$$
	- pro každé kladné reálné číslo $\epsilon$ existuje takové dělení intervalu, že rozdíl příslušných horních a dolních součtů je $<$  $\epsilon$

5. Je-li $f$ monotónní na $\langle a, b \rangle$, pak $f \in \mathcal{R}(a, b)$.

### Stejnoměrná spojitost
- Funkce $f$ definovaná na $\langle a, b \rangle$ je stejnoměrně spojitá, jestliže
$$\forall \epsilon > 0 \; \exists \delta > 0 \; \forall x, y \in \langle a, b \rangle : (|x - y| < \delta ) \implies |f(x) - f(y)| < \epsilon).$$

6. Nechť $f$ je definovaná a spojitá na $\langle a, b \rangle$. Pak $f$ je na $\langle a, b \rangle$ stejnoměrně spojitá.

7. Nechť $f$ je spojitá na $\langle a, b \rangle$. Pak $f \in \mathcal{R}(a, b)$.
	- Funkce $f$ je integrovatelná na uzavřených spojitých intervalech
	- Některé funkce s konečným počtem skokových nespojitostí však integrovatelné jsou 
	- Výjimkou jsou ale např. Dirichletovy funkce, které bodů nespojitostí mají příliš mnoho

### Vlastnosti Riemannova integrálu
- Nechť $f, g \in \mathcal{R}(a, b)$, pak
1. $$\int_{a}^{b} [\alpha f(x) + \beta g(x)]dx = \alpha \int_{a}^{b} f(x)dx + \beta \int_{a}^{b} g(x)dx,$$
2. $$\int_{a}^{b} f(x)dx = \int_{a}^{c} f(x)dx + \int_{c}^{b} f(x)dx, \quad a \leq c \leq b,$$
3. je-li $f(x) \leq g(x)$ pro $\forall{x} \in \langle a, b \rangle$, pak $$\int_{a}^{b} f(x)dx \leq \int_{a}^{b} g(x)dx,$$
4. $$\left| \int_{a}^{b} f(x)dx \right| \leq \int_{a}^{b} |f(x)|dx.$$
5. $$\int_{a}^{b}f(x) = -\int_{b}^{a}f(x)$$

>[!Tip] Poznámka
> - Nechť $f \in \mathcal{R}(a, b)$ a $x \in \langle a, b \rangle$, pak podle části (2) předchozí věty je také $f \in \mathcal{R}(a, x)$ a předpisem $$F(x) = \int_{a}^{x} f(t)dt$$
> - je na intervalu $\langle a, b \rangle$ definována funkce. Položíme ještě $$F(a) = \int_{a}^{a} f(t)dt = 0.$$
> - Nechť $f \in \mathcal{R}(a, b)$ a $F(x) = \int_{a}^{x} f(t)dt$, pak $F$ je spojitá na $\langle a, b \rangle$.
> - Nechť $f$ je spojitá na $\langle a, b \rangle$, pak $F(x) = \int_{a}^{x} f(t)dt$, je diferencovatelná na $\langle a, b \rangle$, a platí $F' = f$.
> 	- $F$ je tedy primitivní k $f$.



### Newton-Leibnizova formule
- Následující věta umožňuje snadný způsob výpočtu určitého integrálu:
- Nechť $f$ je spojitá na $\langle a, b \rangle$ a $F$ je libovolná primitivní funkce k $f$ na tomto intervalu, pak
$$\int_{a}^{b} f(x)dx = F(b) - F(a).$$
- Integrál funkce $f$ na intervalu $\langle a, b \rangle$ je rovno rozdílu:
	- $F(b)$ - funkční hodnota primitivní funkce v $b$
	- $F(a)$ - funkční hodnota primitivní funkce v $a$ 
- Pro výpočet určitého integrálu tedy stačí vypočítat primitivní funkci podobně jako neurčitého integrálu
	- + dosadit koncové body $a$ a $b$
	- + provést rozdíl pravého od levého
- Formule lze dokázat pomocí Lagrangeovy věty o střední hodnotě spojitých funkcí

### Metody výpočtu
- Analogické jako u výpočtu neurčitého integrálu
#### Metoda per-partes
- Nechť $F$ a $G$ jsou spojitě diferencovatelné funkce na $\langle a, b \rangle$, pak
$$\int_{a}^{b} F(x)g(x)dx = \left[ F(x)G(x) \right]_{a}^{b} - \int_{a}^{b} f(x)G(x)dx.$$
#### Metoda substituce
- Nechť $f$ je spojitá na $\langle a, b \rangle$ a $g$ spojitě diferencovatelná na $\langle \beta, \gamma \rangle$. Pak
	$$\int_{a}^{b} f(x)dx = \int_{\beta}^{\gamma} (f \circ g)(t) g'(t)dt,$$kde $g(\beta) = a$ a $g(\gamma) = b$.
- Při substituci je třeba pamatovat na to, že při zavedení nové proměnné, je nutné změnit příslušně i integrační meze


navíc...
### Po částech spojitá funkce
- Funkce $f$ se nazývá po částech spojitá na $\langle a, b \rangle$, jestliže existuje dělení $D = \{x_0, x_1, \ldots, x_n\}$ intervalu $\langle a, b \rangle$ a spojité funkce $f_i$ definované na $\langle x_{i-1}, x_i \rangle$ taková, že $f(x) = f_i(x)$ pro $x \in \langle x_{i-1}, x_i \rangle$, $i = 1, 2, \ldots, n$.

### Nevlastní integrál 1. druhu
- Nechť je funkce $f$ omezená na $\langle a, \infty \rangle$ a $R$-integrovatelná pro libovolné $b > a$. Jestliže existuje vlastní
$$\lim_{b \to \infty} \int_{a}^{b} f(x)dx$$
říkáme, že $\int_{a}^{\infty} f(x)dx$ konverguje. V opačném případě říkáme, že daný integrál diverguje.

### Nevlastní integrál 2. druhu
- Nechť $f$ je definována na $\langle a, b \rangle$ a je $R$-integrovatelná na $\langle a + \epsilon, b \rangle$ pro $0 < \epsilon < b - a$. 
- Jestliže existuje
$$\lim_{\epsilon \to 0^+} \int_{a + \epsilon}^{b} f(x)dx$$
říkáme, že $\int_{a}^{b} f(x)dx$ konverguje.
