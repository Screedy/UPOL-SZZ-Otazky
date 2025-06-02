## Počítačová síť
- Je skupina mezi sebou propojených a komunikujících uzlů
- Nejsou pouze počítače (servery, tiskárny, ...., IoT)
- Propojení mezi uzly = **síťová infrastruktura**
	- zahrnuje přenosové médium, pasivní a aktivní propojovací prvky
- Umožňuje poskytování *síťových služeb* uzlům v síťi
	- např. sdílení hardware, software a dat
	- Služby jsou realizovány pomocí komunikace
- Nejznámější počítačová síť je síť Internet
	- Jeden z největších systémů, který člověk vytvořil
- Dělení podle velikosti/použití
	1. **PAN** - personální - Bluetooth
	2. **LAN** - lokální - Ethernet, Wi-Fi
	3. **WAN** - rozlehlé - GSM
#### Parametry sítí
- propustnost \[Mb/s]
- ztrátovost
- zpoždění (latence)
- jitter (kolísání latence)
### Komunikace v počítačové síti
![[MacBook-2024-03-18-000909.png]]
- Pro implementování takovéto komunikace musíme vyřešit několik problémů:
	1. Určit formát vyměňovaných zpráv
	2. Identifikovat aplikace na jednotlivých uzlech
	3. Určit adresaci uzlu
	4. Identifikace rozhraní
	5. Specifikovat parametry fyzického přenosu dat
#### Realizace
- máme 2 způsoby
1. **Přepínání okruhů**
	- spojované sítě jelikož se před zahájením komunikace vytvoří ustálené spojení
	- výhodou je garance doručení a stabilita
	- nevýhodou je větší náročnost na režijní informace a realizovatelnost
	- dnes již nepoužívané
2. **Přepínání paketů**
	- nespojované sítě
	- data jsou dělena menší části (pakety), které jsou pak posílany
		- každý paket může jít jinou cestou
		- příjmence musí pakety následně složit zpět do celku
	- nevýhodou je nestabilnost (zpráva nemusí dorazit, je nutné je skládat atd.)
	- přesto v dnešní době jejich výhody převažují a jsou tedy jasnou volbou
#### Typy služeb
- Dva druhy:
1) End-to-End
	- Implementace složitější funkcionality v uzlech, které spolu komunikují
	- Mezilehlé uzly si vystačí pouze s jednoduchými operacemi
	- \+ spolehlivější přenos dat
	- \- vyšší zpoždění při přenosu
2) Hop-by-Hop
	- Stejná funkcionalita na každém uzlu
	- \- méně spolehlivý přenos (selhání jakéhokoliv uzlu = konec komunikace)
	- \- omezené škálování
	- \- udržovat stav komunikace
	- \+ zpoždění přenosu je minimální

## Model ISO/OSI
- Jedná se o obecný popis komunikace mezi dvěma uzly
- Je používán jako **abstraktní a referenční** model komunikace
	- Pouze obecný popis komunikace
	- Při implementaci se na něj odkazujeme
- Model ISO/OSI rozděluje komunikaci na 7 vrstev, které označujeme L1-L7
  ![[MacBook-2024-03-18-000910.png| 300]]
- Vrstva L1 je považována za nejnižší vrstvu a L7 za nejvyšší
- Obecně ne všechny vrstvy musí být v reálné komunikaci implementovány
- Při komunikaci, kde je po cestě mezilehlý uzel, tak ten data "rozbalí" jen do L3 síťové vrstvy
- ![[MacBook-2024-03-18-000911.png]]

## Model TCP/IP
- Jedná se o reálný model používaný v síti Internet
- Je tvořen čtyřmi vrstvami: **aplikační, transportní, síťová a síťového rozhraní**
- Jednotlivé vrstvy jsou popsány standardy a jejich funkce je zajištěna pomocí protokolů, které tyto standardy implementují
- ![[MacBook-2024-03-18-000912.png]]
#### Topologie sítí
- Dnes se používá obvykle kombinace
![[Pasted image 20230104112018.png]]
##### Navigace
Předchozí:  [[Hardware osobního počítače - základní deska a čipset, procesor a instrukce, vnitřní a vnější paměti, ostatní zařízení]]
Následující: [[Ethernet - přepínač, použití média, linkový rámec]]
Celý okruh: [[2. Informační technologie]]