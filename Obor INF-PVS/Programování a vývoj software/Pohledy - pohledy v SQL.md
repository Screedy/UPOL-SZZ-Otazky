- Relační proměnné máme 2 typů
	1) základní - přímo obsahují svou hodnotu, jsou vždy aktualizovatelné
	2) virtuální - její hodnota je definována relačním výrazem (počítá se), aktualizovatelné jen někdy
- Uživatel nepozná navenek o jaký typ se jedná (*princip zaměnitelnosti*)
#### Virtuální tabulka v SQL
```SQL
CREATE VIEW table As expr;

DROP VIEW table;
```
- Tabulková proměnná table se nazývá virtuální
- Aktualizovatelná pokud platí:
	1) Jedná se o `SELECT` výraz
	2) Ve `FROM` klauzuli musí být jediná aktualizovatelná tabulková proměnná
	3) Nesmí obshaovat `DISTINCT` klauzuli

- Na pohledech nelze vytvářet index (možné snížení výkonu)