## Architektura webových aplikací
- Moderní webové aplikace běží na principu **klient-server** architektury.  
- Na straně serveru (backend) běží logika aplikace, databáze a obsluha požadavků.  
- Na straně klienta (frontend) se zobrazuje UI – HTML, CSS, JavaScript.
- Typy aplikací:
	- **Statické stránky** – čisté HTML, žádná serverová logika
	- **Dynamické stránky** – generované serverem při každém požadavku
	- **AJAX** – částečné načítání dat bez reloadu stránky
	- **SPA (Single Page Application)** – kompletní logika na klientovi

## ASP.NET
- Rozšíření platformy .NET pro tvorbu webových aplikací.

#### Co ASP.NET přináší:
- Zpracování HTTP požadavků (routování, session)
- Možnost využít C# pro celý backend
- Šablonovací jazyk **Razor**
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
	- `Views/` – šablony (razor)
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

#### Helpery (např. asp-route):
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

---
## Shrnutí
- ASP.NET umožňuje psát výkonné a typově bezpečné webové aplikace v C#.
- MVC architektura zajišťuje čisté oddělení zodpovědnosti.
- Razor je jednoduchý, ale výkonný nástroj pro tvorbu šablon.
- Entity Framework může být přirozeně použit jako datová vrstva.
- ASP.NET MVC je vhodný pro aplikace s kompletním serverovým řízením – např. administrace, katalogy, formuláře, reporty.

