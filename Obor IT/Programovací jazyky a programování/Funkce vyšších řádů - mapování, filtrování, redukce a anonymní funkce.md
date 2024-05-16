- Funkce vyšších řádů jsou funkce, které buď přijímají jako argumenty jiné funkce, nebo je vracejí.
- Python poskytuje několik vestavěných funkcí vyššího řádu, jako jsou `map()`, `filter()`, a také podporuje anonymní funkce pomocí `lambda`.
- Funkce `reduce()` musí být importována přes modul `functools`

## Mapování (`map()`)
- Funkce `map()` aplikuje danou funkci na každý prvek iterovatelného objektu (seznamu, n-tici, ...) a vrací iterátor s výsledky.

>[!Example] funkce `map()`
>```python
>numbers = [1, 2, 3, 4, 5]
>squared = map(lambda x: x ** 2, numbers)
>
>print(list(squared))  # Výstup: [1, 4, 9, 16, 25]
>```

## Filtrování (`filter()`)
- Funkce `filter()` aplikuje danou funkci na každý prvek iterovatelného objektu a vrací iterátor s prvky, pro které funkce vrátí `True`.

>[!Example] funkce `filter()`
>```python
>numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>even_numbers = filter(lambda x: x % 2 == 0, numbers)
>
>print(list(even_numbers))  # Výstup: [2, 4, 6, 8, 10]
>```

## Redukce (`reduce()`)
Funkce `reduce()` postupně aplikuje zadanou binární funkci k prvkům sekvence a vrátí jedinou hodnotu.

- Funkce `reduce()` aplikuje danou funkci kumulativně na prvky iterovatelného objektu, odleva doprava, aby se zredukovaly na jednu hodnotu. 
- `reduce()` není vestavěná funkce a musí být importována z modulu `functools`.

```Python
from functools import reduce

# Příklad: Součet všech prvků seznamu
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)  # 15
```

## Anonymní funkce
- Anonymní funkce jsou malé, jednorázové funkce, které nemusí být definovány pomocí klíčového slova `def`.

>[!Example] normální vs lambda funkce
>```python
># Normální funkce
>def add(x, y):
> 	return x + y
>
># Lambda funkce
>add_lambda = lambda x, y: x + y
>
>print(add(3, 5))        # Výstup: 8
>print(add_lambda(3, 5))  # Výstup: 8
>```

##### Navigace
Předchozí:  [[Události v objektovém programování]]
Následující: [[Rekurze a rekurzivní datové struktury (spojové seznamy, stromy)]]
Celý okruh: [[3. Programovací jazyky a programování]]