## Tabulkový výraz
- Výrazu, jehož hodnota je tabulka, říkáme **tabulkový výraz**. 
## Výraz `SELECT`
- Příkazy se skládají z částí, které se nazývají **klauzule**.
- Klauzule se většinou jmenují podle klíčového slova, které klauzuli uvozuje.
- Například výraz `SELECT` se může skládat z klauzulí `SELECT` a `FROM`

### Klauzule `SELECT` a `FROM`
- `( SELECT columns FROM table )`
- Část `SELECT columns` je `SELECT` klauzule a část `FROM table` je `FROM` klauzule.
	- Místo `columns` popisujeme sloupce výsledné tabulky.

---
Např. pokud vyhodnotíme:
```sql
SELECT title AS title, year + 1 AS next_year FROM movies;

-- Pro tabulku:
      title      | year | length
-----------------+------+--------
The Matrix       | 1999 |    136
The Avengers     | 2012 |    143
The Avengers     | 1998 |     89
A Space Odyssey  | 1968 |    149
(4 rows)

-- Dostaneme:
      title      | next_year
-----------------+-----------
The Matrix       |      2000
The Avengers     |      2013
The Avengers     |      1998
A Space Odyssey  |      1969
```
---
Pro odstranění duplicit slouží klauzule `DISTINCT`:
```sql
SELECT DISTINCT title FROM movies;

-- Dostaneme:
      title
-----------------
 The Matrix
 The Avengers
 A Space Odyssey
(3 rows)
```

### Klauzule `WHERE`
Výraz `SELECT` může mít tvar:
```sql
( SELECT DISTINCT columns FROM table WHERE condition )
```
- Pomocí podmínky `condition` získáme tabulku, která bude v těle obsahovat právě jeden řádek za každý řádek originální tabulky, pro který je podmínka `condition` splněna.
```sql
SELECT * FROM movies WHERE title = 'The Avengers';

-- Získáme:
    title     | year | length
--------------+------+--------
 The Avengers | 2012 |    143
 The Avengers | 1998 |     89
(2 rows)
```
### Klauzule `ORDER BY`
- `ORDER BY` klauzule se skládá z výrazů tvaru: `column ASC` a `column DESC`.
```sql
SELECT * FROM movies ORDER BY year ASC;

-- Získáme:
    director     |            title                | year
-----------------+---------------------------------+------
 Stanley Kubrick | Lolita                          | 1962
 Robert Mulligan | To Kill a Mockingbird           | 1962
 Carol Reed      | Oliver!                         | 1968
 Stanley Kubrick | 2001: A Space Odyssey           | 1968
 Milos Forman    | One Flew Over the Cuckoo’s Nest | 1975
 Stanley Kubrick | Barry Lyndon                    | 1975
 Terry Gilliam   | Monty Python and the Holy Grail | 1975
(7 rows)
```

### Klauzule `LIMIT` a `OFFSET`
```sql
LIMIT count
OFFSET start
```
- Nejprve se vyhodnocuje klauzule `OFFSET`, která pro tabulku $D$ vrátí tabulku $D'$, jejíž tělo tvoří řádky tabulky D bez prvních `start` řádků
- Klauzule `LIMIT` vrátí pro tabulku $D$ tabulku $D'$, jejíž tělo tvoří prvních `count` řádků těla tabulky D.

### Klauzule `GROUP BY`
```sql
GROUP BY column1, column2, ...
```
- **Seskupení dat**: `GROUP BY` seskupí řádky výsledné tabulky, které mají stejné hodnoty ve specifikovaných sloupcích.
- **Agregační funkce**: Po seskupení můžete nad těmito skupinami použít různé agregáční funkce. 
	- Například `COUNT()`, `SUM()`, `AVG()`, `MAX()`, a `MIN()`.

Máme tabulku:
```sql
-- Pro tabulku:
| title                           | year | country | duration |
|---------------------------------|------|---------|----------|
| 2001: A Space Odyssey           | 1968 | UK      | 161      |
| Barry Lyndon                    | 1975 | UK      | 184      |
| The Man Who Shot Liberty Valance| 1962 | USA     | 113      |
| The Return of the Pink Panther  | 1975 | UK      | 113      |
| One Flew Over the Cuckoo’s Nest | 1975 | USA     | 133      |
| To Kill a Mockingbird           | 1962 | USA     | 129      |
| Monty Python and the Holy Grail | 1975 | UK      | 91       |
| Lolita                          | 1962 | UK      | 152      |
| Jaws                            | 1975 | USA     | 130      |
(9 rows)

-- Položíme dotaz:
SELECT year, country, count(*) AS count
FROM movies
GROUP BY year, country;

-- Výsledek:
| year | country | count |
|------|---------|-------|
| 1962 | UK      | 1     |
| 1968 | UK      | 1     |
| 1975 | USA     | 2     |
| 1975 | UK      | 3     |
| 1962 | USA     | 2     |
(5 rows)
```
## Klauzule `SELECT` výrazu
```sql
( SELECT   columns
  FROM     tables
  WHERE    condition
  GROUP BY columns
  HAVING   condition
  ORDER BY ordering
  LIMIT    count
  OFFSET   start )
```

Klauzule se vyhodnocují v tomto pořadí:
1. `FROM` - získání vstupní tabulky
2. `WHERE` - filtrování řádků
3. `GROUP BY` - seskupování
4. `HAVING` - filtrování skupin
5. `SELECT` - výpočet výstupní tabulky
6. `ORDER BY` - třídění řádků
7. `OFFSET` - vynechání řádků ze začátku
8. `LIMIT` - omezení počtu řádků