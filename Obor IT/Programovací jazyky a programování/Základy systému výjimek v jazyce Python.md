Výjimky jsou události, které narušují běžný průběh programu a mohou být způsobeny různými faktory, jako jsou chyby syntaxe, chybné vstupy nebo neexistující soubory.

## Try-Except blok:

Syntaxe bloku `try-except` umožňuje zachytit a zpracovat výjimku, která může nastat v určitém bloku kódu. Pokud je v bloku `try` vyvolána výjimka, bude se program pokračovat ve vykonávání bloku `except`.

```Python
try:
    # Blok kódu, ve kterém může dojít k výjimce
    result = 10 / 0
except ZeroDivisionError:
    # Zpracování výjimky
    print("Nelze dělit nulou!")
```

## Blok Finally:

Volitelný blok `finally` může být použit k provedení kódu, který se vykoná vždy, bez ohledu na to, zda došlo k výjimce nebo ne. Obvykle se v tomto bloku provádí kód pro uzavření souborů nebo uvolnění zdrojů.

```Python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Soubor nebyl nalezen.")
finally:
    file.close()  # Uzavření souboru bez ohledu na výjimku
```

## Typy výjimek:

Python má řadu zabudovaných výjimek pro různé typy chyb, například:

- **ZeroDivisionError**: Vzniká při dělení nulou.
- **FileNotFoundError**: Vzniká při pokusu o práci se souborem, který neexistuje.
- **TypeError**: Vzniká při aplikaci operace na objekt nesprávného typu.
- **ValueError**: Vzniká, když funkce dostane argument správného typu, ale s neplatnou hodnotou.
- A další...

## Vytváření vlastních výjimek:

Kromě zabudovaných výjimek můžete také vytvářet vlastní výjimky podle potřeby pomocí dědění z třídy `Exception`.

```Python
class CustomError(Exception):
    pass

try:
    raise CustomError("Toto je vlastní výjimka.")
except CustomError as e:
    print("Chyba:", e)
```

## Použití klauzule `raise`:

Klauzule `raise` umožňuje explicitní vyvolání výjimky v libovolném bodě programu.

```Python
x = -1
if x < 0:
    raise ValueError("Hodnota musí být kladná.")
```


##### Navigace
Předchozí:  [[Základní datové typy v jazyce Python]]
Následující: [[Typy chyb a jejich hledání v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]