Principy adresování a práce s ukazateli (pointery) jsou základními koncepty v jazyce C. Ukazatele umožňují pracovat s pamětí přímo a poskytují možnost dynamické alokace paměti a efektivní manipulace s daty. Zde jsou klíčové principy adresování a práce s ukazateli v jazyce C:

## **Adresování paměti**:

- V jazyce C můžete pracovat s pamětí pomocí adres. Každá proměnná nebo objekt v paměti má svou adresu, což je číselná hodnota, která určuje umístění v paměti.

- Adresu proměnné získáte pomocí operátoru `&`. Například `&variable` vrátí adresu proměnné `variable`.

## **Ukazatele (pointery)**:

- Ukazatel je proměnná, která obsahuje adresu jiné proměnné nebo objektu v paměti.

- Definice ukazatele vypadá takto: `type *pointer;`, kde `type` je typ dat, na který ukazatel odkazuje.

- Ukazatel se inicializuje přiřazením adresy existující proměnné: `int *ptr = &variable;`

## **Dereferencování ukazatele**:

- Dereferencování ukazatele znamená přístup k hodnotě, na kterou ukazuje.

- Dereferencování se provádí pomocí operátoru `*`. Například `*ptr` vrátí hodnotu, na kterou ukazuje ukazatel `ptr`.

## **Operace s ukazateli**:

- Ukazatele mohou být inkrementovány nebo dekrementovány, což se vztahuje k přesunutí adresy v paměti o počet bajtů odpovídající velikosti datového typu, na který ukazatel ukazuje.

- Aritmetika ukazatelů je velmi užitečná pro práci s poli a dynamickou alokací paměti.

## **Dynamická alokace paměti**:

- Ukazatele jsou často používány pro dynamickou alokaci paměti za běhu programu pomocí funkcí jako `malloc()`, `calloc()` a `realloc()`.

- Například: `int *array = (int*)malloc(n * sizeof(int));`

## **Uvolňování alokované paměti**:

- Po použití alokované paměti je důležité ji uvolnit pomocí funkce `free()`, aby nedocházelo k paměťovým únikům.

- Například: `free(array);`

## **Vztah mezi polem a ukazatelem**:

- Pole v jazyce C je ve skutečnosti ukazatel na jeho první prvek.

- Pokud máte pole `int array[5];`, můžete získat ukazatel na jeho první prvek pomocí `int *ptr = array;`.

Příklad práce s pointerem:
```C
#include <stdio.h>

int main() {
    int variable = 10; // Deklarace a inicializace proměnné
    
    int *ptr; // Deklarace ukazatele
    ptr = &variable; // Přiřazení adresy proměnné ukazateli
    
    printf("Hodnota proměnné: %d\n", variable); // Výpis hodnoty proměnné
    printf("Adresa proměnné: %p\n", (void*)&variable); // Výpis adresy proměnné
    printf("Hodnota ukazatele: %d\n", *ptr); // Výpis hodnoty, na kterou ukazuje ukazatel
    printf("Adresa ukazatele: %p\n", (void*)ptr); // Výpis adresy, kam ukazatel ukazuje
    
    return 0;
}
```

Příklad práce s pointerem a polem:
```C
#include <stdio.h>

int main() {
    int array[] = {10, 20, 30, 40, 50}; // Deklarace a inicializace pole

    // Deklarace ukazatele na int
    int *ptr;

    // Ukazatel nastavíme na začátek pole
    ptr = array;

    // Výpis prvků pole pomocí ukazatele
    printf("Prvky pole: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", *ptr); // Výpis hodnoty, na kterou ukazuje ukazatel
        ptr++; // Posuneme ukazatel na další prvek v poli
    }
    printf("\n");

    return 0;
}
```

##### Navigace
Předchozí:  [[Principy správy paměti v jazyce C]]
Následující: [[Typy chyb a jejich hledání v jazyce C]]
Celý okruh: [[3. Programovací jazyky a programování]]