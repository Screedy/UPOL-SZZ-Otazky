## Úvod do objektově orientovaného programování (OOP)
- Objektově orientované programování je hlavní paradigma jazyka C#. Program je tvořen objekty, které mají:
	- Stav (vlastnosti)
	- Chování (metody)
	- Možnost interakce
- Výhodou OOP je:
	- Snadná strukturalizace a údržba kódu
	- Možnost rozdělení vývoje mezi více programátorů
	- Rozšiřitelnost a znovupoužitelnost
#### Základní principy OOP
- **Zapouzdření** – oddělení vnitřní reprezentace od vnějšího rozhraní.
- **Dědičnost** – možnost odvození nové třídy z existující.
- **Polymorfismus** – schopnost volat stejné rozhraní s různým chováním.
- **Rozhraní objektů** – přesně definovaný způsob, jak s objektem komunikovat.

## Třídy v C\#
- Třída je šablona pro vytváření objektů. Obsahuje:
	- **Fields (políčka)** – proměnné reprezentující stav objektu.
	- **Konstanty** – neměnné hodnoty, často `public static`.
	- **Metody** – operace prováděné objektem.
	- **Properties (vlastnosti)** – přístupové metody ke stavovým proměnným.
	- **Konstruktory** – speciální metody volané při vytvoření objektu.
	- **Destruktor** – volán při odstranění objektu (většinou spravován GC).
	- **Vnořené třídy** – třídy definované uvnitř jiné třídy.

#### Příklad definice třídy
```csharp
public class HardDiskDrive {
    public const string Name = "Hard disk drive";
    private uint capacity;
    private string manufacturer;
    private string partNumber;
    public uint BufferSize;
    public uint WriteSpeed;

    public string StoreName => manufacturer + partNumber;

    public uint GetFreeSpace() { ... }
    public bool WriteNumber(int number, uint position) { ... }
    public int ReadNumber(uint position) { ... }
    public void ParkReadHead() { ... }
}
```

#### Konstruktor
```csharp
public HardDiskDrive(uint capacity, string manufacturer, string partNumber, uint bufferSize, uint writeSpeed)
{
    this.capacity = capacity;
    this.manufacturer = manufacturer;
    this.partNumber = partNumber;
    BufferSize = bufferSize;
    WriteSpeed = writeSpeed;
}
```
- Vytvoření objektu:
```csharp
HardDiskDrive disk = new HardDiskDrive(1000000, "WD", "SX04210345", 1000, 10000);
```

## Volání metod a přetěžování
- Metody voláme pomocí tečkové notace:
```csharp
disk.WriteNumber(42, 42468);
```
- Třída může obsahovat více metod se stejným názvem, ale různými parametry – tzv. **přetěžování metod**.

## Statické metody
- Statické metody jsou volány bez nutnosti vytvářet instanci třídy
- Příkladem je `Math.Sqrt(25)` (vypočítá odmocninu z $25$)
- Používají se ke zpřístupnění obecné funkcionality spojené s třídou.
- Měly by se vždy chovat stejně
```csharp
public static double Vypocitej(...) { ... }
```
- Nejznámější statickou metodou je metoda `Main`, vstupní bod programu.

## Zapouzdření
- Zapouzdření (encapsulation) znamená skrytí interního stavu a implementace objektu před okolním světem. Cílem je umožnit interakci pouze přes definované rozhraní (např. veřejné metody nebo vlastnosti).
- Zabraňuje přímé manipulaci s vnitřními daty objektu.
- Umožňuje snadnější údržbu a změny v kódu.
- Podporuje princip "co nejmenší znalosti" – ostatní části systému nemusí vědět, jak objekt funguje uvnitř.
- V praxi to znamená použití modifikátorů přístupu, jako jsou `private`, `public`, `protected`, apod.

## Modifikátory přístupu v C\#
- Přístupové modifikátory určují, kdo může přistupovat ke třídám, metodám a datovým členům.
#### private
- Přístup pouze z dané třídy.
- Nejčastěji používaný pro proměnné (fields), které nemají být přístupné zvenku.

```csharp
private int[,] matrix;
```
#### public
- Přístup odkudkoli, bez omezení.
- Používá se pro metody nebo vlastnosti, které tvoří veřejné rozhraní třídy.

```csharp
public int GetVal(int x, int y) {
    return matrix[x, y];
}
```
#### protected
- Přístup z dané třídy a jejích potomků.
#### internal 
- Přístup je možný z jakéhokoliv místa ve **stejném sestavení** (např. projekt nebo knihovna).   
- Hodí se pro sdílení funkcionality uvnitř jednoho projektu, ale ne mimo něj.
#### protected internal
- Přístup buď z **potomků**, nebo odkudkoli ve **stejném sestavení**.
- Přístup je omezen pouze na **potomky**, kteří jsou zároveň ve **stejném sestavení**.

```csharp
internal void LoadInternalConfig() { ... }
```

