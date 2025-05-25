#### Symbolický výraz
- Jde o jednoduchý výraz (*atom*) nebo složený výraz (*seznam*)
#### Jednoduchý výraz (atom)
- Jde o *číslo* (10, -5, 4.9999D0) nebo *symbol* (posloupnost písmen/čísel/znaků) nebo *literál*
#### Složený výraz (seznam)
- Posloupnost jednoho nebo více výrazů (*prvky složeného výrazu*), které jsou odděleny mezerami
- `(+ 1 2), (+). (1 2 3)`
- ![[Pasted image 20250320210700.png]]

> [!info] Terminologie složeného výrazu
> ![[Pasted image 20250320210811.png]]
> **Operátor** ... co se má udělat
> **Operandy** ... s čím se to má udělat
- Lisp důsledně používá *prefixovou notaci*
## Vyhodnocení symbolických výrazů v Lispu
- Když symbolický výraz napíšeme do Listeneru a dostaname výsledek tak mu říkáme *hodnota symbolického výrazu*
	- $\frac{1}{4}$ je hodnotou symbolického výrazu `(/ (- 5 3) (+ 5 3))
- Přesně popsanému procesu, který vede v této hodnotě říkáme *vyhodnocovací proces*

> [!info] Vyhodnocovací proces
> **Vyhodnocení výrazu** $E$
> 1. Je-li $E$ symbol, výsledkem je hodnota symbolu $E$
> 2. Je-li $E$ jiný atom než symbol, výsledkem je $E$
> 3. Je-li $E$ seznam s operátorem $o$ a operandy $a_1, ..., a_n$, pak
>> - jestliže $o$ je speciální operátor, vyhodnotí se podle jeho pravidel
>> - jestliže $o$ je název makra, $E$ se expanduje podle pravidel makra a výsledný výraz se vyhodnotí v prostředí $env$
>> - jinak $o$ musí být symbol -> se zjistí hodnota $f$ funkční vazby symbolu $o$ v prostředí $env$
>> - zjistí se hodnoty $v_1, ..., v_n$ argumentů $a_1, ..., a_n$ v prostředí $env$ (opět vyhodnocovací proces)
>>-  výsledkem je výsledek aplikace funkce $f$ na hodnoty $v_1, ..., v_n$ (aplikace může mít vedlejší efekt)

- Symbol může sloužit jako *jméno* pro hodnotu (např. `pi` pro $3.14159...$) a říkáme mu *proměnná*
	- Říkáme, že symbol je na hodnotu navázán
	- Hodnota se vždy hledá v aktuálním prostředí, při neúspěchu se postupuje o úrovně výš
#### Funkce v Lispu
- Ucelená část programu obsahující výpočet
- Hodnoty použité při aplikaci funkce jsou argumenty
- Aplikace funkce = spuštění kódu 
- Používáme jako **abstrakci** (vyšší srozumitelnost, snadnější změny, snížení chybovosti, ...)
- Funkce si pamatuje prostředí svého vzniku a tím pádem ji můžeme nazvat *lexikální uzávěr* (kromě toho i seznam parametrů a tělo)
- Funkce bez názvu ... **anonymní funkce** (operátor `lambda`)

> [!tip] lambda výraz ($\lambda$-výraz)
> ![[Pasted image 20250321134823.png]]
#### Predikát
- Funkce, která jako výsledek vrací jednu z pravdivostních hodnot (`t` nebo `nil`)
#### Speciální operátory
- Operátor pro který neplatí standardní (zjednodušený) vyhodnocovací proces a mají svůj vlastní
- Např. `if`, `setf`
## Prostředí a vazby
- Symbol může mít více vazeb (jedna je vždy aktuální)
- Máme 2 typy vazeb
	1) hodnotová
	2) funkční
- Každá vazba má hodnotu (hodnota symbolu = hodnota aktuální vazby)
- ![[Pasted image 20250320221627.png]]
- Vazby jsou organizovány v prostředí (znázornění pomocí tabulky)
	- ![[Pasted image 20250320221956.png]]

>[!tip] **Operátor** `let`
>- Slouží k explicitnímu vytvoření nového prostředí.
>![[Pasted image 20250320222111.png]]

- Operátor `labels` vytváří prostředí s funkčními vazbami symbolů

> [!info] Datová struktura
> Zajišťuje nám datovou abstrakci. Pracujeme s ní pomocí: *konsturktorů, selektorů, mutátorů*. Mutátory nejsou přípustné ve funkcionálním programování.


> [!warning] Vedlejší efekt
> Může nastat při vyhodnocení výrazu, pokud kromě vrácení hodnoty výrazu je způsobena ještě nějaká **vnější změna**.
> 
> *interní vedlejší efekt* ... např. mutace hodnoty v datové struktuře
> *externí vedlejší efekt* ... není možné zpětně programem zjistit (např. tiskový výstup)

- **literál** ... textový řetězec zadaný přímo ve zdrojovém kódu
