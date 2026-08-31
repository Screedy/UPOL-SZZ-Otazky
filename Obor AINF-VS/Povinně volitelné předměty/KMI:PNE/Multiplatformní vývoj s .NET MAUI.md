> [!success]
> **.NET MAUI (Multi-platform App UI)** je _open-source multiplatformní framework_ společnosti Microsoft určený pro vývoj **nativních desktopových i mobilních aplikací**.
>
> Umožňuje vytvářet aplikace pro Android, iOS, macOS a Windows z **jednoho sdíleného zdrojového kódu** v jazyce **C#** a pomocí uživatelského rozhraní definovaného v **XAML** (případně přímo v C#).

- Framework je součástí platformy .NET od verze **.NET 6** a představuje přímého nástupce technologie **Xamarin**.

# 1. Hlavní motivace vzniku

- Vývoj .NET MAUI reagoval na několik omezení předchozí platformy Xamarin:
  1. **Sjednocení .NET runtime** – Xamarin.Android, Xamarin.iOS a Xamarin.Forms _používaly historicky oddělené implementace základních knihoven_. MAUI běží nad jednotným .NET runtime a **sdílí stejné Base Class Libraries** jako například _ASP.NET Core nebo konzolové aplikace_.
  2. **Single Project** – Xamarin vyžadoval _samostatné projekty pro jednotlivé platformy_ (Android, iOS a sdílený projekt). MAUI **používá jediný projekt** (`.csproj`), který obsahuje veškerý sdílený kód i prostředky aplikace.
  3. **Vyšší výkon** – vykreslování uživatelského rozhraní bylo _přepracováno z architektury Renderer_ na modernější systém **Handlers**, který má nižší režii a využívá přímo nativní ovládací prvky.
  4. **Jednotný vývojový ekosystém** – aplikace _využívají stejné nástroje_ (`dotnet build`, `dotnet publish`, NuGet, Dependency Injection apod.) _jako ostatní projekty platformy .NET_.

## 1.1 Single Project

- Platformně specifický kód se řeší složkou `Platforms/` (`Platforms/Android/`, `Platforms/iOS/`...) s automatickým zahrnutím jen pro danou platformu.
- Při sestavení aplikace systém MSBuild automaticky připraví potřebné prostředky v odpovídajících formátech a rozlišeních pro každou cílovou platformu. (dřív ruční práce na Xamarinu).

---

# 2. Architektura

- **Architektura MAUI** je navržena tak, aby poskytovala **abstraktní vrstvu** nad **nativními API** jednotlivých operačních systémů, ale zároveň umožňovala _přímý přístup k hardwaru_.

## 2.1 Handlers

> [!info]
> Nejdůležitějším architektonickým prvkem je přechod od **Rendererů** (Xamarin) k **Handlerům** (MAUI).

> [!success]
> Každý _multiplatformní ovládací prve_k v .NET MAUI je **_reprezentován abstraktním rozhraním_** (například `IButton`). Pro každou _podporovanou platformu existuje odpovídajíc_í **Handler**, který tento **abstraktní prvek mapuje na skutečný nativní ovládací prvek** operačního systému.

> [!info]
> Například tlačítko je na Androidu reprezentováno třídou `AppCompatButton`, na iOS třídou `UIButton` a ve Windows ovládacím prvkem `Button` z frameworku WinUI.

![[019fb9df-4323-77ff-9ea6-ca7fe81550da.png]]

- Vlastnosti jednotlivých ovládacích prvků jsou mapovány pomocí tzv. **Property Mapperů**, které umožňují _měnit chování nebo vzhled nativních komponent_ **bez nutnosti vytvářet vlastní odvozené třídy**.

## 2.2 Kompilace a Runtime

- Přestože vývojář vytváří jednu společnou aplikaci, její spuštění se na jednotlivých platformách liší.
  - Na **Androidu** běží aplikace prostřednictvím **.NET for Android**, kde se _využívá prostředí Mono Runtime společně s Android Runtime_ (ART). Kód je standardně překládán metodou **JIT (Just-In-Time)**, případně lze využít **Ahead-Of-Time (AOT)** kompilaci _pro rychlejší spuštění aplikace_.
  - Na **iOS** a **macOS** využívá .NET MAUI platformu **.NET for iOS (resp. .NET for Mac Catalyst)**, která je rovněž _založena na Mono runtime_. Kvůli omezením operačního systému Apple však **není možné používat JIT kompilaci**, a proto jsou aplikace kompletně překládány pomocí **Ahead-Of-Time (AOT)** _kompilace do nativního strojového kódu_.
  - Na **Windows** využívá .NET MAUI framework **WinUI 3**, který _představuje moderní nativní framework pro tvorbu desktopových aplikací_ nad Windows App SDK.

