#imat1 #diferencialni-pocet #extremy-funkce #asymptoty #konkavni #konvexni #prubeh-funkce
## Geometrický význam derivace funkce
- Derivace v bodě vyjadřuje okamžitou rychlost růstu funkce v daném bodě
- Vezmeme-li obecně přírůstek hodnoty $\Delta x$ ($x_1 - x_0$) a příslušný přírůstek $\Delta y$ ($y_1 - y_0$), pak podíl $\frac{\Delta{y}}{\Delta{x}}$ je rovno průměrné rychlosti růstu v úseku  $x_0$ a $x_1$ 
	- hodnota tohoto podílu je rovna **směrnici sečny**, která protíná body $[x_0, y_0]$ a $[x_1, y_1]$
- **Derivace v daném bodě $a$** je limitní hodnota tohoto podílu, když se $\Delta x$ blíží nule. 
	- jinými slovy, derivace je  $\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}$  
	- tato hodnota zároveň vyjadřuje **směrnici tečny** v konkrétním bodě
- Dodejme, že:
	- $x_1$ = $x_0 + \Delta{x}$
	- $y_1$ = $y_0 + \Delta{y}$

- Na obrázku níže jsou znázorněny body $T$ a $S$ na grafu příslušné funkce a sečna, která tyto dva body protíná.
- ![[Pasted image 20240628174720.png]]
- Pokud bychom bod $S$ stále přibližovali k bodu $T$ (snižovali $\Delta{x}$) až by splynuly v jeden bod, vznikla by tečna, jejíž směrnice by udávala okamžitou rychlost růstu v daném bodě
- Směrnici této tečny můžeme znázornit pomocí **limity**: $$k_t = \lim_{\Delta x \to 0} k_s = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$
- ve výpočtu se často využívá substituce $x = x_0 + h$, tedy $h=x-x_0$ ($\Delta{x}$ je označen $h$,) $$k_t = \lim_{\Delta x \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$
- Tato limita díky svojí důležitosti dostala název **derivace funkce v bodě**
- Jelikož jde o směrnici tečny v daném bodě, můžeme říci, že pokud je kladná, je tečna v daném bodě rostoucí (v opačném případě klesající)
- ![[Pasted image 20240628184706.png]]
- Má-li funkce $f$ v každém bodě intervalu $(a, b)$ kladnou, resp. zápornou derivaci, je v tomto intervalu rostoucí, resp. klesající.

## Základní věty diferenciálního počtu
>[!Example]- Isibalo - Motivace přůběhu funkce
><iframe width="660" height="385" src="https://www.youtube.com/embed/5ZhAVU_qGGw?si=7nKNmnWEGsLfBiYR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


- Nyní si uvedeme několik vět, které nám pomohou jednoduše zjišťovat, na kterých intervalech je funkce rostoucí (klesající), resp. jak dohledat lokální extrémy těchto funkcí.
### Stacionární bod
- Bod $x_0$ nazýváme stacionárním bodem funkce $f$, existuje-li $f'(x_0)$ a je-li $f'(x_0) = 0$.
- Tyto body někdy označovány výstižněji jako *body podezřelé z extrémů*
	- nulová první derivace je nutnou podmínkou pro existenci extrému

### Monotónnost funkce
- Říkáme, že funkce $f : \mathbb{R} \to \mathbb{R}$ je rostoucí v bodě $a \in \mathbb{R}$ právě tehdy, když existuje $P(a) \subseteq D(f)$ takové, že
$$\forall x \in P_-(a) : f(x) < f(a) \quad \text{a} \quad \forall x \in P_+(a) : f(x) > f(a).$$
- Obdobně můžeme definovat pojmy klesající, neklesající a nerostoucí.
- $P_-(a)$, resp. $P_+(a)$ značí levé, resp. pravé prstencové okolí bodu $a$.

#### Postačující podmínka pro lokální monotonii
- Necht' $f : \mathbb{R} \to \mathbb{R}, a \in \mathbb{R}$ a existuje $f'(a) \in \mathbb{R}$. Pak
	1. je-li $f'(a) > 0$, je $f$ v $a$ rostoucí,
	2. je-li $f'(a) < 0$, je $f$ v $a$ klesající.

#### O monotonii na intervalu
- Nechť  je $f$ na intervalu $I$ spojitá a nechť v každém vnitřním bodě intervalu existuje derivace, pak platí:
1. Funkce $f$ je na intervalu $I$ rostoucí (klesající), právě když pro všechny vnitřní body $x$ je $f'(x) > 0$ ($f'(x) < 0$).
2. Funkce $f$ je na intervalu $I$ neklesající (nerostoucí), právě když pro všechny vnitřní body $x$ je $f'(x) \geq 0$ ($f'(x) \leq 0$).
3. Je-li $f'(x) = 0$ pro každý vnitřní bod intervalu $I$, je $f$ konstantní na $I$.

