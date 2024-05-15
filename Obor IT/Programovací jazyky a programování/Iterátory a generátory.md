
## Iterátory

Iterátory jsou objekty, které představují sekvenci dat. Každý iterátor má metodu `__next__()`, která vrací další prvek ze sekvence. Když jsou všechny prvky vyčerpány, vyvolá se výjimka `StopIteration`.

Příklad vytvoření iterátoru:
```Python
class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_iter = MyIterator([1, 2, 3, 4, 5])
for item in my_iter:
    print(item)  # Vypíše 1, 2, 3, 4, 5
```

## Generátory

Generátory jsou jednoduchým způsobem vytváření iterátorů v Pythonu. Jsou vytvářeny pomocí klíčového slova `yield`, které umožňuje funkcím vracet hodnoty postupně, místo aby vrátily vše najednou. To umožňuje generovat hodnoty na požádání, což šetří paměť a umožňuje práci s velkými datovými soubory nebo nekonečnými sekvencemi.

Příklad vytvoření generátoru:

```Python
def my_generator(data):
    for item in data:
        yield item * 2

gen = my_generator([1, 2, 3, 4, 5])
for item in gen:
    print(item)  # Vypíše 2, 4, 6, 8, 10
```

Generátory jsou užitečné v situacích, kdy potřebujete efektivně generovat velké množství dat nebo pracovat s nekonečnými sekvencemi. Jsou také často používány ve spojení s funkcemi jako `map()`, `filter()` a `reduce()` pro elegantní manipulaci s daty.

Generátor pro nekonečnou řadu:

```Python
def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

# Vytvoření instance generátoru
numbers_gen = infinite_numbers()

# Vypsání prvních deseti čísel z nekonečné řady
for _ in range(10):
    print(next(numbers_gen))  # Vypíše 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```


>[!note] Iterátory a generátory
>- **Každý generátor je iterátor**, ale ne každý iterátor je generátor.
>- Generátory poskytují jednodušší a kompaktnější způsob psaní iterátorů, protože automatizují vytváření metod `__iter__()` a `__next__()` a správu stavu.


##### Navigace
Předchozí:  [[Rekurze a rekurzivní datové struktury (spojové seznamy, stromy)]]
Následující: [[Synchronizace vláken - problém kritické sekce, zámky, semafory]]
Celý okruh: [[3. Programovací jazyky a programování]]