## Zapouzdření:

 **Zapouzdření** je mechanismus, který umožňuje skrýt určité části třídy a umožnit přístup k nim pouze pomocí definovaného rozhraní. Tím se minimalizuje přímý přístup k datům třídy ze strany vnějšího kódu a snižuje se riziko neoprávněné manipulace s daty.

```Python
class Car:
    def __init__(self, brand):
        self.__brand = brand  # Privátní atribut
        
    def get_brand(self):  # Getter pro získání hodnoty privátního atributu
        return self.__brand
    
    def set_brand(self, brand):  # Setter pro nastavení hodnoty privátního atributu
        self.__brand = brand

# Použití getteru a setteru
car = Car("Toyota")
print(car.get_brand())  # Výstup: Toyota

car.set_brand("Honda")
print(car.get_brand())  # Výstup: Honda
```

## Polymorfismus:

**Polymorfismus** umožňuje třídě mít více metod se stejným názvem, ale jiným chováním. To umožňuje různým třídám poskytnout různé implementace stejného konceptu.

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

 **Dědičnost** umožňuje třídě získat atributy a metody jiné třídy. Třída, která dědí, se nazývá potomkem (podtřída), zatímco třída, ze které dědí, se nazývá rodičem (nadřazená třída).

```Python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Zvuk zvířete"

    def introduce(self):
        return f"Jmenuji se {self.name}."


class Dog(Animal):
    def sound(self):
        return "Haf"


class Cat(Animal):
    def sound(self):
        return "Mňau"


dog = Dog("Buddy")
print(dog.introduce())  # Výstup: Jmenuji se Buddy.

cat = Cat("Fluffy")
print(cat.introduce())  # Výstup: Jmenuji se Fluffy.

print(cat.sound())  # Výstup: Mňau
print(dog.sound())  # Výstup: Haf
```


##### Navigace
Předchozí:  [[Základy objektového programování - třídy, objekty zasílání zpráv]]
Následující: [[Události v objektovém programování]]
Celý okruh: [[3. Programovací jazyky a programování]]