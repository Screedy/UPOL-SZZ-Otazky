## Jazyk C\#
- C# je moderní, multiparadigmatický programovací jazyk navržený primárně jako objektově orientovaný, ale podporuje i procedurální a funkcionální prvky. Od svého uvedení v roce 2002 prošel C# výrazným vývojem a dnes je ve verzi 12.0, s verzí 13.0 v přípravě.
- Syntaxe je podobná jazykům C a Java.
- Jazyk má vestavěnou podporu pro správu paměti pomocí **Garbage Collectoru**.
- Obsahuje pokročilé konstrukce jako výjimky, události, delegáty a podporu pro asynchronní programování.
- Původně vyvinut firmou Microsoft pro platformu Windows, dnes je plně multiplatformní díky .NET.
- C# lze využít pro vývoj:
	- Konzolových aplikací
	- Desktopových GUI aplikací (např. pomocí WPF)
	- Webových a mobilních aplikací (např. pomocí ASP.NET nebo MAUI)

## Platforma .NET

>[!info]
>.NET je multiplatformní, open-source vývojová platforma pro tvorbu různých typů aplikací. Zahrnuje jazyky, knihovny a nástroje pro vývojáře.

- Složení:
	- **Jazyky**: C# je hlavní jazyk, podporovány jsou i F#, Visual Basic aj.
	- **Knihovny**: Např. BCL (Base Class Library), obsahující základní typy a API.
	- **Nástroje**: buildovací systémy, debuggery, kompilátory.
- Aktuální verze .NET je 8.x a klade důraz na výkon, bezpečnost a multiplatformní použití (Windows, Linux, macOS).

## Vývojová prostředí pro C\#

### Visual Studio
- Oficiální IDE od Microsoftu pro vývoj v C# a .NET:
- Community edice je zdarma a vhodná pro studenty a jednotlivce.
- Podporuje návrháře GUI, ladění, testování a integraci s Gitem.
- K dispozici pro Windows a částečně i macOS.

### Visual Studio Code
- Odlehčený, rozšiřitelný editor vhodný pro multiplatformní vývoj.
- Pro plnohodnotný vývoj v C# je nutné doinstalovat rozšíření pro .NET.
- Nabízí menší komfort než Visual Studio, ale je svižnější a přenosný.

### JetBrains Rider
- Plnohodnotné IDE s pokročilými funkcemi, vhodné i pro Linux.
- Podporuje .NET Core i .NET 8, výborná alternativa k Visual Studiu.
- Pro studenty je dostupný zdarma po ověření školního e-mailu.

## Základní datové typy v C\#

| Klíčové slovo | Popis                            | Rozsah                              |
| ------------- | -------------------------------- | ----------------------------------- |
| `bool`        | Logická hodnota                  | `true`, `false`                     |
| `sbyte`       | 8bitové celé číslo se znaménkem  | `-128` až `127`                     |
| `byte`        | 8bitové celé číslo bez znaménka  | `0` až `255`                        |
| `short`       | 16bitové celé číslo se znaménkem | `-32 768` až `32 767`               |
| `ushort`      | 16bitové celé číslo bez znaménka | `0` až `65 535`                     |
| `int`         | 32bitové celé číslo se znaménkem | `-2 147 483 648` až `2 147 483 647` |
| `uint`        | 32bitové celé číslo bez znaménka | `0` až `4 294 967 295`              |
| `long`        | 64bitové celé číslo se znaménkem | `±9.2×10^18`                        |
| `ulong`       | 64bitové celé číslo bez znaménka | `0` až `18.4×10^18`                 |
| `float`       | Reálné číslo (32bit)             | přibližně `±3.4×10^38`              |
| `double`      | Reálné číslo (64bit)             | větší přesnost než `float`          |
| `decimal`     | 128bitové číslo                  | vhodné pro finanční výpočty         |
| `char`        | Unicode znak                     | `U+0000` až `U+FFFF`                |
| `string`      | Imutabilní řetězec znaků         | délka omezena pamětí systému        |
| `object`      | Základní typ všech ostatních     | předek všech typů v C#              |

## Proměnné
- **Deklarace proměnné**:
  ```csharp
  int cislo;
  string retezec;
  ```

- **Deklarace s inicializací**:
  ```csharp
  int cislo = -34;
  string retezec = "nějaký text";
  ```

- **Více proměnných najednou**:
  ```csharp
  int a = 1, b = 2, c = 3;
  ```
- Proměnná v C# má vždy definovaný datový typ. Rozsah platnosti proměnné je omezen na blok, ve kterém byla vytvořena (lokální proměnná).

## Metody v C#
- Metoda je pojmenovaný blok kódu, který může přijímat vstupní parametry, provést operaci a vrátit výsledek.
- Definice:
  ```csharp
  int AreaOfTriangle(int baseLength, int height) {
      return baseLength * height / 2;
  }
  ```
- Volání:
  ```csharp
  int area = AreaOfTriangle(6, 3);
  ```

- Metody mohou být součástí tříd a mohou mít různé úrovně přístupu (např. `public`, `private`).

## Debugger v C\#
- Ladicí nástroje slouží ke sledování a opravám chyb v běžícím programu.
- **Breakpoint** – místo v kódu, kde se běh programu pozastaví.
- **Podmíněné breakpointy** – aktivují se jen při splnění určité podmínky.
- **Krokování** – umožňuje postupné vykonávání kódu (`Step Into`, `Step Over`).
- **Call Stack** – zobrazuje aktuální zanoření volání metod.
- Debugger je základní nástroj při analýze chybového chování programů.

