## Funkční závislost
- Pokud 2 řádky mají stejnou hodnotu atributu X i atributu Y nazýváme je funkčně závislé
- Triviální funkční závilost je taková, kde atrbiuty v Y jsou podmnožinou atributů v X
- Slouží k dekompozici databáze a udržení v BCNF![[Screenshot 2022-12-10 at 11.35.32.png]]
## Normalizace
- Používá se k optimalizaci struktury (odstranění redundace)
	- Abychom zbytečně neukládali duplicitní záznamy
	- Lidově řečeno se dělí tabulky na menší
- Existuje několik různých normálních forem
#### Seznam normálních forem
- **UNF**: Nenormalizovaná databáze
- **0NF**: Alespoň jeden atribut obsahuje více než jednu hodnotu.
- **1NF**: Každý atribut obsahuje pouze atomické hodnoty.
- **2NF**: Každý neklíčový atribut je plně závislý na každém kandidátním klíči. (Neklíčovým atributem rozumíme atribut, který není součástí žádného kandidátního klíče.)
- **3NF**: Všechny neklíčové atributy musí být vzájemně nezávislé.
- **BCNF**: Atributy, které jsou součástí primárního klíče, musí být vzájemně nezávislé.
- **4NF**: Relace popisuje pouze příčinnou souvislost mezi klíčem a atributy.
- **5NF**: Relaci již není možno bezeztrátově rozložit.
## BCNF (Boyceho-Coddova normální forma)
- Je **splněna** pokud v tabulce není žádná netrivální funkční závislost nebo pokud pro každou platí, že je nadklíčem
- Přísnější než 3NF
#### Rozklad
- ![[Pasted image 20250428211034.png]]
- Spojením oněch 2 relací (podle relační algebry) opět dostaneme původní relaci
	- Pokud je to přesně ona (nic není navíc), tak se jedná o **beztrarátový rozklad**