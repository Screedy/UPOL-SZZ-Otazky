## Základní operace se soubory

### 1. Otevření souboru:

Funkce `open()` se používá k otevření souboru. Tato funkce vrací objekt souboru, který se používá k provádění operací na souboru.

```Python
file = open("example.txt", "r")  # Otevření souboru pro čtení
```

### 2. Čtení ze souboru:

Metoda `read()` slouží k čtení obsahu souboru.

```Python
content = file.read()
```


### 3. Zápis do souboru:

Metoda `write()` umožňuje zápis do souboru.

``` Python
file.write("Hello, World!")
```

### 4. Zavření souboru:

Je důležité zavřít soubor po dokončení operací s ním, abyste uvolnili systémové prostředky.

```Python
file.close()
```

## Typy režimů otevírání souborů:

- **'r'**: Čtení – výchozí režim. Pokusí se otevřít soubor pro čtení.
- **'w'**: Zápis – pokud soubor existuje, smaže jeho obsah a otevře ho pro zápis. Pokud neexistuje, vytvoří nový soubor pro zápis.
- **'a'**: Přidání – otevře soubor pro zápis. Pokud soubor neexistuje, vytvoří nový. Data budou připojena na konec souboru.
- **'r+'**: Čtení a zápis – otevře soubor pro čtení a zápis. Soubor se nepřepíše.
- **'w+'**: Zápis a čtení – stejný jako 'r+', ale smaže obsah souboru.
- **'rb'**: Čtení binárního souboru – otevře soubor pro čtení v binárním režimu.
- **'wb'**: Zápis binárního souboru – otevře soubor pro zápis v binárním režimu.
- **'ab'**: Přidání binárního souboru – otevře soubor pro zápis v binárním režimu. Data budou připojena na konec souboru.
- **'rb+'**: Čtení a zápis binárního souboru – otevře soubor pro čtení a zápis v binárním režimu. Soubor se nepřepíše.
- **'wb+'**: Zápis a čtení binárního souboru – otevře soubor pro zápis a čtení v binárním režimu. Obsah souboru se smaže.
- **'ab+'**: Přidání a čtení binárního souboru – otevře soubor pro zápis a čtení v binárním režimu. Data budou připojena na konec souboru.

### Příklady otevření souboru:
#### Pomocí bloku `with`:
```Python
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Soubor nebyl nalezen.")
except IOError:
    print("Nastala chyba při čtení souboru.")

```

#### Pomocí `try`/`finally`:
```Python
file = None
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Soubor nebyl nalezen.")
except IOError:
    print("Nastala chyba při čtení souboru.")
finally:
    if file is not None:
        file.close()

```


##### Navigace
Předchozí:  [[Typy chyb a jejich hledání v jazyce Python]]
Následující: [[Binární data v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]