
- I/O zařízení jsou zásadní složkou Von Neumannovi architektury
## Typy zařízení
1. **Bloková zařízení**:
	- data jsou přenášena v blocích stejné velikosti
	- možné nezávisle adresovat/zapisovat/číst data po jednotlivých blocích
	- HDD, SSD, optické disky, ...
2. **Znaková zařízení**:
	- proud znaků/bytů (nelze se posouvat)
	- klávesnice, myš, tiskárna, terminál, ...
3. **Ostatní**:
	- nespadající ani do jedné kategorie
	- hodiny (přerušení), grafické rozhraní (mapovaná paměť), ...

## Přístup k zařízením
### Port-Mapped I/O
- registry jednotlivých zařízení mají samostatný adresní prostor (oddělený od paměti)
- přístupné přes operace `in`, `out` - čtení/zápis hodnoty z portu
>[!fail] Nevýhody
>- omezené na speciální operace
>- omezené řízení přístupu

### Memory-Mapped I/O
- registry jednotlivých zařízení jsou mapovány do paměťového prostoru
- data se čtou/zapisují přímo na sběrnici
>[!info] 
>>[!success] Výhody
>>- k začízení se přistupuje stejně jako k paměti (možné použít všechny instrukce)
>>- k řízení přístupu lze použít vše co pro paměť
>
>
>>[!fail] Problém
>>- cache, oddělená sběrnice pro paměť

## Přístup k I/O
### Aktivní čekání
- data se kopírují z bufferu do registru zařízení (popř. opačně)
- podle stavového registru se čeká, až budou přesunuta
- jednoduchá implementace, není efektivní

### I/O s přerušením
- není nutné čekat na dokončení přenosu dat
- v průběhu přenosu může procesor provádět další činnost
- po čas přenosu dat je proces zablokován
- přenos dat řídí obsluha přerušení

### I/O s DMA (Direct Memory Access)
- řadič DMA dostane požadavek: čtení + cílová adresa
- předá požadavek řadiči disku
- zapisuje data do paměti
- dokončení je oznámeno řadiči DMA
- DMA vyvolá přerušení
>[!Example]+ Ukázka DMA
>![[MacBook-2024-05-03-001164@2x.png]]

### Bufferování
- optimalizace přenosu dat - zpoždění zápisu/čtení
- ve skutečnosti dva buffery (v každém prostoru jeden)
>[!Example]+ Bufferování
>![[MacBook-2024-05-03-001165@2x.png]]


## Ovladače zařízení
- zajišťují přístup k zařízení (zápis, čtení, inicializace, správa, napájení, logování, ...)
- typicky součást jádra OS
- zakompilována do jádra (pomocí modulů) nebo dynamicky načítané (pomocí knihoven)
- měl by být dodáván výrobcem HW

##### Navigace
Předchozí: [[Správa operační paměti - segmentace, stránkování, virtuální paměť]]
Následující: [[Správa diskového prostoru - oddíly, souborové systémy, zajištění konzistence dat]]
Celý okruh: [[2. Informační technologie]]