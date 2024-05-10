- Používají se pro zajištění **integrity a spolehlivosti** přenosu dat.
- Umožňují **detekci** a **opravu** chyb, které mohou nastat během přenosu dat mezi zařízeními nebo v datových úložištích.
- chyba = nechtěná **změna bitu**

## Detekční kódy
- umožňují **zjistit**, zda došlo k chybě při **přenosu** nebo **ukládání** dat
- **neopravují chyby**, ale poskytují systému informace, že data jsou chybná
- data jsou obvykle znovu vyžádána
1. **Paritní bit**:
	- nejjednodušší formou detekčního kódu
	- přidává **jeden bit** k datům tak, aby celkový počet jedniček byl buď sudý (**sudá parita**) nebo lichý (**lichá parita**)
	- umožňuje detekci jednoduchých chyb v jednom bitu
2. **Kontrolní součty**:
	- suma všech přenesených datových slov
	- často používaná v síťové komunikaci a souborových systémech
	- chyba je detekována, pokud kontrolní součet přijatých dat nesouhlasí s kontrolním součtem odeslaných dat
	- detekuje lichý počet chyb na stejných pozicích v blocích, nedetekuje změnu pořadí bloků
1. **CRC (Cyklický redundantní kód)**:
	- přidává k datům speciální sekvenci bitů, známou jako kontrolní součet (checksum), která umožňuje příjemci ověřit integritu dat pomocí jednoduchého výpočtu
	- ![[MacBook-2024-04-27-001089.png]]
	1. **Zvolení generujícího polynomu**: V našem případě je to polynom $x^{3} + x + 1$ který můžeme zapsat jako binární číslo $1101$
	2. **Příprava**: K datům se přidají nuly, počet nul odpovídá stupni polynomu (v našem případě 3)
	3. **Dělení dat pomocí operace XOR**: Využijeme operaci XOR pro simulaci dělení polynomem.
	- **Výhody:** vysoká spolehlivost, jednoduchost implementace v hw i sw
	- **Limitace:** pouze detekuje chyby, výběr polynomu ovlivňuje efektivitu detekce

## Samoopravné kódy (ECC - Error Correction Code)
- způsob, jak zabezpečit přenos dat, aby bylo možné chyby detekovat  a také je automaticky opravit
- k datům přidávají redundanci prostřednictvím matematických algoritmů
- **Multidimenzionální parita:**
	- rozšiřuje jednoduchou paritní kontrolu z jednorozměrného lineárního prostoru do dvourozměrných prostorů
	- to umožňuje lepší detekci a lokalizaci chyb
	- paritní bity jsou vypočítány pro řádky i sloupce, což umožňuje nejen detekci chyb, ale i identifikaci přesné lokality chyby v matici
	```bash
	1. Datová matice:        |  2. Přidáme prázdné řádky/sloupce:
	1 0 1                    |  1 0 1 P
	0 1 1                    |  0 1 1 P
	1 0 0                    |  1 0 0 P
							 |  P P P P
	
	
	3. Příklad výpočtu pro první řádek:
	1 XOR 0 XOR 1 = 0  (sudá parita, protože chceme sudý počet 1)
	
	4. Výsledná matice:
	1 0 1 0
	0 1 1 0
	1 0 0 1
	0 1 0 P
	```

- **Hammingův kód**:
	- umožňuje automatickou opravu jednobitových chyb v **reálném čase**
	- ideální pro aplikace, kde jsou chyby **pravděpodobné**, ale **ne příliš časté**, jako například v telekomunikacích nebo v systémech **RAM**
	- umožňuje detekovat až 2 chyby současně a opravit 1
- **Reed-Solomonovy kódy**:
	- Např. v CD/DVD/BD

##### Navigace
Předchozí:  [[Reprezentace čísel a znaků v počítači]]
Následující: [[Hardware osobního počítače - základní deska a čipset, procesor a instrukce, vnitřní a vnější paměti, ostatní zařízení]]
Celý okruh: [[2. Informační technologie]]