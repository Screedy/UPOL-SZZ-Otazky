## Práce s konzolí

### Vstup od uživatele
Čtení textového vstupu:
```csharp
string vstup = Console.ReadLine();
```

Příklad čtení číselného vstupu s ošetřením výjimky:
```csharp
static void ReadNumber(out int a, string text) {
    Console.Write(text);
    string input = Console.ReadLine();
    try {
        a = int.Parse(input);
    } catch (Exception) {
        ReadNumber(out a, text);
    }
}
```

### Změna vzhledu konzole
```csharp
Console.BackgroundColor = ConsoleColor.Green;
Console.ForegroundColor = ConsoleColor.Red;
Console.ResetColor();
Console.Clear();
Console.SetWindowSize(80, 25);
Console.Title = "Moje aplikace";
```

### Reakce na stisk klávesy
```csharp
ConsoleKeyInfo info = Console.ReadKey();
if (info.Key == ConsoleKey.Backspace) {
    Console.WriteLine("Zmáčkl backspace");
}
```

## Struktury (`struct`)

Struktura je **hodnotový typ**, definovaný uživatelem, podobný třídě, ale jednodušší.

### Deklarace
```csharp
public struct StorageItem {
    public int Length;
    public int Width;
    public int Height;
    public string Name;

    public int Volume() => Length * Width * Height;
    public int Area() => Length * Width;
}
```

### Vytváření instancí
```csharp
StorageItem si = new StorageItem(); // volání bez parametrů
si.Length = 32;

// nebo vše ručně, nutno inicializovat všechny hodnoty
StorageItem si2;
si2.Length = 32;
si2.Width = 10;
si2.Height = 20;
si2.Name = "Box";
```

### Přiřazování struktur
Při přiřazení se kopíruje hodnota:
```csharp
StorageItem kopie = si;
kopie.Length = 5;
// si.Length zůstává nezměněné
```

## Rozdíl mezi strukturou a třídou

| Vlastnost              | Struktura (`struct`) | Třída (`class`) |
|------------------------|----------------------|------------------|
| Uložení v paměti       | zásobník (stack)     | halda (heap)     |
| Dědičnost              | ne (jen z ValueType) | ano              |
| Typ                    | hodnotový            | referenční       |
| Výchozí konstruktor    | implicitní bez parametrů | definovatelný |
| Metoda Equals()        | porovnává po složkách | lze přepsat      |

## Indexery

Indexery umožňují přistupovat k prvkům třídy podobně jako k prvkům pole pomocí `[]`.

### Deklarace
```csharp
public class Dictionary<K, V> {
    private List<K> keys = new List<K>();
    private List<V> values = new List<V>();

    public V this[K key] {
        get {
            int index = keys.IndexOf(key);
            if (index > -1) return values[index];
            else return default(V);
        }
        set {
            int index = keys.IndexOf(key);
            if (index == -1) {
                keys.Add(key);
                values.Add(value);
            }
        }
    }
}
```

### Použití
```csharp
Dictionary<string, int> d = new Dictionary<string, int>();
d["jablko"] = 5;
Console.WriteLine(d["jablko"]);
```

Indexery mohou být i vícerozměrné a nemusí používat jen celočíselné indexy – typ může být libovolný.

---

## Shrnutí

- Pomocí `Console.ReadLine()` a dalších metod lze číst a ovlivňovat výstup v konzoli.
- `struct` je lehká alternativa třídy pro jednoduché datové objekty bez dědičnosti.
- Indexery umožňují přistupovat k prvkům tříd podobně jako k poli pomocí `[]`.