### Lokální extrémy funkce
- Říkáme, že funkce $f : \mathbb{R} \to \mathbb{R}$ má v bodě $a \in \mathbb{R}$
1. **ostré lokální maximum** právě tehdy, když existuje $P(a) \subseteq D(f)$ takové, že $\forall x \in P(a) : f(x) < f(a)$,
2. **ostré lokální minimum** právě tehdy, když existuje $P(a) \subseteq D(f)$ takové, že $\forall x \in P(a) : f(x) > f(a)$.
- Pokud zaměníme ostré nerovnosti za neostré, dostaneme definici pro **lokální maximum**, resp. **lokální minimum**
- Obecně mluvíme o lokálních extrémech 
- Jedná se o body, ve kterých funkce mění svojí monotonii

>[!Example]- Isibalo - Co je to monoténnost a extrémy
><iframe width="660" height="385" src="https://www.youtube.com/embed/pRPIjzGmHQw?si=-1G3i5fc_3YuiN79" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Fermatova věta - nutná podmínka pro lokální extrém
- Necht' $f : \mathbb{R} \to \mathbb{R},\ a \in \mathbb{R}$ a existuje $f'(a) \in \mathbb{R}$. Má-li funkce $f$ v bodě $a$ extrém, pak $f'(a) = 0$.
- Znaménková změna první derivace ovlivňuje monotonii funkce
- Tyto body označujeme jako **stacionární body** 
	- Výstižněji také "**body podezřelé z extrému**".

>[!Tip] Poznámka
>- Tvrzení nám sice zajišťuje podmínku, za které by mohl nastat v bodě extrém, nic nám však neříká, zda tam opravdu nastane.
>	- kladná (záporná) derivace v bodě $\implies$ funkce v bodě roste (klesá),
>	- extrém v bodě $\implies$ nulová derivace v bodě.
>- Obráceně to neplatí, což si ukážeme na příkladu.
>- Uvažujme funkci $f : y = x^3$, $x \in \mathbb{R}$ v bodě $x = 0$. Derivace $f'(x) = 3x^2$ a tedy $f'(0) = 0$, přitom v libovolném levém okolí nuly platí:
>$$\forall x \in P_-(0) : f(x) < f(0) \land \forall x \in P_+(0) : f(x) > f(0)$$

>[!Tip] Poznámka
>- Extrému může nabýt funkce v bodě, v němž derivace vůbec neexistuje
>- Např. funkce $f : y = |x|$ nemá v bodě $x = 0$ derivaci, má zde pouze jednostranné derivace (jednostranné limity) $f'_− = −1$ a $f'_+ = 1$. 
>- Přitom víme, že má v tomto bodě minimum ($\forall x \in P(0) : f(x) > 0$).

- Bylo by tedy žádoucí poznat nějaké kritérium, které by nám nejen zaručilo, že v daném bodě extrém nastane, ale také nám objasnilo, o jaký extrém se bude jednat 

#### Postačující podmínky pro lokální maximum
- Nechť $f : \mathbb{R} \to \mathbb{R}$, je spojitá v bodě $a \in \mathbb{R}$. Pak:
1. Je-li $f$ rostoucí na $P_-(a)$ a klesající na $P_+(a)$, pak $f$ má v bodě $a$ ostré lokální maximum.
2. Je-li $\forall x \in P_-(a) : f'(x) > 0$ a $\forall x \in P_+(a) : f'(x) < 0$, pak $f$ má v bodě $a$ ostré lokální maximum.

#### Postačující podmínky pro lokální minimum
- Nechť $f : \mathbb{R} \to \mathbb{R}$, je spojitá v bodě $a \in \mathbb{R}$. Pak:
1. Je-li $f$ klesající na $P_-(a)$ a rostoucí na $P_+(a)$, pak $f$ má v bodě $a$ ostré lokální minimum.
2. Je-li $\forall x \in P_-(a) : f'(x) < 0$ a $\forall x \in P_+(a) : f'(x) > 0$, pak $f$ má v bodě $a$ ostré lokální minimum.

