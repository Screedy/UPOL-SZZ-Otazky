## Zapouzdření

Zapouzdření (encapsulation) znamená skrytí interního stavu a implementace objektu před okolním světem. Cílem je umožnit interakci pouze přes definované rozhraní (např. veřejné metody nebo vlastnosti).

- Zabraňuje přímé manipulaci s vnitřními daty objektu.
- Umožňuje snadnější údržbu a změny v kódu.
- Podporuje princip "co nejmenší znalosti" – ostatní části systému nemusí vědět, jak objekt funguje uvnitř.

V praxi to znamená použití modifikátorů přístupu, jako jsou `private`, `public`, `protected`, apod.

## Modifikátory přístupu v C#

Přístupové modifikátory určují, kdo může přistupovat ke třídám, metodám a datovým členům.

### private
- Přístup pouze z dané třídy.
- Nejčastěji používaný pro proměnné (fields), které nemají být přístupné zvenku.

```csharp
private int[,] matrix;
```

### public
- Přístup odkudkoli, bez omezení.
- Používá se pro metody nebo vlastnosti, které tvoří veřejné rozhraní třídy.

```csharp
public int GetVal(int x, int y) {
    return matrix[x, y];
}
```

### protected
- Přístup z dané třídy a jejích potomků.

### internal 
- Přístup je možný z jakéhokoliv místa ve **stejném sestavení** (např. projekt nebo knihovna).   
- Hodí se pro sdílení funkcionality uvnitř jednoho projektu, ale ne mimo něj.
### protected internal
- Přístup buď z **potomků**, nebo odkudkoli ve **stejném sestavení**.
- Přístup je omezen pouze na **potomky**, kteří jsou zároveň ve **stejném sestavení**.

```csharp
internal void LoadInternalConfig() { ... }
```

## Kódovací konvence v C#

Jednotný styl kódu zajišťuje:
- Lepší čitelnost
- Snazší spolupráci v týmu
- Automatickou validaci a formátování v IDE

Příklady zásad:
- PascalCase pro názvy tříd a veřejných metod: `public class IntSet`, `public void Add()`
- camelCase pro názvy proměnných a parametrů: `int count`, `string input`
- Používat odsazení a mezery konzistentně

Oficiální dokumentace ke stylu kódu v C# je dostupná na:  
https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions

## Doporučení k použití getterů a setterů

Přístup k interním proměnným by měl být zprostředkován pomocí veřejných metod nebo vlastností, nikoliv přímým přístupem k proměnným. Důvody:
- Zajištění kontroly nad validací dat
- Možnost snadné změny implementace bez vlivu na uživatele třídy
- Zamezení nekonzistentních nebo nebezpečných změn stavu objektu

Ukázka:
```csharp
private int _value;

public int Value {
    get { return _value; }
    set {
        if (value >= 0) _value = value;
    }
}
```

Tímto způsobem je možné do getteru/setteru přidat kontrolu nebo logiku bez změny veřejného rozhraní.

