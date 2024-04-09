### Počítačová síť
- Je skupina mezi sebou propojených a komunikujících uzlů
- Nejsou pouze počítače (servery, tiskárny, ...., IoT)
- Propojení mezi uzly = **síťová infrastruktura**
	- zahrnuje přenosové médium, pasivní a aktivní propojovací prvky
- Umožňuje poskytování *síťových služeb* uzlům v síťi
	- např. sdílení hardware, software a dat
	- Služby jsou realizovány pomocí komunikace
- Nejznámější počítačová síť je síť Internet
	- Jeden z největších systémů, který člověk vytvořil.

### Komunikace v počítačové síti
![[MacBook-2024-03-18-000909@2x.png]]
- Pro implementování takovéto komunikace musíme vyřešit několik problémů:
	1. Určit formát vyměňovaných zpráv
	2. Identifikovat aplikace na jednotlivých uzlech
	3. Určit adresaci uzlu
	4. Identifikace rozhraní
	5. Specifikovat parametry fyzického přenosu dat

### Typy služeb
- Dva druhy:
	- End-to-End
	- Hop-by-Hop

- End-to-End
	- Implementace složitější funkcionality v uzlech, které spolu komunikují
	- Mezilehlé uzly si vystačí pouze s jednoduchými operacemi
	- + spolehlivější přenos dat
	- - vyšší zpoždění při přenosu
- Hop-by-Hop
	- Stejná funkcionalita na každém uzlu
	- - méně spolehlivý přenos (selhání jakéhokoliv uzlu = konec komunikace)
	- - omezené škálování
	- - udržovat stav komunikace
	- + zpoždění přenosu je minimální

### Model ISO
- Jedná se o obecný popis komunikace mezi dvěma uzly
- Je používán jako **abstraktní a referenční** model komunikace
	- Pouze obecný popis komunikace
	- Při implementaci se na něj odkazujeme
- Model OSI rozděluje komunikaci na 7 vrstev, které označujeme L1-L7
  ![[MacBook-2024-03-18-000910@2x.png | 300]]
- Vrstva L1 je považována za nejnižší vrstvu a L7 za nejvyšší
- Obecně ne všechny vrstvy musí být v reálné komunikaci implementovány
- ![[MacBook-2024-03-18-000911@2x.png]]

### Model TCP/IP
- Jedná se o reálný model používaný v síti Internet
- Je tvořen čtyřmi vrstvami: **aplikační, transportní, síťová a síťového rozhraní**
- Jednotlivé vrstvy jsou popsány standardy a jejich funkce je zajištěna pomocí protokolů, které tyto standardy implementují
- ![[MacBook-2024-03-18-000912@2x.png]]
