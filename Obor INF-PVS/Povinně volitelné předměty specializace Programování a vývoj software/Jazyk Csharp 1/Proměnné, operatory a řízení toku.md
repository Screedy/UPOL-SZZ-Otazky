## Základní datové typy v jazyce C#

V jazyce C# je datový typ každé proměnné striktně určen – buď přímo při deklaraci, nebo automatickou inferencí. Mezi základní typy patří:

| Klíčové slovo | Rozsah                          | Popis                           |
|---------------|----------------------------------|----------------------------------|
| `bool`        | `true`, `false`                 | Pravdivostní hodnoty            |
| `sbyte`       | `-128` až `127`                 | 8bitové číslo se znaménkem      |
| `byte`        | `0` až `255`                    | 8bitové číslo bez znaménka      |
| `short`       | `-32 768` až `32 767`           | 16bitové číslo se znaménkem     |
| `ushort`      | `0` až `65 535`                 | 16bitové číslo bez znaménka     |
| `int`         | `-2^31` až `2^31 - 1`           | 32bitové číslo se znaménkem     |
| `uint`        | `0` až `2^32 - 1`               | 32bitové číslo bez znaménka     |
| `long`        | `±9×10^18`                      | 64bitové číslo se znaménkem     |
| `ulong`       | `0` až `1.8×10^19`              | 64bitové číslo bez znaménka     |
| `char`        | `U+0000` až `U+FFFF`            | Unicode znak                    |
| `float`       | `±3.4×10^38`                    | 32bitové reálné číslo           |
| `double`      | -                               | 64bitové reálné číslo           |
| `decimal`     | -                               | 128bitové číslo s přesností     |
| `string`      | dle paměti                      | Imutabilní řetězec znaků        |
| `object`      | -                               | Základní třída všech typů       |

## Proměnné

V C# je nutné při deklaraci proměnné specifikovat typ nebo použít inferenci přes `var`.

### Deklarace
```csharp
int cislo;
string retezec;
```

### Deklarace s inicializací
```csharp
int cislo = -34;
string retezec = "Text";
```

### Více proměnných najednou
```csharp
int a = 1, b = 2, c = 3;
```

### Platnost proměnné
Proměnné mají blokovou platnost – existují jen v rámci kódu, kde byly vytvořeny.

## Automatická inference typu (`var`)

Použitím klíčového slova `var` lze nechat kompilátor určit typ proměnné na základě hodnoty:

```csharp
var pi = 3.14; // typ: double
```

- Proměnná musí být při deklaraci inicializována.
- Není možné použít `null`, protože z něj nelze odvodit typ.

## Konstanty

Konstanta je proměnná, jejíž hodnota se nemění:

```csharp
const int x = 15;
```

- Hodnota musí být známá už při překladu programu (kompilaci).

## Přetypování

V C# existují dva druhy převodů:

### Implicitní převod
Probíhá automaticky mezi kompatibilními typy bez ztráty informace:

```csharp
int a = 10;
double b = a;
```

### Explicitní převod (cast)
Nutný v případě možného přetečení nebo ztráty dat:

```csharp
int a = -32;
uint c = (uint)a; // přetečení, hodnota bude interpretována jako velmi vysoké číslo
```

## Komentáře

Slouží k dokumentaci kódu pro programátory. Nejsou součástí přeloženého programu.

```csharp
// Jednořádkový komentář

/* 
   Víceřádkový
   komentář
*/
```

## Operátory

### Aritmetické
Používají se k výpočtům:

- `+`, `-`, `*`, `/`, `%`
- Inkrementace a dekrementace: `++`, `--`
- Zkrácené přiřazení: `+=`, `-=`, `*=`, `/=`

### Porovnávací
Vrací hodnoty typu `bool`:

- `==`, `!=`, `<`, `>`, `<=`, `>=`

### Logické
Slouží k práci s logickými výrazy:

- Negace: `!`
- Krátké zhodnocení: `&&`, `||`
- Bitové: `&`, `|`, `^`

### Bitové operace
Práce na úrovni jednotlivých bitů:

- NOT: `~`
- AND, OR, XOR: `&`, `|`, `^`
- Posun: `<<`, `>>`

### Terciární operátor
Zkrácená podmínka:

```csharp
int x = a > b ? a : b;
```

## Zápis čísel

Číselné hodnoty lze zapisovat i binárně a hexadecimálně:

```csharp
int a = 123_456;         // čitelnější zápis
int b = 0b1010_1011;     // binární
byte c = 0xFF;           // hexadecimální
```

## Řízení toku programu

### Podmínky (`if`, `else if`, `else`)
Umožňují větvit kód podle podmínek:

```csharp
if (podminka) {
    // blok kódu
} else if (dalsiPodminka) {
    // další větev
} else {
    // výchozí větev
}
```

### Přepínač (`switch`)
Přehlednější alternativa pro více hodnot:

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

### For
Vhodný, když známe počet opakování předem:

```csharp
for (int i = 0; i < 10; i++) {
    // tělo cyklu
}
```

### While
Podmínka se testuje před každým během:

```csharp
while (podminka) {
    // tělo cyklu
}
```

### Do...while
Tělo cyklu se provede minimálně jednou:

```csharp
do {
    // tělo cyklu
} while (podminka);
```

- `break` – ukončí cyklus předčasně
- `continue` – přeskočí zbytek aktuální iterace

## Řetězce v C#

Řetězce (`string`) jsou imutabilní, tzn. nelze je po vytvoření změnit – každá úprava vytváří nový objekt.

### Základní operace
- Délka: `text.Length`
- Převod malých/velkých písmen: `ToLower()`, `ToUpper()`
- Vyhledávání: `IndexOf()`, `StartsWith()`
- Spojování: pomocí operátoru `+` nebo interpolace

### Interpolace řetězců
```csharp
string text = $"a={a}, b={b}";
```

### Přístup ke znakům
```csharp
char znak = text[2];
```

Pro efektivní práci s řetězci ve smyčkách se doporučuje použít `StringBuilder`, aby se předešlo nadměrné alokaci paměti.
