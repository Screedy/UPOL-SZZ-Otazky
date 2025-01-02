## Synchronizace
- je **forma komunikace** mezi procesy nebo vlákny v počítačovém systému
- *Cílem synchronizace* je zajistit, aby *přístup k sdíleným prostředkům* (sdílená paměť, zařízení, databáze, ...) byl prováděn v **souladu s předem stanovenými pravidly** a aby **nedocházelo k nekonzistencím nebo konfliktům**

- Rozlišujeme pokud procesy/vlákna mají:
	- **Sdílenou paměť**:
		- Klasické synchronizační nástroje jsou **atomické operace, synchronizační primitiva** (zámek, semafor, bariéra, ...)
		- Pokročilejší nástroje jsou **threadpool, RW zámky, pasivní čekání**
		- **Škálovatelnost je omezená**
	- **Nesdílenou paměť**:
		- Komunikace probíhá pomocí **zasílání zpráv**
		- Synchronizační nástroje jsou **pipe, fronty zpráv, sockety**
		- Rychlost komunikace je omezení, má větší možnost škálování

## Atomická operace
- Klasický synchronizační nástroj, pokud pracujeme se sdílenou pamětí
- **Nelze ji přerušit jiným procesem**
- *Paralelní vykonávání atomických akci* je **sekvenční** vyhodnocení v libovolném pořadí

- Korektnost algoritmu závisí na definici atomické akce
- Podle potřeby různé úrovně abstrakce:
	- **Hrubé** - například atomické operace na úrovni jazyka (vestavěné funkce/knihovny)
	- **Jemné** - například atomické instrukce procesoru (Compare-and-Swap)

- **Složené atomické akce**:
	- Lze provádět **čtení i zápis** jako **jednu operaci** (atomicky)
	- Příklady operací:
		- `test-and-set`, `exchange`, `fetch-and-add`, `compare-and-swap`
	- Mohou být implementovány v OS nebo přímo v HW

## Kritická reference
- Proměnná je kritická reference, pokud
	1. Do proměnné je zapisování a je čtena v jiném procesu
	2. Proměnná je čtena a je do ní zapisováno v jiném procesu (to stejné, akorát naopak)
- Podmínka kritických referencí = **každá akce** programu obsahuje **nejvýše jednu** kritickou referenci
- Není dostatečné, pořád je potřeba synchronizace

## Korektnost programu
- Sekvenční program má smysl ladit, má pouze jeden scénář
- Paralelní program **má více scénářů, nelze** ladit jako sekvenční
- **Vlastnost programu** je **tvrzení**, které **je platné** pro **všechny** možné scénáře
- **Korektnost** konkurentního programu definována pomocí vlastní programu:
	- **Bezpečnost (safety)** = **tvrzení**, nebo jeho negace, které **je platné** pro každý stav výpočtu (např. "program nikdy nezatuhne")
	- **Živost (liveliness)** = **tvrzení,** které **je platné** pro **alespoň jeden** stav výpočtu (např. "program se někdy rozběhne")
- Bezpečnost a živost jsou duální vlastnosti - negace jedné je druhá

## Férovost
- Korektnost programu vyžaduje férovost, závisí na plánování politice konkrétní architektury
![[MacBook-2024-12-30-002333@2x.png]]
- Proces A může jet donekonečna

## Kritická sekce
- Dijkstra, 1965
- n procesů vykonává (v nekonečné smyčce) posloupnost akcí rozdělenou na dvě části: **kritická sekce a nekritická sekce**
- **Kritická sekce** je část kódu, kdy **program pracuje se sdílenými zdroji** (například pamětí)
- Pokud je jeden proces v kritické sekci, další proces **nesmí vstoupit** do kritické sekce

Požadavky na kritickou sekci (korektnost):
- **Vzájemné vyloučení** = nejvýše **jeden** proces je v kritické sekci
- **Absence uváznutí** = jestliže se nějaké procesy snaží současně vstoupit do kritické sekce, pak **jeden** z nich **musí** někdy uspět
- **Zaručený vstup** = pokud se proces snaží vstoupit do kritické sekce, **jednou musí uspět**

