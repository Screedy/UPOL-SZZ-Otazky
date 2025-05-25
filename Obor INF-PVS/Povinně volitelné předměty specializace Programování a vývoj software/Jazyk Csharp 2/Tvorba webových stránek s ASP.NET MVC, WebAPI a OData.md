## Architektura webových aplikací
- Moderní webové aplikace běží na principu **klient-server** architektury.  
- Na straně serveru (backend) běží logika aplikace, databáze a obsluha požadavků.  
- Na straně klienta (frontend) se zobrazuje UI – HTML, CSS, JavaScript.
- Typy aplikací:
	- **Statické stránky** – čisté HTML, žádná serverová logika
	- **Dynamické stránky** – generované serverem při každém požadavku
	- **AJAX** – částečné načítání dat bez reloadu stránky
	- **SPA (Single Page Application)** – webová stránka jako 1 dokument, aktualizace probíhají propsáním do onoho dokumentu pomocí API

## ASP.NET
- Rozšíření platformy .NET pro tvorbu webových aplikací.

#### Co ASP.NET přináší:
- Zpracování HTTP požadavků (routování, session)
- Možnost využít C# pro celý backend
- Šablonovací jazyk **Razor** (frontend)
- MVC strukturu a REST API
- Zabezpečení (autentizace, HTTPS, cookies)

## MVC – Model View Controller
- Striktní oddělení logiky aplikace do tří vrstev:
#### Model
- Obsahuje datové třídy (např. `Student`, `Product`)
- Implementuje logiku pro práci s daty (často Entity Framework)
#### View
- UI komponenty = HTML šablony doplněné o C# logiku (Razor)
- Zodpovědné za zobrazení dat uživateli
#### Controller
- Zajišťuje interakci mezi uživatelem a systémem
- Odpovídá na HTTP požadavky, zpracuje je a vrací View nebo JSON

## ASP.NET MVC – průběh zpracování požadavku
1. Prohlížeč odešle HTTP požadavek
2. **Router** určí správný Controller a akci (`/Home/Index`)
3. Controller provede potřebnou logiku
4. Vrátí View (HTML stránku) nebo např. `Redirect`, `Json`
5. Odpověď je odeslána zpět klientovi

## Vytvoření projektu
- Typ: ASP.NET Core Web App (Model-View-Controller)  
- Struktura složek:
	- `Controllers/` – logika aplikace
	- `Models/` – datové modely
	- `Views/` – šablony (Razor)
	- `wwwroot/` – statický obsah (CSS, JS, obrázky)

## Razor – šablonovací jazyk
- Kombinuje C# a HTML pro vytváření dynamického obsahu.
#### Základní syntaxe:
```cshtml
@model Student
<p>@Model.Name</p>
```

#### Podmínky a cykly:
```cshtml
@if (Model.Age > 18) {
    <p>Dospělý</p>
}

@foreach (var s in Model.Students) {
    <li>@s.Name</li>
}
```

#### Helpery (např. `asp-route`):
```html
<a asp-action="Edit" asp-route-id="@s.Id">Editovat</a>
```

## Controllers – zpracování požadavků

```csharp
public class StudentController : Controller {
    public IActionResult All() {
        var students = db.Students.ToList();
        return View(students);
    }

    [HttpGet]
    public IActionResult Edit(int id) {
        var s = db.Students.FirstOrDefault(x => x.Id == id);
        return View(s);
    }

    [HttpPost]
    public IActionResult Edit(Student s) {
        var original = db.Students.FirstOrDefault(x => x.Id == s.Id);
        original.Name = s.Name;
        db.SaveChanges();
        return RedirectToAction("All");
    }
}
```

## Dynamické šablony – Razor runtime compilation
- Nutno doinstalovat:
```bash
Microsoft.AspNetCore.Mvc.Razor.RuntimeCompilation
```
- V konfiguraci:
```csharp
builder.Services.AddControllersWithViews().AddRazorRuntimeCompilation();
```
- Díky tomu se změny ve Views projeví okamžitě bez restartu.

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
