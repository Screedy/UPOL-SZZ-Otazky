## DirectoryInfo

Třída `DirectoryInfo` slouží k práci se složkami.

### Příklad:
```csharp
DirectoryInfo di = new DirectoryInfo("E:\1\");
```

### Metody:
- `EnumerateFiles()`, `EnumerateDirectories()` – výčet bez načtení všech dat najednou (lazy)
- `GetFiles()`, `GetDirectories()` – načte vše do paměti

### Atributy:
Používá `FileAttributes` (např. `Hidden`, `ReadOnly`, `System`, `Directory`, ...)

---

## FileInfo

Třída `FileInfo` reprezentuje soubor a umožňuje s ním provádět různé operace.

```csharp
FileInfo fi = new FileInfo("E:\1\test.txt");
```

Lze získat cestu, název, velikost, datum vytvoření, upravit obsah apod.

---

## DriveInfo

Třída pro získání informací o discích v systému.

```csharp
DriveInfo[] disky = DriveInfo.GetDrives();
```

### Informace:
- Název disku (`Name`)
- Typ disku (`DriveType`) – např. `Fixed`, `Removable`, `Network`
- Volné a celkové místo

---

## Čtení souboru – statická třída `File`

### Načtení celého obsahu
```csharp
string obsah = File.ReadAllText(path);
```

### Načtení jako pole řádků
```csharp
string[] radky = File.ReadAllLines(path);
```

---

## Práce s proudy (Streams)

Stream je obecný koncept pro čtení a zápis dat z/na různé zdroje: soubor, síť, paměť.

### Čtení pomocí `StreamReader`:
```csharp
using (StreamReader sr = new StreamReader(path)) {
    string radek;
    while ((radek = sr.ReadLine()) != null) {
        Console.WriteLine(radek);
    }
}
```

---

## Zápis do souboru

### Textový zápis pomocí `StreamWriter`:
```csharp
using (StreamWriter sw = new StreamWriter(File.Create(path))) {
    sw.WriteLine("Řádek 1");
}
```

### Komprimovaný zápis – `GZipStream`:
```csharp
using GZipStream gzs = new GZipStream(File.Create("soubor.gzip"), CompressionLevel.Optimal);
using StreamWriter sw = new StreamWriter(gzs);
sw.WriteLine("Komprimovaná data");
```

---

## Binární zápis – `BinaryWriter`

Pro efektivní uložení čísel, znaků, struktur apod.  
Zapisuje se přímo binární reprezentace:

```csharp
using BinaryWriter bw = new BinaryWriter(File.Create("soubor.dat"));
bw.Write(0.33f); // rozdíl mezi float a double zápisem
```

Výsledný soubor není čitelný v textovém editoru, ale je prostorově úspornější.

---

## Shrnutí

- `DirectoryInfo`, `FileInfo`, `DriveInfo` umožňují přístup k informacím o souborovém systému.
- Statická třída `File` poskytuje jednoduché API pro čtení/zápis.
- Proudy (`StreamReader`, `StreamWriter`, `BinaryWriter`) slouží pro efektivní práci se soubory.
- `GZipStream` umožňuje transparentní kompresi během zápisu.