## 2.3 Dependency Injection (DI) a životní cyklus

> [!success]
> Další významnou změnou oproti Xamarin je využití standardního **Dependency Injection (DI)** kontejneru platformy .NET
>
> **Dependency Injection slouží k automatickému poskytování potřebných objektů (závislostí) jednotlivým částem aplikace, aniž by je musely samy vytvářet.**

- Zatímco Xamarin.Forms používal službu `DependencyService`, .NET MAUI využívá stejný mechanismus jako například ASP.NET Core.
- Celá aplikace se konfiguruje v souboru `MauiProgram.cs` pomocí třídy `MauiAppBuilder`.
  - Zde se registrují služby (Services), ViewModely a fonty.
  - Využívá se vestavěný kontejner pro vkládání závislostí, což výrazně zlepšuje modularitu a testovatelnost kódu.

---

# 3. UI Systém a moderní navigace (MAUI Shell)

- _Uživatelské rozhraní aplikací_ v .NET MAUI je nejčastěji vytvářeno pomocí jazyka **XAML (Extensible Application Markup Language)**, který slouží k _deklarativnímu popisu jednotlivých ovládacích prvků_, jejich _vlastností a vzájemného rozložení_.
- _Logika_ jednotlivých stránek je následně _implementována v jazyce C#_ (tzv. _code-behind_) nebo pomocí _architektury_ **MVVM**.
- Základními soubory uživatelského rozhraní jsou například `App.xaml`, `AppShell.xaml` a `MainPage.xaml`, které jsou _součástí každého projektu .NET MAUI_.

- _Rozvržení uživatelského rozhraní_ je vytvářeno **pomocí kontejnerů** (_Layouts_), které _určují rozmístění jednotlivých ovládacích prvků na obrazovce_. Mezi nejčastěji používané patří:
  - **Grid** – umožňuje rozdělit stránku do řádků a sloupců a je vhodný pro složitější rozvržení.
  - **VerticalStackLayout** a **HorizontalStackLayout** – slouží pro jednoduché řazení prvků pod sebe nebo vedle sebe.
  - **FlexLayout** – poskytuje flexibilní rozvržení podobné CSS Flexboxu a je vhodný pro responzivní návrh uživatelského rozhraní.

> [!info]
> Protože .NET MAUI podporuje mobilní telefony, tablety i desktopové počítače, umožňuje vytvářet **adaptivní uživatelské rozhraní**, které se přizpůsobuje velikosti obrazovky i konkrétní platformě.
>
> Využití prvků `OnPlatform` a `OnIdiom`

## 3.1 MAUI Shell

- **MAUI Shell** představuje moderní navigační framework, který slouží k definici navigace mezi jednotlivými stránkami aplikace. Je konfigurován v souboru **AppShell.xaml**, kde lze přehledně definovat nabídky, záložky, navigační hierarchii i jednotlivé routy, aniž by bylo nutné většinu navigační logiky implementovat ručně.
- Shell podporuje několik typů navigace:
  - **Flyout Menu** – vysouvací postranní nabídka.
  - **TabBar** – navigace pomocí záložek.
  - **Hierarchická navigace** mezi jednotlivými stránkami.
  - **Navigaci pomocí rout (Route-based navigation)**, kdy se stránky otevírají pomocí jejich registrovaných cest.

> [!info]
> Automaticky zachovává historii navigace (_navigation stack_).

```xml
<Shell>
    <TabBar>
        <ShellContent
            Title="Domů"
            ContentTemplate="{DataTemplate local:MainPage}" />

        <ShellContent
            Title="Nastavení"
            ContentTemplate="{DataTemplate local:SettingsPage}" />
    </TabBar>
</Shell>
```

---

# 4. Návrhové vzory a Data Binding

- Při vývoji aplikací v .NET MAUI se _nejčastěji využívá architektonický vzor_ **MVVM (Model–View–ViewModel)**, který odděluje _uživatelské rozhraní od aplikační logiky_.
- MVVM rozděluje aplikaci **do tří částí**:
  - **Model** představuje _datový model aplikace a obsahuje_ _komunikaci s databází či webovými službami_.
  - **View** tvoří _uživatelské rozhraní aplikace_. View pouze _zobrazuje data_ a _předává uživatelské akce dále_.
  - **ViewModel** představuje _prostředníka mezi modelem a uživatelským rozhraním_. Připravuje _data pro zobrazení, zpracovává uživatelské akce a komunikuje s modelem_.

## 4.1 Data Binding a INotifyPropertyChanged

