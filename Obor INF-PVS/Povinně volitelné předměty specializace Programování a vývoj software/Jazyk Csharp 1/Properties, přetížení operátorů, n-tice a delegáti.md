## Properties a fields

### Fields
- Základní datové členy třídy
- Uchovávají stav objektu
- Měly by být `private`, přístupné přes `property` nebo metody

### Properties
- Veřejné rozhraní pro přístup k `field` hodnotám
- Mohou obsahovat validaci nebo výpočty
- Automaticky generované property:
```csharp
public int Length { get; set; }
```

### Vlastní implementace s validací
```csharp
private int _length;

public int Length {
    get => _length;
    set {
        if (value >= 0) _length = value;
    }
}
```

---

## Přetížení operátorů

C# umožňuje definovat vlastní chování standardních operátorů pro vlastní typy.

### Přípustné operátory k přetížení:
- Aritmetické: `+`, `-`, `*`, `/`, `%`, `++`, `--`
- Relační: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logické: `!`, `~`, `&`, `|`, `^`, `<<`, `>>`

### Syntaxe
```csharp
public static Complex operator +(Complex c1, Complex c2) {
    return new Complex(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
}
```

- Nepřetěžují se: `=`, `.` (členové), `?:`, `as`, `is`, `new`, `typeof`...

---

## N-tice (tuples)

Rychlý způsob, jak vracet nebo uchovávat více hodnot bez nutnosti vytvářet třídu.

### Deklarace
```csharp
(int, string, double) mojeNtice = (5, "text", 3.14);
Console.WriteLine(mojeNtice.Item3);
```

### Pojmenování prvků
```csharp
(int id, string jmeno, double hodnota) zaznam = (1, "Jana", 99.5);
Console.WriteLine(zaznam.jmeno);
```

> Pojmenování funguje pouze v době kompilace, ne při reflexi.

---

## Delegáti

Delegát je typ bezpečný z hlediska typů, který uchovává odkaz na metodu.

### Základní použití
```csharp
delegate int MathOperation(int x, int y);

int Add(int a, int b) => a + b;
int Mul(int a, int b) => a * b;

int[] MapMathOperation(int[] a, int[] b, MathOperation op) {
    int[] result = new int[a.Length];
    for (int i = 0; i < a.Length; i++) {
        result[i] = op(a[i], b[i]);
    }
    return result;
}
```

- Delegáty lze kombinovat (např. v GUI, nebo pro více `void` metod).
- Používají se také pro paralelní operace (`BeginInvoke`, `EndInvoke`).

---

## Shrnutí

- `Property` je mechanismus pro bezpečný přístup ke `fieldům`.
- Operátory v C# lze přetížit a definovat jejich chování pro vlastní typy.
- N-tice (`tuple`) jsou lehká náhrada struktury/třídy pro vícenásobné návraty.
- Delegáti umožňují předávání metod jako parametrů a dynamické volání funkcí.

