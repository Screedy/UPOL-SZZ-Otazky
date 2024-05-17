- Typový systém jazyka C zahrnuje primitivní datové typy, odvozené typy, složené typy a ukazatele.

## **Primitivní datové typy**
1. **Integer (celá čísla):**
    - `int (4B)`: Standardní celočíselný typ.
    - `short int (2B)`: Krátký celočíselný typ.
    - `long int (4B)`: Dlouhý celočíselný typ.
    - `unsigned int (4B)`: Bez znaménka.
2. **Floating-point numbers (desetinná číslo):**
    - `float (4B)`: Jednoduchá přesnost s pohyblivou řádovou čárkou.
    - `double (8B)`: Dvojitá přesnost s pohyblivou řádovou čárkou.
    - `long double (12B - 32bit a 16B - 64bit)`: Rozšířená přesnost s pohyblivou řádovou čárkou.
3. **Character (znakové typy):**
    - `char (1B)`: Reprezentace jednoho znaku nebo malého celého čísla.
4. **Void (prázdný typ):**
    - `void`: Používá se pro funkce, které nevracejí hodnotu, a pro ukazatele bez konkrétního typu.
5. **Enum (Enumerace):**
	- enum: Umožňuje definovat typ, který může mít jednu z několika pojmenovaných hodnot.
	- `enum week { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };`

## Odvozené typy
1. **Array (pole):**
	- Pole je kolekce prvků stejného typu uložených v sousedních paměťových místech.
```C
int arr[5] = {1, 2, 3, 4, 5};
```
2. **Pointers (ukazatele):**
	- Ukazatele jsou proměnné, které obsahují adresu v paměti.
	- Deklarace ukazatele se provádí před typem proměnné, např. `int *ptr;` pro ukazatel na celé číslo.
	- Ukazatele mohou být použity k práci s dynamickou pamětí a pro předávání adres funkcím pro manipulaci s daty mimo danou funkci.
```C
int num = 10; // Deklarace a inicializace celočíselné proměnné
int *ptr;     // Deklarace ukazatele na celočíselnou hodnotu

ptr = &num;   // Nastavení ukazatel tak, aby ukazoval na adresu proměnné num

// Změna hodnoty proměnné num pomocí ukazatele
*ptr = 20; //Pomocí operátoru dereference měníme hodnotu a né adresu

printf("Hodnota na adrese, kam ukazuje ptr: %d\n", *ptr);
```
3. **Strings (řetězce):**
	- V C jsou řetězce implementovány jako pole znaků zakončené nulovým znakem `\0`.
```C
char str[] = "Hello, World!";
```
4. **Structures (struktury):**
	- Struktura je uživatelem definovaný typ, který umožňuje seskupení různých typů dat pod jeden název.
```C
struct Person {
    char name[50];
    int age;
    float salary;
};

struct Person p1;
```
5. **Unions (uniony):**
	- Unie je podobná struktuře, ale všechny její členy sdílejí stejnou paměťovou oblast.
	- To znamená, že v unii může být v daném okamžiku uložen pouze jeden člen, a všechny ostatní členy přepíšou stejnou oblast paměti.
```C
union Data {
    int i;
    float f;
    char str[20];
};

union Data data;
```

## Složené typy
- Složené typy jsou typy, které kombinují více primitivních nebo odvozených typů
1. **Pole struktur:**
```C
struct Person people[5];
```
2. **Pole ukazatelů:**
```C
int *ptrArr[5];
```
3. a další


## Typové modifikátory:

- `const`: Určuje, že hodnota proměnné je neměnná.
	- `const int constantValue = 10;`
- `volatile`: Indikuje, že hodnota proměnné se může změnit mimo kontrolu programu
	- například hardwarovým zařízením
	- `volatile int sensorValue;`
- `signed`/`unsigned`: Určuje, zda může být hodnota typu záporná (signed) nebo je vždy nezáporná (unsigned).
- `restrict`: používá se s ukazateli, aby kompilátoru sdělilo, že ukazatel je jediným referenčním ukazatelem na objekt, na který ukazuje.

## Typové přetypování:

- Přetypování umožňuje změnit typ proměnné na jiný typ.
- Například `(int) 5.5` provede přetypování desetinného čísla na celé číslo.

##### Navigace
Předchozí:  [[Večeřící filozofové]]
Následující: [[Principy správy paměti v jazyce C]]
Celý okruh: [[3. Programovací jazyky a programování]]