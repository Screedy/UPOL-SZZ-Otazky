# 1. ASP.NET Core

> [!success]
> **ASP.NET Core** je _multiplatformní framework platformy .NET_ určený pro **vývoj webových aplikací, webových API** a _dalších webových služeb_.

- Umožňuje _využívat jazyk C#_ a _standardní knihovny .NET_ pro tvorbu **BE části aplikace**.
- **Další důležité vlastnosti** _frameworku jsou_:
  - Obsahuje _vestavěný webový server_ **Kestrel**
  - Obsahuje _middleware pipeline_ pro **zpracování HTTP** **požadavků**
  - _Umožňuje tvorbu FE_ pomocí **šablonovacího systému Razor** (FE)
  - Umožňuje vývoj _jednostránkových aplikací_ (SPA) pomocí **Blazoru** (umožňuje psát i frontend v C#)
  - _Podpora architektury_ **MVC architektury**
  - Umožňuje tvorba **REST API**
  - **Nabízí zabezpečení** aplikací (HTTPS, autentizace, autorizace)
  - Podporuje _dependency injection_
  - Lze jej hostovat na _různých operačních systémech_ i _cloudových platformách_

- **Rozdíl ASP.NET Framework vs. ASP.NET Core:**
  - Klasický ASP.NET _běží pouze na Windows_
  - ASP.NET Core je multiplatformní, výkonější.

## 1.1 Vytvoření nové aplikace

```bash
dotnet new mvc # Vytvoření nového projektu 
dotnet new mvc --no-https # Bez https
dotnet run # Spuštění aplikace
```

> [!info]
> Po spuštění _začne vestavěný webový server_ **naslouchat na zvoleném portu** (např. `http://localhost:5000`)
>
> Na to se používá **nejčastěji** **(při vývoji)** **soubor** `launchSettings.json`, nebo (při produkci) `Program.cs`, pomocí parametrů spuštění nebo proměnných prostředí.

---

# 2. Přístupy k tvorbě webové aplikace

- ASP.NET Core nabízí _několik programovacích modelů postavených na stejném základu_. Všechny využívají _společné mechanismy_, jako je **middleware**, **dependency injection**, **routování** nebo **konfigurační systém**, liší se však **_způsobem tvorby uživatelského rozhraní_** a **_architekturou aplikace_**.

| Model | Použití | Charakteristika |
| --- | --- | --- |
| **MVC** | Dynamické webové aplikace | HTML stránky jsou generovány na serveru pomocí Razor Views. |
| **Razor Pages** | Menší webové aplikace | Logika je svázána s jednotlivými stránkami, není potřeba samostatný controller. |
| **Web API** | REST služby | Aplikace vrací data (nejčastěji JSON), nikoli HTML stránky. |
| **Minimal API** | Jednoduchá API | Endpointy jsou definovány přímo v souboru `Program.cs`. |
| **Blazor** | Moderní interaktivní aplikace | Uživatelské rozhraní je vytvářeno v jazyce C# pomocí komponent. |

## 2.1 MVC

> [!success]
> **MVC** je _architektonický vzor_, který odděluje _aplikaci do tří vrstev_ s jasně definovanými odpovědnostmi: **Model** (data + datová logika), **View** (zobrazení) a **Controller** (řídící logika, propojení modelu a view).

- **Vhodnost:** ideální pro klasické **dynamické weby** generované na serveru.

### 2.1.1 Model

> [!success]
> Model představuje **datovou vrstvu aplikace**. Popisuje _strukturu dat, jejich vzájemné vztahy a pravidla_, která se k nim vztahují. V ASP.NET Core bývá _model často tvořen_ **entitami Entity Framework Core**, které jsou _mapovány na databázové tabulky_. (Využívání ORM)

- **DTO (Data Transfer Object)**
  - Určený pro přenos dat mezi jednotlivými vrstvami aplikace
  - Neobsahuje navigační vlastnosti ani citlivé údaje (například hash hesla)

#### 2.1.1.1 Konvence

- Modely se standardně umisťují do složky `Models`.
- Název třídy obvykle reprezentuje jednu entitu (např. `Student`, `Product`, `Order`)

```csharp
// Model (entita)
public class Student {
    public int Id { get; set; }
    public string Name { get; set; }
    public string PasswordHash { get; set; }
}

// DTO pro view nebo API
public class StudentDto {
    public int Id { get; set; }
    public string Name { get; set; }
}
```

### 2.1.2 View

> [!success]
> View představuje **prezentační vrstvu aplikace**. Jeho úkolem je _zobrazit data uživateli_.  
> V ASP.NET Core jsou View tvořeny _pomocí šablonovacího systému_ **Razor**, který umožňuje **kombinovat HTML, CSS a C#**.

- View by nemělo obsahovat logiku aplikace. Mělo by pouze zobrazovat data připravená controllerem.

#### 2.1.2.1 Konvence

- View se ukládají do složky `Views`.
- Každý controller má vlastní podsložku se stejným názvem (bez přípony **Controller**).
- Název View obvykle odpovídá názvu akce controlleru.

```
Views/
 ├── Home/
 │    ├── Index.cshtml
 │    └── Detail.cshtml
 └── Student/
      ├── Index.cshtml
      └── Detail.cshtml
```

> [!info]
> Akce `Detail()` ve třídě `StudentController` tedy standardně vrací pohled `Views/Student/Detail.cshtml`

### 2.1.3 Controller

> [!success]
> Controller představuje **řídicí vrstvu aplikace**.
>
> Přijímá _HTTP požadavky, komunikuje s modelem, provádí potřebnou aplikační logiku a vrací odpověď klientovi._

- Jednotlivé **veřejné metody** _controlleru_ se nazývají **Akce** (Actions) a představují _jednotlivé_ **endpointy** _aplikace_.
- Akce _nejčastěji vrací objekt typu_ `IActionResult`, který může představovat například:
  - **HTML stránku** (`View()`),
  - **JSON odpověď** (`Json()` nebo `Ok()`),
  - **přesměrování** (`Redirect()`),
  - **HTTP stavový kód** (`NotFound()`, `BadRequest()` apod.).
- Pro mapování HTTP metod se používají atributy:
  - `[HttpGet]` (výchozí)
  - `[HttpPost]`
  - `[HttpPut]`
  - `[HttpDelete]`

#### 2.1.3.1 Konvence

- Controllery se ukládají do složky `Controllers`.
- Název controlleru končí příponou `Controller` (např. `StudentController` nebo `HomeController`).
- Veřejné metody controlleru představují jednotlivé **Actions**.
- Názvy controllerů a jejich akcí slouží při konvenčním routování k automatickému mapování URL na odpovídající metody aplikace.

```csharp
public class StudentsController : Controller {
    public IActionResult Detail(int id) {
        if (id > 10) return NotFound();
        var student = new { Name = "Jan", Id = id };
        return Json(student);
    }

    [HttpPost]
    public IActionResult Create(Student s) {
        // model binding automaticky naplní 's' z formuláře
        return RedirectToAction("Detail", new { id = s.Id });
    }
}
```

---

# 3. Razor

> [!success]
> **Razor** je **šablonovací jazyk** používaný v _ASP.NET Core_. Umožňuje **kombinovat statické HTML** se **syntaxí jazyka C#**, přičemž výsledkem je _HTML stránka odeslaná klientovi_.

- **Klíčový znak** `@` — _značí přechod z HTML do C#_.

> [!info]
> Razor podporuje _většinu konstrukcí jazyka C#_, například _podmínky, cykly nebo práci s objekty_.

```cshtml
@model List<Product>
<ul>
@foreach (var p in Model)
{
    <li>@p.Name – @p.Price Kč</li>
}
</ul>
```

```cshtml
@if (number > 15) {
    <div>Je to větší</div>
} else if (number < 10) {
    <div>Je to menší</div>
}

@switch (mark) {
    case 1: <p>Jednička!</p> break;
    case 5: <p>Za pět!</p> break;
    default: <p>Normál...</p> break;
}
```

## 3.1 Předávání dat do View

- Data lze z controlleru do View předávat několika způsoby.

### **3.1.1 Silně typovaný model (**`@model`)

- Jedná se o doporučený způsob.
- Typ modelu je znám již při kompilaci, což umožňuje kontrolu typů i podporu IntelliSense.

```cshtml
// Controller
public IActionResult Detail() {
    var student = new Student { Id = 1, Name = "Jan Novák" };
    return View(student);
}

// View
@model Student

<h2>@Model.Name</h2>
<p>ID: @Model.Id</p>
```

### **3.1.2 Slabě typovaný (**`ViewData` **a** `ViewBag`**)**

- `ViewData["key"]` — _slovník typu_ `string → object`. Hodnoty je při použití **potřeba přetypovat** na správný datový typ.
- `ViewBag.key` — dynamický obal nad `ViewData`. Umožňuje _jednodušší zápis pomocí vlastností_ (přístup přes tečku), ale **neposkytuje kontrolu typů** při kompilaci.
- Oba sdílí stejné úložiště, ale liší se přístupem.

```csharp
// Controller
public IActionResult Detail()
{
    ViewData["Student"] = new Student { Id = 2, Name = "Josef Novák" };
    ViewBag.Student = new Student { Id = 3, Name = "Karel Novák" };
    return View();
}

//View
@{ var student = ViewData["Student"] as Student; }
<h2>@student?.Name</h2>

<h2>@ViewBag.Student.Name</h2>
```

> [!danger]
> **View může mít pouze jeden objekt** `@model`. Pokud je potřeba předat _více různých datových objektů_, vytváří se **obvykle vlastní ViewModel**, který sdružuje všechny _potřebné informace do jedné třídy_.
>
> `ViewData` a `ViewBag` se používají spíše pro _předávání doplňujících údajů_.

## 3.2 Tag Helpers

> [!success]
> **Tag Helpers** rozšiřují _standardní HTML elementy_ o atributy začínající `asp-`. Tyto atributy ASP.NET Core při generování stránky _automaticky převede na odpovídající HTML_.
>
> Používají se například pro **generování odkazů**, **formulářů** nebo **validaci vstupních dat**.

```csharp
<a asp-controller="Students" asp-action="Detail" asp-route-id="3" class="nav-link">
  Detail studenta
</a>
```

## 3.3 Automatická rekompilace views

- V ASP.NET Core je _nutné doinstalovat balíček_ na **rekompilace views bez restartu aplikace** a registrovat:

```csharp
// Program.cs
builder.Services
    .AddControllersWithViews()
    .AddRazorRuntimeCompilation();   // balíček Microsoft.AspNetCore.Mvc.Razor.RuntimeCompilation
```

---

# 4. Zpracování HTTP požadavku

> [!info]
> _Každý požadavek odeslaný klientem_ (například webovým prohlížečem) prochází v ASP.NET Core několika navazujícími kroky, než je _vytvořena a odeslána odpověď_. Celý proces zajišťuje webový server **Kestrel** společně s **Request Pipeline**.

1. Klient _odešle HTTP požadavek na server_.
2. Požadavek **přijme** webový server **Kestrel**.
3. Požadavek prochází **Request Pipeline**, která obsahuje jednotlivé middleware komponenty.
4. **Routing** **určí endpoint**, který bude požadavek zpracovávat.
5. V případě MVC je _vytvořena instance příslušného controlleru_.
6. Zavolá se _odpovídající_ **Action** _controlleru_.
7. Controller komunikuje s modelem, případně s databází nebo službami.
8. Controller _vrátí objekt typu_ **IActionResult** (například View, JSON nebo přesměrování).
9. ASP.NET Core _vytvoří HTTP odpověď_.
10. _Kestrel odešle odpověď_ klientovi.

---

# 5. Middleware

> [!success]
> **Middleware** je **komponenta** zařazená do **Request Pipeline**, která zpracovává příchozí HTTP požadavky a odchozí HTTP odpovědi.

- Každý middleware může:
  - **zpracovat** _příchozí požadavek_,
  - **upravit** _požadavek_,
  - **předat řízení** další _middleware_ komponentě,
  - po návratu **upravit** _odpověď_,
  - nebo **zpracování** požadavku **ukončit**.
- Jednotlivé middleware jsou **registrovány** v souboru `Program.cs` a jsou _vykonávány v pořadí_, _ve kterém byly zaregistrovány_ (např. `UseAuthentication` musí být před `UseAuthorization`).

```
app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();
app.MapControllers();
app.Run();
```

- Mezi _nejpoužívanější middleware komponenty_ patří:
  - **HTTPS Redirection** – přesměrování HTTP na HTTPS.
  - **Static Files** – zpřístupnění statických souborů (CSS, JavaScript, obrázky).
  - **Routing** – výběr správného endpointu.
  - **Authentication** – ověření identity uživatele.
  - **Authorization** – kontrola oprávnění uživatele.
  - **Exception Handling** – zpracování výjimek.
  - **CORS** – řízení přístupu z jiných domén.
  - **Response Compression** – komprese HTTP odpovědí.

## 5.1 Vlastní middleware

```csharp
app.Use(async (context, next) => {
    await context.Response.WriteAsync("První middleware – příchod\n");
    await next();                         // předáme dalšímu
    await context.Response.WriteAsync("První middleware – odchod\n");
});

app.Use(async (context, next) => {
    await context.Response.WriteAsync("Druhý middleware – příchod\n");
    await next();                         // předáme dalšímu
    await context.Response.WriteAsync("Druhý middleware – odchod\n");
});

app.Run(async (context) => {              // Run = terminální middleware (už nevolá next)
    await context.Response.WriteAsync("Poslední!\n");
});
```

- **Rozdíl** `Use` **vs.** `Run`**:**
  - `Use` umožňuje pokračovat dál (`next()`),
  - `Run` je koncový middleware — ukončuje Request Pipeline.

---

# 6. Routování

> [!success]
> **Routování** je _mechanismus_, který určuje, _který endpoint_ aplikace **obslouží** daný HTTP požadavek.

- **Endpoint** = kus kódu, který umí obsloužit požadavek (typicky akce controlleru, ale i Minimal API delegát).

> [!info]
> **Registrace:** `app.UseRouting()` + `app.MapControllerRoute(...)`.

- **Kritéria výběru endpointu:**
  - Pattern matching na URL.
  - HTTP metoda (GET, POST, ...).
  - Případná omezení parametrů (např. `{id:int}`).

## 6.1 Konvenční routy

- **Konvenční routování (Conventional Routing)** využívá **předem definovaný vzor URL** (route template), který se _registruje při konfiguraci aplikace_. Na základě tohoto vzoru ASP.NET Core **automaticky mapuje** _části URL na názvy controllerů, akcí a parametrů_ podle stanovených konvencí.

```csharp
// Registrace vzoru URL
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");
// Např. požadavek: /Student/Detail/5
```

- `=Home`, `=Index` — výchozí hodnoty.
- `?` — volitelný parametr.

## 6.2 Atributové routy

- **Atributové routování (Attribute Routing)** definuje pravidla směrování přímo **pomocí atributů** _umístěných u controllerů a jejich akcí_. Každý endpoint tak může mít vlastní URL nezávislou na konvenčním vzoru, což poskytuje větší flexibilitu při návrhu aplikace.

```csharp
[Route("api/[controller]")]
public class StudentsController : ControllerBase {
    [HttpGet("{id:int}")]            
    public IActionResult Get(int id) => Ok();
}
// Výsledný požadavek: // GET /api/students/5
```

## 6.3 Minimal API (mimo MVC)

- V **Minimal API** se routování nedefinuje pomocí controllerů ani atributů, ale **přímo při registraci endpointů v souboru** `Program.cs`. Každý endpoint je _vytvořen metodami_ `MapGet()`, `MapPost()`, `MapPut()`, `MapDelete()` nebo `MapPatch()`, které určují URL i HTTP metodu.

```csharp
app.MapGet("/secretPlace/{id:int}", async context => {
    await context.Response.WriteAsync(
        $"Good morning, agent #{context.Request.RouteValues["id"]}!");
});
```

---

# 7. Web API (REST)

> [!success]
> **Web API (Application Programming Interface)** umožňuje _komunikaci mezi aplikacemi prostřednictvím protokolu HTTP_. Na rozdíl od klasického MVC nevrací HTML stránky, ale data, nejčastěji ve formátu **JSON**.

- V ASP.NET Core lze Web API vytvářet pomocí **API Controllerů** nebo **Minimal API**.
- API Controller dědí z třídy `ControllerBase` a využívá atributy jako `[ApiController]`, `[Route]`, `[HttpGet]` nebo `[HttpPost]`.

- **Hlavní rozdíly oproti MVC:**
  - `[ApiController]` → **automatické mapování dat z HTTP požadavku** (_Model Binding_), **automatická validace vstupních dat** – pokud model není validní, odpověď **400 Bad Request**,
  - Akce vrací `ActionResult<T>` — kombinace typu a status kódu.
  - **Bez** Razor views.

```csharp
[ApiController]
[Route("api/[controller]")]
public class StudentsController : ControllerBase {
    [HttpGet("{id}")]
    public ActionResult<Student> Get(int id) {
        var s = _repo.Find(id);
        return s is null ? NotFound() : Ok(s);
    }

    [HttpPost]
    public ActionResult<Student> Create(Student s) {
        _repo.Add(s);
        return CreatedAtAction(nameof(Get), new { id = s.Id }, s);
    }
}
```

---

# 8. Dependency Injection (DI)

> [!success]
> **Dependency Injection (DI)** je návrhový princip, při kterém _objekt nevytváří své závislosti sám_, ale jsou mu **předány zvenčí**.

- Služby se registrují v souboru `Program.cs`.
- Nejčastěji jsou služby předávány pomocí **constructor injection**.

- **Tři lifetime možnosti:**
  - `AddSingleton<T>` — jedna instance pro celou aplikaci.
  - `AddScoped<T>` — jedna instance na každá HTTP požadavek (typické pro `DbContext`).
  - `AddTransient<T>` — nová instance při každém požadavku o službu.

```csharp
// Registrace
builder.Services.AddScoped<IStudentRepository, StudentRepository>();
builder.Services.AddDbContext<AppDbContext>(o => o.UseSqlServer(connStr));

// Použití v controlleru
public class StudentsController : Controller {
    private readonly IStudentRepository _repo;
    public StudentsController(IStudentRepository repo) => _repo = repo;
}
```

---

# 9. Konfigurace

> [!success]
> Konfigurace umožňuje **oddělit nastavení aplikace** _od zdrojového kódu_. Nejčastěji je uložena v souboru `appsettings.json`, případně v souborech _pro jednotlivá prostředí_ (např. `appsettings.Development.json`).

- ASP.NET Core _podporuje více prostředí_, například:
  
  - Development,
  - Staging,
  - Production.
  
  Každé prostředí může mít _vlastní konfiguraci_.

---

# 10. ASP.NET Core Identity

> [!success]
> **ASP.NET Core Identity** je framework určený pro správu uživatelů, autentizaci a autorizaci.

- Poskytuje funkcionality jako:
  - registrace uživatelů,
  - přihlášení a odhlášení,
  - správa hesel,
  - správa rolí,
  - dvoufaktorová autentizace.
- **Klíčové třídy:**
  - `UserManager<TUser>` — operace nad uživatelem (vytvoření, hesla, role).
  - `SignInManager<TUser>` — přihlášení / odhlášení.
  - `IdentityUser` — výchozí entita uživatele (lze rozšířit).
- **Autorizace v kódu:**

```csharp
[Authorize]                             // jen přihlášený uživatel
public IActionResult Profile() => View();

[Authorize(Roles = "Admin")]            // jen role Admin
public IActionResult AdminPanel() => View();

[AllowAnonymous]                        // výjimka — všichni
public IActionResult Login() => View();
```

> [!warning]
> Je důležité rozlišovat:
>
> - **Autentizaci** – ověření identity uživatele.
> - **Autorizaci** – ověření oprávnění uživatele.