## Vlákna v C\#
- Standardně má aplikace jedno hlavní vlákno. Pomocí knihovny `System.Threading` lze pracovat s více vlákny a dosáhnout tak paralelního zpracování.

#### Výhody více vláken
- Paralelizace výpočtů
- Oddělení výpočtů od uživatelského rozhraní (např. GUI)
- Efektivní využití vícejádrových procesorů

## Třída `System.Threading.Thread`

#### Základní vlastnosti
- `Thread.CurrentThread` – aktuální vlákno
- `ThreadPriority` – nastavení priority (např. `Highest`, `Normal`)
- `ThreadState` – stav vlákna (`Running`, `Stopped`, `Unstarted`, ...)

#### Vytvoření vlákna
```csharp
Thread t = new Thread(new ThreadStart(RunMethod));
t.Start();
```

#### S parametrem
```csharp
Thread t = new Thread(new ParameterizedThreadStart(SomeMethod));
t.Start(argument);
```

#### Lambda výraz
```csharp
Thread t = new Thread(() => Console.WriteLine("Práce ve vlákně"));
t.Start();
```

#### Čekání na dokončení
```csharp
t.Join();
```

## Synchronizace vláken
- Při přístupu více vláken ke stejným proměnným může docházet k chybám. Např. výraz `x = x + 5` není atomický.

#### Řešení pomocí `lock`
```csharp
lock (someObject) {
    // kritická sekce
}
```
- **Pozor!**
	- Deadlock – zablokování vláken při chybném zamykání
	- Nezamykat `string` a typy s interním sdílením

## Asynchronní programování (`async`, `await`, `Task`)
- Moderní způsob práce s časově náročnými operacemi bez blokování vlákna.
#### `async`
- Modifikátor, který označuje metodu jako asynchronní
- Umožňuje použití klíčového slova `await` uvnitř těla metody.
- Taková metoda obvykle vrací `Task` nebo `Task<T>` (nebo `void` u událostí).
```csharp
public async void DoWork() {
    await SomeTask();
}
```

#### `Task`
- Reprezentuje probíhající asynchronní operaci.
- Podobný vláknu, ale mnohem lehčí.
- Vrací hodnotu (`Task<T>`) nebo nevrací (`Task`).
```csharp
public Task SomeTask() {
    return Task.Factory.StartNew(() => {
        Thread.Sleep(4000);
    });
}
```
#### `await`
- Čeká na dokončení asynchronní operace, aniž by zablokoval běžící vlákno.
- Umožňuje "pozastavit" běh metody, a pokračovat až po dokončení `Tasku`.

---
## Shrnutí
- `Thread` umožňuje explicitní práci s vlákny.
- Synchronizace pomocí `lock` zabraňuje konfliktům při přístupu ke sdíleným datům.
- `async`/`await` a `Task` poskytují moderní a přehledný přístup k asynchronnímu programování.
```csharp
public async Task<int> GetDataAsync() {
    await Task.Delay(1000); // čekání bez blokace vlákna
    return 42;
}

public async void Start() {
    int result = await GetDataAsync();
    Console.WriteLine(result);
}
```
`
- `Task.Delay(...)` je - příklad neblokujícího čekání.
- Asynchronní kód zlepšuje odezvu aplikací (např. UI nebo serverů).
