## Účel
- Network Address Translation - překlad síťových adres
- pro komunikaci v IP síti (třeba internetu) potřebuje zařízení unikátní IP adresu, tím vzniká problém:
	- IPv4 má nedostatečný rozsah adres (dnes už téměř na všech úrovních)

- Jedním z možných řešení tohoto problému je NAT
	- Mezi další řešení by patřily dynamické adresy (adresy budou přidělený jen dočasně)
	- IPv6
		- toto je preferovanější varianta než NAT

- NAT = přepisování lokální adresy v IP paketu na přidělenou adresu v síti ISP a naopak 
- pro LAN vyhrazené rozsahy:
	- 10.0.0.0/8
	- 172.16.0.0/12
	- 192.168.0.0/16

### Jak se překládají adresy
- adresa v LAN se při překladu neukládá do paketu (vede si NAT translation table)
- krom IP se přepisuje i port z transportní vrstvy
![[MacBook-2024-04-22-001061.png]]

## Typy
- **Statický NAT (SNAT)**:
	- Překládá jednu vnitřní IP adresu na jednu veřejnou IP adresu.
- **Dynamický NAT (DNAT)**:
	- Přiřazuje veřejnou IP adresu z poolu adres jedné nebo více vnitřním IP adresám.
- **Port Address Translation (PAT)**:
	- Umožňuje mnoha zařízením sdílet jednu veřejnou IP adresu.
	- Tento typ NAT je nejčastěji používán domácnostmi a malými kancelářemi.
	- V tomto případě se kromě IP adresy překládají také porty, aby bylo možné rozlišit jednotlivé interní hosty.

## Problémy
- **narušení koncové end-to-end komunikace**
	- přenos dat jedním směrem není možný, dokud není zahájen druhým
	- problém pro P2P sítě
	- řešení: proxy/relay (prostředním), DNAT (port-triggering), NAT traversal
- **narušení unikátnosti identifikace zařízení**
- **proměna Internetu z nespojové sítě na "jakousi" spojovou**
- **narušení nezávislosti na vyšší vrstvě**
	- využití TCP/UDP portů pro přeposlání IP paketů
- **omezení počtu aktivních TCP spojení a UDP výměn mezi LAN a ISP**
	- okolo 60 tisíc volných TCP/UDP portů na adresu
- **mezi LAN a ISP manipulace s tabulkou překladů**
	- nutné výpočetní zdroje