- Komunikace mezi **View** a **ViewModelem** probíhá pomocí mechanismu **Data Binding**, který _propojuje vlastnosti uživatelského rozhraní s vlastnostmi ViewModelu_.
- Pokud se **hodnota** ve ViewModelu **změní**, Data Binding zajistí **automatickou aktualizaci zobrazených dat** v uživatelském rozhraní. Stejným způsobem mohou být změny provedené uživatelem automaticky přeneseny zpět do ViewModelu.
- Například _vlastnost_ `Text` _ovládacího prvku může být navázána na vlastnost_ `Name` _ve ViewModelu:_

```
<Entry Text="{Binding Name}" />
```

> [!info]
> Aby mohl Data Binding _automaticky reagovat na změny da_t, **implementují** ViewModely obvykle **rozhraní** `INotifyPropertyChanged`.
>
> Toto rozhraní obsahuje událost `PropertyChanged`, která _informuje uživatelské rozhraní o změně hodnoty některé vlastnosti._ Po vyvolání této události se **automaticky překreslí všechny prvky** navázané na danou vlastnost.

## 4.3 CommunityToolkit.Mvvm

- Pro _usnadnění vývoje se často používá knihovna_ **CommunityToolkit.Mvvm**, která **automaticky generuje opakující se kód** potřebný pro ViewModely. Díky tomu není nutné ručně implementovat například `INotifyPropertyChanged` a ViewModely jsou přehlednější a kratší.
- Vývojář tak může pomocí jednoduchých atributů, například `[ObservableProperty]` nebo `[RelayCommand]`

---

## 4.4 Komunikace mezi částmi aplikace

- Mechanismus `WeakReferenceMessenger` z knihovny CommunityToolkit.Mvvm funguje na principu **publish–subscribe**. Jedna část aplikace _odešle zprávu a všechny komponenty, které jsou k odběru této zprávy přihlášeny, ji mohou zpracovat_. Díky využití slabých referencí (_Weak References_) nedochází ke zbytečnému držení objektů v paměti, což snižuje riziko vzniku paměťových úniků.

---

# 5. Přístup k nativním API a platformní funkce

- Funkce, které _byly dříve součástí knihovny_ **Xamarin.Essentials**, jsou **dnes integrovány přímo** do .NET MAUI.
- Mezi _nejčastěji využívané platformní funkce_ patří:
  - **Geolokace** – zjištění aktuální polohy zařízení.
  - **Fotoaparát a galerie** – pořizování fotografií nebo výběr obrázků.
  - **Senzory** – například akcelerometr, kompas nebo gyroskop.
  - **Preferences** – ukládání jednoduchých nastavení aplikace ve formě dvojic klíč–hodnota.
  - **SecureStorage** – bezpečné ukládání citlivých údajů, například přihlašovacích tokenů nebo hesel.
  - **Connectivity** – zjištění stavu síťového připojení.
  - **Battery** – informace o stavu a nabití baterie.
  - **Clipboard** – práce se systémovou schránkou.
  - **Share** – sdílení obsahu prostřednictvím systémových aplikací.

## 5.1 Platformně specifický kód

- Přestože většina aplikace využívá sdílený kód, některé funkce jsou dostupné pouze na konkrétních platformách nebo vyžadují rozdílnou implementaci.
- V .NET MAUI lze platformně specifický kód řešit několika způsoby:
  - **Podmíněnou kompilací**, kdy se pomocí direktiv `#if ANDROID`, `#if IOS` nebo `#if WINDOWS` překládá pouze kód určený pro danou platformu.
  - **Oddělenou implementací ve složce** `Platforms`, kde má každá platforma vlastní soubory obsahující její specifickou funkcionalitu.

---

# 6. Data a perzistence

## 6.1 SQLite a Entity Framework Core

> [!info]
> Pro lokální databáze se v MAUI používá **SQLite**.  
> **EF Core** slouží k tomu abychom mohli pracovat s databázi snadněji.

- **ORM (Object-Relational Mapping):** **EF Core** umožňuje pracovat s databází pomocí **C# objektů** a **LINQ dotazů** namísto psaní surových SQL příkazů.

## 6.2 Preferences a SecureStorage

- Pro ukládání dat nabízí .NET MAUI několik možností podle typu ukládaných informací.
  - **Preferences** slouží k ukládání jednoduchých nastavení aplikace, například zvoleného jazyka, tmavého režimu nebo dalších uživatelských voleb. Data jsou ukládána jako dvojice **klíč–hodnota** a nejsou určena pro citlivé informace.
  - **SecureStorage** je určeno pro bezpečné ukládání citlivých údajů, jako jsou přístupové tokeny nebo přihlašovací údaje. Využívá bezpečnostní mechanismy přímo operačního systému (například **Keychain** v iOS nebo **Keystore** v Androidu), takže uložená data jsou šifrována a chráněna před neoprávněným přístupem.