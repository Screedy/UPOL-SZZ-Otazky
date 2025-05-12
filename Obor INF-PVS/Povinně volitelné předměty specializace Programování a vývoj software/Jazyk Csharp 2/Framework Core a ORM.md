## Co je ORM?

ORM (Object-Relational Mapping) je technologie, která umožňuje pracovat s databází pomocí běžných objektů v jazyce C#.  
Cílem je **odstínit programátora od přímé práce se SQL** a umožnit přístup k datům přes třídy, kolekce a vlastnosti.

---

## Entity Framework (EF)

Entity Framework je nejpoužívanější ORM framework v C#.

- **EF 6** – starší verze, součást .NET Frameworku
- **EF Core** – moderní, multiplatformní verze (doporučeno)

Oficiální dokumentace: [https://docs.microsoft.com/en-us/ef/](https://docs.microsoft.com/en-us/ef/)

---

## Přístupy vývoje databáze

- **Code First** – definujeme modely v kódu → databáze se generuje podle něj.
- **Database First** – začínáme existující databází → generuje se kód z databáze.

V této lekci používáme přístup **Code First**.

---

## Instalace EF Core pomocí NuGet

Nutné balíčky (pro SQLite např.):
- `Microsoft.EntityFrameworkCore`
- `Microsoft.EntityFrameworkCore.Sqlite`
- `Microsoft.EntityFrameworkCore.Design`
- `Microsoft.EntityFrameworkCore.Tools` (pro příkazy jako `dotnet ef`)

---

## Model – datové třídy

Třída reprezentující tabulku:
```csharp
public class Custommer {
    public int Id { get; set; }                 // primární klíč
    public string Name { get; set; }
    public int AddressId { get; set; }
    public virtual Address Address { get; set; } // navigační vlastnost
}
```

**Konvence EF:**
- Vlastnost `Id` nebo `NázevTřídyId` je automaticky primární klíč.
- Navigační vlastnosti (`virtual`) propojují entity mezi sebou.

---

## Kontext databáze – `DbContext`

Objekt zajišťující komunikaci s databází:
```csharp
public class EshopContext : DbContext {
    public DbSet<Address> Addresses { get; set; }
    public DbSet<Custommer> Custommers { get; set; }
}
```

Pro každý model vytvoříme `DbSet<T>` – což reprezentuje tabulku.

---

## Vytvoření databáze a migrace

1. Nainstalovat nástroje:
```bash
dotnet tool install --global dotnet-ef
```

2. Přidat migraci:
```bash
dotnet ef migrations add InitialCreate
```

3. Vytvořit databázi:
```bash
dotnet ef database update
```

---

## Práce s daty

### Vložení dat
```csharp
using (var ctx = new EshopContext()) {
    var address = new Address { City = "Olomouc", Street = "17. listopadu", Number = 14 };
    var customer = new Custommer { Name = "Karel Vomáčka", Address = address };
    ctx.Custommers.Add(customer);
    ctx.SaveChanges(); // nutné volat pro uložení změn
}
```

### Výběr dat
```csharp
using (var ctx = new EshopContext()) {
    var customers = ctx.Custommers.Where(c => c.Address.City == "Olomouc");
    foreach (var c in customers) {
        Console.WriteLine($"{c.Name}, {c.Id}");
    }
}
```

---

## Vztahy mezi entitami

### Vazba 1:N (např. adresa má více studentů)
```csharp
public class Address {
    public int Id { get; set; }
    public string City { get; set; }
    public virtual ICollection<Student> Students { get; set; }
}
```

### Vazba M:N (student má více předmětů)
Musíme vytvořit **mezi-entitu**:

```csharp
public class StudentSubject {
    public int StudentId { get; set; }
    public Student Student { get; set; }
    public int SubjectId { get; set; }
    public Subject Subject { get; set; }
}
```

A nakonfigurovat ve `DbContext`:
```csharp
modelBuilder.Entity<StudentSubject>().HasKey(ss => new { ss.StudentId, ss.SubjectId });
```

---

## Úprava dat
```csharp
var student = ctx.Students.FirstOrDefault(s => s.Id == 1);
if (student != null) {
    student.Name = "Dave Lister";
    ctx.SaveChanges();
}
```

## Smazání záznamu
```csharp
var student = ctx.Students.FirstOrDefault(s => s.Id == 1);
ctx.Students.Remove(student);
ctx.SaveChanges();
```

Nebo nastavením stavu:
```csharp
ctx.Entry(student).State = EntityState.Deleted;
```

Pozor na kaskádové mazání: nutné nastavit v modelu (viz dokumentace).

---

## Shrnutí

- EF Core umožňuje práci s databází přímo přes C# objekty.
- Code First vývoj je rychlý a flexibilní.
- `DbContext` je základní brána pro práci s daty.
- Podporuje LINQ pro dotazy, navigační vlastnosti a migrace schématu.

EF šetří čas, ale je třeba chápat jeho principy – zejména vztahy, konvence a životní cyklus objektů.

