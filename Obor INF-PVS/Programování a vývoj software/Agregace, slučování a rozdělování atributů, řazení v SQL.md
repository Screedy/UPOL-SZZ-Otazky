## Agregace
- Provádí se výpočet nad datami, abychom získali souhrnou hodnotu
- V SQL pomocí agregačních funkcí
- Dostaneme hodnoty z více řádků do jednoho
#### Agregační funkce SQL
- `COUNT()`: Počítá počet řádků, které splňují podmínku
- `SUM()`: Sečítá hodnoty v daném sloupci
- `AVG()`: Vypočítá průměr hodnot v daném sloupci
- `MIN()`: Vrátí minimální hodnotu v daném sloupci
- `MAX()`: Vrátí maximální hodnotu v daném sloupci
- ![[agregace.png]]
#### Slučování atributů
- Sloučení podle konkrétního kritéria (stejné hodnoty ve sloupci)
- V SQL příkaz `GROUP BY`
```SQL
SELECT nazev, AVG(cena) AS avg_cena
FROM Produkty
GROUP BY nazev;
```
- ![[group_by.png]]
#### Rozdělování atributů
- `HAVING` ... omezí pak atributy na nějakou podmínky (`avg_cena` < 100)
- Děje se po agregaci