>[!Example]- Isibalo - Proč používáme první derivace
><iframe width="660" height="385" src="https://www.youtube.com/embed/vAJKLwfbaKk?si=4nmnDHi7RSoH8K30" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Derivace vyšších řádů
- Derivaci
$$(f')'(x_0) = \lim_{h \to 0} \frac{f'(x_0 + h) - f'(x_0)}{h}$$
budeme nazývat druhou derivací funkce $f$ v bodě $x_0$.
- Indukcí pak můžeme zavést derivace vyšších řádů:
- Nechť $f : \mathbb{R} \to \mathbb{R}$ má vlastní derivaci $f^{(n-1)}$, $n \in \mathbb{N}$ v nějakém okolí bodu $x_0$ z definičního oboru $D(f)$. Pak definujeme n-tou derivaci funkce v bodě $x_0$ jako
$$f^{(n)}(x_0) = \left(f^{(n-1)}\right)'(x_0).$$
- Má-li smysl, klademe $f^{(0)} = f$.

### Určení monotonie a extrémů pomocí derivace vyšších řádů
- Tvrzení, které nám mnohdy může pomoci rozhodnout o monotonii či extrému v bodě v případě, kdy prvních $n - 1$ derivací v bodě je nulových.
- Nechť $f : \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}$ a existuje $n \in \mathbb{N}$, $n \geq 1$ takové, že $f'(a) = f''(a) = \ldots = f^{(n-1)}(a) = 0$ a $f^{(n)} \neq 0$. Pak:
1. Je-li $n$ sudé a $f^{(n)} > 0$, pak $f$ má v bodě $a$ ostré lokální minimum.
2. Je-li $n$ sudé a $f^{(n)} < 0$, pak $f$ má v bodě $a$ ostré lokální maximum.
3. Je-li $n$ liché a $f^{(n)} > 0$, pak $f$ je v bodě $a$ rostoucí.
4. Je-li $n$ liché a $f^{(n)} < 0$, pak $f$ je v bodě $a$ klesající.

- Mnohdy stačí najít body podezřelé z extrému a spočítat druhou derivaci v těchto bodech. 
- Pokud bude záporná, jedná se o **ostré lokální maximum**, pokud bude kladná, můžeme ho prohlásit za **ostré lokální minimum**.

### Postačující podmínky pro lokální extrémy.
- Nechť $f'(x_0) = 0$ a nechť existuje v bodě $x_0$ druhá derivace.
	1. Je-li $f''(x_0) < 0$, má funkce $f$ v bodě $x_0$ ostré lokální maximum
		- posloupnost směrnic tečen totiž klesá
	2. Je-li $f''(x_0) > 0$, má funkce $f$ v bodě $x_0$ ostré lokální minimum
		- posloupnost směrnic tečen totiž roste

![[Pasted image 20240629130440.png | 200]]


## Věty o střední hodnotě
- Tyto věty mají velký význam v dokazování dalších vět
	- např. L'Hospitalovo pravidlo, určitý integrál...
#### Rolleova věta
- Nechť funkce $f$ má následující vlastnosti:
1. Je spojitá na uzavřeném intervalu $\langle a, b \rangle$.
2. Je diferencovatelná na otevřeném intervalu $(a, b)$.
3. Platí $f(a) = f(b)$.
- Potom v otevřeném intervalu $(a, b)$ existuje alespoň jeden bod $x$ takový, že $f'(x) = 0$
	- v nějakém bodě změní monotonii (rovnost koncových bodů)
- Věta sama zaručuje pouze existenci alespoň jednoho takového bodu, neumožňuje nám však ani tento bod určit, ani stanovit počet takových bodů

![[Pasted image 20240629131912.png]]
#### Lagrangeova věta
- Nechť funkce $f$ má následující vlastnosti:
	1. Je spojitá na uzavřeném intervalu $\langle a, b \rangle$.
	2. Má derivaci na otevřeném intervalu $(a, b)$.
- Potom v otevřeném intervalu $(a, b)$ existuje alespoň jeden bod $x$ takový, že $$f'(x) = \frac{f(b) - f(a)}{b - a}$$
- **Geometrická interpretace:** 
	- spojíme-li přímkou $p$ body $A=[a,f(a)]$  a $𝐵=[𝑏,𝑓(𝑏)]$ potom mezi body $a$ a $b$ existuje alespoň jeden bod $C=(c,f(c))$, v níž je tečna ke grafu funkce $f$ je rovnoběžná s přímkou $p$
- ![[Pasted image 20240629144430.png]]
- **Fyzikální interpretace**
	- Uvážíme-li nějakou veličinu, která se v čase mění podle hladké funkce, pak existuje okamžik uvnitř časového intervalu $(a,b)$, kdy je **okamžitá změna této veličiny rovna průměrné změně** za celý časový interval $(a,b)$ - střední hodnota


