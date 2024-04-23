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

## Ukázka
```sql
CREATE TABLE Filmy (
    id INT AUTO_INCREMENT,
    nazev VARCHAR(255) NOT NULL,
    rok_vydani YEAR NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Herci (
    id INT AUTO_INCREMENT,
    jmeno VARCHAR(255) NOT NULL,
    film_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (film_id) REFERENCES Filmy(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);
```
Vysvětlení kódu:
- Tabulka `Filmy` má primární klíč `id`, který se automaticky zvyšuje pro každý nový záznam.
- Tabulka `Herci` má vlastní primární klíč `id` a cizí klíč `film_id`.
- Cizí klíč `film_id` v tabulce `Herci` odkazuje na sloupec `id` v tabulce `Filmy`.
- `ON DELETE SET NULL` znamená, že pokud je film odstraněn, hodnota `film_id` u herce, který se na tento film odkazoval, bude nastavena na `NULL`.
- `ON UPDATE CASCADE` zajistí, že pokud dojde k aktualizaci `id` filmu, změní se automaticky i hodnoty `film_id` v tabulce `Herci`, aby odpovídaly nové hodnotě.