- Relační proměnné máme 2 typů
	1) základní - přímo obsahují svou hodnotu, jsou vždy aktualizovatelné
	2) virtuální - její hodnota je definována relačním výrazem (počítá se), aktualizovatelné jen někdy
>[!info] Princip zaměnitelnosti
>Uživatel nepozná navenek o jaký typ se jedná (základní nebo virtuální).
#### Virtuální tabulka v SQL
```SQL
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name;

DROP VIEW view_name;

UPDATE view_name SET column1 = value1 WHERE condition;
```
- Tabulková proměnná table se nazývá virtuální
- Aktualizovatelná pokud platí:
	1) Jedná se o `SELECT` výraz
	2) Ve `FROM` klauzuli musí být jediná aktualizovatelná tabulková proměnná
	3) Nesmí obshaovat `DISTINCT` klauzuli
>[!info] Zlaté pravidlo změny hodnoty relační proměnné
> Po změně hodnoty relační proměnné musí její hodnota splňovat její omezení.
- Na pohledech nelze vytvářet index (možné snížení výkonu)
- Používají se k: zjednodušení složitých dotazů, lepší čitelnosti kódu