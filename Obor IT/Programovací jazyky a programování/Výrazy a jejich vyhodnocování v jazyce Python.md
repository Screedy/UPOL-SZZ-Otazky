- Výrazy (expressions) jsou kombinace hodnot a operátorů, které Python vyhodnocuje s cílem získat novou hodnotu. Například `3 * (5 + 2)`.

## Typy výrazů

- **Aritmetické výrazy**
	- Aritmetické výrazy používají aritmetické operátory k provádění matematických výpočtů.
	- `+`, `-`, `*`, `/`, `//`, `%`, `**`

>[!Example]- aritmetické výrazy
>```python
>a = 10
>b = 5
>
># Sčítání
>print(a + b)  # Výsledek: 15
># Odčítání
>print(a - b)  # Výsledek: 5
># Násobení
>print(a * b)  # Výsledek: 50
># Dělení
>print(a / b)  # Výsledek: 2.0
># Celé dělení
>print(a // b)  # Výsledek: 2
># Zbytek po dělení
>print(a % b)  # Výsledek: 0
># Mocnina
>print(a ** b)  # Výsledek: 100000
>```

- **Logické výrazy**
	- Logické výrazy používají logické operátory k provádění logických operací.
	- `and`, `or`, `not`

>[!Example]- logické výrazy
>```python
>x = True
>y = False
>
># And
>print(x and y)  # Výsledek: False
># Or
>print(x or y)  # Výsledek: True
># Not
>print(not x)  # Výsledek: False
>```

- **Porovnací výrazy**
	- Porovnávací výrazy používají porovnávací operátory k porovnávání hodnot.
	- `==`, `!=`, `<`, `>`, `<=`, `>=`

>[!Example]- porovnávací výrazy
>```python
>a = 10
>b = 5
>
># Rovná se
>print(a == b)  # Výsledek: False
># Nerovná se
>print(a != b)  # Výsledek: True
># Větší než
>print(a > b)  # Výsledek: True
># Menší než
>print(a < b)  # Výsledek: False
># Větší nebo rovno
>print(a >= b)  # Výsledek: True
># Menší nebo rovno
>print(a <= b)  # Výsledek: False
>```

- **Řetězcové výrazy**
	- Řetězcové výrazy umožňují manipulaci s řetězci.
	- `+`, `*`

>[!Example]- řetězové výrazy
>```python
>s1 = "Hello"
>s2 = "World"
>
># Konkatenace
>print(s1 + " " + s2)  # Výsledek: "Hello World"
># Násobení
>print(s1 * 3)  # Výsledek: "HelloHelloHello"
>```

- **Výrazy se seznamy a jinými datovými typy**
	- Python podporuje výrazy, které manipulují s různými datovými typy, jako jsou seznamy, n-tice, slovníky a množiny.

>[!Example]- výrazy se seznamy
>```python
># Seznamy
>list1 = [1, 2, 3]
>list2 = [4, 5, 6]
># Spojování seznamů
>print(list1 + list2)  # Výsledek: [1, 2, 3, 4, 5, 6]
># Opakování seznamu
>print(list1 * 2)  # Výsledek: [1, 2, 3, 1, 2, 3]
>
># N-tice
>tuple1 = (1, 2, 3)
>tuple2 = (4, 5, 6)
># Spojování n-tic
>print(tuple1 + tuple2)  # Výsledek: (1, 2, 3, 4, 5, 6)
>
># Slovníky
>dict1 = {"a": 1, "b": 2}
>dict2 = {"c": 3, "d": 4}
># Sloučení slovníků (Python 3.9+)
>print({**dict1, **dict2})  # Výsledek: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>
># Množiny
>set1 = {1, 2, 3}
>set2 = {3, 4, 5}
># Sjednocení množin
>print(set1 | set2)  # Výsledek: {1, 2, 3, 4, 5}
># Průnik množin
>print(set1 & set2)  # Výsledek: {3}
>```

- **Bitové operátory**
	- umožňují manipulaci s jednotlivými bity čísel
	- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (bitový posun vlevo), `>>` (bitový posun vpravo)

>[!Example]- bitový posun
>```python
>a = 3  # 3 v binární soustavě:  0011
>result = a << 2  # Výsledek: 12 (v binární soustavě: 1100)
>
>print(result)  # Výsledek: 12
>```

## Priorita operátorů
- Python vyhodnocuje výrazy na základě priority operátorů.
- `*` a `/` mají vyšší prioritu než `+` a `-`. Tedy `*` a `/` bude vyhodnoceno dříve.
- Pomocí závorek `()` můžeme změnit pořadí vyhodnocování operací.

>[!Example]- priorita operátorů
>```python
>a = 2 + 3 * 4  # Násobení má vyšší prioritu než sčítání
>print(a)  # Výsledek: 14
>
>b = (2 + 3) * 4  # Závorky mají nejvyšší prioritu
>print(b)  # Výsledek: 20
>```

## Vyhodnocování výrazů
- Když Python narazí na výraz, začne jej vyhodnocovat od nejvyšší priority operátoru k nejnižší.
- Pokud narazí na dva operátory se stejnou prioritou, vyhodnocuje se zleva doprava (s výjimkou exponenciály, která se vyhodnocuje zprava doleva).

## Vyhodnocení podmínek
- Python umožňuje vyhodnocování podmínek pomocí konstrukcí jako `if`-`else` výrazy. Tyto výrazy umožňují rozhodnutí na základě logických podmínek.


##### Navigace
Předchozí:  [[Řízení vykonávání programu v jazyce Python - bloky, cykly, větvení, funkce]]
Následující: [[Základní datové typy v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]