- Synchronizací kritické sekce zajišťujeme její korektnost

### Proces hledání řešení kritické sekce
#### Nesprávné pokusy

| ![[MacBook-2025-01-02-002335@2x.png]] | ![[MacBook-2025-01-02-002336@2x.png]] |
| ------------------------------------- | ------------------------------------- |
| ![[MacBook-2025-01-02-002337@2x.png]] | ![[MacBook-2025-01-02-002338@2x.png]] |
- **První pokus:**
	- Proces, který je na řadě na kritickou sekci, může zůstat v nekritické sekci.
	- Druhý proces **vyhladoví.** (Porušení zaručení vstupu a absence uváznutí)
- **Druhý pokus:**
	- Není zaručeno **vzájemné vyloučení**. Proces *A* i *B* se mohou dostat do kritické sekce spolu.
- **Třetí pokus:**
	- Může dojít k **uváznutí**. *wantA* a *wantB* budou obě `true`
- **Čtvrtý pokus:**
	- Může dojít k **vyhladovění**. Procesy budou vyžadovat a vzdávat přístup současně.

#### Dekkerův algoritmus
![[MacBook-2025-01-02-002339@2x.png]]
- Kombinace prvního a čtvrtého pokusu
- Lze použít **jen pro dva procesy**. Jinak je to strašně složité.

#### Řešení kritické sekce pomocí složených akcí
![[MacBook-2025-01-02-002341@2x.png]]
- Implementace zámku
- Funguje na **libovolný** počet procesů
- Vyžaduje **silnou férovost**

#### Petersonův algoritmus (Tie-breaker)
![[MacBook-2025-01-02-002342@2x.png]]
- Vychází z Dekkerova algoritmu
- `last` indikuje který proces jako poslední začal vykonávat vstupní protokol (a bude dále čekat)
- Podmínka nesplňuje podmínku kritických referencí
- Algoritmus je **korektní** i když se podmínky **vykonávají neatomicky**
- Zobecnění na *n* procesů je poměrně komplikované

#### Bakery algoritmus
![[MacBook-2025-01-02-002343@2x.png]]
- Čísla v proměnných `nA` a `nB` **představují pořadové lístky**
- Vyžaduje `fetch-and-add`, jinak není férový
![[MacBook-2025-01-02-002344@2x.png]]
- "Elegantní"
- Počítáme s tím, že máme neomezený počet lístků (lze vyřešit pomocí modulo)
- Potřeba **zjistit největší lístek**, což je pomalé
- Navíc musíme počítat, že operace `max` musí být **atomická**

#### Lampart-Bakery algoritmus
![[MacBook-2025-01-02-002345@2x.png]]
- První **skutečně použitelný algoritmus**
- Problém: Pokud **selže jeden proces**, může dojít k **deadlocku**

#### Szymanského algoritmus
![[MacBook-2025-01-02-002346@2x.png]]
- Odstraňuje nedostatky předchozích algoritmů
- Analogie **čekárny**
- **Testy** (všechny, existuje) **musejí být jednotné** (záleží na pořadí), jinak nefunguje
	- `0` - nekritický sekce
	- `1` - vstup do kritické sekce
	- `2` - čekání na ostatní vstupující do čekací místnosti
	- `3` - vstup do čekací místnosti
	- `4` - vstup do kritické sekce

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="predchozi-otazka.html" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FZ%C3%A1kladn%C3%AD%20synchroniza%C4%8Dn%C3%AD%20primitiva%20a%20jejich%20pou%C5%BEit%C3%AD" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Následující otázka
            </button>
        </a>
    </div>
    <!-- Spodní tlačítko -->
    <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2F2.%20Povinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty" style="text-decoration: none;">
        <button style="padding: 15px 30px; background-color: #ADD8E6; color: black; border: none; border-radius: 5px; cursor: pointer; width: 43%;">
            Všechny otázky
        </button>
    </a>
</div>