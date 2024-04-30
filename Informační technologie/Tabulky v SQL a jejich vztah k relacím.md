## Pojmy popisující tabulku
- **Skalární typ**
	- pojmenovaná nejvýše spočetná množina hodnot
	- Např:
		- Pro každé přirozené číslo $i$ je `varchar(i)` typem, který pojmenovává množinu všech řetězců délky nejvýše $i$
		- `integer` je typem, který dává jméno množině celých čísel od $-2,147,483,648$ do $2,147,483,647$.
		- Typ `text` pojmenovává množinu všech řetězců
		- A další...
	- Konkrétně:
		- "The Avengers" je typu `varchar(12)`, ale už není typu `varchar(11)`.
		- Hodnoty $1998$ a $2012$ jsou typu `integer`.
- **Typ řádku**
	- $n$-tice skalárních typů
	- např. `<text, integer>`
- **Null**
	- speciální hodnota označující prázdnotu
- **Řádek**
	- Neprázdná $n$-tice se nazývá **řádek**. Například `<¨The Avengers¨, 2012>` je řádek.
- **Záhlaví sloupce**
	- Skládá se z názvu a skalárního typu.
	- Např. `title text` je záhlaví jménem `title` typu `text`.
	- Pokud je typ záhlaví určený kontextem, můžeme typ vynechat.
- **Typ tabulky**
	- Je neprázdná $n$-tice skládající se ze záhlaví sloupců
	- Např. `<title text, year integer>`.

## Tabulky
- Tabulka D je hodnota, který se skládá z typu tabulky $<A_{1}T_{1},...,A_{n}T_{n}>$ je $n$-tice $<T_{1},...,T_{n}$ a $m$-tice řádků, kde každý řádek je typu $<T_{1},...,T_{n}>$.
- Typ tabulky D se nazývá **záhlaví tabulky** a $m$-tice řádků tabulky D jejím **tělem**.
 
- Například uvažujme tabulku $D_{1}$ se záhlavím `<title text, year integer>` a tělem `<<¨The Avengers¨, 1998>, <¨The Avengers¨, 2012>, <¨The Matrix¨, 1999>>`.
- Tuto tabulku můžeme přirozeně zapsat následující tabulkou:

| title text   | year integer |
| ------------ | ------------ |
| The Avengers | 1998         |
| The Avengers | 2012         |
| The Matrix   | 1999         |

- Pokud tabulka nemá v těle žádný řádek, říkáme, že je prázdná:

| title | year |
| ----- | ---- |

## Vztah k relacím
- Tabulka nemusí mít unikátní jména sloupců. Například:

| title        | num  | num |
| ------------ | ---- | --- |
| The Avengers | 1998 | 89  |
| The Avengers | 2012 | 143 |
| The Matrix   | 1999 | 136 |

- Ale tabulka, která má jedinečné názvy sloupců, neobsahuje `null` hodnoty a duplicitní řádky, nazýváme **relací**. 
- Tabulka, která je relací:

| title        | year | length |
| ------------ | ---- | ------ |
| The Avengers | 1998 | 89     |
| The Avengers | 2012 | 143    |
| The Matrix   | 1999 | 136    |

- Pokud je tabulka relací, můžeme k ní uvažovat **klasickou relaci** známou z **diskrétní matematiky.** Předchozí tabulka určuje relaci `{⟨‘The Avengers’,1998,89⟩,⟨‘The Avengers’,2012,143⟩,⟨‘The Matrix’,1999,136⟩}`
- Pokud chápeme tabulku jako relaci, nespoléháme se na pořadí řádků v tabulce. Tělo tabulky, která je relací, může být podobně jako klasická množina **určeno charakteristickou vlastností**.
- Pokud má být hodnota tabulky relace, měli bychom zformulovat její charakteristickou vlastnost. V případě základní tabulky v posledním obrázku by to byla vlastnost: *"Vlastním film `title`, vytvořený roku `year`, který má délku `length` minut".*

## Příkazy
### Vytvoření prázdné tabulky:
```sql
CREATE TABLE movies (
	title text,
	year integer
	length integer
);
```
### Zobrazení hodnoty základní tabulky
```sql
SELECT * FROM movies;

 title | year | length
-------+------+--------
(0 rows)
```
## Přidání řádků do tabulky
```sql
INSERT INTO movies VALUES
       ( ’The Matrix’, 1999, 136 ),
       ( ’The Avengers’, 2012, 143 ),
       ( ’The Avengers’, 1998, 89 );

-- Vypsání tabulky:
SELECT * FROM movies;
    title     | year | length
--------------+------+--------
 The Matrix   | 1999 |    136
 The Avengers | 2012 |    143
 The Avengers | 1998 |     89
(3 rows)
```

Přídání jednoho řádku:
```sql
INSERT INTO movies VALUES (’A Space Odyssey’, 1968, 149);
```
### Vymazání tabulky
```sql
DROP TABLE movies;
```

##### Navigace
Předchozí:  [[Správa diskového prostoru - oddíly, souborové systémy, zajištění konzistence dat]]
Následující: [[Výraz SELECT v SQL]]
Celý okruh: [[2. Informační technologie]]