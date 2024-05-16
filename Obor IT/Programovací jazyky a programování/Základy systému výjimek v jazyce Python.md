- Výjimky v Pythonu jsou mechanismus pro **zpracování chyb**, které se vyskytnou **během běhu programu**
- Pomocí výjimek můžete reagovat na chyby, aniž byste museli program neustále kontrolovat na přítomnost chyb

## Try-Except blok

- Syntaxe bloku `try-except` umožňuje zachytit a zpracovat výjimku, která může nastat v určitém bloku kódu. 
- Pokud je v bloku `try` vyvolána výjimka, bude program pokračovat ve vykonávání bloku `except`.

>[!Example] Try-Except
>```Python
>try:
> 	result = 10 / 0 # Blok kódu, ve kterém může dojít k výjimce
>except ZeroDivisionError:
> 	# Zpracování výjimky
> 	print("Nelze dělit nulou!")
>```

- Blok `try-except` může být doplněn o blok `else`, který se vykoná pouze tehdy, když k výjimce nedojde.

>[!Example] Try-Except-Else
>```python
>try:
> 	x = int("42")
>except ValueError:
> 	print("Chyba: nelze převést řetězec na číslo.")
>else:
> 	print("Převod proběhl úspěšně.")
>```

- Blok `finally` může být použit k provedení kódu, který se vykoná vždy, bez ohledu na to, zda došlo k výjimce nebo ne. 
- Obvykle se v tomto bloku provádí kód pro uzavření souborů nebo uvolnění zdrojů.

>[!Example] Try-Except-Finally
>```Python
>try:
> 	file = open("example.txt", "r")
> 	content = file.read()
> 	print(content)
>except FileNotFoundError:
> 	print("Soubor nebyl nalezen.")
>finally:
> 	file.close()  # Uzavření souboru bez ohledu na výjimku
>```

## Typy výjimek
- Python má řadu zabudovaných výjimek pro různé typy chyb, například:
	- **ZeroDivisionError**: Vzniká při dělení nulou.
	- **FileNotFoundError**: Vzniká při pokusu o práci se souborem, který neexistuje.
	- **TypeError**: Vzniká při aplikaci operace na objekt nesprávného typu.
	- **ValueError**: Vzniká, když funkce dostane argument správného typu, ale s neplatnou hodnotou.
	- A další...

## Vytváření vlastních výjimek
- Kromě zabudovaných výjimek můžete také vytvářet vlastní výjimky podle potřeby pomocí dědění z třídy `Exception`.

>[!Example] Vytvoření výjimky
>```Python
>class CustomError(Exception):
> 	pass
>
>try:
> 	raise CustomError("Toto je vlastní výjimka.")
>except CustomError as e:
> 	print("Chyba:", e)
>```

## Použití klauzule `raise`
- Klauzule `raise` umožňuje explicitní vyvolání výjimky v libovolném bodě programu.

>[!Example] klauzule raise
>```Python
>x = -1
>if x < 0:
> 	raise ValueError("Hodnota musí být kladná.")
>```

##### Navigace
Předchozí:  [[Základní datové typy v jazyce Python]]
Následující: [[Typy chyb a jejich hledání v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]