## Operační systém
- Operační systém je komplexní software, který řídí hardwarové a softwarové zdroje počítače a poskytuje společné služby pro počítačové programy.
- OS je **rozhraní** mezi HW a SW.
- Poskytuje **abstrakci** nad daným hardwarem (a jazyky vyšší úrovně).
>[!Info] Vrstvy HW/SW:
>1. hardware
>2. operační systém (OS)
>3. standardní knihovny (libc, CRT)
>4. systémové nástroje 
>5. aplikace
>* Hranice mezi vrstvami **nemusí být ostrá**

## Architektura OS
- Architektura operačního systému popisuje jeho vnitřní strukturu a způsob, jakým jsou spravovány systémové zdroje a služby. 
- Mezi klíčové aspekty architektury OS patří jeho 
	- **jádro**, 
	- **správa procesů a vláken**, 
	- **správa paměti**, 
	- **systémové volání**

### Jádro (kernel)
1. **Monolitické jádro**
	- Celý operační systém běží jako **jeden velký proces** v **jednom adresním prostoru**.
	- Všechny základní služby jako **správa paměti, ovladače zařízení, systémová volání a správa souborů** jsou integrovány do **jednoho velkého bloku kódu**.
	- Např. tradiční **Linuxové** jádro.
	- **Výhody**:
		- výkon
		- jednoduchost
	- **Nevýhody**:
		- bezpečnost
		- stabilita
		- horší rozšířitelnost
2. **Mikrojádro**
	- Mikrojádrové jádro minimalizuje služby běžící v privilegovaném režimu jádra.
	- **Přesouvá služby jádra** (ovladače zařízení, protokoly síťové komunikace a systémové služby) **do uživatelského prostoru**
	- **Výhody:**
		- bezpečnost
		- stabilita
		- lehčí rozšířitelnost
	- **Nevýhody:**
		- výkon
		- složitost
3. **Hybridní jádro**
	- Kombinují principy monolitických a mikrojádrových architektur.
	- Poskytují modulární strukturu, kde některé služby běží v jádře, zatímco jiné mohou být provozovány v uživatelském prostoru.
	- Např. Windows.
	- **Výhody:**
		- flexibilita
		- výkon
		- stabilita
	- **Nevýhody:**
		- složitost
		- náročnost na návrh

## Poskytovaná rozhraní
Operační systémy poskytují několik typů rozhraní:
1. **Uživatelské Rozhraní (User Interface - UI)**:
    - **Grafické uživatelské rozhraní (GUI)**
    - **Příkazová řádka (CLI)**
2. **Programovací rozhraní (Application Programming Interface - API)**:
    - Umožňuje vývojářům softwaru psát aplikace, které mohou využívat služby poskytované operačním systémem, jako je **přístup k souborovému systému, síťové komunikaci, správě okna** atd.
3. **Hardwarové abstrakční vrstvy (Hardware Abstraction Layers - HAL)**:
    - **Poskytuje konzistentní rozhraní k hardwarovým zdrojům**, což zjednodušuje programování a správu systému.

##### Navigace
Předchozí: 
Následující: [[Vykonávání programu a proces překladu]]
Celý okruh: [[2. Informační technologie]]