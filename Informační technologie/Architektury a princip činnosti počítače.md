### John von Neumannova architektura
![[MacBook-2024-03-17-000893.png| 500]]
- CPU:
	- ALU (Aritmeticko-logická jednotka), provádí výpočty
	- řadič (řídící jednotka), stará se o komunikaci po sběrnici
- Operační paměť:
	- Společná pro program i data (lehčí implementace, horší časová náročnost)
- Sběrnice (datová, instrukční, řídící - byla schopná dělat vše)

- Výhody:
	- Rozdělení paměti pro kód a data provádí programátor
	- Řídící jednotka přistupuje do paměti pro kód i data stejným způsobem
	- Jedna sběrnice - jednodušší a levnější výroba
- Nevýhody:
	- Procesor může najednou pouze číst (resp. zapisovat) data nebo instrukce (von Neumann bottleneck)
	- společné uložení dat a kódu může při chybě vést k přepsání vlastního kódu

- program = předpis pro řešení úlohy, zápis algortmu, posloupnost elementárních kroků (tzv. instrukcí)
- instrukce = interpretovaná (binární) data - mezi programem a zpracovávanými daty není z technického hlediska rozdíl

### Harvardská architektura počítače
![[MacBook-2024-03-17-000894.png|| 500]]
- Velice podobná John von Neumannově, až na oddělené paměti pro program a pro data (ty tedy lze číst současně)

- Výhody:
	- Program nemůže přepsat sám sebe
	- Paměti mohou být vyrobeny odlišnými technologiemi
	- Každá paměť může mít jinou velikost nejmenší adresovací jednotky
	- Lze přistupovat pro instrukce i data současně
- Nevýhody:
	- Dvě sběrnice kladou vyšší nároky na vývoj řídící jednotky procesoru a zvyšují i náklady na výrobu výsledného počítače
	- Nevyužitou část paměti dat nelze použít pro program a obráceně