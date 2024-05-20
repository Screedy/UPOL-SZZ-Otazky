- Organizace kódu v jazyce C je klíčová pro vytváření přehledného, udržovatelného a efektivního softwaru. 
- Dobrá organizace kódu usnadňuje jeho čtení, ladění a rozšiřování.

## **Struktura projektu:**

1. **Hlavičkové soubory (*.h):** Obsahují deklarace funkcí a datových typů, které jsou dostupné pro ostatní moduly.
2. **Implementační soubory (*.c):** Obsahují samotnou implementaci funkcí a datových struktur.
3. **Makefile:** Konfigurační soubor pro sestavení projektu, definující závislosti a postupy sestavení.

## Konvence pro organizaci kódu
1. **Modularita**: 
	- Rozdělení kódu do logických modulů (funkcí a souborů) podle jejich funkčnosti. 
	- **Funkce**: Každá funkce by měla mít jednoznačně definovaný účel a měla by být zodpovědná za jednu úlohu.
	- **Soubory**: Kód by měl být rozdělen do více souborů, kde každý soubor má specifický účel.
2. **Rozdělení do hlavičkových souborů (.h) a zdrojových souborů (.c)**: 
	- Deklarace funkcí, struktur a globálních proměnných by měly být v hlavičkových souborech, zatímco implementace by měla být v zdrojových souborech. 
	- To usnadňuje opětovné použití kódu a zlepšuje přehlednost.

3. **Správné používání záhlaví (#include)**: 
	- Použití záhlaví na začátku souborů pro zahrnutí potřebných knihoven a hlavičkových souborů.
	- Je důležité minimalizovat počet zahrnutých souborů a zahrnout pouze ty, které jsou skutečně potřebné.
```C
#include <stdio.h> - standardní knihovna
#include "myfile.h" - můj hlavičkový soubor
```
4. **Dobrá pojmenování**: 
	- Používání výstižných a významných názvů pro proměnné, funkce a soubory. 
	- To usnadňuje čtení a porozumění kódu.
5. **Konzistentní formátování kódu**: 
	- Dodržování konzistentního stylu formátování kódu (odsazení, pojmenování proměnných a funkcí, mezery) zvyšuje čitelnost a usnadňuje spolupráci více vývojářů.
	- **Proměnné**: `int counter;`
	- **Funkce**: `void calculateSum();`
	- **Konstanty**: `#define MAX_SIZE 100`
6. **Komentáře**: 
	- Přidávání komentářů k vysvětlení složitých částí kódu, zvláště pokud je kód obtížně čitelný nebo vyžaduje specifické vysvětlení.
```C
// Jednořádkový komentář

/*
 * Víceřádkový komentář
 * popisující funkci
 */
```
7. **Organizace souborů v projektech**:
	- Strukturování souborů a adresářů v projektu zlepšuje přehlednost a usnadňuje navigaci.
```
project/
├── include/
│   └── math.h
├── src/
│   ├── main.c
│   └── math.c
├── tests/
│   └── test_math.c
└── Makefile
```
8. **Error handling**: Správné zacházení s chybami a výjimkami, aby byl kód robustní a odolný vůči neočekávaným situacím.
```C
FILE *file = fopen("data.txt", "r");
if (file == NULL) {
    perror("Error opening file");
    return -1;
}
```
9. **Testování**:
	- Pravidelné testování kódu je klíčové pro odhalení chyb a ověření správné funkčnosti programu.
```C
// test_math.c
#include "math.h"
#include <assert.h>

void test_add() {
    assert(add(2, 3) == 5);
}

int main() {
    test_add();
    printf("All tests passed.\n");
    return 0;
}
```

##### Navigace
Předchozí:  [[Typy chyb a jejich hledání v jazyce C]]
Následující: [[Zařazení jazyka C mezi ostatní jazyky, výhody a nevýhody]]
Celý okruh: [[3. Programovací jazyky a programování]]