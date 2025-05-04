### Síťová vrstva TCP/IP architektury
![[MacBook-2024-03-24-000937.png]]
- Síťová vrstva je **nezávislá** na nižších vrstvách.
- Úkolem této vrstvy je **jedinečná identifikace uzlů** v síti a zajištění komunikace mezi uzly které se **nenacházejí ve stejné lokální síti**.
- Síťová vrstva je tvořena několika protokoly, tím nejdůležitějším je IP (Internet Protocol)
	- Umožňuje propojení více sítí a poskytuje **nespolehlivý přenos dat**
	- Další protokoly: ICMP, IGMP, ARP (sporné zda patří do L3 nebo L2)

### IP paket (IPv4)
- Na úrovni síťové vrstvy jsou data **přenášena** ve formě **IP paketů**
![[MacBook-2024-03-24-000938.png]]
- Obsahuje:
	- Hlavičku ve velikosti minimálně 20B
		- V ní je vyhrazena sekce pro volitelné položky o velikosti až 40B
		- Může tedy mít až 60B
	- Za hlavičkou je datová část obsahující data z vyšší vrstvy
- Políčko verze má pouze historický význam, nerozlišuje IPv4 a IPv6 (je vždy 4).

### IP adresa
- **Každý** uzel v síti je **jedinečně identifikován** pomocí IP adresy
- IPv4 adresa je číslo o velikost **32b**, pro přehlednost se zapisuje **dekadicky po** jednotlivých **bajtech** ve tvaru **X.X.X.X**, kde **X** je hodnota $0-255$
- Položka IP adresa odesílatele a IP adresa příjemce v hlavičce IP paketu jsou IP adresy uzlů, které mezi sebou komunikují.

- 32b umožňuje adresovat $2^{32} = 4.294.967.296$ různých adres.

- O přidělování IPv4 adres v síti Internet se starají různé organizace
	- **IANA** (Internet Assigned Numbers Authority) - celosvětové IP adresy, přidělení jednotlivým regionům
	- **RIR** (Regional Internet Registry) - přidělují dalším jednotkám (např. státům).
- IPv4 adres **není dostatek** - na nejvyšších úrovních už **došly**

#### Adresace
- IP adresa se dělí na **adresu sítě** a **adresu uzlu**
- Rozlišujeme dva typy adresace:
	- **Classful**
	- **Classless**

##### Classful
- Adresní prostor rozdělen do tříd $A-E$
- Každá třída má pevně danou velikost pro adresu sítě a uzlů v síti
  ![[MacBook-2024-03-24-000939.png]]
- Dnes se již **nepoužívá**.

##### Classless
- Adresa sítě a uzlu je určena pomocí **síťové masky**.
- Narozdíl od Classful adresace je **hierarchická**.

- Síťová maska:
	- Má stejnou velikost jako IP adresa 
	- Rozděluje se na dvě části: **adresa sítě** a **adresa v síti**
	- Tyto části jsou určeny: 
		- nepřerušenou sekvencí **po sobě jdoucích jedniček** (část pro **adresu sítě**)
		- nepřerušenou sekvencí **po sobě jdoucích nul** (číst pro **adresu v síti**)
	- Počet po sobě jdoucích jedniček se označuje jako **délka masky**
	- Zapisuje se:
		- Stejně jako IP adresa (255.255.255.0)
		- **CIDR** formátu (**/24**)

- Adresu sítě snadno získáme z IP adresy provedením logického součinu (**operace AND**) **na IP adresu a masku sítě**
	- 192.168.1.42 AND 255.255.255.0 $\rightarrow$ 192.168.1.0

- První a poslední adresa v síti je **vyhrazena** pro **adresu sítě** a pro **broadcast** adresu
![[MacBook-2024-03-24-000940.png]]

- Počet adres v síti je určen jako $2^{32-n}$, kde $n$ je délka masky
- **Broadcast** adresu zjistíme jako **IP OR (NOT maska)**.

