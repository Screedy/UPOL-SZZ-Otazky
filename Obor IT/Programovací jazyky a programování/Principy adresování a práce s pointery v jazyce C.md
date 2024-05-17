- Adresování a práce s pointery (ukazateli) jsou klíčové aspekty programování v jazyce C. 
- Pointery umožňují přímý přístup a manipulaci s paměťovými adresami, což zvyšuje výkon a flexibilitu programů. 

## Pointery a jejich deklarace
- Pointer je proměnná, která obsahuje adresu jiné proměnné.
- definice: `type *pointer;`
```C
int *ptr;  // Pointer na integer
char *cptr;  // Pointer na char
```

## Adresování a operátor adresy
- Operátor `&` se používá k získání adresy proměnné.
- Každá proměnná nebo objekt v paměti má svou adresu, což je číselná hodnota, která určuje umístění v paměti.
```C
int a = 10;
int *ptr = &a;  // ptr nyní obsahuje adresu proměnné a
```

## Dereferencování pointeru
- Operátor `*` se používá k přístupu k hodnotě, na kterou pointer ukazuje.
```C
int a = 10;
int *ptr = &a;
int b = *ptr;  // b nyní obsahuje hodnotu 10
```

## Aritmetika pointerů
- Pointery podporují **aritmetiku**, což umožňuje **posun ukazatele** na další prvky pole.
- *Since the variable "y" stores 1000 (the address of "x"), we expect it to become 1001 because of the "++" operator, but it increments by 4, which is the size of "int" variable.*
```C
int x = 10; // created at address 1000 

// "y" is created at address 2000 
// it holds 1000 (address of "x") 
int *y = &x ; 
y++; // y becomes 1004
```
- U pole díky tomu můžeme hned vidět následující prvek:
```C
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;  // ptr ukazuje na začátek pole
ptr++;  // ptr nyní ukazuje na druhý prvek pole
int val = *ptr;  // val nyní obsahuje hodnotu 2
```

## Pointery na pointery
- Pointer může také ukazovat na jiný pointer, což umožňuje vytváření složitých datových struktur, jako jsou dynamicky alokované víceúrovňové pole nebo seznamy.
```C
int a = 10;
int *ptr = &a;
int **pptr = &ptr;  // Pointer na pointer
int val = **pptr;  // val nyní obsahuje hodnotu 10
```

## Pointery a dynamická alokace paměti
- Pointery se často používají pro práci s dynamicky alokovanou pamětí pomocí funkcí jako `malloc()`, `calloc()`, `realloc()` a `free()`.
```C
int *ptr = (int *)malloc(5 * sizeof(int));  // Alokace pole o 5 prvcích
if (ptr == NULL) {
    // Zpracování chyby při alokaci
}
for (int i = 0; i < 5; i++) {
    ptr[i] = i * 2;  // Inicializace pole
}
free(ptr);  // Uvolnění paměti
ptr = NULL;  // Prevence dereferencování neplatného pointeru
```

## Pointery a funkce
- Pointery mohou také ukazovat na funkce, což umožňuje dynamické volání funkcí.
```C
void func() {
    printf("Hello, World!\n");
}
void (*fptr)() = &func;  // Pointer na funkci
(*fptr)();  // Volání funkce přes pointer
```


## Vztah mezi polem a ukazatelem
- Pointery a pole jsou úzce spjaty. 
- Pole je ve skutečnosti konstantní pointer na první prvek pole.
```C
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;  // ekvivalentní k &arr[0]
for (int i = 0; i < 5; i++) {
    printf("%d ", *(ptr + i));  // Přístup k prvkům pole
}
```

## Bezpečnost práce s pointery
- Bezpečnost práce s pointery je kritická, protože chyby mohou vést k neplatným přístupům do paměti, což může způsobit pád programu nebo bezpečnostní zranitelnosti.
- **Zásady bezpečnosti:**
	- Nikdy nedereferencujte neplatný nebo `NULL` pointer.
	- Vyhněte se přístupu mimo hranice pole.
	- Po uvolnění paměti nastavte pointer na `NULL`.
	- Pravidelně používejte nástroje pro detekci chyb paměti, jako je Valgrind.

##### Navigace
Předchozí:  [[Principy správy paměti v jazyce C]]
Následující: [[Typy chyb a jejich hledání v jazyce C]]
Celý okruh: [[3. Programovací jazyky a programování]]