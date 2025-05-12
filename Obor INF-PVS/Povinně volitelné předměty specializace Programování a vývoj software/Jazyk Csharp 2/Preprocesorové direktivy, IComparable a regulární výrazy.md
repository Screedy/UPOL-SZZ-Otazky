## Preprocesorové direktivy

V C# začínají znakem `#` a slouží k ovlivnění chování překladače ještě **před samotným překladem kódu**.

### Základní direktivy
```csharp
#define DEBUG
#undef DEBUG

#if DEBUG
    Console.WriteLine("Debug režim");
#else
    Console.WriteLine("Release režim");
#endif
```

### Další:
- `#error`, `#warning` – vynucení chyby nebo varování
- `#region`, `#endregion` – pro skládání kódu ve Visual Studiu

---

## Rozhraní `IComparable`

Slouží k **porovnávání objektů** mezi sebou, například při řazení v kolekcích.

### Definice:
```csharp
public interface IComparable {
    int CompareTo(object obj);
}
```

### Návratová hodnota:
- `< 0` – objekt je menší než `obj`
- `= 0` – objekty jsou stejné
- `> 0` – objekt je větší než `obj`

### Implementace:
```csharp
public int CompareTo(object obj) {
    if (obj is Person other) {
        return this.Age.CompareTo(other.Age);
    }
    throw new ArgumentException("Object is not a Person");
}
```

---

## Třída `Regex` – regulární výrazy

Umožňuje efektivní **vyhledávání a zpracování textových vzorů**.

### Základní použití:
```csharp
Regex rx = new Regex("pattern");
Match m = rx.Match("nějaký text");

foreach (Match match in rx.Matches("další text")) {
    Console.WriteLine($"Nalezeno: {match.Value}, index: {match.Index}");
}
```

### Typické využití:
- Ověření struktury (např. e-mail)
- Extrakce údajů z textu
- Získání více výskytů určitého vzoru

---

## Shrnutí

- **Direktivy** ovlivňují kompilaci programu podmíněným překladem.
- **Rozhraní `IComparable`** umožňuje přirozené třídění objektů.
- **Regulární výrazy (`Regex`)** poskytují výkonný nástroj pro analýzu a zpracování textu.
