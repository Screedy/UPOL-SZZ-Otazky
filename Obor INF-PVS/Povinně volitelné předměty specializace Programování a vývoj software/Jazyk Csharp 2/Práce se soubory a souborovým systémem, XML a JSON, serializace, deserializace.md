## Třída `DirectoryInfo`
- Třída `DirectoryInfo` slouží k práci se složkami.

```csharp
DirectoryInfo di = new DirectoryInfo("E:\1\");
```

#### Metody:
- `EnumerateFiles()`, `EnumerateDirectories()` – výčet bez načtení všech dat najednou (lazy)
- `GetFiles()`, `GetDirectories()` – načte vše do paměti

#### Atributy:
Používá `FileAttributes` (např. `Hidden`, `ReadOnly`, `System`, `Directory`, ...)

## Třída `FileInfo`
- Třída `FileInfo` reprezentuje soubor a umožňuje s ním provádět různé operace.

```csharp
FileInfo fi = new FileInfo("E:\1\test.txt");
```
- Lze získat cestu, název, velikost, datum vytvoření, upravit obsah apod.

## Třída `DriveInfo`
- Třída pro získání informací o discích v systému.
```csharp
DriveInfo[] disky = DriveInfo.GetDrives();
```

#### Informace:
- Název disku (`Name`)
- Typ disku (`DriveType`) – např. `Fixed`, `Removable`, `Network`
- Volné a celkové místo

## Čtení souboru – statická třída `File`
#### Načtení celého obsahu
```csharp
string obsah = File.ReadAllText(path);
```

#### Načtení jako pole řádků
```csharp
string[] radky = File.ReadAllLines(path);
```

## Práce s proudy (Streams)
- Stream (viz [[Líné vyhodnocování v datových strukturách, přísliby a proudy]]) je obecný koncept pro čtení a zápis dat z/na různé zdroje: soubor, síť, paměť.

#### Čtení pomocí `StreamReader`:
```csharp
using (StreamReader sr = new StreamReader(path)) {
    string radek;
    while ((radek = sr.ReadLine()) != null) {
        Console.WriteLine(radek);
    }
}
```

## Zápis do souboru

#### Textový zápis pomocí `StreamWriter`:
```csharp
using (StreamWriter sw = new StreamWriter(File.Create(path))) {
    sw.WriteLine("Řádek 1");
}
```

#### Komprimovaný zápis – `GZipStream`:
```csharp
using GZipStream gzs = new GZipStream(File.Create("soubor.gzip"), CompressionLevel.Optimal);
using StreamWriter sw = new StreamWriter(gzs);
sw.WriteLine("Komprimovaná data");
```

#### Binární zápis – `BinaryWriter`
- Pro **efektivní** uložení čísel, znaků, struktur apod.  
- Zapisuje se přímo binární reprezentace:
```csharp
using BinaryWriter bw = new BinaryWriter(File.Create("soubor.dat"));
bw.Write(0.33f); // rozdíl mezi float a double zápisem
```
- Výsledný soubor není čitelný v textovém editoru, ale je prostorově úspornější.

## Čtení XML pomocí `XmlDocument`
- Pro čtení XML lze využít přístup přes DOM (Document Object Model).

#### Ukázkový XML vstup:
```xml
<items>
  <item att1="foo" att2="bar">
    <number>25</number>
    <str>Some string</str>
  </item>
</items>
```

#### Zpracování XML:
```csharp
XmlDocument doc = new XmlDocument();
doc.Load("in.xml");
XmlNodeList nodes = doc.GetElementsByTagName("item");

foreach (XmlNode node in nodes) {
    foreach (XmlNode child in node.ChildNodes) {
        Console.WriteLine($"{child.Name}: {child.InnerText}");
    }

    foreach (XmlAttribute att in node.Attributes) {
        Console.WriteLine($"{att.Name} = {att.Value}");
    }
}
```

## Zápis XML
- Stromová konstrukce XML a zápis do souboru:
```csharp
XmlDocument doc = new XmlDocument();
XmlDeclaration declaration = doc.CreateXmlDeclaration("1.0", "UTF-8", null);
doc.AppendChild(declaration);

XmlElement item = doc.CreateElement("item");
item.SetAttribute("att1", "value1");
item.SetAttribute("att2", "value2");

XmlElement number = doc.CreateElement("number");
number.InnerText = "123";
item.AppendChild(number);

XmlElement str = doc.CreateElement("str");
str.InnerText = "text";
item.AppendChild(str);

doc.AppendChild(item);

XmlTextWriter writer = new XmlTextWriter("out.xml", Encoding.UTF8);
writer.Formatting = Formatting.Indented;
doc.WriteContentTo(writer);
writer.Close();
```

## Serializace do XML
- Serializace je konvertování objektu do proudu bytů a následné uložení
- Serializace umožňuje převod objektu do XML
```csharp
public class Item {
    public int Number { get; set; }
    public string Str { get; set; }
    public int[] Numbers { get; set; }
}

Item i = new Item { Number = 42, Str = "text", Numbers = new[] { 1, 2, 3 } };
XmlSerializer serializer = new XmlSerializer(typeof(Item));
using TextWriter writer = new StreamWriter("item.xml");
serializer.Serialize(writer, i);
```
## Deserializace z XML
- Načtení dat ze souboru zpět do objektu
```csharp
XmlSerializer serializer = new XmlSerializer(typeof(Item));
using FileStream fs = new FileStream("item.xml", FileMode.Open);
Item deserialized = (Item)serializer.Deserialize(fs);
```

## Formát JSON
- JSON je textový formát pro výměnu dat, např.
```json
{
  "jmeno": "Tomáš",
  "prijmeni": "Novák",
  "rocnik": 2
}
```

#### Serializace do JSON (`System.Text.Json`)
```csharp
Item obj = new Item { Number = 42, Str = "text", Numbers = new[] { 1, 2, 3 } };
string json = JsonSerializer.Serialize(obj);
```

#### Deserializace z JSON
```csharp
string json = "{"Number":42,"Str":"text","Numbers":[1,2,3]}";
Item obj = JsonSerializer.Deserialize<Item>(json);
```
