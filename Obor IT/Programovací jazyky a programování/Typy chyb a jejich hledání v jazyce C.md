### 1. Syntax Errors (Chyby syntaxe):

Syntax errors se vyskytují, když je v kódu nalezena neplatná syntaxe, kterou překladač nemůže pochopit. Syntax errors jsou detekovány při překladu kódu pomocí kompilátoru. Jsou zpravidla doprovázeny výzvou, která ukazuje, kde byla nalezena chyba v kódu.

```C
#include <stdio.h>

int main() {
    printf("Hello, world!"  // Chybějící uzavírací závorka
    return 0;
}
```

### 2. Runtime Errors (Běhové chyby):

Runtime errors se objevují, když program běží a narazí na chybu, která se neobjevila během překladu, například dělení nulou nebo přístup k neplatné paměti.

```C
#include <stdio.h>

int main() {
    int x = 10;
    int y = 0;
    int result = x / y;  // Dělení nulou
    return 0;
}
```

### 3. Logic Errors (Logické chyby):

Logic errors jsou chyby v implementaci, kdy kód produkuje nežádoucí výsledky kvůli chybnému algoritmu nebo nesprávnému výpočtu.

```C
#include <stdio.h>

int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    printf("%d\n", factorial(5));  // Správný výstup: 120
    printf("%d\n", factorial(-1));  // Logická chyba: Factorial of negative number
    return 0;
}
```

### 4. Memory Errors (Chyby paměti):

Chyby paměti jsou častým problémem v jazyce C a mohou mít závažné důsledky. Některé z běžných chyb paměti zahrnují:

- **Segmentation Fault (Přetečení paměti):** Vzniká, když program přistupuje k paměti, ke které nemá oprávnění. To může nastat při pokusu o čtení nebo zápis do neplatné paměti.

```C
#include <stdio.h>

int main() {
    int *ptr = NULL;
    *ptr = 10;  // Přístup k neinicializovanému ukazateli
    return 0;
}
```

- **Memory Leaks (Úniky paměti):** Vznikají, když program dynamicky alokuje paměť, ale neuvolňuje ji správně, což vede ke ztrátě dostupné paměti a může způsobit, že program zpomalí nebo spadne.

```C
#include <stdlib.h>

int main() {
    while (1) {
        int *ptr = malloc(100 * sizeof(int));  // Neuvolněná paměť
    }
    return 0;
}
```

### 5. Undefined Behavior (Nedefinované chování):

Nedefinované chování je situace, kdy standard jazyka C nedefinuje výsledek určité operace. To může vést k neočekávanému chování programu, což je obtížné identifikovat a debugovat.

```C
#include <stdio.h>

int main() {
    int a = 10;
    int b = 0;
    int result = a / b;  // Nedefinované chování - dělení nulou
    printf("%d\n", result);
    return 0;
}
```

## Hledání chyb:

- **Valgrind:** Nástroj Valgrind poskytuje detekci memory leaks a dalších chyb paměti pomocí nástrojů jako Memcheck.
- **Statická analýza:** Některé nástroje pro statickou analýzu kódu mohou identifikovat potenciální chyby paměti a nedefinované chování v kódu.
- **Manuální inspekce kódu:** Pečlivé prohlížení kódu s ohledem na správu paměti a manipulaci s ukazateli může odhalit chyby, jako jsou memory leaks a segmentační chyby.

##### Navigace
Předchozí:  [[Principy adresování a práce s pointery v jazyce C]]
Následující: [[Organizace kódu v jazyce C]]
Celý okruh: [[3. Programovací jazyky a programování]]