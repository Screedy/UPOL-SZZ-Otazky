Moduly jsou základním stavebním kamenem v Pythonu, který umožňuje organizovat kód do samostatných a znovupoužitelných bloků. Importování modulů je klíčové pro rozšíření funkcionalit Pythonu.

Modul je soubor obsahující Python kód, včetně definic funkcí, tříd a proměnných. Může obsahovat i spustitelný kód.

**Druhy importování:**
1. **Import celého modulu:** `import module_name`
2. **Import specifických funkcí nebo tříd:** `from module_name import function_name, class_name`
4. **Přejmenování modulu:** `import module_name as alias`

Python hledá moduly v určených cestách, které jsou uloženy v proměnné `sys.path`. Standardní cesty obsahují umístění standardních knihoven, aktuálního pracovního adresáře a cesty uvedené v proměnné prostředí PYTHONPATH.

Vlastní moduly můžeme vytvářet tím, že uložíme kód do souboru s příponou `.py`. Poté je lze importovat do jiných souborů.

**Přehled některých standardních modulů:**

- **math:** Pro matematické funkce.
- **os:** Pro operace nad operačním systémem.
- **random:** Pro generování náhodných čísel.
- **datetime:** Pro manipulaci s datumem a časem.
- **sys:** Pro práci s interpretem Pythonu.


##### Navigace
Předchozí:  [[Binární data v jazyce Python]]
Následující: [[Základy objektového programování - třídy, objekty zasílání zpráv]]
Celý okruh: [[3. Programovací jazyky a programování]]