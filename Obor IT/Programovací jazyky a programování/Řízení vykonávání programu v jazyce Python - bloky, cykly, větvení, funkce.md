## **Blok kódu:**
- Bloky kódu v Pythonu jsou označeny **odsazením** (indentací).
- Všechny příkazy, které patří do stejného bloku **musí být odsazeny stejným počtem mezer nebo tabulátorů**.

>[!Example] blok kódu
>```python
>if True:
> 	print("Toto je součástí bloku if.")
> 	print("Tento řádek také.")
>print("Tento řádek je mimo blok if.")
>```

## **Větvení:**
- Větvení umožňuje provádění **různých bloků kódu na základě splnění podmínek**.
- Používá klíčová slova `if`, `elif` a `else`.

>[!Example] větvení
>```python
>x = 10
>if x > 0:
> 	print("x je kladné číslo.")
>elif x == 0:
> 	print("x je nula.")
>else:
> 	print("x je záporné číslo.")
>```

## **Cykly:**

- Cykly umožňují **opakování** určitých částí kódu.
- Používá se klíčová slova:
	- `for` - iteruje přes sekvenci (např. seznam, tuple, string) nebo jiné iterovatelné objekty
	- `while` - pokračuje v opakování bloku kódu, dokud je podmínka pravdivá

>[!Example] for cyklus
>```python
>for i in range(5):
> 	print(i)
>```

>[!Example] while cyklus
>```python
>i = 0
>while i < 5:
> 	print(i)
> 	i += 1
>```
- Cykly můžeme ovládat pomocí:
	- `break` - ukončí cyklus předčasně
	- `continue` - přeskočí aktuální iteraci a pokračuje další
## **Funkce:**

- Funkce jsou **bloky kódu**, které lze **opakovaně používat** a které mohou **přijímat vstupy** (parametry) a **vracet výstupy** (hodnoty).
- Definuje se pomocí klíčového slova `def`.
- `return` slouží k vrácení hodnoty z funkce. Pokud není uvedeno, funkce vrací `None`.

>[!Example] funkce
>```python
>def pozdrav(jmeno):
> 	print(f"Ahoj, {jmeno}!")
>
>pozdrav("Petr")
>```

>[!Example] funkce vracející hodnotu
>```python
>def soucet(a, b):
> 	return a + b
>
>vysledek = soucet(3, 5)
>print(vysledek)
>```

- Lambda funkce jsou malé anonymní funkce definované pomocí klíčového slova `lambda`.

>[!Example] anonymní funkce
>```python
>soucet = lambda a, b: a + b
>print(soucet(3, 5))
>```

##### Navigace
Předchozí:  
Následující: [[Výrazy a jejich vyhodnocování v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]