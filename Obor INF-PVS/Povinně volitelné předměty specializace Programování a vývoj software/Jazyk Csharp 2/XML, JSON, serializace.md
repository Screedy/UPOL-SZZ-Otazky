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
- Serializace umožňuje převod objektu do XML:
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
- Načtení dat ze souboru zpět do objektu:
```csharp
XmlSerializer serializer = new XmlSerializer(typeof(Item));
using FileStream fs = new FileStream("item.xml", FileMode.Open);
Item deserialized = (Item)serializer.Deserialize(fs);
```

## Formát JSON
- JSON je textový formát pro výměnu dat, např.:
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

---
## Shrnutí
- `XmlDocument` umožňuje ruční manipulaci s XML.
- Serializace/deserializace zjednodušuje práci s objekty a jejich uložením.
- `System.Text.Json` poskytuje rychlý a efektivní způsob práce s JSON formátem.
