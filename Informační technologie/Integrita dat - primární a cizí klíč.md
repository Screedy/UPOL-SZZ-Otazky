- Integrita dat je klíčový koncept v relačních databázích, který zajistí správnost a konzistenci dat. Základními mechanismy pro udržení integrity dat jsou primární a cizí klíče.

## Primární klíč (Primary Key)
- Primární klíč je sloupec nebo skupina sloupců v relační databázové tabulce, které jednoznačně identifikují každý řádek tabulky.
- Pravidla pro primární klíče:
	- Hodnota primárního klíče musí být unikátní pro každý řádek.
	- Primární klíč nesmí obsahovat `NULL` hodnoty.
	- V jedné tabulce může být pouze jeden primární klíč, ale může obsahovat více sloupců (složený primární klíč).

## Cizí klíč (Foreign Key)
- Cizí klíč je sloupec nebo skupina sloupců v jedné tabulce, která odkazuje na primární klíč jiné tabulky.
- Role cizího klíče:
	- Umožňuje vytvoření relace (vazby) mezi tabulkami.
	- Zajišťuje referenční integritu mezi daty dvou tabulek.
	- Hodnota cizího klíče musí odpovídat hodnotě existujícího primárního klíče v jiné tabulce, nebo musí být `NULL`, pokud je to povoleno.
- Když se pokusíte vložit data do tabulky s cizím klíčem, databázový systém zkontroluje, zda existují odpovídající hodnoty v referenční tabulce. Pokud ne, operace vložení nebo aktualizace selže.