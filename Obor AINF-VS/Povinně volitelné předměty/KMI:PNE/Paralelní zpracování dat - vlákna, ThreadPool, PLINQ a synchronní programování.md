# **1. Úvod do paralelního programování v .NET**

> [!success]
> **Paralelní programování** v .NET znamená **současné** (či zdánlivě současné) _vykonávání více částí programu_. K jeho realizaci .NET využívá například **vlákna** (threads).

- **Hlavní cíle paralelizace:**
  - **Vyšší výkon** při _výpočetně náročných úlohách_
  - **Neblokující UI** — _GUI nezamrzne_, dokud se něco počítá na pozadí
  - **Efektivní využití HW** — _moderní CPU má více jader_
  - **Asynchronní I/O** — neblokovat vlákno při čekání na disk/síť (I/O-bound)

## **1.1** Vývoj přístupů k paralelnímu a asynchronnímu programování v .NET

1. **Asynchronní delegáti** (od .NET 1.0) – **první možnost** spouštění _metod na pozadí_ pomocí `BeginInvoke()` a `EndInvoke()`.
2. **System.Threading** (od .NET 1.0) – **přímá práce s vlákny** prostřednictvím třídy `Thread`, kdy programátor _vlákna vytváří a řídí ručně_.
3. **Task Parallel Library (TPL)** (od .NET 4.0) – _modernější přístup založený na třídách_ `Task` a `Parallel`, který zjednodušuje paralelní programování a **využívá** `ThreadPool`.
4. **async / await** (od .NET 4.5 / C# 5) – současný doporučený způsob psaní **asynchronního kódu**, který _zjednodušuje práci s úlohami_ (`Task`) a _zpřehledňuje zápis_.

---

# 2. Vlákna — třída `System.Threading.Thread`

- Každý _spuštěný proces_ obsahuje **alespoň jedno vlákno** – **hlavní vlákno** **(Main Thread)**.
- Program však může _vytvářet další vlákna_, která umožňují vykonávat více částí programu současně.

> [!success]
> Ve jmenném prostoru `System.Threading` slouží **k práci s vlákny třída** `Thread`.
>
> Třída`Thread` je _objektový mechanismus_ pro paralelní výpočty. **Abstrakce nad systémovým vláknem** operačního systému.

- Dnes spíše _historický pohled_ — pro běžnou práci se používá **ThreadPool** nebo **Task Parallel Library (TPL)**

## 2.1 Vytvoření a spuštění vlákna

- Pro vytvoření **nového vlákna** se použije třída `Thread`. _Konstruktoru se předá metoda_, která se má vykonat, a vlákno se _spustí voláním metody_ `Start()`.

```csharp
Thread t = new Thread(() => Console.WriteLine("Běžím ve vlákně!"));
t.Start();
t.Join(); // počká, až vlákno skončí
```

> [!danger]
> **Problém přímého vytváření** `Thread`: vytvoření OS vlákna je drahé (typicky ~1MB stack, kontextové přepínání), proto se v praxi téměř nepoužívá pro krátké/časté úlohy – od toho je **ThreadPool**.

## 2.2 Vlastnosti vlákna

- `Thread.CurrentThread` — odkaz na aktuální vlákno
  - Objekt obsahuje informace o:
    - `ThreadPriority` — `Highest`, `AboveNormal`, `Normal`, `BelowNormal`, `Lowest`
    - `ThreadState` — `Running`, `Stopped`, `Background`, `Suspended`, `Aborted`, ...
    - `IsBackground` — pokud `true`, vlákno nebrání ukončení procesu (background thread)
      - Foreground vlákno = **drží proces naživu**, dokud nedoběhne
      - Background vlákno = **umře s aplikací**

---

# 3. ThreadPool

- Vytváření a ukončování vláken pomocí třídy `Thread` je poměrně nákladná operace. Pokud aplikace často vytváří krátkodobá vlákna, dochází ke zbytečné režii a zhoršení výkonu. Proto .NET poskytuje **ThreadPool.**

> [!success]
> **ThreadPool je fond** _předem vytvořených_ a _znovupoužívaných_ vláken spravovaný CLR. Místo zakládání nového vlákna se úloha **zařadí do fronty** a je zpracována některým z volných vláken v ThreadPoolu.

- Vlastnosti:
  - Vlákna jsou _vytvářena a_ _spravována automaticky_ prostředím .NET
  - Vlákna se po dokončení úlohy **neukončují, ale vracejí se zpět** do fondu
  - _Počet vláken_ se **dynamicky** přizpůsobuje _zatížení aplikace_
  - Programátor **nemusí řešit** jejich vytváření ani rušení

## 3.1 Zařazení úlohy do ThreadPoolu

- Metoda vloží úlohu do fronty a _její vykonání zajistí první dostupné vlákno_ z ThreadPoolu.

```csharp
ThreadPool.QueueUserWorkItem(state => Console.WriteLine("Práce z poolu"));
```

- **Výhody:**
  - **Minimalizuje** počet skutečně **vytvořených vláken**
  - Vlákna se **recyklují** → menší alokace, méně práce pro OS
  - Vhodné pro _velké množství krátkých_ úloh
- **Nevýhody:**
  - Programátor **nemá přímou kontrolu** nad jednotlivými vlákny
  - **Nelze nastavovat vlastnosti** konkrétního vlákna (např. prioritu)
  - Nehodí se pro dlouhotrvající úlohy (zaplní se pool a další čekají)

- Na ThreadPoolu _je postavena také knihovna_ **Task Parallel Library** (TPL), která představuje _modernější a doporučený způsob_ paralelního programování v .NET.

---

# 4. Task Parallel Library (TPL)

> [!success]
> **TPL** je _knihovna_, která poskytuje **vysokoúrovňovou abstrakci nad vlákny** pro paralelní a asynchronní zpracování práce. Místo _přímé práce s vlákny_ využívá **úlohy (**`Task`**)**, jejichž vykonávání zajišťuje **ThreadPool**. Díky tomu programátor _nemusí řešit vytváření ani správu jednotlivých vláken_.
>
> Runtime sám rozhoduje, kolik vláken použije, jak práci rozdělí a naplánuje na dostupná jádra (přes ThreadPool a jeho work-stealing scheduler)

> [!info]
> TPL je _součástí jmenného prostoru_ `System.Threading.Tasks`.

## 4.1 `Task`

- Třída `Task` představuje jednu úlohu, která má být vykonána (_asynchronní/paralelní_ operace)
- Úlohu _lze spustit například pomocí metody_ `Task.Run()` (zařadí delegát na ThreadPool a vrátí `Task`, který reprezentuje jeho běh)

```csharp
Task t = Task.Run(() => VypocetneNarocnaOperace());
t.Wait(); // blokující počkání na dokončení

Task<int> t2 = Task.Run(() => Vypocet());
int result = t2.Result; // blokující získání výsledku
```

- Více úloh lze také spouštět současně a čekat na jejich dokončení pomocí metod `Task.Wait()`, `Task.WaitAll()` nebo property `.Result`

## 4.2 `Parallel`

- Třída `Parallel` slouží k paralelnímu zpracování opakujících se operací. Poskytuje zejména metody:
  - `Parallel.For()`, `Parallel.ForEach()` — Aplikuje stejnou operaci na **každý prvek kolekce** paralelně
  - `Parallel.Invoke()` — Spustí několik _různých_ úloh paralelně a **počká**, až všechny doběhnou
- Tyto metody automaticky rozdělí práci mezi dostupná vlákna z ThreadPoolu.

```csharp
Parallel.For(0, 100, (i) => {
    ZpracujPolozku(i);
});

Parallel.ForEach(items, item => {
    ZpracujPolozku(item);
});

Parallel.Invoke(
    () => Metoda1(),
    () => Metoda2(),
    () => Metoda3()
);
```

---

# 5. PLINQ (Parallel LINQ)

> [!success]
> **PLINQ (Parallel LINQ)** je _rozšíření technologie LINQ_, které umožňuje **paralelní zpracování kolekcí**. Namísto sekvenčního zpracování r_ozdělí data na více částí a zpracuje je současně_ pomocí **Task Parallel Library (TPL)**.

> [!info]
> PLINQ je _součástí jmenného prostoru_ `System.Linq`.

```
 var result = numbers
    .Where(x => x % 2 == 0)   # ponechá sudá čísla
    .Select(x => x * x);      # každé sudé číslo umocní na druhou
```

- Pokud chceme stejné zpracování provádět paralelně, stačí přidat metodu `AsParallel()`

```csharp
var result = numbers
    .AsParallel()
    .Where(x => x % 2 == 0)
    .Select(x => x * x);
```

- Metoda `AsParallel()` převede kolekci na `ParallelQuery<T>`, takže jednotlivé části dotazu mohou být vykonávány současně.

- Další možnosti:
  - `.AsSequential()` – vrátí zpět k sekvenčnímu zpracování (např. pro operace, které musí být v pořadí).
  - `.AsOrdered()` – **zachová pořadí prvků původní kolekce** (**za cenu výkonu** – jinak PLINQ pořadí negarantuje).
  - `.WithCancellation(token)` — možnost zrušení
  - `.WithDegreeOfParallelism(n)` — kolik vláken

---

# 6. Synchronní programování

> [!info]
> Pokud víc vláken přistupuje ke sdílenému stavu (proměnná, kolekce) bez koordinace, vzniká **race condition** (chyba souběhu) → výsledek závisí na _nedeterministickém pořadí přepínání vláken_.

```csharp
int counter = 0;
Parallel.For(0, 100000, i => counter++); // race condition! Není atomická operace.
```

- `counter++` je **ve skutečnosti tři kroky** (načti, přičti, ulož) → dvě vlákna je mohou proložit a jeden inkrement se "ztratí".

## 6.1 Synchronizační primitiva

| Synchronizační primitivum | K čemu slouží |
| --- | --- |
| `lock` | Nejjednodušší vzájemné vyloučení (syntaktická zkratka pro `Monitor`). |
| `Monitor` | Pokročilé zamykání (`Enter`, `Exit`, `Wait`, `Pulse`, `TryEnter`). |
| `Interlocked` | Atomické operace nad proměnnými (`Increment`, `Exchange`, `CompareExchange`...). |
| `Mutex` | Vzájemné vyloučení i **mezi různými procesy**. |
| `Semaphore` **/** `SemaphoreSlim` | Omezuje počet vláken, která mohou současně vstoupit do kritické sekce. |
| `ReaderWriterLockSlim` | Umožňuje více současných čtenářů, ale pouze jednoho zapisovatele. |
| `AutoResetEvent` | Signalizační objekt – po uvolnění propustí jedno čekající vlákno a automaticky se znovu uzamkne. |
| `ManualResetEvent` **/** `ManualResetEventSlim` | Signalizační objekt – po uvolnění propouští všechna čekající vlákna, dokud není znovu resetován. |
| `Barrier` | Synchronizuje více vláken v jednotlivých fázích výpočtu. |
| `CountdownEvent` | Čeká, dokud určitý počet vláken nedokončí svou práci. |
| `SpinLock` | Aktivní čekání místo uspání vlákna; vhodný jen pro velmi krátké kritické sekce. |
| `SpinWait` | Pomocná třída pro krátké aktivní čekání. |

### 6.1.1 `lock`

```
private readonly object _lockObj = new object();
private int counter = 0;

void Increment()
{
    lock (_lockObj)
    {
        counter++;
    }
}
```

- _Nejjednodušší_ způsob synchronizace v C#.
- **Interně využívá třídu** `Monitor` —`Monitor.Enter`/`Monitor.Exit`.
- Zamyká se vždy na **referenčním typu** (objektu), nikdy _na hodnotovém typu_, `string`, ani na `this`
- **Dobrá praxe**: privátní `readonly object`.

### 6.1.2 `Monitor`

- Poskytuje _stejné možnosti_ jako `lock`, ale **nabízí větší kontrolu nad zamykáním**.Nejdůležitější metody:
  - `Enter()` – vstup do kritické sekce,
  - `Exit()` – opuštění kritické sekce,
  - `TryEnter()` – pokus o získání zámku,
  - `Wait()` – uvolní zámek a čeká na signál,
  - `Pulse()` / `PulseAll()` – probudí jedno nebo všechna čekající vlákna.

```
private static readonly object _lock = new();

// Vlákno A
lock (_lock)
{
    Monitor.Wait(_lock);   // čeká na signál
    Console.WriteLine("Pokračuji.");
}

// Vlákno B
lock (_lock)
{
    Monitor.Pulse(_lock);  // probudí jedno čekající vlákno
}
```

### 6.1.3 `Interlocked`

- Slouží k provádění **atomických operací** nad jednoduchými proměnnými.

```
Interlocked.Increment(ref counter);
```

- Nejčastější operace:
  - `Increment()`
  - `Decrement()`
  - `Add()`
  - `Exchange()`
  - `CompareExchange()`
- Výhodou je velmi vysoký výkon, protože není potřeba zamykat celý blok kódu.

### 6.1.3 `SemaphoreSlim`

- Semafor **omezuje počet vláken**, která mohou současně vstoupit do určité části programu.

```
var semaphore = new SemaphoreSlim(5);

async Task ZpracujAsync(Item item) {
    await semaphore.WaitAsync();
    try {
        await VolejApiAsync(item);
    }
    finally {
        semaphore.Release();
    }
}
```

---

# 7. `async` a `await`

> [!success]
> Klíčová slova `async` a `await` umožňují psát asynchronní kód, který _vypadá jako synchronní_, ale **neblokuje volající vlákno během čekání** (typicky na I/O).

- `async` — **modifikátor metody**; označuje, že metoda **obsahuje await** a může běžet _asynchronně_
  - CLR při volání zařídí, aby se metoda chovala jako stavový automat
- `await` — operátor **před asynchronním voláním**
  - Pozastaví aktuální „logické" vykonávání metody
  - Vlákno **není zablokováno** — vrátí se do volajícího kontextu
  - Po dokončení awaitované úlohy pokračuje dále (často na vlákně z ThreadPoolu)

```
public async Task<string> DownloadAsync(string url)
{
    using var client = new HttpClient();
    string content = await client.GetStringAsync(url);
    return content;
}
```

> [!info]
> Asynchronní operace jsou nejvhodnější pro **I/O operace** (čtení souborů, databáze, síťová komunikace), kdy aplikace nemusí po dobu čekání nečinně blokovat vlákno.