## Pravděpodobnost
- zabývá se určováním **pravděpodobností** náhodných jevů
- pravděpodobnost řeší problémy typu:
	- Jaká je pravděpodobnost, že při hodu kostkou padne číslo $4$?
	- Jaká je pravděpodobnost, že při hodu kostkou padne sudé číslo?
- Teorie pravděpodobnosti vznikla spolu s kombinatorikou při **analýze hazardních her**.
- Pravděpodobnost a statistika nás učí, jak **kvantitativně vyhodnocovat data**.
	- Na pravděpodobnosti je založen pojem **složitost algoritmu v průměrném případě**

### Klasická definice pravděpodobnosti (Laplaceova)
- Nechť $\Omega$ je konečný vzorový prosto a všechny elementární jevy v $\Omega$ jsou stejně pravděpodobné. Pro libovolnou událost $A \subseteq \Omega$, pravděpodobnost $P(A)$ je definována: $$P(A) = \frac{počet\ příznivých\ výsledků\ pro\ A}{celkový\ počet\ možných\ výsledků}$$kde **počet příznivých výsledků** pro $A$ je počet prvků v množině $A$ a **celkový počet možných výsledků** je počet všech prvků ve vzorovém prostoru $\Omega$.


## Kolmogorova definice pravděpodobnosti
- Je dán **náhodný pokus**:
	- hod kostkou
	- výběr člověka z populace ČR
- K pokusu patří **množina $\Omega$ možných** výsledků, tzv. **elementárních jevů**
	- hod kostkou: $\Omega = \set{1,2,3,4,5,6}$
	- výběr člověka: $\Omega = \set{\text{člověk }1, ..., \text{člověk }10^{7}}$
- Určujeme **pravděpodobnost** tzv. **jevů**
	- Hod kostkou: jev "sudé číslo" $= \set{2,4,6}$
	- Výběr člověka: jev "žena" $= \set{\text{člověk } c \text{ v ČR } | c \text{ je žena}}$
- $\mathcal{A}$ = množina měřitelných jevů
- pravděpodobnost, přesněji **pravděpodobnostní míra**, je funkce $P: \mathcal{A} \rightarrow [0,1]$ splňující jisté vlastnosti

- Základním pojmem v Kolmogorově přístupu je pojem **pravděpodobnostní prostor**:

### Pravděpodobnostní prostor
- Pravděpodobnostní prostor je trojice $<\Omega, \mathcal{A}, P>$, kde
	- $\Omega$ je neprázdná množina elementárních jevů (výsledků pokusu)
	- $\mathcal{A} \subseteq 2^{\Omega}$ je množina jevů
	- $P: \mathcal{A} \rightarrow [0,1]$ je pravděpodobnostní míra pro jev $A \in \mathcal{A}$ je $P(A) \in [0, 1]$ pravděpodobnost, že nastane jev $A$
---
- Pravděpodobnostní prostor je trojice $<\Omega, \mathcal{A}, P>$, kde:
	- $<\Omega, \mathcal{A}>$ je $\sigma$-algebra (sigma) na $\Omega$, tj. $\Omega \neq \varnothing,$ $\varnothing \neq \mathcal{A} \subseteq 2^{\Omega}$ a platí:
		- je-li $A \in \mathcal{A}$, pak $\overline{A} \in \mathcal{A}$
		- jsou-li $A_{1}, A_{2}, ... \in \mathcal{A}$, pak $\bigcup_{i = 1}^{\infty}\ A_{i} \in \mathcal{A}$
	- $P$ je pravděpodobnostní míra, tj. $P$ je zobrazení přiřazující každé množině $A \in \mathcal{A}$ reálné číslo $P(A)$, které splňuje:
		- $P(A) \geq 0$ pro každý $A \in \mathcal{A}$
		- $P(\Omega) = 1$
		- $P(\cup_{i=1}^{\infty}\ A_{i}) = \sum_{i=1}^{\infty} P(A_{i})$ pro každou posloupnost jevů $A_{1}, A_{2}, ...,$ které jsou po dvou disjunktní, tj. $A_{i}\ \cap A_{j} = \varnothing$ pro $i \neq j$.
