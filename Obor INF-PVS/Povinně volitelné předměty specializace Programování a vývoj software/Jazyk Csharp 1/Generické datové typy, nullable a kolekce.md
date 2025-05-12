## Generické typy v C#

Generické typy umožňují definovat třídy a metody, které mohou pracovat s libovolným datovým typem, aniž by bylo třeba přepisovat stejný kód pro různé typy.

### Motivace
Namísto psaní zvláštní třídy pro `int`, `string`, atd. můžeme využít typový parametr `T`:
```csharp
public class Stack<T> {
    private T[] data;

    public Stack(uint initCapacity) {
        data = new T[initCapacity];
    }
}
```

### Výchozí hodnota typu
Pro přiřazení výchozí hodnoty generického typu se používá:
```csharp
a = default;
```

### Omezení generických typů (`where`)
Můžeme omezit, jaké typy je možné do generické třídy dosadit:
```csharp
where T : struct          // pouze hodnotové typy
where T : class           // pouze referenční typy
where T : new()           // musí mít bezparametrový konstruktor
where T : Person          // typ T musí dědit z Person
where T : IComparable     // typ T musí implementovat rozhraní
```

## Nullable hodnotové typy

Běžné hodnotové typy (např. `int`) nemohou obsahovat `null`. Pro případy, kdy potřebujeme hodnotu i její nepřítomnost, existuje `Nullable<T>`:

Zkrácený zápis:
```csharp
int? x = null;
```

### Vlastnosti
- `HasValue` – vrací `true`, pokud má hodnota nastavenou hodnotu
- `Value` – přístup ke skutečné hodnotě (pozor na výjimku při `null`)
- `GetValueOrDefault()` – vrátí buď hodnotu, nebo výchozí hodnotu

### Příklad:
```csharp
int? b = null;
int a = b ?? -1; // null-coalescing operátor
```

## Kolekce v C#

Rozhraní a třídy z `System.Collections` a `System.Collections.Generic` umožňují pracovat s pokročilými datovými strukturami.

### Základní rozhraní

| Rozhraní       | Popis                                           |
|----------------|--------------------------------------------------|
| `IEnumerable`  | Umožňuje iteraci pomocí `foreach`                |
| `ICollection`  | Přidává informace o počtu prvků, možnost kopírování |
| `IList`        | Přístup k prvkům podle indexu, přidávání, mazání |

Mezi běžné kolekce patří: `List<T>`, `LinkedList<T>`, `Queue<T>`, `Stack<T>`, `Dictionary<K,V>`, `HashSet<T>`, atd.

## Enumerator a foreach

Každý objekt, který implementuje `IEnumerable`, lze procházet pomocí `foreach`.

Enumerator je objekt (nebo struktura), který si pamatuje aktuální pozici v kolekci. Získává se metodou `GetEnumerator()`.

Ukázka použití:
```csharp
foreach (var item in kolekce) {
    Console.WriteLine(item);
}
```

Pro vlastní kolekce je možné `IEnumerable<T>` implementovat a poskytnout vlastní enumerátor.

---

## Shrnutí

- Generické typy umožňují psát znovupoužitelný a bezpečný kód bez nutnosti přetypování.
- Nullable typy rozšiřují možnosti hodnotových typů a umožňují reprezentaci "žádné hodnoty".
- Kolekce v .NET zahrnují širokou škálu datových struktur, jejichž procházení je podporováno přes `foreach` a `IEnumerable`.

