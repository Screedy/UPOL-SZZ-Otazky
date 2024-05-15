## **Dynamická alokace paměti**:

- V jazyce C můžete alokovat paměť dynamicky za běhu programu pomocí funkcí `malloc()`, `calloc()`, `realloc()`.

- `malloc(size_t size)` alokuje paměť určenou velikostí `size` a vrací ukazatel na začátek alokované paměti.

- `calloc(size_t num, size_t size)` alokuje paměť pro `num` prvků velikosti `size` každý a inicializuje je na nulu.

- `realloc(void *ptr, size_t size)` změní velikost již alokované paměti na `size`. Pokud je `ptr` `NULL`, chování je stejné jako u `malloc()`.

## **Správa alokované paměti**:

- Po použití alokované paměti je důležité ji uvolnit pomocí funkce `free()`, abyste zabránili paměťovým únikům.

- `free(void *ptr)` uvolní paměť, na kterou ukazuje `ptr`. Po uvolnění paměti je ukazatel neplatný a neměl by být použit

## **Správné použití ukazatelů**:

- Ukazatele jsou klíčovým prvkem pro práci s pamětí v jazyce C. Je důležité zajistit, aby byly ukazatele řádně inicializovány a aby neukazovaly na neplatnou nebo uvolněnou paměť.

- Nebezpečné operace jako je dereferencování neinicializovaných nebo neplatných ukazatelů mohou vést k chybám v běhu programu.

## **Paměťové úniky**:

- Paměťové úniky nastávají, když alokovaná paměť není uvolněna a program již na ni nemá odkaz.

- Paměťové úniky mohou vést k postupnému plnění paměti a zhoršování výkonu programu. Je důležité pečlivě sledovat, kde se alokuje a uvolňuje paměť, a minimalizovat riziko paměťových úniků.

## **Správné použití statické a automatické paměti**:

- Kromě dynamické alokace paměti máte v C také statickou paměť (deklarace globálních proměnných nebo statických lokálních proměnných) a automatickou paměť (lokální proměnné vytvořené uvnitř funkce).

- Statická paměť existuje po celou dobu běhu programu, zatímco automatická paměť je platná pouze do konce bloku, ve kterém byla vytvořena.

## **Paměťové útoky**:

- Je důležité si být vědom možných paměťových útoků jako jsou útoky typu buffer overflow, které mohou vést k nežádoucímu přepisování paměti a zneužití programu.

Zde je typický scénář, jak k buffer overflow útoku může dojít:

1. **Alokace paměti pro buffer**: Program alokuje paměť pro buffer s určitou velikostí. Například:

```C
char buffer[10];
```

2. **Překročení kapacity bufferu**: Program následně čte nebo zapisuje do bufferu více dat, než je jeho kapacita. Například:

```C
#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10]; // Buffer s kapacitou 10 znaků
    printf("Zadejte text (max. 10 znaků): ");
    scanf("%s", buffer); // Přečte vstup od uživatele

    // Zde může dojít k buffer overflow útoku, pokud uživatel zadá více než 10 znaků
    printf("Váš text: %s\n", buffer);
    
    return 0;
}
```

3. **Přepsání paměti**: Pokud uživatel zadá více dat než je velikost bufferu, data se zapisují mimo paměťový blok určený pro buffer. To může vést k přepsání jiných důležitých dat v paměti, včetně návratové adresy, ukazatelů nebo jiných proměnných.

4. **Potenciální zneužití útočníkem**: Pokud útočník dokáže vhodně manipulovat s daty zapsanými za hranice bufferu, může zneužít tuto chybu k provádění škodlivých akcí, jako je spuštění škodlivého kódu, získání citlivých informací nebo destabilizace programu.

##### Navigace
Předchozí:  [[Přehled typového systému jazyka C]]
Následující: [[Principy adresování a práce s pointery v jazyce C]]
Celý okruh: [[3. Programovací jazyky a programování]]