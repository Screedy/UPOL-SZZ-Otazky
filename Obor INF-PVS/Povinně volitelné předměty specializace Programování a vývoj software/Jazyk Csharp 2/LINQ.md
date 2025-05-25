## Delegáti v C\#
- Delegát v C# je objekt, který reprezentuje odkaz na metodu. Chová se jako typově bezpečný ukazatel na funkci.

#### Vlastnosti:
- Umožňuje předávat metody jako parametry.
- Delegát může odkazovat na více metod (multicast).
- Podporuje anonymní metody i lambda výrazy.

#### Vlastní deklarace delegáta
```csharp
delegate string FuncDelegate(int input1, out int input2);
```

#### Předdefinované generické typy:
- **`Func<T1,...,TResult>`** – až 16 vstupních parametrů, vrací hodnotu
  ```csharp
  Func<int, int, int> add = (a, b) => a + b;
  ```
- **`Action<T1,...>`** – až 16 vstupních parametrů, nevrací žádnou hodnotu (`void`)
  ```csharp
  Action<string> write = s => Console.WriteLine(s);
  ```
- **`Predicate<T>`** – vrací `bool`, typicky pro filtrování
  ```csharp
  Predicate<int> isPositive = x => x > 0;
  ```

## Lambda výrazy
- Lambda výraz je anonymní metoda, která může být použita pro přiřazení k delegátu, `Func<>`, `Action<>` nebo jako argument metod.
#### Zápis:
```csharp
(parametry) => výraz
```
#### Příklad:
```csharp
Func<int, int> square = x => x * x;
Console.WriteLine(square(5)); // Výstup: 25
```

- Může být předán jako parametr.
- Může být použit pro tvorbu výrazu (`Expression<T>`).
- Staticky typovaný – při přiřazení musí být znám typ.

## LINQ
- *Language Integrated Query*
- LINQ je technologie, která umožňuje psát dotazy přímo v jazyce C#. Tyto dotazy fungují nad:
	- kolekcemi (`IEnumerable`)
	- databázemi (Entity Framework)
	- XML dokumenty
	- a dalšími datovými zdroji
- LINQ poskytuje jednotný způsob práce s daty bez ohledu na jejich původ

#### Dotazovací (query) syntaxe
```csharp
var result = from number in numbers
             where number > 5
             select number;
```

#### Fluent (method chaining) syntaxe – preferovaná:
```csharp
var result = numbers.Where(n => n > 5).Select(n => n * 2);
```

#### Filtrování (`Where`)
Vrací všechny prvky, které splňují podmínku:
```csharp
var adults = people.Where(p => p.Age >= 18);
```

#### Projekce (`Select`)
Převod objektů do jiného tvaru:
```csharp
var names = people.Select(p => new { p.Name, p.Surname });
```

#### Řazení (`OrderBy`, `ThenBy`)
```csharp
people.OrderBy(p => p.Age).ThenBy(p => p.Name);
```

#### Ořezání (`Take`, `Skip`)
```csharp
people.Take(10);       // prvních 10
people.Skip(5).Take(5); // 6. až 10.
```

#### Prvky (`First`, `FirstOrDefault`, `Last`, `Single`)
```csharp
var student = people.First(p => p.Grade == 1);
```

#### Kontrola (`Any`, `All`, `Contains`)
```csharp
bool hasAdults = people.Any(p => p.Age >= 18);
```

#### Počet (`Count`)
```csharp
int numOfPVS = people.Count(p => p.OborKomb == "INF-PVS");
```

#### Unikátní prvky (`Distinct`)
```csharp
var uniqueValues = values.Distinct();
```

#### Množinové operace
```csharp
var intersection = list1.Intersect(list2);
var union = list1.Union(list2);
var difference = list1.Except(list2);
```

#### Kdy použít LINQ
- Kdykoli pracujete s kolekcemi (pole, seznamy, výsledky dotazů).
- Potřebujete přehledný způsob filtrování, řazení, transformace.
- Vhodné i pro dotazování nad objekty načtenými z databáze nebo XML/JSON.

---
## Shrnutí
- **Delegáti** umožňují pracovat s metodami jako s daty – např. je předávat, ukládat, nebo řetězit.
- **Lambda výrazy** zjednodušují zápis a jsou základním kamenem moderního C#.
- **LINQ** je výkonný nástroj pro efektivní, přehledné a typově bezpečné zpracování dat.
