# 1. Platforma .NET

> [!success]
> **.NET** je _open-source vývojářská platforma_ (framework) určená pro _vývoj a spouštění aplikací_.  
> .**NET** je spravován _společností Microsof_t a _komunitou na GitHubu_.  
> Poskytuje _runtime prostředí_, _sadu standardních knihoven_ a _podporu pro více programovacích jazyků_.

> [!note]
> **Intuice:** .NET je vrstva mezi kódem a operačním systémem.

- Platforma **.NET** prošla během let několika vývojovými etapami.
- _Původní_ **.NET Framework** byl určen **pouze** pro operační systém **Windows**, zatímco projekt **Mono** vznikl jako jeho open-source implementace umožňující spouštění .NET aplikací **_na dalších platformách_**, například Linuxu nebo macOS.
- V roce 2016 představil Microsoft **.NET Core**, moderní, otevřenou a _multiplatformní verzi .NET_, která postupně **nahradila** .NET Framework. Od verze **.NET 5** bylo označení _Core_ opuštěno a dnes se používá jednoduše název **.NET**, který představuje _hlavní platformu pro vývoj moderních aplikací_.

## 1.1 CLR (Common Language Runtime)

> [!success]
> **CLR** je _runtime prostředí_ (virtuální stroj), které **spouští .NET programy**.  
> Zajišťuje _správu paměti, typovou bezpečnost, ošetření výjimek a JIT kompilaci_.

- **JIT (Just In Time) kompilace** — Převod IL kódu na nativní strojový kód při prvním spuštění metody. (Až když je to potřeba)
- **Garbage Collection (GC)** — Automatická správa paměti.
- **Type safety (Typová bezpečnost)** — Zabraňuje přístupu mimo povolenou paměť a porušení typového systému.
- **Exception handling** — Standardizovaný mechanismus výjimek napříč jazyky.
- **Thread management** — Správa vláken a synchronizace.

## 1.2 IL / CIL

