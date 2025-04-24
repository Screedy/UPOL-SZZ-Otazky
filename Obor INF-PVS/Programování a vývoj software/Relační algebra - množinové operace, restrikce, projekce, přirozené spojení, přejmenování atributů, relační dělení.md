## Relační algebra
- Je tvořena operacemi
	- průnik, sjednocení, rozdíl
	- restrikce, projekce, spojení, přejmenování
- **skalární typ** = říká jakého typu hodnota je (text, interger, boolean atd.)
- `null` nemá žádný skalární typ
- **sloupec má záhlaví**, které se skládá z názvu a skalárního typu

- v praxi relace reprezentujeme tabulkami a pro jejich správu máme NoSQL a [[SQL]]

- **relační kalkul** je jazyk, který vychází z predikátové logiky
	- má stejné schopnosti jako relační algebra
## Operace na relacích
- značení podmínky $\theta$ ... *théta*
#### Restrikce relace $\delta$
- omezení řádků (podmožina relace) v tabulce
#### Projekce relace $\Pi$
- výběr sloupců
- pokud nějaké sloupce omezením může pak tabulka působit duplicitně, přestože původní má řádky unikátní
#### Spojení relací $\bowtie$
- pokud disjunktní -> **kartézský součin**
- jinak spojíme podle stejných sloupců
#### Přejmenování atributů $\rho$
- změna názvu sloupců
- pro více účelů (lepší orientace, aby se sloupce se stejnými hodnotami nesloučily)

- jednotlivé operace můžeme řetězit a dostat výsledný složený zápis, případně je převádět do [[SQL]] a naopak
![[Screenshot 2022-12-10 at 10.41.28.png]]
#### Relační dělení
![[Screenshot 2022-12-10 at 10.37.47.png]]
- mám 2 tabulky a dostanu 3. s 1 sloupcem
- systém postupu
	- pokud se záznam z tabulky A nachází ve všech možnostech tabulky B, bude se nacházet i ve výsledné tabulce
- používáme pro dotazy typu "*Osoba P má ráda všechny filmy tvůrce C.*"