## Rozhraní (interface)
- Rozhraní v C# je formální popis veřejného rozhraní třídy – tj. jaké metody (nebo vlastnosti) musí třída implementovat. Rozhraní neobsahuje implementaci, pouze hlavičky metod.
#### Definice rozhraní
```csharp
public interface IStorageDevice {
    uint GetFreeSpace();
    bool WriteNumber(int number, uint position);
    int ReadNumber(uint position);
}
```
- Třída, která rozhraní implementuje, musí všechny tyto metody definovat:
```csharp
public class HardDiskDrive : IStorageDevice {
    ...
}
```
- Konvence: názvy rozhraní začínají písmenem `I`.

#### Příklad – zásobník
```csharp
public interface IStack {
    int Size();
    int Pop();
    int Peek();
    bool Push(int number);
    void Print();
}

public class Stack : IStack {
    ...
}
```

## Hodnotové a referenční datové typy

#### Hodnotové typy
- Ukládají hodnotu přímo (např. `int`, `bool`, `float`, `double`)
- Ukládají se na zásobník (stack)
- Parametry se předávají jako kopie

#### Referenční typy
- Ukládají odkaz (adresu) na skutečná data, která se nachází na halde
- Typicky instance tříd (`class`, `string`, pole)
- Parametry se předávají jako odkaz (reference)

#### Klíčová slova `ref` a `out`
- `ref` – parametr se předává jako reference (musí být inicializován)
- `out` – parametr se používá pro návrat hodnot, nemusí být inicializován, ale musí být nastaven ve volané metodě
```csharp
void AddFive(ref int number) {
    number += 5;
}

bool TryParse(string s, out int result) {
    ...
}
```

## Dědičnost v C\#
- C# podporuje **jednoduchou dědičnost** (z jedné třídy), ale třída může implementovat více rozhraní.
- Každá třída dědí ze základní třídy `System.Object` a tím i metody:
	- `ToString()`
	- `Equals()`
	- `GetHashCode()`
	- `GetType()`
#### Příklad: třída `Person` a `Employee`
```csharp
public class Person {
    public string Name;
    public string Surname;
    private int Id;
    public Address address;

    public Person(string name, string surname, Address a) {
        Name = name;
        Surname = surname;
        address = a;
    }

    public override string ToString() {
        return $"{Name} {Surname}";
    }
}

public class Employee : Person {
    ...
}
```

#### Překrývání metod (`virtual`, `override`)
- Metodu lze v nadtřídě označit jako `virtual`
- V potomkovi ji lze přepsat pomocí `override`

```csharp
public override string ToString() {
    return $"Zaměstnanec: {Name} {Surname}";
}
```

## Modifikátory přístupu při dědičnosti
- Dědičnost ovlivňuje, jaké členy jsou přístupné:

| Modifikátor         | Přístup                      |
|---------------------|------------------------------|
| `public`            | odkudkoli                    |
| `private`           | pouze v rámci dané třídy     |
| `protected`         | v dané třídě a jejích potomcích |
| `internal`          | v rámci sestavení (assembly) |
| `protected internal`| kombinace výše uvedeného     |
| `private protected` | jen v potomcích a ve stejném sestavení |

#### Zjišťování typu objektu
- Pomocí operátoru `is` lze testovat, zda objekt implementuje rozhraní nebo je určitého typu:
```csharp
if (obj is Person) { ... }
if (zasobnik is IStack) { ... }
```

## Properties a fields
#### Fields
- Základní datové členy třídy
- Uchovávají stav objektu
- Měly by být `private`, přístupné přes `property` nebo metody
#### Properties
- Veřejné rozhraní pro přístup k `field` hodnotám
- Mohou obsahovat validaci nebo výpočty
- Automaticky generované property:
```csharp
public int Length { get; set; }
```

#### Vlastní implementace s validací
```csharp
private int _length;

public int Length {
    get => _length;
    set {
        if (value >= 0) _length = value;
    }
}
```

## Přetížení operátorů
- C# umožňuje definovat vlastní chování standardních operátorů pro vlastní typy.
#### Přípustné operátory k přetížení:
- Aritmetické: `+`, `-`, `*`, `/`, `%`, `++`, `--`
- Relační: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logické: `!`, `~`, `&`, `|`, `^`, `<<`, `>>`

#### Syntaxe
```csharp
public static Complex operator +(Complex c1, Complex c2) {
    return new Complex(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
}
```
- Nepřetěžují se: `=`, `.` (členové), `?:`, `as`, `is`, `new`, `typeof`...

## N-tice (tuples)
- Rychlý způsob, jak vracet nebo uchovávat více hodnot bez nutnosti vytvářet třídu.

#### Deklarace
```csharp
(int, string, double) mojeNtice = (5, "text", 3.14);
Console.WriteLine(mojeNtice.Item3);
```

#### Pojmenování prvků
```csharp
(int id, string jmeno, double hodnota) zaznam = (1, "Jana", 99.5);
Console.WriteLine(zaznam.jmeno);
```

>[!tip]
> Pojmenování funguje pouze v době kompilace, ne při reflexi.

## Delegáti
- Delegát je typ bezpečný z hlediska typů, který uchovává odkaz na metodu.

#### Základní použití
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
