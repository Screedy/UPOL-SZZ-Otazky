$$R = {<The Avengers, 1998>, <The Avengers, 2012>, <The Matrix>, 1999}$$
- n-tice (tuple) nemají význam
	- $Tupl(S)$  ... relace nad $S$
- Zavedeme tedy *relace*, kde složky budou pojmenovány a tyto jména nazýváme **atributy**
- Atributy mají svou doménu (nejvýše spočetná množina hodnot)
- $Y$ ... množina všech atributů
- **relační schéma** ... konečna podmnožiny množiny atributů 
- Pokud nějaké n-tice splňuje relační schéma ($R$) nazýváme ji ***n-tice nad $R$**
- Relace reprezentujeme **tabulkami** a **n-tici nazýváme řádek**
	- Tabulky jsou uloženy v **tabulkové proměnné** či **relační proměnné**
- Můžeme s nimi provádět běžné množinové operace
#### Podmínky relačního modelu
- musí splňovat 3 podmínky
	1. jedinečné názvy sloupců
	2. neobsahuje `null`
	3. nemá duplicitní řádky
## Atributy
- Sloupce tabulky
- Definují vlastnost, která je jednotlivým záznamům přiřazena
- Atribut má:
	1) Název - musí být jedninečný
	2) Doménu - soubor možných hodnot
	3) Datový typ - typ hodnoty (`int`, `text`, ...)
- Např.
	- `employee_id`(identifikátor zaměstnance, číslo)
	- `name` (jméno, text)
	- `age` (věk, celé číslo)
## N-tice
- Představují řádky tabulky (konkrétní záznamy)
- Každá n-tice obsahuje hodnoty pro všechny atribut

| employee_id | name | age | department |
| ----------- | ---- | --- | ---------- |
| 1           | Bob  | 30  | IT         |
## Relace
- Konečná podmnožina n-tic
- Musí být nad určitou množinou atributů (relační schéma)
## Relační proměnné
- Proměnná jejíž hodnotou je relace
- V SQL jsou to obvykle názvy tabulek
## Charakteristické vlastnosti relací
- Vlastnosti, které definují strukturu a chování tabulek
- Určitý výrok
- Pokud relace obsahuje danou n-tici, pak je výrok pravdivý
	- Např. mám tabulky s filmy (`title`) a roky vydání (`year`), vlastnost *"Vlastním film `title` natočený roku `year`."* je pravdivá
	- Nechť $R$ je relace nad $S$ a $V(t)$ je vlastnost nad $R$. Poté $V(t)$ je charakteristická vlastnost pokud platí $t \in R$ pokud $V(t) = true$
	- $V(t)$ určujte $R$ pokud $R = \{t \in Tupl(S) \; | \; V(t)\}$ 