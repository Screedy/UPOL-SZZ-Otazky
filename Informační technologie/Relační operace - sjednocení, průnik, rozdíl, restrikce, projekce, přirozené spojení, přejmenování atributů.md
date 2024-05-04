## Výraz sjednocení
- Hodnota výrazu sjednocení, označme $D'$. Tělo $D'$ je sjednocením těl $D_{1}$ a $D_{2}$
- `( expr1 UNION expr2 )`
- Např. pro tabulky:
```sql
TABLE movies1;                 | TABLE movies2;
    title     | year           |     title     | year
--------------+------          | --------------+------
 The Matrix   | 1999           |  The Matrix   | 1999
 The Avengers | 2012           |  The Avengers | 1998
(2 rows)                       | (2 rows)
```
- Můžeme provést jejich sjednocení:
```sql
( TABLE movies1 ) UNION ( TABLE movies2 );
    title     | year
--------------+------
 The Avengers | 1998
 The Avengers | 2012
 The Matrix   | 1999
(3 rows)
```

## Výraz průniku
- Hodnotu výrazu průniku označme $D'$. Tělo $D'$ je průnikem těl $D_{1}$ a $D_{2}$.
- `( expr1 INTERSECT expr2 )`
- Pro tabulky ze sjednocení můžeme provést:
```sql
( TABLE movies1 ) INTERSECT ( TABLE movies2 );
   title    | year
------------+------
 The Matrix | 1999
(1 row)
```

## Výraz rozdíl
- Hodnotu výrazu rozdílu označme $D'$. Tělo $D'$ je množinovým rozdílem těl $D_{1}$ a $D_{2}$.
- Pro tabulku ze sjednocení můžeme provést:
```sql
( TABLE movies1 ) EXCEPT ( TABLE movies2 );
    title     | year
--------------+------
 The Avengers | 2012
```

## Skládání relačních výrazů
- Relační výrazy můžeme i skládat.
```sql
( ( TABLE movies1 ) EXCEPT ( TABLE movies2 ) )
				  UNION
( ( TABLE movies2 ) EXCEPT ( TABLE movies1 ) );
    title     | year
--------------+------
 The Avengers | 2012
 The Avengers | 1998
(2 rows)
```

## Výrazy ve `FROM` klauzuli
- Výrazem `expr AS name` ve `FROM` klauzuli určíme tabulku, která bude hodnotou tabulkového výrazu `expr` a bude se jmenovat `name`.
- Například:
```sql
TABLE movies1;                 | TABLE movies2;
    title     | year           |     title     | year
--------------+------          | --------------+------
 The Matrix   | 1999           |  The Matrix   | 1999
 The Avengers | 2012           |  The Avengers | 1998
(2 rows)                       | (2 rows)


SELECT   DISTINCT year
FROM ( ( TABLE movies1 )
	   UNION
	 ( TABLE movies2 ) ) AS movies;
 year
------
 2012
 1998
 1999
(3 rows)
```

## Restrikce
- Je dán relační výraz `expr` s podmínkou `condition` a jménem `name`. Pak
```sql
( SELECT *
	FROM expr AS name 
	WHERE condition )
```
- je relační výraz `restrikce`.
- Hodnotou výrazu `expr` si označíme $D$. Hodnotou výrazu restrikce je relace $D'$. Řádek $r$ bude v těle $D'$, právě když $r$ je v těle $D$ a $r$ splňuje podmínku `condition`
- Například:
```sql
TABLE movies;
      title      | year | length
-----------------+------+--------
The Matrix
The Avengers
The Avengers
A Space Odyssey | 1968 |    149
(4 rows)

SELECT *
FROM ( TABLE movies ) AS t
WHERE  title = 'The Avengers';
    title     | year | length
--------------+------+--------
 The Avengers | 2012 |    143
 The Avengers | 1998 |     89
(2 rows)
```
Výraz můžeme ještě zjednodušit:
```sql
SELECT *
FROM   movies
WHERE  title = 'The Avengers';
    title     | year | length
--------------+------+--------
 The Avengers | 2012 |    143
 The Avengers | 1998 |     89
(2 rows)
```

## Projekce
- Projekce je operace, která vytváří novou relaci se záznamy složenými pouze z určitých sloupců původní relace.
- Tato operace redukuje počet sloupců v relaci a může také odstranit duplikátní tuple.
```mysql
( SELECT DISTINCT A1, . . ., Am FROM expr AS name )
```
- Například:
```sql
TABLE movies;
    title           | year | length
--------------------+------+--------
 The Matrix         | 1999 | 136
 The Avengers       | 2012 | 143
 The Avengers       | 1998 | 89
 A Space Odyssey    | 1968 | 149
(4 rows)

SELECT DISTINCT title
FROM ( TABLE movies ) AS m;
	title
-----------------
 The Matrix
 The Avengers
 A Space Odyssey
(3 rows)
```
- Zjednošuděně:
```sql
SELECT DISTINCT title
FROM   movies;
      title
-----------------
 The Matrix
 The Avengers
 A Space Odyssey
(3 rows)
```

