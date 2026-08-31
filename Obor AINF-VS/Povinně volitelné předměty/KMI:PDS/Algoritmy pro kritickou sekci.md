> [!warning]
> **Chyba souběhu**. Může k ní dojít, když _více procesů/vláken_ pracuje se **sdílenými prostředky najednou**.
>
> **Synchronizace** zaručuje, že procesy/vlákna _přístupují k sdíleným prostředkům_ (sdílená paměť, zařízení, databáze…), tak **aby nedocházelo** _k nekonzistencím nebo konfliktům_.
>
> **Atomická operace** je operace, která sice _může být složena z více dílčích kroků_, ale je **nepřerušitelná**. (klasický synchronizační nastroj)
>
> **Kritická reference**
>
> - Do proměnné je **zapisováno** a je **čtena** v jiném procesu.
> - Proměnná je **čtena** a je do ní **zapisováno** v jiném procesu.

# 1. Kritická sekce

> [!success]
> **Úsek kódu** _přistupující ke sdílenému zdroji_, kde by _souběžné provádění vedlo k nekonzistenci_.

## **1.1 Formální požadavky na kritickou sekci**

1. **Vzájemné vyloučení (mutual exclusion):** _Nejvýše jeden_ proces je v kritické sekci
2. **Absence uváznutí (no deadlock):** Pokud se _více procesů_ _snaží_ najednou _vstoupit_ do kritické sekce, _alespoň jeden uspěje_.
3. **Absence vyhladovění (no starvation):** Pokud se libovolný _proces snaží vstoupit do kritické sekce_, nakonec se mu to _podaří_.

---

# 2. Algoritmy pro kritickou sekci

## 2.1 Dekkerův algoritmus

> [!info]
> První správné řešení pro 2 procesy.

- **Autor:** T. J. Dekker (1965), publikoval Dijkstra.
- **Princip**: Každý proces oznámí “_Chci vstoupit._” Pokud chtějí vstoupit oba současně, rozhodně proměnná `turn`.
- **Používá**:
  - proměnné `wantA` a `wantB`
  - proměnnou `turn`
- **Výhody**:
  - Splňuje všechny podmínky KS.
  - Nepotřebuje HW podporu. (Nepoužívá žádnou speciální instrukci procesoru)
- **Nevýhody**:
  - Složitý
  - Pouze pro 2 procesy

### 2.1.1 Pseudokód

![[019f51bb-195d-75ea-966d-42fa824268b9.png]]

---

## 2.2 Petersonův algoritmus

> [!info]
> _Jednodušší varianta_ Dekkerova algoritmu.
>
> Též nazývaný “**Tie-breake**r”.

- **Autor:** G. L. Peterson (1981).
- **Princip**: Proces _indikuje, že chce vstoupi_t do KS (jeho odpovídající proměnná). Nastaví do `last` _své číslo_ (označí se jako poslední proces, který dokončil vstupní protokol). Pokud chtějí _vstoupit současně_, vstoupí ten, který _dokončil vstupní protokol dřív_ (není uložen v `last`)
- **Používá** (pro 2 procesy):
  - proměnné `wantA` a `wantB`
  - proměnnou `last`

