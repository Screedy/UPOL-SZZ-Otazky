## Co je reflexe?

Reflexe je mechanismus, který umožňuje **získávat informace o typech, objektech, metodách a atributech za běhu programu**.

### Příklady využití:
- Dynamická serializace/deserializace (např. do JSON)
- Vlastní ORM knihovny
- Dynamické vytváření objektů
- Zjišťování, zda objekt obsahuje určitou metodu, vlastnost apod.

---

## Práce s typy přes reflexi

Získání `Type` objektu:

```csharp
Custommer c = new Custommer();
Type t = c.GetType();         // z instance
Type t2 = typeof(Custommer);  // z typu
Type t3 = Type.GetType("Namespace.ClassName"); // z názvu
```

Vlastnosti typu:
```csharp
t.IsClass, t.IsAbstract, t.IsEnum, t.IsArray, t.IsPrimitive, ...
```

---

## Zjišťování informací o členech typu

### Metody
```csharp
MethodInfo[] methods = t.GetMethods();
foreach (var m in methods) {
    Console.WriteLine($"{m.Name} vrací {m.ReturnType}");
}
```

### Vlastnosti a pole
```csharp
PropertyInfo[] props = t.GetProperties();
FieldInfo[] fields = t.GetFields();
```

### Parametry metod
```csharp
MethodInfo m = t.GetMethod("SomeMethod");
ParameterInfo[] parameters = m.GetParameters();
```

---

## Atributy

Atributy umožňují programátorům **připojit metadata ke kódu**, která jsou pak dostupná přes reflexi.

Příklady:
- `[Serializable]`
- `[HttpGet]`, `[HttpPost]`
- `[PrimaryKey]`, `[NonSerialized]`

Použití:
```csharp
[Serializable]
public class Student { ... }
```

---

## Čtení atributů pomocí reflexe

```csharp
FieldInfo[] fields = t.GetFields(BindingFlags.NonPublic | BindingFlags.Instance);
foreach (FieldInfo f in fields) {
    object[] attrs = f.GetCustomAttributes(false);
    foreach (object a in attrs) {
        Console.WriteLine(a.GetType());
    }
}
```

### Kontrola na konkrétní atribut:
```csharp
if (m.GetCustomAttributes(typeof(ThreadStaticAttribute), true).Length > 0) {
    // metoda má atribut
}
```

---

## Vlastní atributy

Lze vytvářet vlastní atributy děděním ze třídy `System.Attribute`:

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Property)]
public sealed class MyAttribute : Attribute {
    public string Info { get; set; }
    public MyAttribute(string info) {
        Info = info;
    }
}
```

Použití:
```csharp
[My("Poznámka")]
public class MyClass { ... }
```

---

## Reflexe – úskalí a doporučení

- Reflexe je výkonná, ale **náročná na výkon** – VM nemůže provádět optimalizace.
- Neměla by se používat, pokud existuje standardní přístup.
- Je možné získat a volat i **non-public členy**, což má bezpečnostní dopady.
- V některých prostředích může být reflexe zakázaná (sandbox).

---

## Shrnutí

- Reflexe umožňuje dynamickou práci s typy a objekty během běhu programu.
- Atributy přidávají metadata, která lze zpracovat pomocí reflexe.
- Kombinace reflexe a atributů je základ pro:
  - ORM nástroje (např. Entity Framework)
  - Serializátory (např. `System.Text.Json`)
  - Dynamické validace, testování, mapování

Správné použití reflexe vede k silným a flexibilním nástrojům – ale je třeba s ní zacházet uvážlivě.