## Spojení
- Přirozené spojení kombinuje relace podle sloupců, které mají stejný název a datový typ v obou relacích.
- Výsledná relace obsahuje všechny kombinace tuplů z obou relací, které mají stejné hodnoty ve sloupcích, podle kterých se spojují.
```sql
SELECT table1.*,
       table2.column1,
       table2.column2
		...
FROM expr1 AS table1,
     expr2 AS table2
WHERE table1.column1 = table2.column1
AND   table1.column2 = table2.column2
	  ...
```
- Například:
```sql
# TABLE movies;                 | # TABLE casting;
movie_title | movie_year        | actor_name        | movie_title | movie_year
------------+-----------        | ------------------+-------------+-----------
The Matrix  | 1999              | Keano Reeves      | The Matrix  | 1999
Dracula     | 1992              | Keano Reeves      | Dracula     | 1992
(2 rows)                        | Laurence Fishburne| The Matrix  | 1999
                                | Gary Oldman       | Dracula     | 1992
                                | (4 rows)

SELECT m.*, c.actor_name
FROM ( TABLE movies ) AS m,
     ( TABLE casting ) AS c
WHERE m.movie_title = c.movie_title
AND   m.movie_year = c.movie_year;

movie_title | movie_year | actor_name
------------+------------+----------------
Dracula     | 1992       | Keano Reeves
Dracula     | 1992       | Gary Oldman
The Matrix  | 1999       | Keano Reeves
The Matrix  | 1999       | Laurence Fishburne
(4 rows)
```
- Můžeme zkrátit:
```sql
SELECT m.*, c.actor_name
FROM   movies AS m, casting AS c
WHERE  m.movie_title = c.movie_title
AND    m.movie_year = c.movie_year;
```

## Přejmenování atributů
- Přejmenování je unární operace, která změní název jednoho nebo více sloupců (atributů) v relaci.
- Tato operace se často používá v kombinaci s jinými operacemi pro zjednodušení nebo zpřehlednění dotazů.
- Například:
```sql
TABLE movies;
   title    | year
------------+------
 The Matrix | 1999
 Dracula    | 1992
(2 rows)

SELECT title AS movie_title,
         year AS movie_year
FROM ( TABLE movies ) AS m;
 movie_title | movie_year
-------------+------------
 The Matrix  |       1999
 Dracula     |       1992
```
- Zjednodušeně:
```sql
SELECT title AS movie_title,
       year AS movie_year
FROM movies;
```

## `SELECT` jako relační výraz
Uvažujme obecný `SELECT` výraz:
```sql
( SELECT DISTINCT
 table1.column1 AS 'column1',
 table2.column2 AS 'column2',
...
FROM
 (expr1) AS name1,
 (expr2) AS name2,
...
WHERE condition )
```
- Pokud `expr1`, `expr2`, ... jsou relační výrazy a `column1`, `column2`, ... jsou po dvou různé názvy sloupců, pak hodnotou výrazu je opět relace.
- Hodnotu výrazu můžeme spočítat pomocí relačních operací následovně:
	1. Získáme hodnoty výrazů `expr1`, `expr2`, ..., které si označíme $D_{1}$, $D_{2}$, ...
	2. Přejmenujeme každý atribut `column` relace $D_{i}$ na `name1.column`. Tím získáme relace $D'_{1}$, $D'_{2}$, ...
	3. Spočítáme spojení $D'_{1}$, $D'_{2}$, ... Vzhledem k tomu, že každé dvě relace nemají žádný společný název sloupce, bude se jednat o kartézský součin. Získáme relaci $D''$
	4. Dále se provede restrikce relace $D''$ vzhledem k podmínce `condition`. Jako výsledek obdržíme relaci $D'''$.
	5. Následuje projekce relace $D'''$ na `{table1.column1, table2.column2, ...}`. Obdržíme relaci $D''''$
	6. Nakonec se provede přejmenování $D''''$ sloupce `table1.column1` na `column1`, `table2.column2` na `column2`, ... Získáme výstupní relaci $D'''''$.


##### Navigace
Předchozí:  [[Výraz SELECT v SQL]]
Následující: [[Integrita dat - primární a cizí klíč]]
Celý okruh: [[2. Informační technologie]]