## Dokumentace
- Slouží k lepšímu pochopení co kód dělá (především pro ostatní programátory)
- Python sám o sobě klade veliký důraz na **čitelnost kódu**
### Docstrings
- Primární proprieta pro dokumentaci
```Python
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
```
- Vestavěná funkce `help(obj)` vypíše *docstring* objektu
- Účelem je poskytnout stručný přehled objektu (maximálně 1 řádek)
- Pokud jde o víceřádkový *docstring* jeho účelem je více než shrnutí a má pevně danou strukturu
```Python
"""This is the summary line

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and elaboration is separated by a blank line.
"""

# continue of another code
```
- Jejich konvence je popsána v [PEP257](https://peps.python.org/pep-0257/)
- Mohou být použity pro 3 typy objektů
	1) třídy a metody
	2) packages and modules
	3) funkce

- Další dokumentace může být uložena ve složce `/doc`
- Existují nástrojce usnadňující její generování ([Sphinx](https://www.sphinx-doc.org/en/master/), [Epydoc](https://epydoc.sourceforge.net/), [Read the Docs](https://about.readthedocs.com/?ref=readthedocs.org))
## Typování
- Jde o dynamicky typovaný jazyk
	- Python provádí kontrolu typů až při běhu programu
- Proměnné může být přiřazená jiná hodnota a změněn její typ
- `type(var)` vrací typ dané proměnné
### Type hinting
- Uživateli umožňuje vidět s jakými typy kód pracuje (avšak **NEovlivňuje** funkčnost)
```Python
def sum_two_numbers(a: int, b: int) -> int:
   """Sums two numbers.
 
   Args:
       a (int): first number
       b (int): second number
 
   Returns:
       int: Summation of a and b
   """

   return a + b
```
- Pokud není vrácena hodnota používáme `-> None`
## PEP8
- Oficiální **coding conventions**
- Formátování se dá zajistit automaticky (nástroj [Black](https://github.com/psf/black))
- Kódování souboru: UTF-8
- Odsazení: 4 mezery
- Maximální délka řádku: 79 znaků (docstring 72)
- Mezi třídami/funkcemi 2 prázdné řádky
- Mezi metodami 1 prázdný řádek
- Pořadí importů: standardní knihovna, ostatní, lokální
- **Názvy**
	- Proměnné a funkce: snake_case
	- Třídy: CamelCase
- **Komentáře**
	- Mezera po `#`
	- Alespoň 2 mezery od kódu