Funkce vyšších řádů jsou mocným nástrojem v Pythonu, který umožňuje provádět operace na kolekcích dat, jako jsou seznamy, slovníky nebo n-tice, elegantním a efektivním způsobem.

## Mapování (`map()`)
Funkce `map()` aplikuje danou funkci na každý prvek v zadané sekvenci (seznamu, n-tici atd.) a vrátí iterátor obsahující výsledky.

```python
# Příklad: Vynásobení každého prvku seznamu číslem 2
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
doubled_list = list(doubled)  # [2, 4, 6, 8, 10]
```

## Filtrování (`filter()`)
Funkce `filter()` vybírá prvky z dané sekvence, které splňují zadanou podmínku, definovanou funkcí.
```Python
# Příklad: Vynásobení každého prvku seznamu číslem 2
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
doubled_list = list(doubled)  # [2, 4, 6, 8, 10]
```

## Redukce (`reduce()`)
Funkce `reduce()` postupně aplikuje zadanou binární funkci k prvkům sekvence a vrátí jedinou hodnotu.
```Python
from functools import reduce

# Příklad: Součet všech prvků seznamu
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)  # 15
```

## Anonymní funkce
Anonymní funkce, často nazývané lambda funkce, jsou malé funkce, které můžete definovat na místě a použít je tam, kde jsou potřeba.
```Python
# Příklad: Lambda funkce pro násobení dvou čísel
multiply = lambda x, y: x * y
result = multiply(3, 4)  # 12

```