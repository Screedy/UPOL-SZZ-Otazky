### Binární logika
- Formální logický základ: výroková logika - zkoumá pravdivostní hodnotu výroků (pravda/nepravda, spojky/operátory $\rightarrow, \vee, \wedge, \leftrightarrow, \neg$)
- Výroky jako logické výrazy vyhodnocované na hodnoty (pravda/nepravda, $1/0$)
- Matematický aparát pro práci s dvouhodnotovými log. výrazy: Booleova algebra (binární/dvouhodnotová logika)
- Fyzická realizace: (elektronické binární) logické obvody - základ digitálních zařízení

- Logická proměnná $x$
	- Veličina nabývající dvou možných diskrétních logických hodnot: $0$ a $1$
	- definice: $x = 1$, jestliže $x \neq 0$ a $x = 0$, jestliže $x \neq 1$

- Logická funkce $f(x_{1}, ..., x_{n})$
	- Funkce $n$ logických proměnných $x_{1}, ..., x_{n}$ (= $n$-ární funkce) nabývající dvou možných diskrétních hodnot $0$ a $1$
	- Logická proměnná = logická funkce identity proměnné, skládání funkcí
	- základní = logické operace

- Booleova algebra (binární logika)
	- Algebra ("Matematika") logických proměnných a logických funkcí
	- Dvouhodnotová algebra, algebra dvou stavů
	- Relace rovnost: $f = g$, právě když $(f = 1$ a $g = 1)$ nebo $(f = 0$ a $g = 0)$

- Logický výraz
	- Korektně vytvořená posloupnost (symbolů) logických proměnných a funkcí (operátorů) spolu se závorkami
	- Priority sestupně: negace, log. součin, log. součet
	- = zápis logické funkce

