# 1. Object-Relational Mapping (ORM)

> [!success]
> **ORM (Object-Relational Mapping)** je technologie, která umožňuje pracovat **s relační databází pomocí objektů** v programovacím jazyce _místo ručního psaní SQL dotazů_.

> [!note]
> _Jednoduše řečeno_:
>
> - objekt v C# ↔ řádek v databázové tabulce,
> - vlastnost objektu ↔ sloupec tabulky,
> - kolekce objektů ↔ tabulka

- **Výhody:**
  - Transparentní práce s databází pomocí objektů.
  - Odstínění od konkrétní DB implementace, vyšší přenositelnost mezi databázemi (skrývá rozdíly mezi jednotlivými databázovými systémy)
  - Typová kontrola už při kompilaci. (LINQ dotazy, ne stringy)
  - Vyšší bezpečnost – automaticky parametrizuje dotazy, čímž snižuje riziko SQL Injection
- **Nevýhody:**
  - Složitější dotazy (analytika, agregace) bývají v čistém SQL výkonnější.
  - Některé databázové konstrukty (stored procedures, hinty) ORM neumí dobře.

# 2. Entity Framework

> [!success]
> **Entity Framework (EF)** je _oficiální ORM framework společnosti Microsoft_ pro platformu .NET.

> [!info]
> První verze vznikla v roce 2008 jako součást .NET Frameworku.
>
> _Od verze 6 je open-source_ a dnes se používá především **Entity Framework Core (EF Core)**, který je _multiplatformní_.
>
> EF podporuje **mnoho databází** (SQL Server, SQLite, PostgreSQL, Oracle, MySQL...).

> [!warning]
> Entity Framework Core se instaluje pomocí **NuGet Package Manageru**.

## 2.1 Přístupy k vytvoření modelu

- Entity Framework podporuje dva základní přístupy.

### 2.1.1 Code First

> [!success]
> **Vývoj probíhá od kódu směrem k databázi.**

- Nejprve se **vytvoří model pomocí C# tříd**. Z něj Entity framework _vytvoří databázi, tabulky._ Průběžně se _upravuje databáze_ pomocí _migrací_.

> [!info]
> Vhodné pro nové aplikace.

### 2.1.2 Database First

> [!success]
> **Vývoj probíhá od databáze směrem ke kódu.**

- Nejprve existuje databáze. Entity Framework z ní následně vygeneruje C# entity, vytvoří DbContext.

> [!info]
> Vhodné pro existující databáze.

## 2.2 Entity (model)

> [!success]
> **Entita** = **běžná C# třída**, které představují tabulky databáze.

### **2.2.1 Konvence Code First**

- **Vlastnost** `Id` (nebo `<EntityName>Id`) je **automaticky** rozpoznána jako **primární klíč.**
- **Vlastnost typu jiné entity** (např. `public virtual Address Address`) představuje **navigační vlastnost**, která umožňuje přístup k souvisejícímu objektu. Odpovídající **cizí klíč** je obvykle uložen ve vlastnosti `AddressId`.
- **Vlastnost typu** `ICollection<T>` **nebo** `List<T>` představuje **kolekční navigační vlastnost**, která vyjadřuje vztah k více entitám (1:N nebo M:N).
- **Příklad entity:**

```csharp
public class Customer {
    public int Id { get; set; }              // konvencí rozpoznáno jako primární klíč
    public string Name { get; set; }
    public List<Order> Orders { get; set; }   // navigační vlastnost (1:N)
}

public class Order {
    public int Id { get; set; }
    public DateTime CreatedAt { get; set; }
    public int CustomerId { get; set; }       // konvencí rozpoznáno jako FK (CustomerId)
    public Customer Customer { get; set; }    // navigační vlastnost zpět
}
```

### **2.2.2 Tři způsoby konfigurace**