> [!danger]
> Lze **zobecnit na n procesů**, ale je to _velmi komplikované_.
>
> - Pomocí _více úrovní_ **(Peterson's Tournament Algorithm)**.
> - Procesy jsou _uspořádány do turnajového stromu_:
>
> ```
>         vítěz
>        /     \
>      A         B
>     / \       / \
>    P1 P2    P3  P4
> ```

### 2.2.1 Pseudokód (2 procesy)

![[019f51ce-50d8-77ec-b8b1-5328b290ff48.png]]

---

## 2.2 Lamportův Bakery algoritmus

> [!info]
> Název je inspirován pekárnou (s pořadníkem).

- **Autor:** L. Lamport (1974).
- **Princip:** Využívá se tu _pořadník_, tedy každý proces si _“vezme číslo”_. _Obsloužen_ (může vstoupit do KS) je ten _s nejmenším čísle_.

### 2.2.1 Základní varianta

![[019f51df-a3ae-75d6-a9fb-1d3818e53166.png]]

- **Používá:**
  - proměnné `nA` a `nB` (představují pořadové lístky)

> [!danger]
> _Vyžaduje_ operaci `fetch-and-add`. (Aby nedošlo ke konfliktu)

![[019f51e0-0f9c-777d-96e6-0eaa09ff381f.png]]

- Počítáme s tím že _máme neomezený počet lístků_ (lze vyřešit pomocí modulo)
- Potřeba _zjistit největší lístek_, což je **pomalé**

> [!danger]
> Počítáme s tím, že operace `max` musí být **atomická**.
>
> Pokud _mají stejné číslo_, rozhodne _ID procesu_.

### 2.2.2 Lamportův Bakery algoritmus pro n procesů

> [!info]
> První skutečně použitelný algoritmus

![[019f51dd-c089-76e6-929b-ea0cf9bdfbfc.png]]

- **Používá** (navíc):
  - `vybrano[]` — Signalizuje: „Ještě nemám definitivní číslo, počkej na mě." → operace `max` nemusí být **atomická**.

> [!danger]
> **Problém**: Pokud selže jeden proces, může dojít k deadlocku.

## 2.3 Szymanského algoritmus

> [!info]
> Odstraňuje nedostatky předchozích algoritmů

- **Autor:** B.K. Szymański (1988)
- **Princip:**
  - Algoritmus využívá analogii **čekárny**.
  - Než proces vstoupí do kritické sekce, _prochází několika stavy_. Ostatní procesy podle hodnoty `flag` poznají, kde se právě nachází.
    - 0 = Nekritická sekce.
    - 1 = Proces požádal o vstup do kritické sekce.
    - 2 = Čeká, až ostatní dokončí vstup do čekárny.
    - 3 = Nachází se v čekárně
    - 4 = Může vstoupit do kritické sekce.
- **Používá**:
  - Pole `flag[1..n]` — každý proces má zde uložený svůj stav.

### 2.3.1 Pseudokód

![[019f520e-6dd1-7508-85d8-36ac919c42d0.png]]

> [!danger]
> Musí být splněno, že testy typu **„pro všechny“** a **„existuje“** jsou prováděny jednotně (ve správném pořadí), jinak algoritmus nemusí fungovat správně.

---

# 3. Složené atomické operace

- Výše popsané softwarové algoritmy jsou historicky a teoreticky důležité, ale v praxi se pro kritické sekce používají **hardwarové instrukce** poskytující atomické složené operace.

### 3.1 Test-and-Set (TAS)

```java
function test_and_set(boolean lock):
   boolean initial = lock;
   lock = true;
   return initial;
```

- `test_and_set` _atomicky přečte hodnotu a nastaví ji na_ `true`.
- Pokud vrátí `true`→ zámek byl volný, nyní uzamčen → vstup do KS.
- Pokud vrátí `false`→ zámek byl zamknutý → čekáme.
- **Nevýhoda:** Vyhladovění možné (není zaručeno pořadí).

### 3.2 Compare-and-Swap (CAS)

```
atomic bool compare_and_swap(int *ptr, int expected, int newval):
    if *ptr = expected:
        *ptr ← newval
        return true
    return false
```

### 3.3 Fetch-and-Add

```
atomic int fetch_and_add(int *ptr, int delta):
    old ← *ptr
    *ptr ← old + delta
    return old
```

- **Použití**: Implementace ticketového zámku.

# 4. Klasické synchronizační problémy a jejich řešení

## 4.1 Večeřící filozofové

- **Příběh**: _5 filozofů_ jí špagety pomocí _5 vidliček_
- **Dvě operace**:
  - Filozof _přemýšlí_.
  - Filozof _jí_. Jíst může pokud má dvě vidličky
- Vidličku **nemůže** mít více filozofů. Potřeba simulace, jelikož _lehce může dojít k deadlocku_!

> [!info]
> Simulace současného přístupu k více zdrojům (aplikace vyžaduje mikrofon a videokameru)

### 4.1.1 Možná řešení

1. **Jeden filozof je levák**
  - Všichni filozofové berou _nejprve levou a pak pravou vidličku._
  - **Jeden** filozof to dělá opačně
  - **Nevýhody**: Není _efektivní ani férové_. Může dojít k _vyhladovění_ (buď leváka nebo jeho souseda)
2. **Číšník**
  - Přidá se centrální koordinátor – **číšník**.
  - Filozof si před zvednutím vidliček _musí vyžádat povolení od číšníka_.
  - Číšník rozhoduje, kdo smí právě jíst.
  - **Nevýhody**: Číšník je _úzké hrdlo, plýtvá zdroji._ Může dojít k _vyhladovění_ (filozofové se budou předbíhat)
3. **Když nezíská druhou vidličku, první položí**
  - **Nevýhoda**: Může vzniknout **livelock** – filozofové si _neustále berou a pokládají vidličky_, ale nikdo se nenají.
4. **Pouze čtyři židle**
  - Přestože je 5 filozofů, u stolu mohou sedět současně jen **4**. **Jeden** filozof **vždy čeká**.

## 4.2 Producent-konzument

- Máme procesy (nebo vlákna) dvou typů:
  - **Producent** – vytváří data.
  - **Konzument** – zpracovává (spotřebovává) data.
- Oba sdílejí **omezený buffer (frontu)**.
  - Producent _nesmí zapisovat do plného bufferu_. Jinak by přepsal ještě nezpracovaná data.
  - Konzument _nesmí číst z prázdného bufferu_. Jinak by četl neexistující data.

> [!info]
> _Příklad_: **Tisk**. Producent = Aplikace vytváří dokument, konzument = Tiskárna

### 4.2.1 Řešení

- _Využívá se_:
  - **Semaforu** `not_full` — Určuje počet volných míst.
  - **Semaforu** `not_empty` — Určuje počet obsazených míst.
  - **Zámek**. Ochrana samotného bufferu při zápisu a čtení.

```javascript
# Producent
not_full.wait()
mutex.lock()
# vlož položku
mutex.unlock()
not_empty.signal()

# Konzument
not_empty.wait()
mutex.lock()
# odeber položku
mutex.unlock()
not_full.signal()
```

## 4.3 Čtenáři a písaři

- Máme **sdílená data**, ke kterým přistupují dva typy procesů:
  - **čtenáři (readers)**
  - **písaři (writers)**
- **Písaři** data mění, proto _musí mít ke zdroji výhradní přístup_. Vzájemně se vylučují.
- **Čtenáři** data pouze čtou. _Více čtenářů se navzájem nepřekáží_ (mohou číst současně). Ale čtenář nesmí číst během zápisu, _písař nesmí zapisovat během čtení_.

> [!info]
> _Příklad_: Zápis a čtení souboru.

### 4.3.1 Řešení

> [!danger]
> Musíme dávat pozor, aby řešení bylo **spravedlivé**!

- Možné i využití _Read-Write Lock_. Některé jazyky jej již obsahují.

- Řešení **preferující čtenáře**:

![[019f574a-26ba-7362-92bc-1d2f558fb155.png]]

- **Spravedlivé řešení**:

![[019f574b-05dd-75fd-a50c-7cd606a86998.png]]

## 4.4 Kuřáci

- Máme:
  - **1 agenta**
  - **3 kuřáky**
- Existují **3 zdroje** potřebné k ubalení cigarety:
  - Papír
  - Tabák
  - Sirky
- Každý kuřák má **neomezené množství právě jednoho zdroje**:

| Kuřák | Má  |
| --- | --- |
| Kuřák A | papír |
| Kuřák B | tabák |
| Kuřák C | sirky |

- **Postup**:
  - Agent vždy položí na stůl **dva náhodné zdroje**. Poté čeká.
  - Pokračovat může pouze kuřák, který vlastní třetí chybějící surovinu.
    - Ubalí si cigaretu a vykouří.
    - Signalizuje agenta, aby nachystal další zdroje.

### 4.4.1 Řešení

- Pomocí “**dealerů**”. Což jsou _pomocná vlákna/procesy_. Každý dealer sleduje určitou kombinaci surovin a poté probudí správného kuřáka.
  
  [ukol03-2.py](files/019f5765-1b00-745c-886c-ccae2bc2b24e/ukol03-2.py)
  

## 4.5 Hodující divoši

- _Máme_:
  - **n divochů**
  - **jednoho kuchaře**
  - **jeden hrnec** o kapacitě **x porcí**.

- **Průběh**:

1. Divoch přijde k hrnci.
2. Pokud je v hrnci porce, vezme si ji a jí.
3. Pokud je hrnec prázdný:
  - **Ten divoch,** který to _objevil_, probudí kuchaře.
  - Kuchař uvaří celý hrnec.
  - Divoch si vezme jednu porci.
  - Ostatní mezitím čekají.

> [!danger]
> Kuchař **nevaří** dokud **není snězeno**!

> [!info]
> _Příklad:_
>
> Představ si **API server**, který načítá data z databáze.
>
> - **divoši** = klientské požadavky,
> - **hrnec** = cache,
> - **kuchař** = proces obnovující cache.
>
> Průběh:
>
> 1. Přijde mnoho klientů.
> 2. Data jsou v cache → okamžitě je dostanou.
> 3. Cache expirovala (prázdný hrnec).
> 4. **Pouze první klient** spustí obnovu cache.
> 5. Ostatní klienti čekají.
> 6. Jakmile jsou data načtena, všichni pokračují.

### 4.5.1 Řešení

[ukol03-3.py](files/019f576f-824b-77b5-9df8-7bd730431f8b/ukol03-3.py)