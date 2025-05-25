## Generické typy v C\#
- Generické typy umožňují definovat třídy a metody, které mohou pracovat s libovolným datovým typem, aniž by bylo třeba přepisovat stejný kód pro různé typy.

#### Motivace
- Namísto psaní zvláštní třídy pro `int`, `string`, atd. můžeme využít typový parametr `T`
```csharp
public class Stack<T> {
    private T[] data;

    public Stack(uint initCapacity) {
        data = new T[initCapacity];
    }
}
```

#### Výchozí hodnota typu
- Pro přiřazení výchozí hodnoty generického typu se používá:
```csharp
a = default;
```

#### Omezení generických typů (`where`)
- Můžeme omezit, jaké typy je možné do generické třídy dosadit:
```csharp
where T : struct          // pouze hodnotové typy
where T : class           // pouze referenční typy
where T : new()           // musí mít bezparametrový konstruktor
where T : Person          // typ T musí dědit z Person
where T : IComparable     // typ T musí implementovat rozhraní
```

## Nullable hodnotové typy
- Běžné hodnotové typy (např. `int`) nemohou obsahovat `null`. Pro případy, kdy potřebujeme hodnotu i její nepřítomnost, existuje `Nullable<T>`:
- Zkrácený zápis:
```csharp
int? x = null;
```

#### Vlastnosti
- `HasValue` – vrací `true`, pokud má hodnota nastavenou hodnotu
- `Value` – přístup ke skutečné hodnotě (pozor na výjimku při `null`)
- `GetValueOrDefault()` – vrátí buď hodnotu, nebo výchozí hodnotu
```csharp
int? b = null;
int a = b ?? -1; // null-coalescing operátor
```

## Kolekce v C\#
- Rozhraní a třídy z `System.Collections` a `System.Collections.Generic` umožňují pracovat s pokročilými datovými strukturami.
#### Základní rozhraní

| Rozhraní       | Popis                                           |
|----------------|--------------------------------------------------|
| `IEnumerable`  | Umožňuje iteraci pomocí `foreach`                |
| `ICollection`  | Přidává informace o počtu prvků, možnost kopírování |
| `IList`        | Přístup k prvkům podle indexu, přidávání, mazání |

- Mezi běžné kolekce patří: `List<T>`, `LinkedList<T>`, `Queue<T>`, `Stack<T>`, `Dictionary<K,V>`, `HashSet<T>`, atd.

## Enumerator a foreach
-  objekt, který implementuje `IEnumerable`, lze procházet pomocí `foreach`.
- Enumerator je objekt (nebo struktura), který si pamatuje aktuální pozici v kolekci. Získává se metodou `GetEnumerator()`.
```csharp
foreach (var item in kolekce) {
    Console.WriteLine(item);
}
```
- Pro vlastní kolekce je možné `IEnumerable<T>` implementovat a poskytnout vlastní enumerátor.

## Výčtový typ (`enum`)
- Výčtový typ (enumeration) slouží k vytvoření vlastního typu, který může nabývat pouze předem definovaných pojmenovaných hodnot.
#### Základní deklarace
```csharp
public enum ComputerFormFactor {
    Atx,
    BigTower,
    Laptop,
    MiniPC,
    Embedded
}

ComputerFormFactor ff = ComputerFormFactor.BigTower;
Console.WriteLine(ff); // vypíše: BigTower
```

#### Interní reprezentace
- Interně je `enum` reprezentován jako `int` (číselné hodnoty).
- Možné je přetypování oběma směry:
```csharp
int x = (int)ComputerFormFactor.Laptop;
ComputerFormFactor cf = (ComputerFormFactor)2;
```

#### Změna základního typu
```csharp
public enum UsbConnector : short {
    Mini = 1,
    Micro = 3,
    C = 4,
    StandardA = 7
}
```

#### Bitová kombinace hodnot (`Flags`)
```csharp
[Flags]
public enum DaysOfWeek {
    Monday = 0x1,
    Tuesday = 0x2,
    Wednesday = 0x4,
    Thursday = 0x8,
    Friday = 0x10,
    Saturday = 0x20,
    Sunday = 0x40,
    Weekend = Saturday | Sunday,
    Workday = 0x1F
}
```

## Rozšiřující metody (`Extension methods`)
- Rozšiřují funkcionalitu existujících tříd bez nutnosti dědění nebo úprav.
#### Syntaxe
- Metoda je statická a definuje se ve statické třídě.
- První parametr musí být označený `this`.
```csharp
public static class Extensions {
    public static int GetWordCount(this string s) {
        return s.Split().Length;
    }

    public static bool IsBelowZero(this int value) {
        return value < 0;
    }
}
```

#### Použití
```csharp
string s = "toto je test";
int count = s.GetWordCount();

int x = -5;
bool isNeg = x.IsBelowZero();
```
- Použití musí být povoleno pomocí `using` pro jmenný prostor obsahující metody.
- Nelze přepsat existující metody daného typu.

## Práce s časem – `DateTime`
- Typ `DateTime` reprezentuje datum a čas s vysokou přesností.
#### Vytváření instancí
```csharp
DateTime begin = new DateTime(); // 01.01.0001
DateTime someDate = new DateTime(2023, 9, 6);
DateTime now = DateTime.Now;
DateTime today = DateTime.Today;

string input = "03.05.2023 20:23:55";
DateTime parsed = DateTime.ParseExact(input, "MM.dd.yyyy HH:mm:ss", CultureInfo.InvariantCulture);
```
#### Formátování
```csharp
Console.WriteLine(now.ToString("D"));
Console.WriteLine(today.ToString("MM.dd.yyyy HH:mm:ss"));
```
#### Operace s DateTime
- Přičítání času: `AddHours()`, `AddMinutes()`, `AddDays()`
- Odečítání: `Subtract()`
- Statické metody:
  - `DateTime.DaysInMonth(year, month)`
  - `DateTime.IsLeapYear(year)`
- Vlastnosti: `Ticks`, `DayOfWeek`, `IsDaylightSavingTime()`

## Výjimky v C\#
- Výjimky (*exceptions*) slouží ke zpracování neočekávaných stavů v běhu programu. Typicky jde o:
	- Dělení nulou
	- Neplatné indexy
	- Neexistující soubory
	- Chybné vstupy
#### Struktura `try-catch`
```csharp
try {
    // rizikový kód
} catch (Exception e) {
    Console.WriteLine("Došlo k chybě: " + e.Message);
}
```
- Lze mít více `catch` větví pro specifické typy výjimek.
- `finally` se vykoná vždy (i při chybě, i bez ní).
```csharp
try {
    // ...
} catch (FileNotFoundException e) {
    // specifická chyba
} finally {
    // úklid (např. zavření souboru)
}
```

#### Vlastní výjimky
- Výjimky lze dědit z `System.Exception` a definovat vlastní chování nebo zprávy.
#### Klíčová slova
- `throw` – vyvolání výjimky
- `throw e` – předání dál (znovuvyvolání)
- `catch (Exception e) {}` – nebezpečné, pokud ignorováno
```csharp
int[] arr = new int[10];
arr[10] = 1; // IndexOutOfRangeException

int x = 0;
int y = 5 / x; // DivideByZeroException
```
