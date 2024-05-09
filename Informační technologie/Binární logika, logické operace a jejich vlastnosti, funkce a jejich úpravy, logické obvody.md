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
	- NEekvivalentní úpravy: "krácení" obou stran o stejný (pod)výraz, např $x + y = x + z$ na $y = z$

### Axiomy (Booleovy algebry)
- Komutativa - $x \cdot y = y \cdot x$          $x + y = y + x$
- Distributivita - $x \cdot (y + z) = x \cdot y + x \cdot z$        $x + y \cdot z = (x + y) \cdot (x + z)$
- Identita/neutrálnost/existence neutrální hodnoty - $1 \cdot x = x$        $0 + x = x$
- Komplementárnost - $x \cdot \neg x = 0$         $x + \neg x = 1$

### Logické operace
3 základní:
#### Negace - $\neg$
- Pravdivá, když operand je neopravdivý, jinak nepravdivá
  ![[MacBook-2024-03-18-000904.png| 100]]

#### Logický součin (konjunkce) - $\wedge$
- Pravdivá, když oba operandy pravdivé, jinak nepravdivá
  ![[MacBook-2024-03-18-000905.png| 100]]

#### Logický součet (disjunkce) - $\vee$
- Nepravdivá, když oba operandy jsou nepravdivé, jinak pravda
  ![[MacBook-2024-03-18-000906.png| 100]]

### Vlastnosti základních logických operací
- agresivita (nuly a jedničky) $0 \cdot x = 0$       $1 + x = 1$
- idempotence $x \cdot x = x$     $x + x = x$
- asociativita $x \cdot (y \cdot z) = (x \cdot y) \cdot z$       $x + (y + z) = (x + y) + z$
- involuce (dvojí negace) $\neg \neg x = x$
- De Morganovy zákony $\neg (x \cdot y) = \neg x + \neg y$      $\neg (x + y) = \neg x \cdot \neg y$
- absorpce $x \cdot (x + y) = x$      $x + x \cdot y = x$
- a další

#### Implikace - $\rightarrow$
- Nepravdivá, když první operand je pravdivý a druhý nepravdivý, jinak pravdivá
  ![[MacBook-2024-03-18-000907.png| 100]]

#### Ekvivalence - $\leftrightarrow$
- Pravdivá, když operandy mají stejnou hodnotu
  ![[MacBook-2024-03-18-000908.png| 100]]


### Logické obvody

##### Navigace
Předchozí:  [[Číselné soustavy]]
Následující: [[Reprezentace čísel a znaků v počítači]]
Celý okruh: [[2. Informační technologie]]