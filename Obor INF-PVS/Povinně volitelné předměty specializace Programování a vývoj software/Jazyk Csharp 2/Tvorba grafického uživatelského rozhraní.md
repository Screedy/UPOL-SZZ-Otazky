## Práce s konzolí
#### Vstup od uživatele
- Čtení textového vstupu:
```csharp
string vstup = Console.ReadLine();
```

- Příklad čtení číselného vstupu s ošetřením výjimky:
```csharp
static void ReadNumber(out int a, string text) {
    Console.Write(text);
    string input = Console.ReadLine();
    try {
        a = int.Parse(input);
    } catch (Exception) {
        ReadNumber(out a, text);
    }
}
```

#### Změna vzhledu konzole
```csharp
Console.BackgroundColor = ConsoleColor.Green;
Console.ForegroundColor = ConsoleColor.Red;
Console.ResetColor();
Console.Clear();
Console.SetWindowSize(80, 25);
Console.Title = "Moje aplikace";
```

#### Reakce na stisk klávesy
```csharp
ConsoleKeyInfo info = Console.ReadKey();
if (info.Key == ConsoleKey.Backspace) {
    Console.WriteLine("Zmáčkl backspace");
}
```


## WPF application
- *Windows presentation foundation*
- Už z názvu vyplývá, že není multiplatformní
- Je to klikací editor (případně pak můžeme upravit v XML)
- Poskytuje řadu prvků
	- Dialogy
	- CheckBox
	- ComboBox
	- TextBox
- Určitě používat vhodnou architekturu (např. [[Návrhové vzory a vzory architektur SW#MVVM - model view viewmodel|MVVM]])
#### Kreslení ve WPF
- **Canvas panel**
	- Absolutní pozicování prvků
	- Počátek souřadnic je v levém horním rohu
	- Osa $x$ roste zleva doprava, osa $y$ shora dolů
- **Shape**
	- Nadtřída pro grafické objekty

### Základní grafické objekty
#### Rectangle
- Parametry `Height` a `Width`, `RadiusX` a `RadiusY` je poloměr zaoblení rohů
- Pozice se určí při vložení do `Canvas`
#### Ellipse
- Parametry `Height` a `Width`
- Pozice opět až při vložení do `Canvas`
#### Polygon
- `Points` je seznam jeho bodů
### Kreslení textu
#### Třída `TextBlock`

```c#
TextBlock tb = new TextBlock();
tb.Text = "Toto je nějaký napsaný text";
canvas.Children.Add(tb);
Canvas.SetLeft(tb, 270);
Canvas.SetTop(tb, 60);
```

- Přidání objektu do plátna probíhá následovně
```c#
Line line = new Line();
line.Stroke = Brushes.Red;
line.X1 = 50;
line.Y1 = 50;
line.X2 = 150;
line.Y2 = 50;
line.StrokeThickness = 5;
line.ToolTip = "Nějaký tooltip";
line.Cursor = Cursors.Hand;
canvas.Children.Add(line);
```

- Nastavení událostí (delegát)
```c#
line.MouseDown+= delegate { MessageBox.Show("Bylo kliknuto!"); };
```

## WinForms
- Nejstarší způsob
- Pro klasické desktopové Windows aplikace
- Formuláře a ovládací prvky
- `Form` je objekt, z které se dědí
- Nepoužívá XML

## MAUI
- *Multiplatform App UI*
- Multiplatformní rozhraní pro tvorbu mobilních a desktopových aplikací
- Nejvíce moderní
- Používá `XAML` a `C#`
- Vrstvy MAUI
	- ![[Pasted image 20250525203208.png]]
- Podporuje funkci *hot reload*
- Uživatelské rozhraní opět představuje XAML
```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="Notes.AboutPage">
    <VerticalStackLayout Spacing="10" Margin="10">
        <HorizontalStackLayout Spacing="10">
            <Image Source="dotnet_bot.png"
                   SemanticProperties.Description="The dot net bot waving hello!"
                   HeightRequest="64" />
            <Label FontSize="22" FontAttributes="Bold" Text="Notes" VerticalOptions="End" />
            <Label FontSize="22" Text="v1.0" VerticalOptions="End" />
        </HorizontalStackLayout>

        <Label Text="This app is written in XAML and C# with .NET MAUI." />
        <Button Text="Learn more..." Clicked="LearnMore_Clicked" />
    </VerticalStackLayout>
</ContentPage>
```
- Backend se zpracovává v běžných `.cs` souborech
- Doporučuje se používat např. `MVVM` architekturu
- Poskytuje předdefinované komponenty pro různé účely - tlačítka, layout, ...


- Pro všechny zmíněné způsoby existuje ve Visual Studio možnost vytvořit onu aplikaci se všemi potřebnými souvislostmi do začátku vývoje