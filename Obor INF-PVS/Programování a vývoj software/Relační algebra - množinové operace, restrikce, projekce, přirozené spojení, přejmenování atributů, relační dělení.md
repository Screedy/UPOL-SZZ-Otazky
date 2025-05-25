## Relační algebra
- Je tvořena operacemi
	- průnik, sjednocení, rozdíl
	- restrikce, projekce, spojení, přejmenování
- **skalární typ** = říká jakého typu hodnota je (text, interger, boolean atd.)
- `null` nemá žádný skalární typ
- **sloupec má záhlaví**, které se skládá z názvu a skalárního typu
- z relační algebry vychází SQL, ale porušuj některé principy
- v praxi relace reprezentujeme tabulkami a pro jejich správu máme NoSQL a [[SQL]]
- **relační kalkul** je jazyk, který vychází z predikátové logiky
	- má stejné schopnosti jako relační algebra
## Operace na relacích
- značení podmínky $\theta$ ... *théta*
#### Sjednocení $\cup$
- Spojí 2 relace se stejnými sloupci
- Výsledek vrací bez duplicit
- V SQL `UNION`
#### Průnik $\cap$
- Pouze řádky v obou tabulkách
- V SQL `INTERSECTION`
#### Rozdíl $-$
- Řádky, které jsou v první tabulce, ale ne ve druhé
- V SQL `EXCEPT`
#### Restrikce $\delta$
- Omezení řádků (podmožina relace) v tabulce
- Jen ty řádky, které splní danou podmínku
- V SQL klauzule `WHERE`
#### Projekce $\Pi$
- Výběr sloupců
- Pokud nějaké sloupce omezením může, pak tabulka působit duplicitně, přestože původní má řádky unikátní
- V SQL `SELECT name, born_year FROM ...` (to co je mezi `SELECT` a `FROM` )
#### Spojení relací $\bowtie$
- Pokud disjunktní -> **kartézský součin**
- Jinak spojíme podle stejných sloupců
- V SQL `JOIN` - natural, left, right
#### Přejmenování atributů $\rho$
- Změna názvu sloupců
- V SQL `SELCT name AS surname ...`
- Pro více účelů (lepší orientace; zabrání sloučení sloupců se stejnými hodnotami)

- Jednotlivé operace můžeme řetězit a dostat výsledný složený zápis, případně je převádět do [[SQL]] a naopak
![[Screenshot 2022-12-10 at 10.41.28.png]]
## Relační dělení
![[Screenshot 2022-12-10 at 10.37.47.png]]
- mám 2 tabulky a dostanu 3. s 1 sloupcem
- systém postupu
	- pokud se záznam z tabulky A nachází ve všech možnostech tabulky B, bude se nacházet i ve výsledné tabulce
- používáme pro dotazy typu "*Osoba P má ráda všechny filmy tvůrce C.*"
- např. mějme tyto 2 tabulky (`peoples_car` a `car_brands`)
```sql
| person | car      |
| ------ | -------- |
| John   | Audi     |
| Peter  | Mercedes |
| Peter  | Skoda    |
| Zoe    | Skoda    |
| Zoe    | Audi     |
| Jane   | Mercedes |

| car      |
| -------- |
| Mercedes |
| Skoda    |
```
- Relačním podílem `peoples_car` a `car_brands` bychom získali následující tabulku
```sql
| person |
| ------ |
| Peter  |
```

