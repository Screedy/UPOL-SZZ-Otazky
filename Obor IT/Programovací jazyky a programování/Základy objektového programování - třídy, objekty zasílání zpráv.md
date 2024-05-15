## **Třída**:

Třída je šablona pro vytváření objektů. Definuje atributy (data) a metody (funkce) pro práci s objekty. V Pythonu se třída definuje pomocí klíčového slova `class`.

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

## **Objekt**:

Objekt je instance třídy. Vytváří se pomocí konstruktoru třídy (typicky metody `__init__()`). Každý objekt má své vlastní atributy a může volat metody třídy.

```Python
person1 = Person("Alice", 30)
person1.greet()  # Výstup: Hello, my name is Alice and I am 30 years old.
```

## Zasílání zpráv:

Zasílání zpráv (messaging) je základním konceptem v objektově orientovaném programování (OOP) a označuje proces volání metod objektů. Zde je zjednodušený popis toho, jak probíhá zasílání zpráv v OOP:

 **1. Identifikace objektu:**
Prvním krokem je identifikace objektu, kterému chceme poslat zprávu. Objekty jsou instance tříd obsahující data (atributy) a funkce (metody).

 **2. Volání metody:**
Poté, co je objekt identifikován, můžeme na něj "poslat zprávu" voláním jeho metody. To znamená vykonání určité akce nebo manipulaci s daty uvnitř objektu.

**3. Zpracování metody:**
Když je metoda volána, objekt přijme zprávu a provede kód přiřazený k dané metodě. To může zahrnovat manipulaci s atributy objektu nebo provádění dalších akcí.

**4. Výsledek:**
Po provedení kódu v metodě může být vrácen výsledek operace (pokud je to vhodné) nebo může být provedena jiná akce v souladu s logikou aplikace.
### Příklad:

Uvažujme jednoduchou třídu `Car`, která má metodu `drive()`:

```Python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def drive(self):
        print(f"{self.brand} {self.model} is driving.")
```

Pokud vytvoříme instanci této třídy a zavoláme její metodu `drive()`, proces zasílání zpráv proběhne následovně:

```Python
my_car = Car("Toyota", "Corolla")
my_car.drive()
```

1. **Identifikace objektu**: `my_car` je identifikován jako instance třídy `Car`.
2. **Volání metody**: Voláme metodu `drive()` na objektu `my_car`.
3. **Zpracování metody**: Objekt `my_car` přijímá zprávu a provádí kód v metodě `drive()`, tedy vypíše zprávu o tom, že auto jede.
4. **Výsledek**: Výstup bude "Toyota Corolla is driving.".

##### Navigace
Předchozí:  [[Moduly v jazyce Python a jejich importování]]
Následující: [[Principy objektového programování - zapouzdření, polymorfismus a dědičnost]]
Celý okruh: [[3. Programovací jazyky a programování]]