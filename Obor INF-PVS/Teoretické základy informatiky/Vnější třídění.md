---
tags:
  - algo1
---
- Technika používající se pro třídění velkých objemů dat (nevejdou se do operační paměti)
- Z logiky věci plyne že je výrazně pomalejší (kvůli využití vnější paměti)
#### Technika vnějšího třídění
- Můžeme rozdělit na 2 fáze
1) Fáze rozdělování
	- Data se rozdělí na menší bloky (= *běhy*) (musí se vejít do interní paměti)
	- Každý blok se jednotlivě setřídí běžným (interním) tříděním
	- Jednotlivé setříděné bloky se pak zapíšou do vnější pamětí
2) Fáze zatřiďování
	- Otevře se více *běhů* a postupně se z nich čte
	- Postupně nově slité setříděné hodnoty zapisujeme do souborů

- Můžeme urychlit pokud použijeme algoritmus vnitřního třídění jako Quick Sort nebo Merge Sort (na menší části)
#### Časová složitost
- Čtení a ukládání má složitost $O(N)$
- Samotný algoritmus vnitřního třídění pak $O(\log n)$
- Celkově tedy $O(\log n)$ (záleží na použití třídícího algoritmu ve vnějším třídění)