- Logická rovnice
	- dva logické výrazy v relaci rovnost $=$
	- ekvivalentní úpravy = zachování (pravdivosti rovnosti výrazů: např. negace obou stran, logický součin/součet obou stran se stejným výrazem, ..., log. funkce obou stran se stejnými ostatními operandy funkce
	- NEekvivalentní úpravy: "krácení" obou stran o stejný (pod)výraz
		- např $x + y = x + z$ není ekvivalentní s $y = z$ 

### Axiomy (Booleovy algebry)
- Komutativa:  $x \cdot y = y \cdot x \qquad x + y = y + x$
- Distributivita:  $x \cdot (y + z) = x \cdot y + x \cdot z \qquad  x + y \cdot z = (x + y) \cdot (x + z)$
- Identita/neutrálnost/existence neutrální hodnoty:  $1 \cdot x = x \qquad 0 + x = x$
- Komplementárnost:  $x \cdot \neg x = 0 \qquad x + \neg x = 1$

### Logické operace
3 základní:
#### Negace (inverze) - $\neg$
- Pravdivá, když operand je nepravdivý, jinak nepravdivá
  ![[MacBook-2024-03-18-000904.png| 100]]

#### Logický součin (konjunkce) - $\wedge$
- Pravdivá, když oba operandy pravdivé, jinak nepravdivá
  ![[MacBook-2024-03-18-000905.png| 100]]

#### Logický součet (disjunkce) - $\vee$
- Nepravdivá, když oba operandy jsou nepravdivé, jinak pravda
  ![[MacBook-2024-03-18-000906.png| 100]]

### Vlastnosti základních logických operací
- agresivita (nuly a jedničky): $0 \cdot x = 0 \qquad 1 + x = 1$
- idempotence: $x \cdot x = x \qquad x + x = x$
- asociativita: $x \cdot (y \cdot z) = (x \cdot y) \cdot z \qquad x + (y + z) = (x + y) + z$
- involuce (dvojí negace):  $\neg \neg x = x$
- De Morganovy zákony:  $\neg (x \cdot y) = \neg x + \neg y \qquad   \neg (x + y) = \neg x \cdot \neg y$
- absorpce:  $x \cdot (x + y) = x \qquad  x + x \cdot y = x$
- a další

#### Implikace - $\rightarrow$
- Nepravdivá, když první operand je pravdivý a druhý nepravdivý, jinak pravdivá
  ![[MacBook-2024-03-18-000907.png| 100]]

#### Ekvivalence - $\leftrightarrow$
- Pravdivá, když operandy mají stejnou hodnotu
- $x \ XNOR \ y$, $x \equiv y$
  ![[MacBook-2024-03-18-000908.png| 100]]

#### Nonekvivalence (negace ekvivalence) - $\oplus$
- pravdivá, když operandy mají různou hodnotu, jinak nepravdivá
- $x \ XOR \ y$ , $x \not\equiv y$, $x \oplus y$
![[nonekvivalence.png|100]]

#### Shefferova funkce (negace logického součinu) - $\uparrow$
- nepravdivá, když oba operandy pravdivé, jinak pravdivá
- $x \ NAND \ y$
![[shefferova.png|100]]

#### Piercova funkce (negace logického součtu) - $\downarrow$
- pravdivá, když oba operandy nepravdivé, jinak nepravdivá
- $x \ NOR \ y$
![[piercova.png|100]]

### Fyzická realizace logických funkcí
- dnes pomocí tranzistorů (a diod) v integrovaných obvodech: technologie RTL, DTL, **TTL**, **CMOS**...
- realizace log. operací pomocí integrovaných obvodů – **logických členů**, **hradel**
![[log-funkce.png|450]]


## Logické obvody
- **jeden výstup**: realizace jedné log. funkce
- **více výstupů**: realizace více log. funkcí zároveň → realizace vícebitové log. funkce ${^n}f$
- **n-tice vstupů**: reprezentace vícebitových (n-bitových) log. proměnných  ${^n}x$ = vícebitový log. obvod

- **kombinační:** stavy na výstupech obvodu (tj. funkční hodnota) závisí pouze na okamžitých stavech na vstupech (tj. hodnotách proměnných)
- **sekvenční:** stavy na výstupech obvodu (tj. funkční hodnota) závisí nejen na okamžitých stavech na vstupech (tj. hodnotách proměnných), ale také na předchozích stavech na vstupech

### Kombinační
##### Komparátor
- provádí srovnání hodnot dvou log. proměnných $A$ a $B$ na vstupu

![[komparator.png|450]]

##### Multiplexor
- přepíná na výstup $Q$ log. hodnotu na jednom z $2^n$ datových vstupů $D_i$ vybraném na základě $n-$bitové hodnoty na adresním vstupu $A$
- mě výstupu $Q$ navíc ještě negovaný (invertovaný) výstup $\overline{Q}$
- použití: multiplexování datových vstupů na základě adresy

![[multiplexor.png|450]]

##### Binární dekodér
- nastaví (na $1$) jeden z $2^n$ výstupů $S_i$ odpovídající $n-$bitové hodnotě na adresním vstupu $A$
- použití: dekodér adresy pro výběr místa v paměti

![[bin-dekoder.png|450]]
##### Binární sčítačka
- sčítačka sečte binární hodnoty v každém řádu dvou $n-$bitových proměnných $A$ a $B$ podle pravidel aritmetiky pro sčítání, tj. s přenosem hodnoty do vyššího řádu
- platí stejná pravidla aritmetiky jako v desítkové soustavě, např. (+ je zde aritmetické sčítání!):
	- $0 + 0 = 0 \quad 0 + 1 = 1 \quad 1 + 1 = 10$
- použití: (aritmetické) sčítání binárně reprezentovaných 8-, 16-, 32-, atd. bitových čísel

![[bin-scitacka.png|450]]

### Sekvenční
- stavy na výstupech obvodu (tj. funkční hodnota) závisí nejen na okamžitých stavech na vstupech (tj. hodnotách proměnných), ale také na předchozích stavech na vstupech
- předchozí stavy na vstupech zachyceny vnitřním stavem obvodu 
- nutné identifikovat a synchronizovat stavy obvodu v čase

**Přenos dat** (hodnot vícebitových log. proměnných):
- **sériový**: bity (hodnoty 0/I) přenášeny postupně v čase za sebou po jednom datovém vodiči
- **paralelní**: bity přenášeny zároveň v čase po více datových vodičích
![[seriovy-paralelni.png|400]]


#### Klopné obvody 
- nejjednodušší sekvenční obvody
- **astabilní**: nemají **žádný stabilní stav**, periodicky překlápí výstupy z jednoho stavu do druhého („kmitají“); použití jako generátory impulsů  
- **monostabilní**: **jeden stabilní stav** na výstupech, po vhodném řídícím signálu je po definovanou dobu v nestabilním stavu; použití k vytváření impulsů dané délky 
- **bistabilní**: **oba stavy na výstupech stabilní**, zůstává v jednom stabilním stavu dokud není vhodným řídícím signálem překlopen do druhého; použití pro realizaci pamětí

**Řízení:**  
- **asynchronně** signály ($0$ nebo $1$) na datových vstupech  
- **synchronně** hodinovým signálem  
- **hladinou signálu**: horní ($1$) nebo dolní ($0$)  
- **hranami signálu**: nástupní ($0 → 1$ u horní hladiny) nebo sestupní ($0 → 1$ u dolní hladiny)

##### Klopný obvod (typu) RS
- nejjednodušší bistabilní, základ ostatních
- asynchronní vstupy $R$ (Reset) pro nulování log. hodnoty na výstupu $Q$ (v čase $i$) a $S$ (Set) pro nastavení hodnoty
- kromě výstupu $Q$ navíc ještě negovaný (invertovaný) výstup $Q$
- varianty: varianta se synchronizačním vstupem CLK s hodinových signálem, varianta Master-Slave
![[klop-rs.png|450]]

##### Klopný obvod (typu) D
![[klop-d.png]]
##### Klopný obvod (typu) JK
![[klop-jk.png|330]]

#### Obvody v počítačích:
##### Paralelní registr (střádač)
- vícebitová paměť pro hodnotu dodanou paralelně na více vstupů, paralelní zapojení klopných obvodů D
##### Sériový (posuvný) registr: 
- vícebitová paměť pro hodnotu dodanou sériově na vstupu, sériové zapojení klopných obvodů D, použití pro transformaci sériových dat na paralelní
##### Čítač:
- paměť počtu impulsů na hodinovém vstupu, binárně reprezentovaný počet na vícebitovém výstupu, zřetězené zapojení klopných obvodů JK
##### Sériová sčítačka
- (aritmetické) sčítání log. hodnot dodávaných na vstupy v sériovém tvaru po jednotlivých řádech

##### Navigace
Předchozí:  [[Číselné soustavy]]
Následující: [[Reprezentace čísel a znaků v počítači]]
Celý okruh: [[2. Informační technologie]]