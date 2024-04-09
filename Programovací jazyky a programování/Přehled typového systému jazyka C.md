## **Základní datové typy:**

1. **Integer (celočíselné typy):**
    - `int`: Standardní celočíselný typ.
    - `short int`: Krátký celočíselný typ.
    - `long int`: Dlouhý celočíselný typ.
    - `unsigned int`: Bez znaménka.
2. **Floating-point (plovoucí desetinné číslo):**
    - `float`: Jednoduchá přesnost s pohyblivou řádovou čárkou.
    - `double`: Dvojitá přesnost s pohyblivou řádovou čárkou.
    - `long double`: Rozšířená přesnost s pohyblivou řádovou čárkou.
3. **Character (znakové typy):**
    - `char`: Reprezentace jednoho znaku nebo malého celého čísla.
4. **Void (prázdný typ):**
    - `void`: Používá se pro funkce, které nevracejí hodnotu, a pro ukazatele bez konkrétního typu.

## Ukazatele:

- Ukazatele jsou proměnné, které obsahují adresu v paměti.
- Deklarace ukazatele se provádí před typem proměnné, např. `int *ptr;` pro ukazatel na celé číslo.
- Ukazatele mohou být použity k práci s dynamickou pamětí a pro předávání adres funkcím pro manipulaci s daty mimo danou funkci.
```C
#include <stdio.h>

int main() {
    int num = 10; // Deklarace a inicializace celočíselné proměnné
    int *ptr;     // Deklarace ukazatele na celočíselnou hodnotu

    ptr = &num;   // Nastavení ukazatele tak, aby ukazoval na adresu proměnné num

    // Výpis hodnoty proměnné num a hodnoty uložené na adrese, na kterou ukazuje ptr
    printf("Hodnota promenne num: %d\n", num);
    printf("Hodnota na adrese, kam ukazuje ptr: %d\n", *ptr);

    // Změna hodnoty proměnné num pomocí ukazatele
    *ptr = 20; //Pomocí operátoru dereference měníme hodnotu a né adresu

    // Výpis změněné hodnoty proměnné num
    printf("Nova hodnota promenne num: %d\n", num);

    return 0;
}

```
## Typové modifikátory:

- `const`: Určuje, že hodnota proměnné je neměnná.
- `volatile`: Indikuje, že hodnota proměnné se může změnit mimo běh programu.
- `signed`/`unsigned`: Určuje, zda může být hodnota typu záporná (signed) nebo je vždy nezáporná (unsigned).

## Struktury a uniony:

- `struct`: Slouží k vytvoření složených datových typů, které mohou obsahovat různé typy dat pod jedním názvem.
- `union`: Podobné strukturám, ale všechny členy sdílejí stejnou paměťovou lokaci, což umožňuje ušetřit paměť.
```C
#include <stdio.h>
#include <string.h>

// Definice struktury pro uchování informací o studentovi
struct Student {
    int id;
    char name[50];
    float gpa;
};

// Definice unionu pro uchování hodnoty buď jako celé číslo nebo jako desetinné číslo
union Number {
    int integer;
    float floating_point;
};

int main() {
    // Vytvoření instance struktury Student
    struct Student student1;
    student1.id = 123;
    strcpy(student1.name, "Jan Novak");
    student1.gpa = 3.75;

    // Vytvoření instance unionu Number
    union Number num;
    num.integer = 10;
    printf("Hodnota integer: %d\n", num.integer);

    // Přiřazení hodnoty desetinného čísla do unionu
    num.floating_point = 5.5;
    // Hodnota integer se přepíše, ale hodnota floating_point zůstane zachována
    printf("Hodnota integer po přiřazení floating_point: %d\n", num.integer);
    printf("Hodnota floating_point: %f\n", num.floating_point);

    return 0;
}
```
## Výčty (enum):

- `enum`: Definuje soubor pojmenovaných celočíselných konstant, které mohou být použity v kódu pro zvýšení čitelnosti.

```C
#include <stdio.h>

// Definice výčtu (enum) pro dny v týdnu
enum Days {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
};

int main() {
    // Deklarace proměnné typu enum Days
    enum Days today;

    // Nastavení hodnoty proměnné today na pondělí (MONDAY)
    today = MONDAY;

    // Výpis aktuálního dne
    switch(today) {
        case MONDAY:
            printf("Dnes je pondeli.\n");
            break;
        case TUESDAY:
            printf("Dnes je utery.\n");
            break;
        case WEDNESDAY:
            printf("Dnes je streda.\n");
            break;
        case THURSDAY:
            printf("Dnes je ctvrtek.\n");
            break;
        case FRIDAY:
            printf("Dnes je patek.\n");
            break;
        case SATURDAY:
            printf("Dnes je sobota.\n");
            break;
        case SUNDAY:
            printf("Dnes je nedele.\n");
            break;
        default:
            printf("Neplatny den.\n");
            break;
    }

    return 0;
}

```

## Typové přetypování:

- Přetypování umožňuje změnit typ proměnné na jiný typ.
- Například `(int) 5.5` provede přetypování desetinného čísla na celé číslo.