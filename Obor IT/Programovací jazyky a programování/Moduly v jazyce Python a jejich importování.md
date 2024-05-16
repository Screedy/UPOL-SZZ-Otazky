- Moduly umožňují znovupoužitelnost kódu a jeho lepší organizaci.
- Python poskytuje mnoho vestavěných modulů a umožňuje také vytváření vlastních modulů.
- Importování modulů je způsob, jakým můžete zahrnout funkce, třídy a proměnné definované v jednom modulu do jiného souboru.

- **Co je modul?**
	- Modul je soubor obsahující Python kód (přípona .py), který může obsahovat definice funkcí, tříd a proměnných. 
	- Moduly jsou základním stavebním kamenem knihoven a balíčků v Pythonu.

## Importování modulů
- K importování modulů používáme klíčové slovo `import`.
- Existuje několik způsobů, jak importovat moduly a konkrétní prvky z modulů:

>[!Example] základní import (celého modulu)
>```python
>import math
>
>print(math.sqrt(16))  # Použití funkce sqrt z modulu math
>```

>[!Example] import konkrétních funkcí nebo proměnných
>```python
>from math import sqrt, pi
>
>print(sqrt(16))  # Použití importované funkce sqrt
>print(pi)        # Použití importované proměnné pi
>```

>[!Example] přejmenování modulu
>```python
>import numpy as np
>
>array = np.array([1, 2, 3])
>print(array)
>```
>- můžeme přejmenovat i funkci `from math import sqrt as s`

>[!Example] import všeho z modulu
>```python
>from math import *
>
>print(sqrt(16))  # Použití funkce sqrt bez prefixu modulu
>```

- Python hledá moduly v určených cestách, které jsou uloženy v proměnné `sys.path`. 
- Standardní cesty obsahují umístění standardních knihoven, aktuálního pracovního adresáře a cesty uvedené v proměnné prostředí `PYTHONPATH`.
- Vlastní moduly můžeme vytvářet tím, že uložíme kód do souboru s příponou `.py`. Poté je lze importovat do jiných souborů.
---
- **Přehled některých standardních modulů:**
	- **math:** Pro matematické funkce.
	- **os:** Pro operace nad operačním systémem.
	- **random:** Pro generování náhodných čísel.
	- **datetime:** Pro manipulaci s datumem a časem.
	- **sys:** Pro práci s interpretem Pythonu.

## Správa balíčků
- Python má správce balíčků pip, který umožňuje instalovat, aktualizovat a odstraňovat balíčky z Python Package Index (PyPI).

>[!Example] příklad instalace balíčku
>```bash
>pip install numpy  # Instalace balíčku numpy
>pip install --upgrade numpy  # Aktualizace balíčku numpy
>pip uninstall numpy  # Odinstalace balíčku numpy
>```

##### Navigace
Předchozí:  [[Binární data v jazyce Python]]
Následující: [[Základy objektového programování - třídy, objekty zasílání zpráv]]
Celý okruh: [[3. Programovací jazyky a programování]]