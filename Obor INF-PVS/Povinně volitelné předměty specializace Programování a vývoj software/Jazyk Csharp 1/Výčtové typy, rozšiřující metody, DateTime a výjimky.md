## Výčtový typ (`enum`)

Výčtový typ (enumeration) slouží k vytvoření vlastního typu, který může nabývat pouze předem definovaných pojmenovaných hodnot.

### Základní deklarace
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

### Interní reprezentace
- Interně je `enum` reprezentován jako `int` (číselné hodnoty).
- Možné je přetypování oběma směry:
```csharp
int x = (int)ComputerFormFactor.Laptop;
ComputerFormFactor cf = (ComputerFormFactor)2;
```

### Změna základního typu
```csharp
public enum UsbConnector : short {
    Mini = 1,
    Micro = 3,
    C = 4,
    StandardA = 7
}
```

### Bitová kombinace hodnot (`Flags`)
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

Rozšiřují funkcionalitu existujících tříd bez nutnosti dědění nebo úprav.

### Syntaxe
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

### Použití
```csharp
string s = "toto je test";
int count = s.GetWordCount();

int x = -5;
bool isNeg = x.IsBelowZero();
```

- Použití musí být povoleno pomocí `using` pro jmenný prostor obsahující metody.
- Nelze přepsat existující metody daného typu.

## Práce s časem – `DateTime`

Typ `DateTime` reprezentuje datum a čas s vysokou přesností.

### Vytváření instancí
```csharp
DateTime begin = new DateTime(); // 01.01.0001
DateTime someDate = new DateTime(2023, 9, 6);
DateTime now = DateTime.Now;
DateTime today = DateTime.Today;

string input = "03.05.2023 20:23:55";
DateTime parsed = DateTime.ParseExact(input, "MM.dd.yyyy HH:mm:ss", CultureInfo.InvariantCulture);
```

### Formátování
```csharp
Console.WriteLine(now.ToString("D"));
Console.WriteLine(today.ToString("MM.dd.yyyy HH:mm:ss"));
```

### Operace s DateTime
- Přičítání času: `AddHours()`, `AddMinutes()`, `AddDays()`
- Odečítání: `Subtract()`
- Statické metody:
  - `DateTime.DaysInMonth(year, month)`
  - `DateTime.IsLeapYear(year)`
- Vlastnosti: `Ticks`, `DayOfWeek`, `IsDaylightSavingTime()`

## Výjimky v C#

### Obecně
Výjimky (exceptions) slouží ke zpracování neočekávaných stavů v běhu programu. Typicky jde o:

- Dělení nulou
- Neplatné indexy
- Neexistující soubory
- Chybné vstupy

### Struktura `try-catch`
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

### Vlastní výjimky
Výjimky lze dědit z `System.Exception` a definovat vlastní chování nebo zprávy.

### Klíčová slova
- `throw` – vyvolání výjimky
- `throw e` – předání dál (znovuvyvolání)
- `catch (Exception e) {}` – nebezpečné, pokud ignorováno

### Příklady
```csharp
int[] arr = new int[10];
arr[10] = 1; // IndexOutOfRangeException

int x = 0;
int y = 5 / x; // DivideByZeroException
```

---

## Shrnutí

- `enum` poskytuje typově bezpečný způsob práce s výčty konstant.
- Extension metody rozšiřují existující typy bez zásahu do jejich definice.
- `DateTime` umožňuje práci s časem včetně formátování a operací.
- Výjimky umožňují bezpečně řešit chyby za běhu programu pomocí `try-catch-finally`.

