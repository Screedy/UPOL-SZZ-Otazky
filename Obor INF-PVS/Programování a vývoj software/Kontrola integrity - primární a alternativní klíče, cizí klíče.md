- **nadklíč** ... kombinace atributů, která jednoznačně identifikuje řádek
- **kandidatní klíč** ... minimální forma nadklíče (obsahuje pouze ty nutné atributy)
- **primární klíč** ... jeden vybraný z kandidátních klíčů (ostatní jsou *alternativní klíče*)

- Pokud má tabulka deklarovaný primární klíč a sloupce nesmí obsahovat `null`, pak jde o relaci
#### Cizi klíč (foreign key)
- Pro každý řádek tabulky 1 existuje právě jeden řádek v tabulce 2 (je určený nějakými sloupci)
- Prostě je to "odkaz" do další tabulky
- Používá se pro rozklad
- Představuje jistou formu závislosti - není možné mazat řádky, na které jsou v jiné tabulce některé řádky navázané
- V SQL určité příkazy
	- `CASCADE` ... změna v primárním klíčí se projeví i v cizích klíčích
	- `SET NULL` ... primární klíč smazán => cizí klíč se nastaví na `null`
	- `RESTRICT` ... zabrání změně/smazání primárního klíče pokud existuje odpovídající hodnota v cizím klíči
#### Kontrola integrity
- Správnost a konzistence dat
#### Omezeí základncíh relací
- `UNIQUE` ... udává alternativní klíče relace
- `NOT NULL` .. zaručí že nejde nastavit `null`
## ACID
- **transakce** je skupina příkazů (posloupnost akcí), která převádí databázi ze jednoho konzistentního stavu do druhého
	- `READ`
	- `WRITE`
	- `COMMIT`
	- `ABORT`
	- `BEGIN` pro začátek, `COMMIT` pro ukončení, `ROLLBACK` pro vrácení změn
- ACID znamená 4 podmínky (slova)
	1. **atomicita**
		- provede se vše nebo nic (transakce jsou atomické operací)
	2. **konzistence**
		- operace vždy skončí v konzistentním stavu
		- zajišťuje dynamické omezení v průběhu transakce
	3. **izolovanost**
		- operace jsou abstraktní čili neovlivňují se navzájem
	4. **trvalost**
		- změny, které se provedou jsou skutečně uloženy

- v průběhu transakcí se data zapisují jen do vyrovnávací paměti
- **logování**
	- záznamy o transakcích (začátek, konec, neúspěch)
- může dojít k problému souběhu nebo nedokončení změn
- za pomoci logu (procházíme se opačně) se chyby zotaví