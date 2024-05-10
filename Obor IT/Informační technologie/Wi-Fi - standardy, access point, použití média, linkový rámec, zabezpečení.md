
## Standardy a frekvence
- (legacy)/b/g
	- Nově **Wi-Fi 0/1/2**
	- 1997/1999/2003
	- pásmo 2.4 GHz
	- rychlosti 2/11/54 Mb/s
- a/ac
	- Nově **Wi-Fi 2/5**
	- 1999/2013
	- pásmo 5 GHz
	- rychlosti 54 Mb/s / 6.9 Gb/s
- n/ax
	- Nově **Wi-Fi 4/6**
	- 2008/2019
	- pásmo 2.4 a 5 GHz
	- rychlosti 0.6 Gb/s / 9.6 Gb/s
- ax
	- Nově **Wi-Fi 6E**
	- 2020
	- pásmo 6 GHz
	- rychlosti 9.6 Gb/s

- ad/ay
	- Nově **WiGig**
	- 2012/2021
	- pásmo 60 GHz
	- rychlosti až 7/40 Gb/s

## AP

## Použití média
- Wi-Fi používá **rádiové vlny** pro přenos dat mezi zařízeními. 
- Signál může být ovlivněn mnoha faktory
	- fyzické překážky
	- interference od jiných zařízení
	- vzdálenost od přístupového bodu

### CSMA/CA (Carrier Sense Multiple Access /Collision Avoidance)
- **náhodný vícenásobný přístup** k sdílenému médiu je **problém**
- **/CA**: předcházení kolizím
	- náročné/nemožné současně přijímat a vysílat
		- **poloduplexní přenos**, **problém skryté/vystavené stanice**
	- možno více současných vysílání (bez detekce kolizí)
	- využívá **mechanismus pozitivního potvrzování** (ACK)
		1. Při klidu chvíle čekání (DIFS), jinak náhodná pauza
		2. Vysílání celého rámce, příjemce po chvíli od přijetí potvrdí, pokud do určité doby ne, tak znovu 1. krok

### Rezervace média
- **volitelné** 
- určené pro **delší vysílání stanice** (ne AP)
1. žádost směrem k AP s časem pro přenos dat, stanice očekává potvrzení
2. AP vyšle všem po chvíli (**SIFS**) rezervaci média (**CTS**) na čas pro stanici
3. vysílání dat a jejich potvrzování, ostatní po čas nezkouší vysílat

![[MacBook-2024-04-19-001050.png| 500]]

## Linkový rámec
- data až 2312B (obvykle **do 1500B** jako u **ethernetu**)
- před rámcem **záhlaví fyzické vrstvy** (rádia)
![[MacBook-2024-04-19-001051.png]]
- až **4 MAC adresy**
	1. **přijímající** stanice
	2. **vysílající** stanice
	3. **přijemce/odesílatel** v infrastruktuře
	4. pokud se jedná o komunikaci **mezi více sítěmi**
		- V takovém případě by **3. adresa byl příjemce** a **4. adesílatel**
![[MacBook-2024-04-19-001052.png]]

- řídící pole (frame control field expanded)
	1. verze (00)
	2. typ       - $\downarrow$ 
	3. subtyp - pro rozlišení rámců (control, management a datové)
	4. od - $\downarrow$
	5. do - význam adres 3 a 4
	6. indikace více fragmentů
	7. opakování rámce
	8. power management
	9. more data
	10. šifrování dat rámce
	11. rezervovaný

### Zabezpečení
- Původní specifikace **WEP** (**problém**)
- dočasné **WPA**, pak **WPA2** a nejnovější **WPA3**
- **Autentizace**:
	- Stanice vůči AP (**AP se vždy důvěřuje**)
	1. Pomocí sdíleného hesla (**personal**)
	2. autentizační protokol (**enterprise**) - až od **WPA2**
- **Šifrování**
	- Šifrují se rámce, data a kontrolní součet rámce
	- u WPA2/3 se šifrují i některé hlavičky
- **WPS** (Wi-Fi Protected Setup)
	- generování a distribuce SSID a nastavení zabezpečení z AP na stanice

##### Navigace
Předchozí:  [[Bezdrátové sítě - režimy, přenosové médium, problémy, bezpečnost]]
Následující: [[NAT - účel, typy, problémy]]
Celý okruh: [[2. Informační technologie]]