---
- Prvky $\omega \in \Omega$ se nazývají **elementární jevy** a představují výsledky náhodného pokusu.
- **Množiny $A \in \mathcal{A}$** se nazývají **jevy**, někdy také **měřitelné jevy**, a jsou to podmnožiny množiny $\Omega$, ale ne každá podmnožina množiny $\Omega$ musí být jevem.
- Jev je tedy množina $A$ sestávající z nějakých výsledků pokusu, o nichž říkáme, že jsou jevy $A$ příznivé.
- Pro **jev $A$ se číslo $P(A)$** nazývá **pravděpodobnost jevu** $A$.
- Pravděpodobnostní prostor se nazývá **diskrétní,** pokud je množina $\Omega$ konečná a nebo spočetná.
> [!Summary] Zjednodušeně
> - Pravděpodobnostní prostor se skládá ze tří hlavních komponent: 
> 	- vzorového prostoru, 
> 	- σ-algebry,
> 	- pravděpodobnostní míry.
> ---
> - **Vzorový prostor**, označovaný jako $\Omega$, je množina všech možných výsledků náhodného experimentu. 
> 	- Při hodu kostkou by vzorový prostor byl $\Omega = \set{1,2,3,4,5,6}$
> - $\sigma$-algebra nad vzorovým prostorem $\Omega$ je kolekce podmnožin $\Omega$ které jsou považovány za **měřitelné**.
> 	- Musí splňovat: 
> 		1. Obsahuje $\varnothing$
> 		2. Je uzavřená na doplňky (pokud množina $A$ je v $\sigma$-algebře, pak její doplněk je taky).
> 		3. Je uzavřená na spočetné sjednocení
> 			- Pokud $A_{1}, A_{2}, ...$ jsou v $\sigma$-algebře, pak $\cup_{i = 1}^{\infty}\ A_{i}$ je také v $\sigma$-algebře.
> - **Pravděpodobnostní míra**, označena jako $P$, je funkce, která přiřazuje číslo mezi $0$ a $1$ každé měřitelné množině v $\sigma$-algebře. Reprezentuje pravděpodobnost, že nastane daný jev repzerentovaný touto množinou. 
> 	- Musí splňovat:
> 		1. **Nezápornost**: $P(A) \geq 0$ pro všechna $A$ v $\sigma$-algebře.
> 		2. **Normalita**: $P(\Omega) = 1$
> 		3. $\sigma$-**aditivita**: Pro jakoukoli sekvenci vzájemně disjunktních množin $A_{1}, A_{2}, ...$ v $\sigma$-algebře platí, že $P(\cup_{i=1}^{\infty}\ A_{i}) = \sum_{i=1}^{\infty} P(A_{i})$


## Náhodná veličina, střední hodnota

### Náhodná veličina
- Představme si, že náhodný pokus spočívá v náhodném výběru muže v České Republice.
- Označíme-li $\Omega = \set{\omega_{1},...,\omega_{k}}$ množinu všech můžu v ČR, lze tento výběr popsat **pravděpodobnostním prostorem**, ve kterém množinou elementárních jevů je $\Omega$ a pravděpodobnost výběru každého muže $\omega_{i}$ je $P(\set{\omega_{i}}) = 1/k$.
- V této situaci nás může zajímat například **výška mužů**. Výšku mužů lze chápat jako funkci $X: \Omega \rightarrow \mathbb{R}$, která muži $\omega \in \Omega$ přiřadí jeho výšku $X(\omega)$.
	- např. $X(\omega) = 182$
- Výška mužů se tedy v tomto pohledu jeví jako **náhodná veličina**
	- výška je náhodná, protože je tento muž vybrán náhodně.
---
- **Náhodná veličina** na konečném nebo diskrétním pravděpodobnostním prostoru $<\Omega, 2^{\Omega}, P>$ je funkce $X: \Omega \rightarrow \mathbb{R}$.

### Střední hodnota náhodné veličiny
- Střední hodnota (také očekávaná hodnota) náhodné veličiny $X$ se značí $E(X)$ a je definována následovně: $$E(X)=\sum_{x \in X(\Omega)} x\ \cdot P(X = x)$$
- $E(X)$ vyjadřuje, s přihlédnutím k pravděpodobnosti hodnot, očekávanou hodnotu výsledku.
- $E(X)$ nemusí být rovna žádné z hodnot, které $X$ nabývá.

### Rozptyl a směrodatná odchylka náhodné veličiny
- Střední hodnota náhodné veličiny nám dává užitečnou, ale jen omezenou informaci. To platí i pro průměrnou hodnotu, která je speciálním případem střední hodnoty: *Jeden člověk sní celé kuře, druhý nic: v průměru měl každý půl kuřete*
- Vidíme tedy, že průměr poskytují jen omezenou informaci o veličině $X$. Hodnoty $X$ mohou být kolem střední hodnoty $E(X)$ různě **rozptýleny**. K vyjádření toho, jak moc jsou rozptýleny, slouží tzv. rozptyl

- **Rozptyl $var\ X$** náhodné veličiny $X$ je definován vztahem $var\ X=E((X-E(X))^{2})$.
- Směrodatná odchylka $\sigma$ náhodné veličiny $X$ je druhá odmocnina rozptylu, tj. $\sigma =  \sqrt{var\ X}$.
- $var\ X$ vyjadřuje, jak moc jsou hodnoty $X$ rozptýleny kolem $E(X)$. Čím je větší, tím jsou více rozptýleny.


> [!note] Kvantil a Modus
> **Kvantil** je míra polohy rozdělení pravděpodobnosti náhodné veličiny. Medián je 0.5-kvantil.
> **Modus** je, zhruba řečeno, nejčastější hodnota náhodné veličiny

##### Navigace. 
Předchozí:  [[Permutace, variace, kombinace]]
Následující: [[Inducke a rekurze, matematická indukce a její varianty]]
Celý okruh: [[1. Teoretické základy informačních technologií]]