1. **Konvence** — automaticky podle jmen (nejjednodušší, ale nejmíň flexibilní)
2. **Atributy (Data Annotations)** — atributy, kterými můžeš _upravit mapování_ nebo _definovat validační pravidla_
  
  | Atribut | Význam |
  | --- | --- |
  | `[Key]` | Označí primární klíč (pokud se nejmenuje `Id`). |
  | `[Required]` | Hodnota je povinná (`NOT NULL`). |
  | `[MaxLength(n)]` / `[StringLength(n)]` | Omezení maximální délky textu. |
  | `[Column("NazevSloupce")]` | Nastaví vlastní název sloupce v databázi. |
  | `[Table("NazevTabulky")]` | Nastaví vlastní název tabulky. |
  | `[ForeignKey("Address")]` | Určí cizí klíč pro navigační vlastnost. |
  | `[NotMapped]` | Vlastnost se nebude ukládat do databáze. |
  
3. **Fluent API** — konfigurace v metodě `OnModelCreating()` třídy `DbContext`. Umožňuje nastavit i složitější mapování, které atributy nepodporují

> [!danger]
> **Priorita:** **Konvence < Atributy < FluentAPI**.

```csharp
// Data Annotations – atributy přímo na entitě
public class Customer {
    [Key]
    public int CustomerId { get; set; }

    [Required, MaxLength(100)]
    public string Name { get; set; }
}

// Fluent API – konfigurace v OnModelCreating, mimo entitu
modelBuilder.Entity<Customer>(entity => {
    entity.HasKey(c => c.CustomerId);
    entity.Property(c => c.Name).IsRequired().HasMaxLength(100);
});
```

## 2.2 DbContext

> [!success]
> **DbContext** je _základní třída Entity Frameworku_, která představuje **relaci mezi aplikací a databází.** Zajišťuje _připojení k databázi, správu entit, sledování jejich změn_ a _provádění databázových operací_.
>
> Pro každou entitu obsahuje `DbSet<T>` (kolekci reprezentující tabulku).

- **Typická definice:**

```csharp
using Microsoft.EntityFrameworkCore;

public class UniversityContext : DbContext {
    public DbSet<Address> Addresses { get; set; }
    public DbSet<Student> Students { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options) {
        options.UseLazyLoadingProxies()
               .UseSqlite("Data Source=/cesta/k/databazi/testDb.db");
    }
}
```

- **Důležité body:**
  - Dědí z `DbContext` (z namespace `Microsoft.EntityFrameworkCore`)
  - `DbSet<T>` musí být `public`, jinak ho EF neuvidí
  - `OnConfiguring` určuje provider a connection string
  - `OnModelCreating(ModelBuilder modelBuilder)` se přepíše (protože to je override) pro Fluent API mapování

> [!danger]
> **Není thread-safe**, nepoužívat jednu instanci napříč vlákny.

## 2.3 Migrace

> [!success]
> Mechanismus pro **verzování** a _evoluci databázového schématu_ při **provedení změn v entitách**

### 2.3.1 Vytvoření první migrace

```bash
dotnet ef migrations add InitialCreate
dotnet ef database update # vytvoření databáze
```

### 2.3.2 Změna modelu

```bash
dotnet ef migrations add AddBirthDate # popis změny
dotnet ef database update # aplikace změn
```

- `migrations add` – porovná aktuální model s posledním snapshotem
- `database update` – aplikuje nevykonané migrace na databázi.

- **Migraci** lze i **vrátit**: `dotnet ef database update <NázevPředchozíMigrace>`

- Při `InitialCreate` vznikne složka `Migrations/` s C# soubory popisujícími `Up()`/`Down()` operace (pro rollback, popisuje, jak změnit verze)
- V databázi vznikne speciální tabulka `__EFMigrationsHistory`, která eviduje, které migrace už byly aplikovány.

## 2.5 Vazby mezi entitami

### 2.5.1 Vazba 1:1

- Ve vztahu 1:1 je _cizí klíč uložen pouze v jedné z entit_ (v závislé entitě).

```
public class Student {
    public int Id { get; set; }
    public StudentCard Card { get; set; }
}

public class StudentCard {
    public int Id { get; set; }
    public int StudentId { get; set; }      // cizí klíč
    public Student Student { get; set; }
}
```

- Je možné ji explicitně specifikovat přes Fluent API (`HasOne(...).WithOne(...)`).

### 2.5.2 Vazba 1:N (one-to-many)

- Nejčastější vazba (např. jeden `Customer`má mnoho `Order`).
- **Stačí přidat kolekci na rodičovskou stranu:**

```csharp
public class Customer {
    public int Id { get; set; }
    public string Name { get; set; }
    public ICollection<Order> Orders { get; set; }
}
```