#### Cauchyova věta
- Nechť funkce $f(x)$, $g(x)$ mají následující vlastnosti:
	1. jsou spojité na intervalu $\langle a, b \rangle$
	2. mají v každém bodě $x$ intervalu $(a, b)$ vlastní derivaci
	3. pro všechna $x \in (a, b)$ platí $g'(x) \neq 0$. 
- Pak existuje bod $c \in (a, b)$ takový, že platí:
$$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}.$$
- Jedná se o zobecnění Lagrangeovy věty o střední hodnotě

#### Prostost funkce
- Nechť funkce $f$ vyhovuje podmínkám **Lagrangeovy věty** a navíc ať $f'(x) \neq 0$ pro všechna $x \in (a, b)$. Potom je funkce $f$ prostá na $\langle a, b \rangle$.
- **Důkaz**: 
	- funkce $f$ je na množině $\langle a, b \rangle$ prostá, jestliže $\forall{x_1, x_2} \in{\langle a, b \rangle},\ x_1\neq x_2\implies f(x_1) \neq f(x_2)$
	- předpokládejme že $f(x_1) = f(x_2)$ a že $x_1 \lt x_2$, pak ale podle Lagrangeovy věty $f^{'}(x)*(x_2-x_1)=0$ 
	- to je však spor s podmínkou "$f'(x) \neq 0$ pro všechna $x \in (a, b)$"

#### Konstantnost funkce
- Funkce $f$ je konstantní na intervalu $x \in (a, b)$, právě když má v tomto intervalu derivaci a platí $f'(x) = 0$ pro všechna $x \in (a, b)$.

#### l'Hospitalovo pravidlo
- Nechť $f, g : \mathbb{R} \rightarrow \mathbb{R}$, $a \in \mathbb{R}$. Nechť existuje
$$\lim_{x \to a} \frac{f'(x)}{g'(x)} = A$$
- a nechť je splněna jedna z následujících podmínek:
	1. $\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0$,
	2. $\lim_{x \to a} |g(x)| = \infty$.
- Pak existuje $\lim_{x \to a} \frac{f(x)}{g(x)}$ a platí $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} = A$$
## Konvexní a konkávní funkce
- Uvažujme obecnou funkci $f(x)$
- Zvolíme-li na grafu funkce tři různé body $P_1 = [x_1, f(x_1)]$, $P_2 = [x_2, f(x_2)]$, $P_3 = [x_3, f(x_3)]$ takové, že $x_1 < x_2 < x_3$. Vidíme, že bod $P_2$ leží pod přímkou $P_1P_3$.
![[Pasted image 20240629155622.png]]

- Má-li přímka $P_1P_3$ rovnici $y = kx + q$, pak výrok „$P_2$ leží pod přímkou $P_1P_3$” znamená, že $P_2$ leží v polorovině $\{ (x, y) \in \mathbb{R}^2 \mid y < kx + q \}$). 
- Rovnice přímky $P_1P_3$ je následovná:

$$y = f(x_1) + \frac{f(x_3) - f(x_1)}{x_3 - x_1} (x - x_1).$$
- Pokud bod $P_2$ má ležet pod touto přímkou, stačí zaměnit „=” za „<” a obecný bod o souřadnicích $(x, y)$ za náš $P_2 = [x_2, f(x_2)]$. 
- Analogickou úvahu lze provést pro bod ležící nad přímkou.

>[!Example]- Isibalo - Co je to konvexnost a konkávnost
><iframe width="660" height="385" src="https://www.youtube.com/embed/MrOskBRFUw4?si=leXLOLx_zeHwTk4o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

>[!Example]- Isibalo - Proč druhá derivace
><iframe width="660" height="385" src="https://www.youtube.com/embed/W_J6YRZqrtA?si=XIB0_nGKikt4vTHK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
### Definice
- Nechť $f$ je definována na intervalu $I$. Říkáme, že funkce $f$ je na intervalu $I$
1. **ryze konvexní** právě tehdy, když pro libovolnou trojici $x_1, x_2, x_3 \in I$, $x_1 < x_2 < x_3$ platí

$$f(x_2) < f(x_1) + \frac{f(x_3) - f(x_1)}{x_3 - x_1} (x_2 - x_1).$$

2. **ryze konkávní** právě tehdy, když pro libovolnou trojici $x_1, x_2, x_3 \in I$, $x_1 < x_2 < x_3$ platí

$$f(x_2) > f(x_1) + \frac{f(x_3) - f(x_1)}{x_3 - x_1} (x_2 - x_1).$$

