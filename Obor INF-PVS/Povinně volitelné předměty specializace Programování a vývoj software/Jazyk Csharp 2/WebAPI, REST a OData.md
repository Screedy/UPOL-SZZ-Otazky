## REST API
- REST (Representational State Transfer) je styl webového rozhraní, který umožňuje **přímou práci s daty přes HTTP**.  
	- Typické HTTP metody:
	- `GET` – načtení dat
	- `POST` – vytvoření nového záznamu
	- `PUT` – úprava existujícího záznamu
	- `DELETE` – odstranění dat
- Backend často pouze vrací data ve formátu JSON a frontend (např. web nebo mobilní appka) se stará o zobrazení.

## ASP.NET Web API
- Projekt typu ASP.NET Core Web API se velmi podobá MVC aplikaci – pouze chybí Views.
### Základní konfigurace:
```csharp
[ApiController]
[Route("[controller]/[action]")]
public class StudentController : ControllerBase {
    ...
}
```

- `ControllerBase` je odlehčená varianta bez podpory Views.
- Odpovědi se vrací jako JSON (automatická serializace).

## DTO – Data Transfer Object
- Při návrhu API neposíláme přímo databázové entity (např. `Student`), ale jejich zjednodušenou kopii.
- Důvody:
	- Skrýváme interní detaily
	- Zajistíme validaci nebo transformaci dat
	- Umožníme flexibilnější změny databáze bez změny API
```csharp
public class StudentDto {
    public string Name { get; set; }
    public string Surname { get; set; }
}
```

## Ukázkové endpointy
```csharp
[HttpGet]
public IEnumerable<Student> Get() => ctx.Students.ToList();

[HttpGet("{name}")]
public IEnumerable<Student> GetByName(string nameContains) =>
    ctx.Students.Where(p => p.Name.Contains(nameContains));

[HttpGet("{id}")]
public Student Get(int id) => ctx.Students.Find(id);

[HttpPut("{id}")]
public void Put(int id, string name, string surname) {
    var s = ctx.Students.Find(id);
    if (s != null) {
        s.Name = name;
        s.Surname = surname;
        ctx.SaveChanges();
    }
}

[HttpDelete("{id}")]
public void Delete(int id) {
    var s = ctx.Students.Find(id);
    if (s != null) {
        ctx.Students.Remove(s);
        ctx.SaveChanges();
    }
}
```

## Swagger (OpenAPI)
- Swagger automaticky generuje **dokumentaci a testovací rozhraní** pro naše API.
- Po spuštění dostupné např. na `https://localhost:5001/swagger`
- Vygeneruje seznam endpointů s popisem parametrů
- Lze rovnou testovat API přes webové UI

## OData
- OData (Open Data Protocol) rozšiřuje API o pokročilé možnosti dotazování:
	- `?$filter=...`
	- `?$select=...`
	- `?$orderby=...`
	- `?$top=...`, `?$skip=...`
	- `?$expand=...` (načtení navázaných entit)

#### Konfigurace
```csharp
builder.Services.AddControllers().AddOData(opt =>
    opt.AddRouteComponents("api", GetEdmModel())
        .Select().Filter().OrderBy().Count().Expand());
```

```csharp
[EnableQuery]
public IQueryable<Student> Get() => ctx.Students;
```

#### Dotazy přes OData
- Příklady požadavků:
	- `/api/Student?$filter=Name eq 'Lukáš'`
	- `/api/Student?$select=Name&$top=3`
	- `/api/Student(2)` – student s ID 2
- Tyto dotazy lze rovnou zapsat do URL a zpracují se automaticky bez ručního filtrování v kontroleru.

## Napojení z jiné aplikace (např. konzolové)
- Přes nástroj **OData Connected Service** (rozšíření pro Visual Studio)
- Automaticky vygeneruje třídy a připojení
- Dotazy se tvoří v LINQ, ale překládají se do OData
```csharp
Container c = new Container(new Uri("http://localhost:54828/"));
var students = c.Student.Where(p => p.Name == "Ivo");
foreach (var s in students) {
    Console.WriteLine(s.Surname);
}
```

---
## Shrnutí
- Web API v ASP.NET Core slouží k tvorbě REST rozhraní pro práci s daty.
- Vhodné pro propojení s frontendy (např. JS, mobilní aplikace).
- DTO třídy pomáhají oddělit logiku databáze od veřejného rozhraní.
- Swagger umožňuje testování a dokumentaci.
- OData výrazně zjednodušuje složité dotazy přes URL.
