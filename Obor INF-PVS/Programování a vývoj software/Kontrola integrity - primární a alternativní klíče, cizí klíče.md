- **nadklíč** ... kombinace atributů, která jednoznačně identifikuje řádek
- **kandidatní klíč** ... minimální forma nadklíče (obsahuje pouze ty nutné atributy)
- **primární klíč** ... jeden vybraný z kandidátních klíčů (ostatní jsou *alternativní klíče*)

- Pokud má tabulka deklarovaný primární klíč a sloupce nesmí obsahovat `null`, pak jde o relaci
#### Cizi klíč (foreign key)
- Pro každý řádek tabulky 1 existuje právě jeden řádek v tabulce 2 (je určený nějakými sloupci)
- Prostě je to "odkaz" do další tabulky
- Používá se pro rozklad
- Představuje jistou formu závislosti - není možné mazat řádky, na které jsou v jiné tabulce některé řádky navázané