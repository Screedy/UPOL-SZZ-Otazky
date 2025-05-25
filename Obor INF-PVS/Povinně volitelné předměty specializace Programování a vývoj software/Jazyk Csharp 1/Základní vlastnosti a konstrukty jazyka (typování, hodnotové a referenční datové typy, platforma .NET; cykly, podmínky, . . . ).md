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
## Proměnné
- V C# je nutné při deklaraci proměnné specifikovat typ nebo použít inferenci přes `var`.
#### Deklarace
```csharp
int cislo;
string retezec;
```
#### Deklarace s inicializací
```csharp
int cislo = -34;
string retezec = "Text";
```
#### Více proměnných najednou
```csharp
int a = 1, b = 2, c = 3;
```

#### Platnost proměnné
- Proměnné mají blokovou platnost – existují jen v rámci kódu, kde byly vytvořeny.

## Automatická inference typu (`var`)
- Použitím klíčového slova `var` lze nechat kompilátor určit typ proměnné na základě hodnoty:
```csharp
var pi = 3.14; // typ: double
```
- Proměnná musí být při deklaraci inicializována.
- Není možné použít `null`, protože z něj nelze odvodit typ.

## Konstanty
- Konstanta je proměnná, jejíž hodnota se nemění:
```csharp
const int x = 15;
```
- Hodnota musí být známá už při překladu programu (kompilaci).

## Přetypování
- V C# existují dva druhy převodů:
#### 1. Implicitní převod
- Probíhá automaticky mezi kompatibilními typy bez ztráty informace:

```csharp
int a = 10;
double b = a;
```
#### 2. Explicitní převod (cast)
- Nutný v případě možného přetečení nebo ztráty dat:

```csharp
int a = -32;
uint c = (uint)a; // přetečení, hodnota bude interpretována jako velmi vysoké číslo
```

## Komentáře
- Slouží k dokumentaci kódu pro programátory. Nejsou součástí přeloženého programu.
```csharp
// Jednořádkový komentář

/* 
   Víceřádkový
   komentář
*/
```
## Operátory

#### Aritmetické
- Používají se k výpočtům:
- `+`, `-`, `*`, `/`, `%`
- Inkrementace a dekrementace: `++`, `--`
- Zkrácené přiřazení: `+=`, `-=`, `*=`, `/=`
#### Porovnávací
- Vrací hodnoty typu `bool`:
- `==`, `!=`, `<`, `>`, `<=`, `>=`

#### Logické
- Slouží k práci s logickými výrazy:
- Negace: `!`
- Krátké zhodnocení: `&&`, `||`
- Bitové: `&`, `|`, `^`

#### Bitové operace
- Práce na úrovni jednotlivých bitů:
- NOT: `~`
- AND, OR, XOR: `&`, `|`, `^`
- Posun: `<<`, `>>`

#### Ternární operátor
- Zkrácená podmínka:
```csharp
int x = a > b ? a : b;
```

## Zápis čísel
- Číselné hodnoty lze zapisovat i binárně a hexadecimálně:
```csharp
int a = 123_456;         // čitelnější zápis
int b = 0b1010_1011;     // binární
byte c = 0xFF;           // hexadecimální
```

## Řízení toku programu
#### Podmínky (`if`, `else if`, `else`)
- Umožňují větvit kód podle podmínek:

```csharp
if (podminka) {
    // blok kódu
} else if (dalsiPodminka) {
    // další větev
} else {
    // výchozí větev
}
```

#### Přepínač (`switch`)
- Přehlednější alternativa pro více hodnot:
```csharp
switch (hodnota) {
    case "A":
    case "B":
        // společný kód
        break;
    default:
        break;
}
```

## Cykly
#### For
- Vhodný, když známe počet opakování předem:
```csharp
for (int i = 0; i < 10; i++) {
    // tělo cyklu
}
```
#### While
- Podmínka se testuje před každým během:
```csharp
while (podminka) {
    // tělo cyklu
}
```
#### Do...while
- Tělo cyklu se provede minimálně jednou:
```csharp
do {
    // tělo cyklu
} while (podminka);
```
- `break` – ukončí cyklus předčasně
- `continue` – přeskočí zbytek aktuální iterace

