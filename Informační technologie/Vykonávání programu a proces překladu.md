## Vykonávání programu
- Procesor zpracovává jednu instrukci za druhou (pokud není uvedeno jinak $\rightarrow$ skok).
- **nepodmíněný skok**: operace `JMP r/m/i` - ekvivalence `GOTO`
- **není** přítomna operace ekvivalentní k `if`

### Příznaky
- operace nastavují za svého chodu příznaky
- **příznaky pro řízení výpočtu:**
	- `SF` (Sign Flag) - výsledek je záporný - `0`, výsledek je kladný - `1`
	- `ZF` (Zero Flag) - výsledek byla $0$
	- `CF` (Carry Flag) - výsledek je větší/menší než největší/nejmenší možné číslo
	- `OF` (Overflow Flag) - příznak přetečení
- **další příznaky:**
	- `AF` (Auxiliary carry Flag) - přenos ze čtvrtého do pátého b (BCD)
	- `PF` (Parity Flag) - sudá parita - `1`, lichá parita - `0`
- **řídící příznaky:**
	- `TF` (Trap Flag) - slouží ke krokování
	- `DF` (Direction Flag) - ovlivňuje chování instrukcí blokového kódu
	- `IOPL` (I/O Privilage Level) - úroveň oprávnění
	- `IF` (Interrupt enable Flag) - možnost zablokovat některá přerušení
### Porovnávání čísel
- porovnání čísel - `CMP r/m`, `CMP r/m/i`
- `JE` - skok při rovnosti
- `JNE` - skok při nerovnosti

### Podmíněné skoky
>[!tldr] Podmíněné skoky pro porovnání neznaménkových hodnot
>```C
>| instrukce | alt. jméno | příznaky           | podmínka   |
|-----------|------------|--------------------|------------|
| JA        | JNBE       | (CF or ZF) = 0     |  A > B     |
| JAE       | JNB        | CF = 0             |  A ≥ B     |
| JB        | JNAE       | CF = 1             |  A < B     |
| JBE       | JNA        | (CF or ZF) = 1     |  A ≤ B     |

>[!tldr] Podmíněné skoky pro porovnání znaménkových hodnot
>```C
>| instrukce | alt. jméno | příznaky               | podmínka |
|-----------|------------|------------------------|----------|
| JG        | JNLE       | (SF = OF) & ZF = 0     | A > B    |
| JGE       | JNL        | (SF = OF)              | A ≥ B    |
| JL        | JNGE       | (SF ≠ OF)              | A < B    |
| JLE       | JNG        | (SF ≠ OF) nebo ZF = 1  | A ≤ B    |

### Smyčky
- speciální operace pro snadnější implementaci cyklů 
- `LOOP` - odečte $1$ or `RCX`/`ECX` a pokud v něm není nula $\rightarrow$ provede skok

### Odhad skoků
- podmíněné skoky zpomalují běh programu $\rightarrow$ procesory provádí různé heuristiky pro odhad, zda bude skok proveden
- Např. čtyčstavové počítadlo se saturací (`11`, `10`, `01`, `00` - až na `00` počítá, že se skok provede)

### Zásobník
- procesor má vyčlenění úsek paměti pro zásobník
	- ten uchovává pomocné výpočty, návratové adresy, lokální proměnné, ...
- vyšší programovací jazyky obvykle neumožňují manipulaci s tímto zásobníkem
- operace: `PUSH r/m/i`, `POP r/m`

### Volání funkcí s konvencí `cdecl`
- **Volání funkce:**
	1. na zásobník jsou uloženy parametry funkce
	2. zavolá se funkce (`call <adresa>`), na zásobník se uloží adresa návratu
	3. funkce uloží obsah registru `EBP` na zásobník (adresa předchozího rámce)
	4. funkce uloží do registru `EBP` obsah `ESP` (začátek nového rámce)
	5. vytvoří se na zásobníku místo pro lokální proměnné
	6. na zásobník se uloží registry, které se budou měnit
- **Návrat z funkce**:
	1. obnovíme hodnoty registrů
	2. odstraníme lokální proměnné
	3. obnovíme hodnotu `EBP`
	4. provedeme návrat z funkce `ret`
	5. odstraníme argumenty ze zásobníku

## Proces překladu
- Je to proces, kterým se zdrojový kód napsaný v programovacím jazyce (např. C, Java) převádí na strojový kód, který může být proveden procesorem.

1. **Preprocesor:** expanduje makra, odstraní nepotřebný kód, načte požadované soubory (např. `math.h`)
2. **Překladač:** generuje kód v assembleru
3. **Assembler:** vygeneruje objektový kód (`foo.c` $\rightarrow$ `foo.obj`/`foo.o`)
4. **Linker:** slouží několik souborů s objektovým kódem + knihovny do spustitelného souboru

##### Navigace
Předchozí: [[Operační systém, architektura, poskytovaná rozhraní]]
Následující: [[Správa procesoru - procesy a vlákna, plánování jejich běhu, komunikace a synchronizace]]
Celý okruh: [[2. Informační technologie]]