## Problém uváznutí (deadlock)
- deadlock je situace ve **vícevláknových nebo distribuovaných systémech**, kdy **dvě nebo více úloh zůstanou navždy zablokované**, protože **každá čeká** na **uvolnění zdrojů**, které jsou **drženy ostatními zablokovanými úlohami**.
>[!tldr] Podmínky vzniku deadlocku (Coffmanovy podmínky)
>1. **mutual exclusion** 
>	- **prostředky** jsou využívány **pouze jedním procesem** naráz
>2. **hold & wait** 
>	- proces může **žádat** **o další** prostředky, i když **už** nějaké **má**
>3. **no preemption**
>	- jakmile proces zmíněný prostředek vlastní, **nelze mu ho odejmout**
>	- musí jej **vrátit**
>4. **circular wait**
>	- dojde k uzavření cyklu, ve kterém každý proces čeká na uvolnění prostředků, který je přidělen jinému procesu v cyklu

## Detekce uváznutí
- Detekce uváznutí zahrnuje **sledování a analýzu** stavu alokace zdrojů a procesů, aby bylo možné identifikovat **výše uvedené podmínky**.
	- Operační systémy mohou udržovat **graf alokace zdrojů**. Uváznutí je detekováno, pokud **existuje cyklus v grafu**.
	- Existují také algoritmy, které pravidelně **kontrolují graf zdrojů a hledají cykly**.
		- Mohou být náročné na výkon.

### Metody předcházení uváznutí
1. **ignorování**
	- pštrosí algoritmus
	- v praxi se často používá
2. **detekce** (detection & recovery)
	- pokud vznikne deadlock, je detekován a nějaký proces je odstraněn
	- využívá graf prostředků a z něj odvozený graf čekání
3. **zamezení vzniku** (prevention)
	- modifikace zdrojových požadavků tak, aby byla eliminována alespoň jedna coffmanova podmínka vzniku deadlocku
4. **vyhýbání se uváznutí** (avoidance)
	- systém se snaží vyhovět těm požadavkům, které nevedou k uváznutí

##### Navigace
Předchozí: [[Správa procesoru - procesy a vlákna, plánování jejich běhu, komunikace a synchronizace]]
Následující: [[Správa operační paměti - segmentace, stránkování, virtuální paměť]]
Celý okruh: [[2. Informační technologie]]