## Řetězce v C\#
- Řetězce (`string`) jsou imutabilní, tzn. nelze je po vytvoření změnit – každá úprava vytváří nový objekt.
#### Základní operace
- Délka: `text.Length`
- Převod malých/velkých písmen: `ToLower()`, `ToUpper()`
- Vyhledávání: `IndexOf()`, `StartsWith()`
- Spojování: pomocí operátoru `+` nebo interpolace

#### Interpolace řetězců
```csharp
string text = $"a={a}, b={b}";
```

#### Přístup ke znakům
```csharp
char znak = text[2];
```

- Pro efektivní práci s řetězci ve smyčkách se doporučuje použít `StringBuilder`, aby se předešlo nadměrné alokaci paměti.

## Práce s poli
- Pole v C# je datová struktura pro pevný počet prvků stejného datového typu. Délka pole je určena při jeho vytvoření a nelze ji později změnit.

#### Deklarace a inicializace
```csharp
int[] pole = new int[] { 2, 4, 6 };
int[] jednodusiZapis = { 1, 3, 4, 6, 7 };
bool[] pBool = new bool[20];
```

#### Přístup k prvkům a vlastnosti
- Indexace začíná od nuly.
- Přístup ke konkrétnímu prvku:
  ```csharp
  int prvni = pole[0];
  pole[2] = 64;
  ```
- Délku pole zjistíme přes `.Length`:
  ```csharp
  int delka = pole.Length;
  ```

#### Iterace přes pole
- Pomocí `for`:
  ```csharp
  for (int i = 0; i < pole.Length; i++) {
      Console.WriteLine(pole[i]);
  }
  ```
- Pomocí `foreach`, pokud nepotřebujeme index:
  ```csharp
  foreach (bool prvek in pBool) {
      if (prvek) { ... }
  }
  ```

### Vícedimenzionální pole
- C# umožňuje práci s vícerozměrnými poli.

#### Obdélníková pole
```csharp
int[,,] pole3d = new int[3,6,9];
int[,] pole2d = new int[,] { {1,2}, {3,4}, {5,6} };
```
- Počet dimenzí: `pole2d.Rank`
- Délka určité dimenze: `pole3d.GetLength(1)`

#### Nepravidelná (zubatá) pole – pole polí
```csharp
int[][] polePoli = new int[3][];
polePoli[0] = new int[] { 1, 2, 3, 4, 5 };
polePoli[1] = new int[] { 6, 7, 8 };
polePoli[2] = new int[] { 1 };
```


## Kódovací konvence v C\#
- Jednotný styl kódu zajišťuje:
	- Lepší čitelnost
	- Snazší spolupráci v týmu
	- Automatickou validaci a formátování v IDE
- Příklady zásad:
	- PascalCase pro názvy tříd a veřejných metod: `public class IntSet`, `public void Add()`
	- camelCase pro názvy proměnných a parametrů: `int count`, `string input`
	- Používat odsazení a mezery konzistentně
- Oficiální dokumentace ke stylu kódu v C# je dostupná na [oficiálních stránkách Microsoftu](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)

#### Doporučení k použití getterů a setterů
- Přístup k interním proměnným by měl být zprostředkován pomocí veřejných metod nebo vlastností, nikoliv přímým přístupem k proměnným. Důvody:
	- Zajištění kontroly nad validací dat
	- Možnost snadné změny implementace bez vlivu na uživatele třídy
	- Zamezení nekonzistentních nebo nebezpečných změn stavu objektu
```csharp
private int _value;

public int Value {
    get { return _value; }
    set {
        if (value >= 0) _value = value;
    }
}
```

- Tímto způsobem je možné do getteru/setteru přidat kontrolu nebo logiku bez změny veřejného rozhraní.