- Ověření těchto vlastností pomocí uvedených postupů je však náročné, nalézt a ověřit je lze pomocí druhé derivace (sudé)

### O konvexnosti a konkávnosti funkce na intervalu
- Nechť je $f$ spojitá na intervalu $I$ a nechť v každém vnitřním bodě tohoto intervalu existuje druhá derivace. Pak
	1. Je-li $f''(x) > 0$ v každém vnitřním bodě $x$ intervalu $I$, je $f$ ryze konvexní na $I$.
		- posloupnost směrnic tečen roste
	1. Je-li $f''(x) < 0$ v každém vnitřním bodě $x$ intervalu $I$, je $f$ ryze konkávní na $I$.
		- posloupnost směrnic tečen klesá
		- "Do konkávy do kávu nenaliješ" :)
	1. Je-li $f''(x) = 0$ v každém vnitřním bodě $x$ intervalu $I$, je $f$ lineární na $I$.

- Bod, kde se konvexnost mění na konkávnost nebo naopak, nazveme **inflexním bodem**.

#### Nutná podmínka pro existenci inflexního bodu
- Je-li bod $x_0$ **inflexním bodem** funkce $f$ a má-li funkce v tomto bodě vlastní druhou derivaci, pak $f''(x_0) = 0$. 
- Jedná se o bod, ve které se funkce $f$ přeměňuje z konkávní na konvexní nebo naopak

## Asymptota
- Při vyšetřování průběhu funkce a především pro přesnější kreslení jejího grafu je dobré znát přímky, kterým se graf funkce v okolí některých zajímavých bodů podobá
- Zjednodušeně řečeno, asymptota je přímka, ke které se graf funkce blíží, ale nikdy se jí nedotkne.

>[!Example]- Isibalo - Co jsou to asymptoty
><iframe width="660" height="385" src="https://www.youtube.com/embed/_bElzjN6tz4?si=76x9eTi8-dvWkIg_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Asymptota bez směrnice - ABS
- Nechť $f : \mathbb{R} \rightarrow \mathbb{R}$. Přímka $p : x = a$ se nazývá asymptota bez směrnice (svislá asymptota) $f$ v bodě $a \in \mathbb{R}$, jestliže
$$\lim_{x \to a^{-}} f(x) = \pm \infty \quad \text{nebo} \quad \lim_{x \to a^{+}} f(x) = \pm \infty.$$
### Asymptota se směrnicí - ASS
- Nechť $f : \mathbb{R} \rightarrow \mathbb{R}$. Přímka $p : y = kx + q, x \in \mathbb{R}$ se nazývá asymptota se směrnicí (asymptota v $\pm \infty$) funkce $f$, jestliže
$$\lim_{x \to \pm \infty} [f(x) - (kx + q)] = 0.$$

- Lineární funkce $p : y = kx + q, x \in \mathbb{R}$ je asymptotou se směrnicí (asymptota v $\infty$), právě když
	- $k = \lim_{x \to \infty} \frac{f(x)}{x}$, kde $k \in \mathbb{R}$,
	- $q = \lim_{x \to \infty} [f(x) - kx]$, kde $q \in \mathbb{R}$.

Podobná věta platí také pro asymptotu v $-\infty$.

## Postup při vyšetřování průběhu funkce
1. Z předpisu funkce $y = f(x)$
    - určíme definiční obor funkce, příp. nulové body
    - určíme paritu funkce (sudá resp. lichá)
    - rozhodneme o spojitosti funkce v definičním oboru
    
2. Vypočítáme první derivaci funkce
    - určíme definiční obor derivace, určíme nulové body derivace (body podezřelé z extrému)
    - určíme intervaly monotonie (roste resp. klesá)
    - klasifikujeme extrémy

3. Vypočítáme druhou derivaci
    - určíme intervaly konkávnosti resp. konvexnosti funkce
    - určíme inflexní body

4. Sestavíme tabulku dosavadních informací o funkci
	- užitečné pro přehlednost
	- určíme a zapíšeme hodnoty funkce ve význačných bodech (extrémy, inflexní body).
    
5. Určíme rovnice asymptot (ABS, ASS), pokud existují.
    
6. Nakreslíme graf funkce.

##### Navigace

Předchozí: [[Derivace funkce a její geometrický význam - Pravidla pro derivování funkcí, derivace složené funkce, derivace inverzní funkce, derivace elementárních funkcí]]
Následující: [[Neurčitý integrál a metody jeho výpočtu]]
Celý okruh: [[1. Teoretické základy informačních technologií]]
