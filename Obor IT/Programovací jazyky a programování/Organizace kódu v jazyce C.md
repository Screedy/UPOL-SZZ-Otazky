
## **Struktura projektu:**

1. **Hlavičkové soubory (*.h):** Obsahují deklarace funkcí a datových typů, které jsou dostupné pro ostatní moduly.
2. **Implementační soubory (*.c):** Obsahují samotnou implementaci funkcí a datových struktur.
3. **Makefile:** Konfigurační soubor pro sestavení projektu, definující závislosti a postupy sestavení.

## Konvence pro rozdělení kódu

1. **Modularita**: Rozdělení kódu do logických modulů (funkcí a souborů) podle jejich funkcí. Každý modul by měl mít jednoznačný účel a měl by být nezávislý na ostatních modulech.

2. **Rozdělení do hlavičkových souborů (.h) a zdrojových souborů (.c)**: Deklarace funkcí, struktur a globálních proměnných by měly být v hlavičkových souborech, zatímco implementace by měla být v zdrojových souborech. To usnadňuje opětovné použití kódu a zlepšuje přehlednost.

3. **Správné používání záhlaví (#include)**: Použití záhlaví na začátku souborů pro zahrnutí potřebných knihoven a hlavičkových souborů. Je důležité minimalizovat počet zahrnutých souborů a zahrnout pouze ty, které jsou skutečně potřebné.
```C
#include <stdio.h> - standardní knihovna
#include "myfile.h" - můj hlavičkový soubor
```

5. **Dobrá pojmenování**: Používání výstižných a významných názvů pro proměnné, funkce a soubory. To usnadňuje čtení a porozumění kódu.

6. **Správné formátování kódu**: Důraz na správné zarovnání, odsazení a používání bílých znaků pro zlepšení čitelnosti kódu. Běžné konvence zahrnují používání odsazení o 4 mezery pro každou úroveň a konzistentní používání složených závorek.

7. **Komentáře**: Přidávání komentářů k vysvětlení složitých částí kódu, zvláště pokud je kód obtížně čitelný nebo vyžaduje specifické vysvětlení.

8. **Správa paměti**: Pokud program pracuje s dynamickou pamětí (např. alokace a dealokace paměti pomocí funkcí malloc() a free()), je důležité pečlivě spravovat paměť a zabránit únikům paměti a jiným chybám.

9. **Error handling**: Správné zacházení s chybami a výjimkami, aby byl kód robustní a odolný vůči neočekávaným situacím.