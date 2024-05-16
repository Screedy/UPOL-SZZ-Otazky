## Zapouzdření
 - **Zapouzdření** je mechanismus, který umožňuje skrýt určité části třídy a umožnit přístup k nim pouze pomocí definovaného rozhraní.
 - Tím se minimalizuje přímý přístup k datům třídy ze strany vnějšího kódu a snižuje se riziko neoprávněné manipulace s daty.

```Python
class Car:
    def __init__(self, brand):
        self._brand = brand  # Privátní atribut

	@property
    def brand(self):  # Getter pro získání hodnoty privátního atributu
        return self._brand

	@brand.setter
    def brand(self, brand):  # Setter pro nastavení hodnoty privátního atributu
        self._brand = brand

# Použití getteru a setteru
car = Car("Toyota")
print(car.brand)  # Výstup: Toyota

car.brand = "Honda"
print(car.brand)  # Výstup: Honda
```

## Polymorfismus:
- Polymorfismus umožňuje použití stejných metod na objektech různých tříd.
- Python podporuje polymorfismus prostřednictvím dědičnosti a přepisování metod.

```Python
class Animal:
    def sound(self):
        pass

class Dog(Animal):    # Třídy dědí
    def sound(self):
        return "Woof"

class Cat(Animal):    # Třídy dědí
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.sound())  # Výstup: Woof
print(cat.sound())  # Výstup: Meow
```

## Dědičnost:
 - Dědičnost umožňuje vytvoření nové třídy na základě existující třídy. 
 - Nová třída dědí atributy a metody základní třídy.
 - Třída, která dědí, se nazývá potomkem, zatímco třída, ze které dědí, se nazývá rodičem.

```Python
class ElektrickeAuto(Auto):
    def __init__(self, znacka, model, rok, kapacita_baterie):
        super().__init__(znacka, model, rok)  # Volání konstruktoru třídy Auto
        self.kapacita_baterie = kapacita_baterie

    def popis_baterie(self):
        return f"Kapacita baterie: {self.kapacita_baterie} kWh"

# Vytvoření objektu třídy ElektrickeAuto
elektro_auto = ElektrickeAuto("Tesla", "Model 3", 2020, 75)

# Volání metod na objektu ElektrickeAuto
print(elektro_auto.popis())  # Výstup: Tesla Model 3, 2020
print(elektro_auto.popis_baterie())  # Výstup: Kapacita baterie: 75 kWh
```

##### Navigace
Předchozí:  [[Základy objektového programování - třídy, objekty zasílání zpráv]]
Následující: [[Události v objektovém programování]]
Celý okruh: [[3. Programovací jazyky a programování]]