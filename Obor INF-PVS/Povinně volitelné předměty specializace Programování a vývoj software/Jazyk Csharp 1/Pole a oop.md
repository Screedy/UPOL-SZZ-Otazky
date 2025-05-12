## Práce s poli
- Pole v C# je datová struktura pro pevný počet prvků stejného datového typu. Délka pole je určena při jeho vytvoření a nelze ji později změnit.

### Deklarace a inicializace
```csharp
int[] pole = new int[] { 2, 4, 6 };
int[] jednodusiZapis = { 1, 3, 4, 6, 7 };
bool[] pBool = new bool[20];
```

### Přístup k prvkům a vlastnosti
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

### Iterace přes pole
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

## Vícedimenzionální pole
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

## Úvod do objektově orientovaného programování (OOP)
- Objektově orientované programování je hlavní paradigma jazyka C#. Program je tvořen objekty, které mají:
	- Stav (vlastnosti)
	- Chování (metody)
	- Možnost interakce
- Výhodou OOP je:
	- Snadná strukturalizace a údržba kódu
	- Možnost rozdělení vývoje mezi více programátorů
	- Rozšiřitelnost a znovupoužitelnost
#### Základní principy OOP
- **Zapouzdření** – oddělení vnitřní reprezentace od vnějšího rozhraní.
- **Dědičnost** – možnost odvození nové třídy z existující.
- **Polymorfismus** – schopnost volat stejné rozhraní s různým chováním.
- **Rozhraní objektů** – přesně definovaný způsob, jak s objektem komunikovat.

## Třídy v C\#
- Třída je šablona pro vytváření objektů. Obsahuje:
	- **Fields (polička)** – proměnné reprezentující stav objektu.
	- **Konstanty** – neměnné hodnoty, často `public static`.
	- **Metody** – operace prováděné objektem.
	- **Properties (vlastnosti)** – přístupové metody ke stavovým proměnným.
	- **Konstruktory** – speciální metody volané při vytvoření objektu.
	- **Destruktor** – volán při odstranění objektu (většinou spravován GC).
	- **Vnořené třídy** – třídy definované uvnitř jiné třídy.

#### Příklad definice třídy
```csharp
public class HardDiskDrive {
    public const string Name = "Hard disk drive";
    private uint capacity;
    private string manufacturer;
    private string partNumber;
    public uint BufferSize;
    public uint WriteSpeed;

    public string StoreName => manufacturer + partNumber;

    public uint GetFreeSpace() { ... }
    public bool WriteNumber(int number, uint position) { ... }
    public int ReadNumber(uint position) { ... }
    public void ParkReadHead() { ... }
}
```

#### Konstruktor
```csharp
public HardDiskDrive(uint capacity, string manufacturer, string partNumber, uint bufferSize, uint writeSpeed)
{
    this.capacity = capacity;
    this.manufacturer = manufacturer;
    this.partNumber = partNumber;
    BufferSize = bufferSize;
    WriteSpeed = writeSpeed;
}
```
- Vytvoření objektu:
```csharp
HardDiskDrive disk = new HardDiskDrive(1000000, "WD", "SX04210345", 1000, 10000);
```

## Volání metod a přetěžování
- Metody voláme pomocí tečkové notace:
```csharp
disk.WriteNumber(42, 42468);
```
- Třída může obsahovat více metod se stejným názvem, ale různými parametry – tzv. **přetěžování metod**.

## Statické metody
- Statické metody jsou volány bez nutnosti vytvářet instanci třídy. Příkladem je `Math.Sqrt(25)`. Používají se ke zpřístupnění obecné funkcionality spojené s třídou.
- Deklarace:
```csharp
public static double Vypocitej(...) { ... }
```
- Nejznámější statickou metodou je metoda `Main`, vstupní bod programu.