##### Speciální IP adresy
- **127.0.0.1/8** - zpětná smyška (**loopback**)
- 10.0.0.0/8 - adresa lokální sítě (24b na adresu v síti)
- 172.16.0.0/12 - adresa lokální sítě (20b na adresu v síti)
- **192.168.0.0/16** - adresa lokální sítě (16b na adresu v síti)
- **192.168.x.0/24** - adresa lokální sítě (8b na adresu v síti), x je 0-255
- 0.0.0.0/32 - host, komunikace, při které odesílatel nezná svoji IP adresu
- **255.255.255.255/32** - omezený broadcast (pouze v lokální síti)

#### Tvorba podsítí
- Sítě je možné dále dělit na menší části (podsítě)
- Případně je možné podsítě **spojovat do větších** sítí.
- Obojí se realizuje **manipulací** se síťovou **maskou**.

- Rozdělení sítě na podsítě umožňuje snadnější správu.
- Při tvorbě podsítí se původní adresní prostor **zmenší** o $m$ bitů, které se využijí pro **adresaci podsítí**.
- To se provede prodloužením délky síťové masky o $m$ bitů.
- Je tedy tvořena původní adresou sítě a $m$ bity, které byly ukrojeny z původního adresního prostoru v síti
![[MacBook-2024-03-24-000941.png]]

- Tvorbu podsítí můžeme realizovat dvěma způsoby:
	1. **Konstantní maska**
		- Rozdělení na stejně velké podsítě pomocí konstantní masky.
		- Příklad:![[MacBook-2024-03-24-000942.png]]
	2. **Variabilní maska**
		- Rozdělení na různě velké podsítě pomocí variabilní masky
		- Docílíme **menšího plýtvání**
		- Nejprve podsítě **seřadíme** dle jejich **velikosti** a postupně jim přidělujeme adresy
		- Příklad:![[MacBook-2024-03-24-000943.png]]

#### Přidělení IP adresy koncovým uzlům
- **Statické přidělení** - adresa je manuálně přidělena
	- **Nepraktické**, pokud se do sítě často připojují a odpojují uzly (např. **bezdrátové sítě**)
- **Dynamické přidělení** - **DHCP**
	- Poskytuje **klient-server službu**, kdy klient automaticky **požadá** o přidělení IP adesy a DHCP server mu ji **poskytne**.

### Komunikace v lokální síti
- Komunikace mezi uzly propojenými na úrovni vrstvy **L2** se označuje jako **komunikace v lokální síti**.
- Je třeba znám **MAC adresu příjemce**, jelikož IP packet je vkládán do linkového rámce.
- Při komunikaci na úrovni L3 vrstvy se využívají pouze IP adresy. Je tedy třeba zajistit překlad **IP adresy na MAC adresu**.
	- Zjistit k dané IP adrese MAC adresu NIC. Tento překlad zajištuje **protokol ARP** (posílající *ARP zprávu* pomocí broadcast).
	- ARP zprávy mohou představovat bezpečnostní hrozbu (útok *ARP spoofing*)
	- Možnost obrany pomocí statické ARP cache nebo automatické detekce útoku
### Směrování mimo lokální síť
- Hlavním úkolem síťové vrstvy je **nalezení nejvhodnější cesty** a následné **odesílání IP paketů** touto cestou mimo lokální síť.
- Komunikaci mimo lokální síť lehce **poznáme porovnáním adres** sítí odesílatele a příjemce.
- Směrování je realizováno pomocí předávání paketů na síťových rozhraních jednotlivých zařízení. **Typicky realizované routerem**. Směrování je rozhodováno na základě IP adresy příjemce IP paketu a směrovací tabulky. Ta obsahuje informace o dalším uzlu sítě (next-hop), který má být paket předán.

##### Navigace
Předchozí:  [[Ethernet - přepínač, použití média, linkový rámec]]
Následující: [[Protokoly TCP a UDP - spojení a řízení toku dat]]
Celý okruh: [[2. Informační technologie]]