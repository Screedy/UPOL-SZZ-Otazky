## Preprocesorové direktivy
- V C# začínají znakem `#` a slouží k ovlivnění chování překladače ještě **před samotným překladem kódu**.

#### Základní direktivy
```csharp
#define DEBUG
#undef DEBUG

#if DEBUG
    Console.WriteLine("Debug režim");
#else
    Console.WriteLine("Release režim");
#endif
```
- `#error`, `#warning` – vynucení chyby nebo varování
- `#region`, `#endregion` – pro skládání kódu ve Visual Studiu

## Třída `Regex` – regulární výrazy
- Umožňuje efektivní **vyhledávání a zpracování textových vzorů**.
#### Základní použití:
```csharp
Regex rx = new Regex("pattern");
Match m = rx.Match("nějaký text");

foreach (Match match in rx.Matches("další text")) {
    Console.WriteLine($"Nalezeno: {match.Value}, index: {match.Index}");
}
```

#### Typické využití:
- Ověření struktury (např. e-mail)
- Extrakce údajů z textu
- Získání více výskytů určitého vzoru
