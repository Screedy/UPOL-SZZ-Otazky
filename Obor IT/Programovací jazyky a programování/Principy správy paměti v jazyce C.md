## Statická alokace paměti
- Statická alokace paměti se provádí během kompilace a zahrnuje pevně definované oblasti paměti.
- Tyto oblasti jsou pevně spojeny s proměnnými a jsou alokovány na zásobníku nebo v datové oblasti programu.
- **Zásobník (stack)**
	- Obsahuje lokální proměnné funkcí a jejich hodnoty
	- Je automaticky uvolňována při opuštění funkce
- **Datová oblast (data segment)**
	- globální a statické proměnné jsou uloženy v této oblasti
	- rozdělena na inicializovanou a neinicializovanou část

## Dynamická alokace paměti
- V jazyce C můžete alokovat paměť dynamicky za běhu programu pomocí funkcí `malloc()`, `calloc()`, `realloc()`.
- Tento typ alokace poskytuje flexibilitu, protože umožňuje alokovat a uvolňovat paměť podle potřeby.

>[!Example] `malloc(size_t size)`
>```C
>int *ptr = (int *)malloc(sizeof(int) * n);
>```
>- Alokuje požadovanou velikost paměti v bajtech a vrací ukazatel na první byte přiděleného bloku. 
>- Paměť není inicializována.

>[!Example] `calloc(size_t num, size_t size)`
>```C
>int *ptr = (int *)calloc(n, sizeof(int));
>```
>- Alokuje paměť pro `num` prvků velikosti `size` každý a inicializuje je na nulu.

>[!Example] `realloc(void *ptr, size_t size)`
>```C
>ptr = (int *)realloc(ptr, new_size);
>```
>- Změní velikost již alokované paměti na `size`. 
>- Pokud je `ptr` `NULL`, chování je stejné jako u `malloc()`.

- Po použití alokované paměti je důležité ji uvolnit pomocí funkce `free()`, abyste zabránili paměťovým únikům.

>[!Example] `free(void *ptr)`
>```C
>free(ptr);
>ptr = NULL;
>```
>- uvolní paměť, na kterou ukazuje `ptr`. 
>- Po uvolnění paměti je ukazatel neplatný a neměl by být použit

## **Správné použití ukazatelů**:
- Ukazatele jsou klíčovým prvkem pro práci s pamětí v jazyce C. Je důležité zajistit, aby byly ukazatele řádně inicializovány a aby neukazovaly na neplatnou nebo uvolněnou paměť.
- Nebezpečné operace jako je dereferencování neinicializovaných nebo neplatných ukazatelů mohou vést k chybám v běhu programu.

## **Paměťové úniky**:
- Paměťové úniky nastávají, když alokovaná paměť není uvolněna a program již na ni nemá odkaz.
- Paměťové úniky mohou vést k postupnému plnění paměti a zhoršování výkonu programu. Je důležité pečlivě sledovat, kde se alokuje a uvolňuje paměť, a minimalizovat riziko paměťových úniků.

## **Paměťové útoky**:
- Je důležité si být vědom možných paměťových útoků jako jsou útoky typu buffer overflow, které mohou vést k nežádoucímu přepisování paměti a zneužití programu.

>[!Example] scénář útoku
>1. **Alokace paměti pro buffer**: Program alokuje paměť pro buffer s určitou velikostí. Například:
>
>```C
>char buffer[10];
>```
>
>2. **Překročení kapacity bufferu**: Program následně čte nebo zapisuje do bufferu více dat, než je jeho kapacita. Například:
>
>```C
>#include <stdio.h>
>#include <string.h>
>
>int main() {
> 	char buffer[10]; // Buffer s kapacitou 10 znaků
> 	printf("Zadejte text (max. 10 znaků): ");
> 	scanf("%s", buffer); // Přečte vstup od uživatele
>
> 	// Zde může dojít k buffer overflow útoku, pokud uživatel zadá více než 10 znaků
> 	printf("Váš text: %s\n", buffer);
>  
> 	return 0;
>}
>```
>
>3. **Přepsání paměti**: Pokud uživatel zadá více dat než je velikost bufferu, data se zapisují mimo paměťový blok určený pro buffer. To může vést k přepsání jiných důležitých dat v paměti, včetně návratové adresy, ukazatelů nebo jiných proměnných.
>4. **Potenciální zneužití útočníkem**: Pokud útočník dokáže vhodně manipulovat s daty zapsanými za hranice bufferu, může zneužít tuto chybu k provádění škodlivých akcí, jako je spuštění škodlivého kódu, získání citlivých informací nebo destabilizace programu.

##### Navigace
Předchozí:  [[Přehled typového systému jazyka C]]
Následující: [[Principy adresování a práce s pointery v jazyce C]]
Celý okruh: [[3. Programovací jazyky a programování]]