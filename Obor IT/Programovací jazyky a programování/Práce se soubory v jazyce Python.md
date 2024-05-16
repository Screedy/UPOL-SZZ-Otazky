## Základní operace se soubory

### 1. Otevření souboru:
- Funkce `open()` se používá k otevření souboru. 
- Tato funkce vrací objekt souboru, který se používá k provádění operací na souboru.

>[!Example] otevření souboru
>```Python
>file = open("example.txt", "r")  # Otevření souboru pro čtení
>```

### 2. Čtení ze souboru:
- Metoda `read()` slouží k čtení obsahu souboru.

>[!Example] čtení celého souboru najednou
>```python
>with open('example.txt', 'r') as file:
> 	content = file.read()
> 	print(content)
>```

>[!Example] čtení po řádcích
>```python
>with open('example.txt', 'r') as file:
> 	for line in file:
> 		print(line, end='')  # end='' zamezuje přidání newline na konec
>```
>

### 3. Zápis do souboru:
- Metoda `write()` umožňuje zápis do souboru.

>[!Example] zápis do souboru
>```python
>with open('example.txt', 'w') as file:
> 	file.write("Hello, World!\n")
> 	file.write("This is a new line.\n")
>```

### 4. Zavření souboru:
- Je důležité zavřít soubor po dokončení operací s ním, abyste uvolnili systémové prostředky.

>[!Example] zavření souboru
>```Python
>file.close()
>```
>- pokud otevřeme soubor pomocí `with`, je po skončení bloku automaticky uzavřen

## Typy režimů otevírání souborů:

- **`r`**: **Čtení** – výchozí režim. Pokusí se otevřít soubor pro čtení.
- **`w`**: **Zápis** – pokud soubor existuje, smaže jeho obsah a otevře ho pro zápis. Pokud neexistuje, vytvoří nový soubor pro zápis.
- **`a`**: **Přidání** – otevře soubor pro zápis. Pokud soubor neexistuje, vytvoří nový. Data budou připojena na konec souboru.
- **`r+`**: **Čtení a zápis** – otevře soubor pro čtení a zápis. Soubor se nepřepíše.
- **`w+`**: Zápis a čtení – stejný jako 'r+', ale **smaže obsah** souboru.
- **`rb`**: **Čtení binárního souboru** – otevře soubor pro čtení v binárním režimu.
- **`wb`**: **Zápis binárního souboru** – otevře soubor pro zápis v binárním režimu.
- **`ab`**: Přidání binárního souboru – otevře soubor pro zápis v binárním režimu. Data budou připojena na konec souboru.
- **`rb+`**: **Čtení a zápis binárního souboru** – otevře soubor pro čtení a zápis v binárním režimu. Soubor se nepřepíše.
- **`wb+`**: Zápis a čtení binárního souboru – otevře soubor pro zápis a čtení v binárním režimu. Obsah souboru se smaže.
- **`ab+`**: Přidání a čtení binárního souboru – otevře soubor pro zápis a čtení v binárním režimu. Data budou připojena na konec souboru.

### Příklady otevření souboru

>[!Example] blok `with`
>```Python
>try:
> 	with open("example.txt", "r") as file:
> 		content = file.read()
> 		print(content)
>except FileNotFoundError:
> 	print("Soubor nebyl nalezen.")
>except IOError:
> 	print("Nastala chyba při čtení souboru.")
>
>```

>[!example] blok `try-except-finally`
>```Python
>file = None
>try:
> 	file = open("example.txt", "r")
> 	content = file.read()
> 	print(content)
>except FileNotFoundError:
> 	print("Soubor nebyl nalezen.")
>except IOError:
> 	print("Nastala chyba při čtení souboru.")
>finally:
> 	if file is not None:
> 		file.close()
>```

##### Navigace
Předchozí:  [[Typy chyb a jejich hledání v jazyce Python]]
Následující: [[Binární data v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]