> [!success]
> **CIL (Common Intermediate Language)** je **mezijazyk** do _kterého se kompilují všechny .NET jazyky_ (C#, F#, VB.NET). Je nezávislý na procesoru. Je stejný pro Windows, Linux i macOS.

> [!info]
> Dříve byl používaný _MSIL (Microsoft Intermediate Language)_

### **1.2.1 Tok kompilace**

![[019fa309-0e2b-713a-b3b6-77f623e37f44.png]]

- Zdrojový kód v C# je nejprve přeložen do platformně nezávislého mezikódu IL. Ten je až při spuštění programu pomocí JIT kompilátoru převeden do nativního strojového kódu konkrétního procesoru. Díky tomu může stejný program běžet na různých platformách.

## 1.3 BCL (Base Class Library)

> [!success]
> **BCL** je _sada základních tříd a rozhraní dodávaných s .NET_ (standardní sada knihoven)  
> Poskytuje datové struktury, I/O operace, síťovou komunikaci, kryptografii, vlákna apod.

## 1.4 GC (Garbage Collector)

> [!success]
> **GC** je _automatický správce paměti v CLR_.
>
> Sleduje živé reference na objekty a uvolňuje paměť objektů, ke kterým už neexistuje žádná reference.

## 1.5 Managed vs. Unmanaged kód

|     | Managed kód | Unmanaged kód |
| --- | --- | --- |
| Správa paměti | CLR — GC | Manuální (malloc/free) |
| Typová bezpečnost | Garantována CLR | Není |
| Jazyk | C#, F#, VB.NET | C, C++, Assembly |

- **Unsafe kód v C#:** C# umožňuje obejít management CLR pomocí klíčového slova `unsafe` a pracovat s pointery jako v C/C++. Vyžaduje explicitní povolení kompilátoru (`/unsafe` flag).

```csharp
unsafe {
    int cislo = 42;
    int* ptr = &cislo;    // Získání adresy proměnné
    *ptr = 987;           // Dereference pointeru
}
```

> [!info]
> Výhodné použít například při optimalizaci výkonu.

---

# 2. Jazyk C#

> [!success]
> C# je **staticky typovaný** jazyk (musíme nejprve deklarovat s jejich datovým typem) s jednotnou hierarchií typů, vše dědí od `System.Object` (všechno je objekt)

- V jazyce C# existují _dva druhy typů_: referenční typy a hodnotové typy.
- **Proměnné referenčního typu** ukládají _odkazy na data_ (objekty), zatímco **proměnné hodnotových typů** přímo _obsahují příslušná data_

## **2.1 Hodnotové typy (value types):**

- Normálně uloženy na _zásobníku_ (lokální proměnná) nebo na _haldě_, když je součástí objektu
- Každá proměnná _má svoji vlastní kopii dat_ a není možné, aby _operace na jedné proměnné ovlivnily druhou proměnnou_
- **Životnost** pouze v _aktuálním prostředí_
- Jako _parametr_ funkce je _kopie hodnoty_
- _Jedná se o_:
  - **Celočíselné typy**: `int`, `uint`, `short`, `ushort`, `byte`, `sbyte`, `long`, `ulong`
  - **Číselné typy s plovoucí desetinnou čárkou**: `double`, `float`, `decimal`
  - `bool`
  - `char`
  - **Výčtové typy**: `enum`
  - **Typy struktur**: `struct`
  - **Tuple typy**
  - **Nullable hodnotové typy**

```csharp
int a = 5;
int b = a;  // Kopie hodnoty — změna b neovlivní a
double d = 3d;
enum Seasons {
  Spring,
  Summer,
  Autumn,
  Winter
}
(double, int) touple1 = (4.5, 3);

int? x = null;  // Nullable<int>
if (x.HasValue) Console.WriteLine(x.Value);
```

## **2.2 Referenční typy (reference types):**

- Uloženy na haldě, proměnná drží referenci (ukazatel)
- Dvě proměnné _mohou odkazovat na stejný objekt_. Operace v rámci jedné proměnné tedy mohou ovlivňovat objekt odkazovaný jinou proměnnou.
- **Životnost** určuje _garbage collector_.
- Jako parametr funkce je předávána reference (na **stacku** je jen **reference** na tento objekt.)
- _Jedná se o_:
  - Typ objektu
  - Dynamický typ
  - Typ řetězce: `string`
  - Typ delegáta: `delegate`
  - Záznam: `record`
  - Třída: `class`
  - Rozhraní: `interface`
  - Pole: `array`

```csharp
var list1 = new List<int> { 1, 2, 3 };
var list2 = list1;  // Kopie reference — list1 a list2 ukazují na stejný objekt
```

## 2.3 Generika

> [!success]
> **Generika** umožňují psát _třídy, metody, rozhraní a delegáty_, které pracují s **typem jako s parametrem**. Typ se specifikuje až při použití, ne při definici.

```csharp
public class Box<T> {
    private T _value;
    public void Set(T value) => _value = value;
    public T Get() => _value;
}

// použití
Box<int> intBox = new Box<int>();
Box<string> strBox = new Box<string>();
```

> [!info]
> `T` je tzv. **type parameter —** konkrétní typ se dosadí až při nasazení.

## 2.4 Delegáti a události

> [!success]
> Delegát je **typově bezpečný ukazatel na metodu**. Je to referenční typ, který drží odkaz na jednu nebo více metod se shodnou signaturou a lze ho zavolat jako funkci.

```csharp
public delegate int Operation(int a, int b);

public static int Add(int a, int b) => a + b;
public static int Sub(int a, int b) => a - b;

Operation op = Add;
Console.WriteLine(op(3, 4)); // 7

op = Sub;
Console.WriteLine(op(3, 4)); // -1
```

> [!danger]
> Delegát musí odpovídat metodě **návratovým typem i parametry** – ne jménem.

## 2.5 LINQ (Language Integrated Query)

> [!success]
> LINQ je sada _rozšiřujících metod_ a _jazykových konstrukcí_, které umožňují **dotazovat se nad libovolnou kolekcí** jednotným deklarativním syntaxem. (místo psaní cyklů se popíše, _co_ chceme získat, ne _jak)_

- Funguje nad vším, co implementuje `IEnumerable<T>` nebo `IQueryable<T>`.

### 2.5.1 Syntax

```csharp
//Querry syntax
var result = from p in people
             where p.Age > 18
             orderby p.Name
             select p.Name;
// Method syntax
var result = people
    .Where(p => p.Age > 18)
    .OrderBy(p => p.Name)
    .Select(p => p.Name);
```

> [!info]
> Query syntax se za kompilace _přeloží na method syntax_ – jsou ekvivalentní.
>
> Method syntax má ale víc metod (query syntax nepokrývá vše, např. `Count`, `Sum`).

> [!danger]
> **_Klíčová vlastnost LINQ_**: Líné vyhodnocování. Dotaz se **nevyhodnotí při definici**, ale až při iteraci.

```csharp
var query = numbers.Where(n => n > 5); // zatím se nic neprovede

numbers.Add(10);
foreach (var n in query) { ... }       // teď se dotaz vyhodnotí, včetně nové 10
```

---

# 3. Základy jazyka F#

> [!success]
> F# je **funkcionální jazyk** v rámci .NET platformy.  
> Je **multiparadigmatický** – primárně funkcionální, ale podporuje i objektově orientované a imperativní konstrukce.

> [!danger]
> **Klíčová filozofie:**
>
> - **immutabilita jako výchozí stav**,
> - funkce jako _plnohodnotné hodnoty_,
> - silná statická typová kontrola s **odvozením typů** (kompilátor typy většinou odvodí sám, minimum explicitních anotací).

## 3.1 Základní odlišnosti od C#

- Odsazení je _významové_ (podobně jako v Pythonu - nahrazuje složené závorky).
- Středníky na konci řádku nejsou potřeba.
- Definice pomocí klíčového slova `let`.

```
let x = 5                   // immutable hodnota (ne proměnná!)
let name = "Petr"
fun x y -> x + y            // anonymní funkce
let add = fun x y -> x + y  // pojmenovaná funkce
let add a b = a + b    // funkce – typy se odvodí automaticky (int -> int -> int)

printfn "%d" (add 2 3) // 5
```

### 3.1.1 Immutabilita

- Vše definované přes `let` je ve **výchozí verzi immutabilní**

```fsharp
let y = 10
y <- 20   // CHYBA: kompilátor to nedovolí

let mutable z = 10
z <- 20   // OK, explicitní mutable
```

> [!danger]
> **Pozor!**
>
> Když uděláme `let y = 25` _nevytvoří novou hodnotu přepsáním_ — vytvoří **nový binding** `y` ve scope. Původní `y = 10` stále existuje v uzávěrech (closure), které na ni odkazují.

```
let y = 10
let getOldY = fun () -> y     // closure zachytí *tento* y (=10)

let y = 25                     // nový binding, stíní předchozí

printfn "%d" (getOldY())       // vypíše 10, ne 25!
printfn "%d" y                 // vypíše 25
```

### 3.1.2 Funkce jako first-class hodnoty

- Funkce se dají _přiřazovat, předávat jako parametry, vracet z jiných funkcí_ (bez potřeby delegátů jako v C#).

```csharp
// Funkce se dá přiřadit stejně jako jakákoliv jiná hodnota
let secti = fun a b -> a + b
let vysledek = secti 3 4   // 7

// Funkce je předána jako parametr (funkci vyššího řádu)
let square x = x * x
let applyTwice f x = f (f x)
applyTwice square 3   // 81

// Funkce, která vrací jinou funkci (closure zachytí "n")
let vytvorNasobicku (n: int) =
    fun x -> x * n
let krat3 = vytvorNasobicku 3   // vrátí novou funkci "x -> x * 3"
printfn "%d" (krat3 5)          // 15
```

### 3.1.3 Currying a parciální aplikace

- _Funkce s více parametry_ jsou ve skutečnosti **řetězec jednoparametrových funkcí** (curried by default)
- Lze je částečně aplikovat:

```
let add a b = a + b
let add5 = add 5       // parciální aplikace, add5 : int -> int
add5 10                // 15
```

## 3.2 Typový systém

### 3.2.1 Odvození typů

- F# kompilátor automaticky odvodí typy bez nutnosti je deklarovat:

```fsharp
let square x = x * x   // odvodí int -> int (podle použití)
```

- Na rozdíl od dynamicky typovaných jazyků je F# **staticky typovaný** – jen se typy nemusí vypisovat ručně (podobné `var` v C#, ale mnohem důslednější).

### 3.2.2 Pattern matching

- Moderní, výrazový způsob větvení kódu
- Nahrazuje komplikované if-else a switch řetězce.

```fsharp
match expr with
| pat1 -> result1
| pat2 -> result2
| pat3 when podmínka -> result3  // Guard podmínka
| _ -> defaultResult             // Wildcard — zachytí vše ostatní

// Příklad — Fibonacciho čísla
// rec = označní rekurzivní funkce
let rec fib n =
    match n with
    | 0 -> 0
    | 1 -> 1
    | _ -> fib (n - 1) + fib (n - 2)
```

- Pattern matching se vyhodnocuje **shora dolů** — první odpovídající větev vyhraje. Kompilátor upozorní na neúplný matching (chybějící případy).

### 3.2.3 N-tice (Tuples)

- Seskupení nepojmenovaných, ale seřazených hodnot různých typů:

```fsharp
let a = (1, 2)           // int * int
let b = (1, "text")      // int * string
let c = struct (1, 2)    // Hodnotová n-tice (struct tuple)
```

### 3.2.4 Záznamy (Records)

- Sdružení pojmenovaných hodnot (jak záznam v C#)
- Ve výchozím nastavení nemutovatelné

```fsharp
// Definice
type Website = { Title : string; Url : string }

// Vytvoření
let homepage = { Title = "Google"; Url = "http://www.google.com" }
```

### 3.2.5 Discriminated Union (DU)

> [!success]
> Datový typ, který může nabývat **právě jedné hodnoty** **z** předem daného **výčtu případů** — každý případ může mít jiný datový typ.

> [!note]
> Je to _takový hodně silnější enum_.

```fsharp
type Shape =
    | Circle of radius: float
    | Rectangle of width: float * height: float
    | Triangle of base: float * height: float

let k = Circle 5.0
let o = Rectangle(3.0, 4.0)
let t = Triangle(6.0, 2.0)
```

### 3.2.6 Option type

- _Předdefinovaný DU pro hodnot_y, které **mohou chybět** — bezpečná náhrada za `null`:

```fsharp
let safediv x y =
  match y with
  | 0 -> None
  | _ -> Some (x / y)

let tryDivide a b =
    if b = 0 then None
    else Some (a / b)
```

### 3.2.7 Pipe operátor `|>`

- Umožňuje _řetězit funkce zleva doprava_ – čitelnější než vnořené volání:

```fsharp
[1; 2; 3; 4; 5]
|> List.filter (fun x -> x % 2 = 0)
|> List.map (fun x -> x * x)
|> List.sum
```

- Podobné metodovým řetězcům v LINQ

### 3.2.8 Seznamy (Lists)

- **Neměnná (immutable) kolekce** prvků stejného typu.
- Vhodné pro rekurzi a funkcionální zpracování dat.

```
let numbers = [1; 2; 3; 4]

let doubled =
    numbers
    |> List.map (fun x -> x * 2)

let even =
    numbers
    |> List.filter (fun x -> x % 2 = 0)
```

### 3.2.9 Pole (Arrays)

- **Měnitelná (mutable) kolekce** prvků stejného typu.
- Umožňuje rychlý přístup pomocí indexu.

```
let arr = [|1; 2; 3|]
arr[0] <- 10
printfn "%A" arr
```

### 3.2.10 Cykly

- F# preferuje **rekurzi** a funkce, ale podporuje i klasické cykly.

```
for i = 1 to 5 do
    printfn "%d" i

let mutable i = 0

while i < 5 do
    printfn "%d" i
    i <- i + 1
```

### 3.2.11 Výjimky v F#

```fsharp
// Definice vlastní výjimky
exception InnerError of string
exception OuterError of string

// try-with (nelze kombinovat s finally ve stejném bloku!)
try
    raise (InnerError "chyba")
with
    InnerError msg -> printfn "Inner: %s" msg

// try-finally (samostatný blok)
try
    // kód
finally
    printfn "Vždy se provede"

// Kombinace: try-with uvnitř try-finally
try
    try
       raise (InnerError "x")
    with
       InnerError msg -> printfn "Chyba: %s" msg
finally
    printfn "Cleanup"
```

### 3.2.12 Interoperabilita F# s C#

- F# kód lze volat z C# projektu a naopak:

```csharp
// F# knihovna (modul)
module Arithmetic
let add x y = x + y
let sub x y = x - y
let rec fac = function
    | 0 | 1 -> 1
    | n -> n * fac (n - 1)
```

```csharp
// C# projekt odkazující na F# knihovnu
// F# funkce jsou dostupné jako statické metody
int result = Arithmetic.add(3, 4);    // = 7
int factorial = Arithmetic.fac(5);   // = 120
```

> [!info]
> **Postup:** Vytvořit F# Class Library projekt → přidat referenci do C# projektu (Add → Project Reference).

# 4. Porovnání

| **C#** | **F#** |
| --- | --- |
| **Object-oriented first** | **Functional-first** |
| Základem jsou **třídy a objekty** | Základem jsou **funkce** |
| Data bývají často **měnitelná (mutable)** | Data jsou ve výchozím stavu **neměnitelná (immutable)** |
| Pro větvení se používá hlavně `if`, `switch` | Často se používá **pattern matching** |
| Iterace pomocí `for`, `foreach`, `while` | Preferuje **rekurzi** a funkce nad kolekcemi (`map`, `filter`, `fold`) |
| Typy se často zapisují explicitně | Typy se většinou **odvozují automaticky** |
| Typické datové struktury jsou **class**, `struct`, `interface` | Typické jsou **recordy** a **discriminated unions** |
| Vedlejší efekty jsou běžné | Preferují se čisté funkce bez vedlejších efektů |
| Snadnější pro klasické OOP aplikace | Vhodný pro výpočty, transformace dat a paralelní zpracování |
| Podporuje i funkcionální prvky (LINQ, lambda) | Podporuje i OOP a imperativní programování |