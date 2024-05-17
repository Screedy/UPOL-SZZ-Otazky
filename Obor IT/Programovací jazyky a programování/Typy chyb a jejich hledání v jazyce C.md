### Syntaktické chyby (Syntax Errors)
- Syntaktické chyby se vyskytují, když kód neodpovídá gramatickým pravidlům jazyka C. 
- Syntaktické chyby jsou odhaleny kompilátorem, který poskytne chybová hlášení s uvedením řádku a typu chyby.

>[!Example] Příklady syntaktických chyb
>- Chybějící středník:
>```C
>int a = 5  // Chybějící středník
>```
>- Nesprávně uzavřený blok kódu:
>```C
>if (a > 5) {
> 	printf("a is greater than 5");
>// Chybějící uzavírací závorka
>```

## Sémantické chyby (Semantic Errors)
- Sémantické chyby vznikají, když kód sice syntakticky správný, ale logicky chybný. 
- Kompilátor je nedokáže detekovat, protože neporušují pravidla jazyka.
- Detekce: Tyto chyby se často projeví během běhu programu a vyžadují testování a ladění.

>[!Example] Příklady sémantických chyb
>- Nesprávná inicializace proměnné:
>```C
>int a = 5;
>int b = a / 0;  // Dělení nulou
>```
>- Použití nesprávného operátoru:
>```C
>if (a = 5) {  // Místo '==' je použito '='
> 	printf("a is equal to 5");
>}
>```

## Chyby během běhu programu (Runtime Errors)
- Chyby během běhu se projeví při spuštění programu. 
- Může jít o chyby, které způsobí pád programu nebo nepředvídatelné chování.
- Detekce: Použití ladicích nástrojů jako GDB nebo Valgrind, které mohou pomoci identifikovat místo a příčinu chyby.

>[!Example] Příklady běhových chyb
>```C
>int arr[5];
>arr[10] = 3;  // Přístup mimo rozsah pole
>```
>- Nebo
>```C
>int *ptr = NULL;
>int val = *ptr;  // Dereferencování NULL pointeru
>```

## Logické chyby (Logic Errors)
- Logické chyby vznikají, když kód neprovádí zamýšlenou činnost. 
- Program běží bez chyb, ale výsledky nejsou správné.
- Detekce: Pečlivé testování a kontrola výsledků, někdy použití **unit testů** nebo jiných testovacích technik.

>[!Example] Příklady logických chyb
>- Nesprávný algoritmus:
>```C
>int sum = 0;
>for (int i = 1; i <= 10; i++) {
> 	sum -= i;  // Místo 'sum += i'
>}
>```

## Chyby ve správě paměti (Memory Management Errors)
- Chyby ve správě paměti zahrnují úniky paměti, dvojité uvolnění paměti a přístupy k neplatným paměťovým oblastem.
- Detekce: Nástroje jako Valgrind mohou pomoci odhalit chyby v alokaci a uvolňování paměti.

>[!Example] Příklad chyb ve správě paměti
>- Únik paměti:
>```C
>int *ptr = (int *)malloc(sizeof(int) * 10);
>// Nedochází k volání free(ptr);
>```
>- Dvojité uvolnění paměti:
>```C
>free(ptr);
>free(ptr);  // Dvojité uvolnění
>```

## Chyby typové kompatibility (Type Compatibility Errors)
- Tyto chyby se vyskytnou, když se pokusíme provést operaci s nesprávným typem dat.
- Kompilátor často upozorní na potenciální problémy, ale některé chyby mohou být detekovány až během běhu programu.

>[!Example] Příklad chyby typové kompatibility
>```C
>float *fptr;
>int *iptr = (int *)fptr;  // Nesprávné přetypování bez explicitního záměru
>```

## Hledání chyb:
- **Valgrind:** Nástroj Valgrind poskytuje detekci memory leaks a dalších chyb paměti pomocí nástrojů jako Memcheck.
- **Statická analýza:** Některé nástroje pro statickou analýzu kódu mohou identifikovat potenciální chyby paměti a nedefinované chování v kódu.
- **Manuální inspekce kódu:** Pečlivé prohlížení kódu s ohledem na správu paměti a manipulaci s ukazateli může odhalit chyby, jako jsou memory leaks a segmentační chyby.

##### Navigace
Předchozí:  [[Principy adresování a práce s pointery v jazyce C]]
Následující: [[Organizace kódu v jazyce C]]
Celý okruh: [[3. Programovací jazyky a programování]]