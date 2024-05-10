## Transportní vrstva
![[MacBook-2024-04-17-001022.png| 500]]

- Transportní vrstva zprostředkovává komunikaci mezi **procesy** (**aplikacemi**), které běží na komunikujících uzlech.
- Poskytuje dvě základní služby
	- **Spojová spolehlivá služba**
		- **Navazuje**, **udržuje** a **ukončuje** spojení mezi dvěma aplikacemi
		- Zajišťuje **spolehlivé doručení dat**
		- Např. protokol **TCP**
	- **Nespojová nespolehlivá služba**
		- **Nevytváří** žádné spojení
		- Nezajišťuje spolehlivé doručení dat
		- Např. protokol **UDP**

### Port
- Ve skutečnosti mezi sebou nekomunikují uzly, ale aplikace které na těchto uzlech běží.
	- Komunikovali by dvě aplikace na jednom uzlu, **jak rozlišíme, pro kterou aplikaci jsou data?** - Pomocí **portu**
- Port je **adresa na úrovni transportní vrstvy**.
- Je to 2B **adresa konkrétní aplikace**.
	- $0-1023$ jsou **privilegované**. Vyhrazené pro standardní služby. Např. $80$ pro službu **WWW**.
	- $1024-65535$ se označují jako **klientské**. Jsou určeny **pro klientské aplikace**.
	- Porty mají **nezávislý** rozsah pro **TCP** a **UDP**.

### Protokol TCP
- **Spojová spolehlivá služba** zajišťující **spolehlivé** doručení dat.
- V jeho kompetenci je:
	- **Potvrzování přijetí** dat
	- **Zaručení správného pořadí** dat
	- **Detekce ztráty** dat
	- **Vyžádání opakování přenosu** ztracených nebo poškozených dat
![[MacBook-2024-04-17-001023.png]]
- Bajty z vyšší vrstvy jsou postupně ukládány do odesílacího bufferu.
- Z bufferu jsou v daném pořadí přenášeny do přijímacího bufferu příjemce, ze kterého jsou data postupně v daném pořadí předávána do vyšší vrstvy.
	- Vyšší vrstva příjemce dostává bajty v pořadí, ve kterém byly vytvořeny vyšší vrstvou na odesílateli.

#### TPC segment
- Transportní vrstva přenáší data ve formě **TCP segmentů**
  ![[MacBook-2024-04-17-001024.png]]
- Skládá se z:
	- Hlavičky - $20-60$ B
	- Datová část - data z vyšší vrstvy
- Celková velikost TCP segmentu je **omezena velikostí IP paketu**, do kterého se vkládá.
	- Data jsou obvykle větší, dochází k rozdělení na menší segmenty $\rightarrow$ **segmentace dat**.![[MacBook-2024-04-17-001025.png]]

#### Navázání spojení
- Založeno na **klient-server** architektuře.
	- Klient **navazuje** spojení, server **přijímá/odmítá**.
- Aby mohlo dojít k navázání spojení, musí mít klient i server otevřený port a poslouchat komunikaci.
- Navázání spojení probýhá technikou **3-fázového handshake**

>[!Example] 3-fázový handshake
>1. Klient posílá TCP segment (bez dat) s příznakem SYN a náhodně vygenerovaným číslem seq. Tento krok se označuje jako aktivní otevření.
>2. Server posílá segment (bez dat) s příznaky SYN a ACK a náhodně vygenerovaným číslem seq a číslem potvrzení ack.
>3. Klient posílá segment s  přiznakem ACK a číslem potvrzení nastavení seq + 1. Již může nést data.
>![[MacBook-2024-04-17-001026.png| 300]]

#### Přenos dat
- Po navázání spojení je možné posílat data oběma směry.
- Data jsou z odesílacího bufferu odstraněna v okamžiku potvrzení jejich přijetí.

