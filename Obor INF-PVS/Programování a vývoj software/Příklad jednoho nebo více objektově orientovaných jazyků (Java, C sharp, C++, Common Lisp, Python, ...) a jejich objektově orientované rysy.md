*Změna názvu u C# z důvodu problémů v Obsidianu.*
## Obecné hlavní rysy
1) Zapouzdření
2) Dědičnost
3) Polymorfismus
4) Abstrakce
- více v [[Objektově orientované programování - třídy a objekty, zprávy a metody]]
## Python a OOP
- multiparadigmatický a dynamicky typovaný jazyk
- z hlediska organizace kódu je každá třída umístěna v samostatném modulu se stejným názvem
- jako jeden z mála jazyků podporuje vícenásobnou dědičnost
	- diamantový problém řeší několika způsoby
		- používá tzv. **Method Resolution Order** pro hledání správné definice metody
		1) metoda přepsána v obou předcích - záleží na pořadí uvedení rodičů `class Class4(Class2, Class3)`
		2) přepsána pouze v jednom - rodiči používá "nejbližší" metodu
- definice pomocí klíčového slova `class`
```Python
class Person:
	# Konstruktor
 	def __init__(self, name, age):
 		self.name = name
 		self.age = age

	# Metoda
 	def greet(self):
 	print(f"Hello, my name is {self.name}. I am {self.age}y. old.")
``` 

- vytvoření instance třídy probíhá metodou `__init__()`
- narozdíl od běžně známých pravidel obvykle v Pythonu nevytváříme settery ani gettery a k vlastnostem přistupujeme napřímo přes tečkovou notaci `honza.age`
	- pokud chceme metodu udělat "privátní" začíná její název podtržítkem `_greet()`
- metoda `super()` umožňuje přístup k metodám předků, od nichž třída dědí
#### Dunder metody
- specifická záležitost Pythonu
- pomocí nich implementujeme vestavěnou funkcionalitu 
	- např. `__repr__` a `__str__` implementujeme `repr()` a `str()`
- existuje široký výčet těchto metod (celý k nalezení [zde](https://docs.python.org/3/reference/datamodel.html#basic-customization))
- doporučuje se užívat tohoto způsobu implementace než si pro ony metody zavádět vlastní názvy
## C\# a OOP
```Csharp
class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public void Display()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}");
    }
}

Person person = new Person();
person.Name = "John";
person.Age = 30;
person.Display() // Output: Name: John, Age: 30
```
- vstupním bodem programu je metoda `Main` (musí být deklarována uvnitř třídy/struktury)
- členy třídy může být řada entit
	- Pole
	- Konstanty
	- Vlastnosti
	- Metody
	- Konstruktory
	- Události
	- Finalizační metody
	- Indexery
	- Operátory
	- Vnořené typy
#### Metody
- existuje několik typů přístupnosti metod
	- `public`
	- `protected`
	- `internal`
	- `protected internal`
	- `private` (výchozí)
	- `private protected`
#### Dědičnost
- s vyjímkou vícenásobné funguje běžně
- třídu můžeme označit jako `abstract`, tzn. některé její metody nemusí mít implementaci (také abstraktní metody) a třída slouží jako předek pro jiné třídy (není zamýšleno vytvářet přímo její instance)
- opakem je klíčové slovo `sealed`, které zakazuje ostatním třídám od této dědit
#### Rozhraní (interface)
- tvoří předpis/definic, kterou musí (neabstraktní) třída jež tohoto rozhraní implementuje splnit
```C#
interface IEquatable<T>
	{ 
		bool Equals(T obj);
	}
```
#### Statická třída
- není možné pro vytvoření instance použít slovo `new`
- pouze jediná instance se vytvoří při načítání programu do paměti, kterou potom je možné použít
- je označena jako `sealed`
## Lisp a OOP
- realizuje CLOS (common lisp object system)
- umožňuj vícenásobnou dědičnost
- základní pojmy
	- `defclass` ... vytvoří třídu
	- `make-instace` ... vytvoří instanci třídy
	- `defmethod` ... definuje metodu
- umožňuje některá implicitní nastavení OOP předefinovat programátorem