- Pokud jsou vazby zřejmé (jen jedna možná), EF si poradí sám.
- Když je nejednoznačnost (např. víc referencí na stejnou entitu), je potřeba využít Fluent API:

```csharp
protected override void OnModelCreating(ModelBuilder modelBuilder) {
    modelBuilder.Entity<Order>()
        .HasOne(o => o.Customer)
        .WithMany(c => c.Orders);
}
```

### 2.5.3 Vazba M:N (many-to-many)

- Např. `Student` má víc `Subject`, `Subject` má víc `Student`
- **Od EF Core 5** stačí oboustranné kolekce → EF si _vazební tabulku vytvoří sám_:

```csharp
public class Subject {
    public int Id { get; set; }
    public string Name { get; set; }
    public virtual List<Student> Students { get; set; } = [];
}
```

- **Obě kolekce musí být** `virtual` (kvůli lazy loading proxy).
- **Když potřebuješ vlastní data ve vazební tabulce** (např. datum zápisu), musíš ji namodelovat ručně jako entitu:

```csharp
public class StudentSubject {
    public int StudentId { get; set; }
    public virtual Student Student { get; set; }
    public int SubjectId { get; set; }
    public virtual Subject Subject { get; set; }
}
```

A přes Fluent API jí dát složený klíč:

```csharp
modelBuilder.Entity<StudentSubject>()
    .HasKey(s => new { s.StudentId, s.SubjectId });

modelBuilder.Entity<StudentSubject>()
    .HasOne(ss => ss.Student)
    .WithMany(s => s.Subjects)
    .HasForeignKey(ss => ss.StudentId);

modelBuilder.Entity<StudentSubject>()
    .HasOne(ss => ss.Subject)
    .WithMany(s => s.Students)
    .HasForeignKey(ss => ss.SubjectId);
```

## 2.7 CRUD operace s EF

### 2.7.1 Vložení (Create)

```csharp
using (var ctx = new UniversityContext()) {
    var address = new Address { Street = "17. Listopadu", Number = 14 };
    var student = new Student { Address = address, Name = "Karel Vomáčka" };
    ctx.Students.Add(student);
    ctx.SaveChanges();      // teprve teď se vykoná INSERT
}
```

> [!danger]
> **Klíčové:** `Add` jen označí entitu jako „k vložení". **Skutečný zápis se děje až při** `SaveChanges()`.

- **Kaskádně se uloží i navigované entity** (zde `Address`, ač ji `Add` přímo nezavolal).

### 2.7.2 Čtení (Read)

```csharp
foreach (var st in ctx.Students.Where(p => p.Address.Street == "17. listopadu")) {
    Console.WriteLine($"{st.Name}, {st.Id}");
}
```

- LINQ se přeloží do SQL a vykoná se na DB — **NE v paměti**.

### 2.7.3 Editace (Update)

```csharp
var s = ctx.Students.FirstOrDefault(p => p.Id == 1);
if (s != null) {
    s.Name = "Dave Lister";        // jen změníš property
    ctx.SaveChanges();             // EF detekuje změnu a vygeneruje UPDATE
}
```

> [!danger]
> **Pozor:** Pracovat musíš s entitou načtenou z `ctx`, ne s „odpojeným" objektem (jinak EF o změnách neví).

### 2.7.4 Mazání (Delete)

```csharp
var s = ctx.Students.FirstOrDefault(p => p.Id == 1);
ctx.Students.Remove(s);
ctx.SaveChanges();
```

- **Cascade delete:** chování závisí na konfiguraci vazeb.
  - Default je obvykle „cascade" pro povinné vazby a „restrict" pro volitelné.

## 2.8 Lazy / Eager / Explicit Loading

Tři strategie, jak načítat související entity (např. `Student.Address`):

| Strategie | Kdy se data načtou |
| --- | --- |
| **Lazy loading** | Při **prvním přístupu** k navigation property |
| **Eager loading** | **Hned** spolu s hlavní entitou |
| **Explicit loading** | **Ručně**, na vyžádání |

- **Eager loading příklad:**

```csharp
var students = ctx.Students
    .Include(s => s.Address)
    .Include(s => s.Subjects).ThenInclude(ss => ss.Subject)
    .ToList();
```