>[!Example] Přenost dat
>1. Klient posílá segment obsahující $1000$ B dat s příznakem ACK. První B odeslaných dat má číslo $8001$, poslední má tedy $9000$. Hodnota čísla potvrzení ack $15001$ identifikuje, že jsou očekávána data začínající bajtem číslo $15001$.
>2. Klient posílá segment obsahující $1000$ B dat s příznakem ACK. První B odeslaných dat má číslo $9001$, poslední $10000$. Hodnota čísla potvrzení je ack je stále $15001$. Server nic neposlal.
>3. Server posílá segment obsahující $2000$ B dat s příznakem ACK. První B má číslo $15001$, poslední $17000$. Hodnota potvrzení ack je $10001$ $\rightarrow$ potvrzuje přejití segmentů z kroku $1$ a $2$. Jsou očekávána data začinající $10001$.
>4. Klient posílá segment bez dat s příznakem ACK. Číslo sekvence se neměni a má hodnotu $10000$. Hodnota potvrzení ack je $17001$, potvrzuje přijetí segmentů z $3$.
>![[MacBook-2024-04-17-001027.png| 300]]

#### Ukončení spojení
- Je možné provést několika způsoby

>[!Example] 3-fázové ukončení spojení
>1. Klient posílá segment (může obsahovat data) s příznakem FIN + ACK. Tento krok se označuje jako aktivní uzavření.
>2. Server posílá segment (může obsahovat data) s příznakem FIN + ACK. 
>3. Klient posílá segment (bez dat) s příznakem ACK. 
>![[MacBook-2024-04-17-001028.png| 300]]

>[!Example] 4-fázové ukončení spojení
>- Tento způsob se využívá pokud pouze jedna strana chce provést ukončení spojení.
>1. Klient posílá segment (může obsahovat data) s příznaky FIN + ACK. Klient dále nemůže posílat data, může ale přijímat a musí posílat segmenty s ACK.
>2. Server posílá segment s příznakem ACK. Server může déle posílat data. Po dokončení tohoto kroku je pro server spojení polouzavřené.
>3. Server posílá segment (může obsahovat data) a příznaky ACK a FIN.
>4. Klient posílá segment s příznakem ACK.
>![[MacBook-2024-04-17-001029.png| 300]]

#### Řízení toku dat
- Při komunikaci mezi uzly může nastat situace, kdy příjemce **nestíhá zpracovávat** přijímaná data. $\rightarrow$ **zahlcení příjemce**
- Při zahlcování dochází k zaplnění přijímacího bufferu v jehož důsledku jsou další příchozí data **ztracena**.

##### Posuvné okénko
- Posuvné okénko **vymezuje**, jak velkou část odesílacího bufferu **je možné poslat**, aniž by došlo k zahlcení příjemce
- Strategie stop and wait je **neefektivní**.
	- Po poslání dat se čeká na potvrzení
- Namísto toho se data v okně odesílají **bez nutnosti čekání na potvrzení** jejich přijetí. Jakmile je odeslaná část potvrzena, **okno se posouvá**.

>[!Example] Příklad posuvného okénka
>![[MacBook-2024-04-17-001030.png]]
>- Posuvné okno má velikost $7$ a obsahuje bajty s čísly $41-47$. 
>- Jsou odeslány bajty $41-44$.
>- Pokud dojde k odeslání bajtu $45$ a potvrzení bajtů $41-42$ posune se okénko následovně:
>![[MacBook-2024-04-17-001031.png]]
- Pokud budeme zmenšovat okno, nesmí dojít k situaci, kdy jsou již odeslané bajty mimo posuvní okénko

