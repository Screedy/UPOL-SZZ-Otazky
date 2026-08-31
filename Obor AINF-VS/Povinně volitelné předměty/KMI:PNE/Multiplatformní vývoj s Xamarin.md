> [!success]
> **Xamarin** byl _framework společnosti Microsoft_ určený pro _vývoj multiplatformních mobilních aplikací_ v jazyce **C#** a na platformě **.NET**. Umožňoval vytvářet aplikace pro **Android** a **iOS** ze společné kódové základny. Od **.NET 6** byl _nahrazen_ frameworkem **.NET MAUI (Multi-platform App UI)**, který je jeho _přímým nástupcem_.

- Místo psaní aplikace dvakrát (např. v Kotlinu pro Android a Swiftu pro iOS) se _většina aplikace napíše v jazyce C#_. Xamarin ji následně **zkompiluje pro cílovou platformu** a **propojí s jejími nativními API**. Výsledkem je **nativní aplikace**, nikoliv _webová nebo hybridní aplikace_.

### Výhody

- Jeden jazyk (**C#**) pro více platforem.
- Sdílení velké části kódu mezi Androidem a iOS.
- Přístup k nativním API zařízení (kamera, GPS, senzory, notifikace).
- Nižší náklady na vývoj a údržbu než při vývoji dvou samostatných aplikací.
- Dobrá integrace s Visual Studiem a .NET ekosystémem.

### Nevýhody

- Ne všechny části aplikace lze sdílet – některé funkce jsou specifické pro jednotlivé platformy.
- Složitější ladění při práci s více platformami.
- Závislost na aktualizacích frameworku.
- Xamarin je dnes zastaralý a již se pro nové projekty nedoporučuje.

---

# 1. Architektura

> [!success]
> Xamarin **nevytváří webovou ani hybridní aplikaci**. Zdrojový kód napsaný v jazyce **C#** kompiluje pro cílovou platformu a propojuje jej s jejími **nativními API**, takže výsledkem je skutečná **nativní aplikace**.

- Architektura Xamarinu je založena na **sdílení co největší části aplikace** mezi jednotlivými platformami. Vývojář píše většinu aplikace pouze jednou a Xamarin se stará o její propojení s operačním systémem Android nebo iOS.
- Architekturu lze _rozdělit do tří základních vrstev_:
  - **Sdílený kód (Shared Code)** – obsahuje _modely_, _business logiku_, _služby_, _komunikaci s REST API_ nebo _práci s databází_. Tato část je **společná pro všechny platformy**.
  - **Platformně specifický kód** – obsahuje uživatelské rozhraní (u Xamarin.Native) a přístup k f_unkcím zařízení, jako je kamera, GPS, Bluetooth nebo notifikace_. Každá platforma **má vlastní implementaci.**
- Xamarin zpřístupňuje _nativní funkce operačních systémů_ pomocí **C# bindingů** (obálek). Ty umožňují **volat nativní API** _Androidu a iOS_ přímo **z jazyka C#**. Vývojář tak může například pracovat s třídami `Android.Views` nebo `UIKit`, přestože celou aplikaci vytváří v C#.

| Přístup | Co to znamená | Sdílení UI kódu | Kdy použít |
| --- | --- | --- | --- |
| **Xamarin.Native** (Xamarin.iOS, Xamarin.Android) | UI se píše zvlášť pro každou platformu | ~75 % (jen logika) | Když chceš maximální nativní vzhled a kontrolu |
| **Xamarin.Forms** | Jednotné UI v XAML, automaticky se mapuje na nativní kontrolky | ~95 % (logika i UI) | Business aplikace, formuláře, prototypy |

## 1.1 Sdílení kódu

- Největší výhodou Xamarinu je možnost **sdílet většinu zdrojového kódu** mezi Androidem a iOS. V závislosti na typu projektu lze sdílet přibližně **70–95 % aplikace**.
- Platformně specifická část aplikace obsahuje _pouze funkce závislé na konkrétním operačním systému_.
- Sdílení bylo možné několika způsoby:
  - **Shared Project** – sdílel **přímo zdrojové soubory**. Při kompilaci se jejich obsah vložil do každého platformního projektu. Výhodou byla možnost _používat podmíněnou kompilaci_ (`#if ANDROID`, `#if IOS`).
  - **.NET Standard Library** – doporučený způsob. _Společná logika byla umístěna_ **do samostatné knihovny**, kterou _využívaly všechny platformní projekty_. Knihovna se zkompilovala pouze jednou a Android i iOS ji následně používaly.
- _Příklad pomocí knihovny_ _(získání lokace)__:_

```
// V knihovně se vytvoří rozhrání s potřebnými metodami
public interface ILocationService
{
    Task<Location> GetLocationAsync();
}

// A pak pro každou platformu se specificky doimplemtuje
public class AndroidLocationService : ILocationService
{
    public Task<Location> GetLocationAsync()
    {
        // Android API
    }
}

public class IOSLocationService : ILocationService
{
    public Task<Location> GetLocationAsync()
    {
        // iOS API
    }
}
```

# 2. Přístup k vývoji aplikací

- Xamarin podporoval _dva základní přístupy k vývoji multiplatformních aplikací_ – **Xamarin.Native** a **Xamarin.Forms**.
- **Xamarin.Native** zahrnuje frameworky **Xamarin.Android** a **Xamarin.iOS**.
  - V tomto případě se **uživatelské rozhraní vytváří samostatně** pro každou platformu **pomocí jejích nativních komponent**.
  - Obvykle lze sdílet přibližně **70–80 % zdrojového kódu**.
  - Tento přístup je vhodný pro aplikace, které _vyžadují maximální výkon_, _plnou kontrolu nad vzhledem_ nebo _využívají specifické funkce jednotlivých platforem_.
- **Xamarin.Forms** umožňuje vytvořit **uživatelské rozhraní pouze jednou** pomocí jazyka **XAML**.
  - Framework následně pomocí **Rendererů** _převádí jednotlivé prvky na nativní ovládací prvky Androidu a iOS_.
  - Celkově bývá společných až **90–95 % zdrojového kódu**.
  - Xamarin.Forms je proto vhodný pro systémy, kde je _požadován podobný vzhled na všech platformách_.

## 2.1 Xamarin.Android

- Vývojář používá _stejné komponenty jako při běžném vývoji pro Android_ (např. **Activity**, **Fragment**, **Service**), pouze místo Javy nebo Kotlinu **programuje v C#**.
- Zdrojový kód se nejprve zkompiluje do **IL (Intermediate Language)**. Při spuštění aplikace jej **Mono Runtime** přeloží do strojového kódu pomocí **JIT (Just-In-Time)** kompilace (v novějších verzích je možné využít také částečnou **AOT** kompilaci).
- Komunikaci s operačním systémem zajišťují **C# bindingy**, které prostřednictvím **JNI (Java Native Interface)** zpřístupňují Android API
- _Příklad vytvoření tlačítka_:

```csharp
Button button = FindViewById<Button>(Resource.Id.myButton);
button.Click += (s, e) =>
{
    Toast.MakeText(this, "Kliknuto!", ToastLength.Short).Show();
};
```

## 2.2 Xamarin.iOS

- Vývojář využívá stejné frameworky jako při vývoji ve Swiftu nebo Objective-C, například **UIKit** nebo **Foundation**, pouze _prostřednictvím C# bindingů_.
- Na rozdíl od Androidu **Apple nepovoluje JIT kompilaci**, protože _z bezpečnostních důvodů zakazuje dynamické generování strojového kódu během běhu aplikace_. Xamarin.iOS proto používá výhradně **AOT (Ahead-of-Time)** kompilaci – celý IL kód je již při sestavení aplikace přeložen přímo do nativního ARM strojového kódu.
- Výsledná aplikace tak běží _přímo na operačním systému iOS a využívá jeho nativní komponenty_.
- _Příklad vytvoření tlačítka_:

```csharp
UIButton button = new UIButton(UIButtonType.System);
button.SetTitle("Klikni", UIControlState.Normal);
button.TouchUpInside += (sender, e) =>
{
    Console.WriteLine("Kliknuto");
};
```

## 2.3 Xamarin.Forms

> [!success]
> **Xamarin.Forms** je knihovna postavená nad Xamarin.Android a Xamarin.iOS, která umožňuje vytvořit **jedno společné uživatelské rozhraní** pro všechny podporované platformy.

- Na rozdíl od Xamarin.Native se _uživatelské rozhraní nevytváří zvlášť pro každou platformu, ale pouze jednou_ pomocí značkovacího jazyka **XAML**. Xamarin.Forms následně využívá mechanismus **Rendererů**, které _převádějí abstraktní prvky XAML na odpovídající nativní ovládací prvky_ jednotlivých operačních systémů.
- **_Například prvek_**:

```
<Button Text="Přihlásit" />
```

- je při _spuštění automaticky převeden_ na:
  - `android.widget.Button` v systému Android,
  - `UIButton` v systému iOS.

- _Kód uživatelského rozhraní_ se zapisuje do souborů **XAML**, zatímco _aplikační logika_ je umístěna v tzv. **code-behind** nebo častěji ve **ViewModelu** podle architektury **MVVM**.

```xml
// XAML — deklarativní popis UI
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms">
    <StackLayout Padding="20">
        <Label Text="Ahoj, Xamarin!" FontSize="24" />
        <Button Text="Klikni" Clicked="OnButtonClicked" />
    </StackLayout>
</ContentPage>
```

```csharp
// Code-behind (C#)
public partial class MainPage : ContentPage {
    public MainPage() {
        InitializeComponent();
    }

    private void OnButtonClicked(object sender, EventArgs e) {
        DisplayAlert("Info", "Kliknuto!", "OK");
    }
}
```

---

# 3. MVVM (Model–View–ViewModel)

> [!success]
> **MVVM (Model–View–ViewModel)** je architektonický vzor, který odděluje uživatelské rozhraní od aplikační logiky. Xamarin.Forms je pro tento vzor přímo navržen.

- MVVM _rozděluje aplikaci do tří částí_:
  - **Model** – reprezentuje data a business logiku aplikace.
  - **View** – představuje uživatelské rozhraní vytvořené v jazyce **XAML**.
  - **ViewModel** – propojuje Model a View. Obsahuje stav aplikace a prezentační logiku.

## 3.1 Data binding

- _Komunikace mezi View a ViewModelem_ probíhá pomocí **Data Bindingu**.
- Ve View se _jednotlivé vlastnosti propojují s vlastnostmi ViewModelu_ pomocí výrazu `{Binding ...}`.

```
<Label Text="{Binding UserName}" />
```

- Pokud se změní hodnota `UserName` ve ViewModelu, automaticky se aktualizuje i text zobrazený v Labelu.
- ViewModel musí implementovat rozhraní `INotifyPropertyChanged` (To obsahuje událost `PropertyChanged`, která informuje View, že se změnila hodnota některé vlastnosti.)

## 3.2 BindingContext

- Aby Data Binding fungoval, musí _View vědět, se kterým ViewModelem má komunikovat_.
- To zajišťuje vlastnost **BindingContext**.

```
BindingContext = new MainViewModel();
```

- Od této chvíle budou všechny výrazy `{Binding ...}` hledat své vlastnosti právě v instanci `MainViewModel`.

## 3.3 ICommand

- Ve Xamarin.Forms se _místo obsluhy událostí_ (`Clicked`) často **používá rozhraní** **ICommand**.
- View pouze _vyvolá příkaz a samotná logika zůstává ve ViewModelu_.

```
<Button
    Text="Uložit"
    Command="{Binding SaveCommand}" />
```

```
public ICommand SaveCommand { get; }

public MainViewModel()
{
    SaveCommand = new Command(Save);
}

private void Save()
{
    // uložení dat
}
```

---

# 4. Přístup k platformně specifickým funkcím

- K propojení sdíleného kódu s platformní implementací Xamarin nabízel několik mechanismů.

## 4.1 DependencyService

- **DependencyService** je jednoduchý mechanismus vestavěný přímo v Xamarin.Forms. _Umožňuje registrovat platformní implementace služeb_ a následně je získat ve sdíleném projektu.
- V novějších aplikacích bývá často nahrazován **Dependency Injection**.

## 4.2 Xamarin.Essentials

- Pro **nejčastěji používané funkce** zařízení Microsoft vytvořil knihovnu **Xamarin.Essentials**, která poskytuje jednotné _C# API nezávislé na platformě_.
- _Například umožňuje přístup k_:
  - **geolokaci**,
  - stavu **baterie**,
  - **síťovému** připojení,
  - schránce (Clipboard),
  - nastavením aplikace (Preferences),
  - bezpečnému úložišti (Secure Storage),
  - sdílení obsahu (Share),
  - otevření URL nebo jiné aplikace (Launcher),
  - výběru fotografie nebo videa (MediaPicker).

```
//Například získání aktuální polohy je velmi jednoduché
var location = await Geolocation.GetLastKnownLocationAsync();
```

## 4.3 Effects a Custom Renderers

- Pokud je potřeba upravit vzhled nebo chování konkrétní komponenty pouze na jedné platformě, lze využít **Effects** nebo **Custom Renderers**.
  - **Effect** provádí drobnou úpravu existující komponenty (např. přidání stínu nebo změnu barvy okraje).
  - **Custom Renderer** nahrazuje celé vykreslování komponenty vlastním řešením a poskytuje plnou kontrolu nad jejím vzhledem i chováním.

# 5. Xamarin vs. .NET MAUI

- **.NET MAUI (Multi-platform App UI)** — od .NET 6 (listopad 2021) **nástupce Xamarin.Forms**.
- Mezi **hlavní změny** oproti Xamarinu patří:
  - **Single Project** – _místo několika samostatných projektů_ (Android, iOS a sdílený projekt) využívá MAUI **jeden společný projekt**, který obsahuje veškerý sdílený i platformně specifický kód.
  - **Součást sjednocené platformy .NET** – MAUI je postaven přímo na moderním .NET (od verze .NET 6) a _není založen na samostatném Xamarin/Mono ekosystému_.
  - **Podpora více platforem** – kromě Androidu a iOS podporuje také **Windows** (WinUI 3) a **macOS** (Mac Catalyst).
  - **Handlers místo Rendererů** – Xamarin.Forms _používal Renderery pro převod prvků XAML na nativní komponenty_. MAUI je nahrazuje modernější architekturou **Handlers**, která má jednodušší implementaci, menší režii a vyšší výkon.
  - **Lepší integrace s Dependency Injection** – MAUI **využívá vestavěný DI kontejner** známý z ASP.NET Core.
  - **Vyšší výkon** – rychlejší spuštění aplikace, efektivnější vykreslování uživatelského rozhraní a menší spotřeba paměti.