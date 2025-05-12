## Rozhraní (interface)

Rozhraní v C# je formální popis veřejného rozhraní třídy – tj. jaké metody (nebo vlastnosti) musí třída implementovat. Rozhraní neobsahuje implementaci, pouze hlavičky metod.

### Definice rozhraní
```csharp
public interface IStorageDevice {
    uint GetFreeSpace();
    bool WriteNumber(int number, uint position);
    int ReadNumber(uint position);
}
```

Třída, která rozhraní implementuje, musí všechny tyto metody definovat:
```csharp
public class HardDiskDrive : IStorageDevice {
    ...
}
```

Konvence: názvy rozhraní začínají písmenem `I`.

### Příklad – zásobník
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

### Hodnotové typy
- Ukládají hodnotu přímo (např. `int`, `bool`, `float`, `double`)
- Ukládají se na zásobník (stack)
- Parametry se předávají jako kopie

### Referenční typy
- Ukládají odkaz (adresu) na skutečná data, která se nachází na halde
- Typicky instance tříd (`class`, `string`, pole)
- Parametry se předávají jako odkaz (reference)

### Klíčová slova `ref` a `out`

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

## Dědičnost v C#

C# podporuje **jednoduchou dědičnost** (z jedné třídy), ale třída může implementovat více rozhraní.

Každá třída dědí ze základní třídy `System.Object` a tím i metody:
- `ToString()`
- `Equals()`
- `GetHashCode()`
- `GetType()`

### Příklad: třída `Person` a `Employee`
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

### Překrývání metod (`virtual`, `override`)
- Metodu lze v nadtřídě označit jako `virtual`
- V potomkovi ji lze přepsat pomocí `override`

```csharp
public override string ToString() {
    return $"Zaměstnanec: {Name} {Surname}";
}
```

## Modifikátory přístupu při dědičnosti

Dědičnost ovlivňuje, jaké členy jsou přístupné:

| Modifikátor         | Přístup                      |
|---------------------|------------------------------|
| `public`            | odkudkoli                    |
| `private`           | pouze v rámci dané třídy     |
| `protected`         | v dané třídě a jejích potomcích |
| `internal`          | v rámci sestavení (assembly) |
| `protected internal`| kombinace výše uvedeného     |
| `private protected` | jen v potomcích a ve stejném sestavení |

## Zjišťování typu objektu

Pomocí operátoru `is` lze testovat, zda objekt implementuje rozhraní nebo je určitého typu:

```csharp
if (obj is Person) { ... }
if (zasobnik is IStack) { ... }
```

## Shrnutí

- Rozhraní umožňují definovat "smlouvu", kterou musí třídy dodržet
- Hodnotové typy pracují s kopiemi, referenční typy s odkazy
- Dědičnost umožňuje tvořit hierarchie tříd a přebírat funkcionalitu
- Klíčová slova `ref` a `out` umožňují předávání parametrů odkazem
- Přístupové modifikátory určují, jak je možné pracovat s členy třídy