#### Pozitivní potvrzování
- TCP využívá **komulativní potvrzování**. 
- To znamená, že je vždy potvrzováno přijetí souvislé sekvence bajtů.
- Potvrzení je generováno dle následujících pravidel:
	1. Při poslání dat je vždy segmentu nastaven příznak ACK a hodnota čísla potvrzení na číslo následující očekávané sekvence.
	2. Pokud příjemce **nemá data k odeslání** a obdrží očekávaný segment a **předchozí** segment **byl potvrzen**, **pozdrží odeslání** potvrzení dokud nepřijde další segment, **maximálně ale 500 ms**. 
		- Toto pravidlo **snižuje celkový počet zaslaných potvrzení**.
	3. Pokud příjemce **obdrží očekávaný segment** a předešlý segment **nebyl potvrzen**, je **okamžitě odesláno potvrzení**. 
		- Toto pravidlo zabraňuje **zbytečnému opakovanému poslání** již poslaného segmentu. V důsledku tohoto pravidla by neměly být více než dva nepotvrzené segmenty.
	4. Pokud příjemce obdrží **neočekávaná segment**, je okamžitě posláno **potvrzení očekávaného segmentu**. 
		- Tímto je **protistrana informována o ztrátě** segmentu
	5. Pokud příjemce **obdrží chybějící segment**, je posláno potvrzení oče**kávaného segmentu**. 
		- Tímto je protistrana informována, že **chybějící segment již přišel**.
	6. Pokud příjemce **obdrží duplicitní segment**, **zahodí jej** a je **posláno potvrzení očekávaného segmentu**. 
		- Toto pravidlo slouží **pro kompenzaci ztracených potvrzení**.

>[!Example] Bezchybová komunikace
>![[MacBook-2024-04-17-001032.png|500]]

>[!Example] Ztracený segment
>![[MacBook-2024-04-17-001033.png | 500]]


#### Zahlcení sítě
- Protokol TCP umožňuje řízení toku dat nejen mezi odesílatelem a příjemcem, ale **také na úrovni sítě** (**mezilehlých uzlů**).
- Kromě posuvného okénka má odesílatel ještě **okno zahlcení**, jehož velikost **je určena stavem sítě.**
- Okno zahlcení udává, kolik dat je **možné poslat**, **aby nedošlo k jejímu zahlcení**. 
- Odesílatel **vždy volí menší z okna zahlcení** a **posuvného okna**.

- Odesílatel řídí tok dat v síti **dle četnosti opětovného zaslání segmentu** následujícím způsobem:
	1. **Fáze pomalého startu.** Okno zahlcení se postupně zvětšuje $1 \times, 2 \times, 4 \times, 8 \times, ...$ až je dosaženo stanovené hodnoty limit. Tato hodnota se v průběhu spojení mění.
	2. **Fáze vyhýbání se zahlcením.** Pokud dojde k potvrzení všech dat v okně zahlcení, je toto okno zvětšeno o hodnotu 1.
	3. **Fáze detekce zahlcení.** V případě, že je detekována potřeba opětovného zaslání segmentu, je dle události, která odeslání spustila, upraveno okno zahlcení.
		- Pokud v**ypršel RTO časovač**: je nastaven limit na hodnotu $\frac{1}{2}$ okna zahlcení a velikost okna zahlcení je nastavena na $1$. Je zahájena fáze pomalého startu.
		- Pokud byl segment poslán na základě detekce tří duplicitních potvrzení: je nastaven limit na hodnotu $\frac{1}{2}$ okna zahlcení a velikost okna zahlcení je nastavena na hodnotu limit. Poté je zahájena fáze vyhýbaní se zahlcení.

![[MacBook-2024-04-17-001034.png| 500]]

### Protokol UDP
- UDP je oproti TCP **výrazně jednodušší**. Zajišťuje pouze **nespojovou nespolehlivou službu** a nedisponuje žádnými prostředky pro řízení toku dat.
- UDP **negarantuje doručení dat**.

- Při použití protokolu UDP se data přenášejí ve formě **UDP datagramů**. 
- Rozdělení do těchto datagramů je ponecháno **na aplikační vrstvě**.

- Přenos dat je **výrazně rychlejší** než přenos dat pomocí TCP. 
- Jednotlivé UDP datagramy **nejsou nijak potvrzovány** a hlavička datagramu **nemusí obsahovat tolik informací**, jelikož není vytvářeno spojení a není řízen tok dat.
![[MacBook-2024-04-17-001035.png]]

##### Navigace
Předchozí:  [[Protokol IP - paket, adresy a podsítě, směrování]]
Následující: [[Systém DNS]]
Celý okruh: [[2. Informační technologie]]