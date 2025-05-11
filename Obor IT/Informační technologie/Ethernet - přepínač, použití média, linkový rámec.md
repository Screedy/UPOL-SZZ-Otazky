### Linková vrstva
![[MacBook-2024-03-18-000913.png]]

### Linkový (ethernetový) rámec
- Zatímco na úrovni fyzické vrstvy jsou data přenášena v jejich surové podobě (sekvence bitů), na úrovni linkové vrstvy jsou data organizována do **linkových rámců**
- Struktura Ethernet II linkového rámce:![[MacBook-2024-03-18-000914.png]]
- Ethernetový rámec má proměnlivou velikost 64-1518 B - závisí na datové části
- Preambule, SFD a mezera nejsou součístí linkového rámce, ale fyzické vrstvy
	- preambule - synchronizace
	- SFD - start frame delimited
	- mezera - odděluje jednotlivé rámce

### Mac adresa
- Každé zařízení v počítačové síti má fyzické síťové rozhraní. (NIC)
- Každé fyzické rozhraní má fyzickou adresu, označujeme jako MAC adresa
- Velikost **6B**, zapisuje se hexadecimálně ve tvaru XX:XX:XX:XX:XX:XX, kde X je $0-9$ nebo $A-F$
	- První 3B - identifikace výrobce
	- ![[MacBook-2024-03-18-000915.png]]
	  Pokud X je 0, jedná se o jedinčnou globální adresu přidělenou výrobcem

- Speciální MAC adresy:
	- **Unicast** adresy - nejméně významný bit  prvního B na 0![[MacBook-2024-03-18-000916.png]]
	- **Multicast** adresy - nejméně významný bit prvního B na 1![[MacBook-2024-03-18-000917.png]]
	- **Broadcast** adresa - ff:ff:ff:ff:ff:ff![[MacBook-2024-03-18-000918.png]]
- Aby bylo možné co nejrychleji identifikovat MAC adresy, jsou bity jednotlivých bajtů posílány v **opačném pořadí**

### Použití média
- Běžně se v počítačových sítích používají různé topologie
	- Sběrnicová, kruhová, hvězdicová, hybridní, full a partial mesh topologie
- Část síťového segmentu, která využívá sdílené médium se označuje jako **kolizní doména**
- Pokud dojde ke kolizi, je třeba opakovat vysílání $\rightarrow$ ovlivňuje přenosovou rychlost
- Je tedy třeba **řídit** přístup k tomuto sdílenému médiu

- **CSMA (Carrier Sense Multiple Access)**
	- Než začne vysílat, poslouchá, zda nevysílá někdo jiný
	- Problém: zpoždění v počítačových sítích $\rightarrow$ chybí detekce kolize![[MacBook-2024-03-18-000919.png| 300]]


- **CSMA/CD (Carrier Sense Multiple Access / Collision Detection)**
	- Jako CSMA, ale jakmile začne vysílat **neustále poslouchá**
	- Pokud dojde ke kolizi okamžitě se zastaví a vyšle signál **JAM**
	- Po odeslání JAM signálu se uzel na náhodnou dobu odmlčí (Výchozí čas podle MAC adresy)

- **CSMA/CA (Carrier Sense Multiple Access / Collision Avoidance)**
	- Snaží se kolizím předcházet
	- V bezdrátových sítích

- Moderní **ethernetový kabel** nevyužívá CSMA/CD, jelikož nedochází ke kolizím

### Switch (přepínač)
- Nejběžnější zařízení používané na **úrovni L2** vrstvy.
- **Předává** (přepíná) přijatý **linkový rámec** na základě položky `adresa přijemce`
- Následně pošle přijatý rámec na **port**, ke kterému je připojeno **NIC** s **MAC adresou** shodnou s položkou `adresa příjemce` **uvedenou v hlavičce**
- Na zbylé porty **není** rámec **předán**
- K realizaci tohoto si udržuje **tabulku**, ve které je ke každému portu uchovávána MAC adresa NIC
	- Možno naplnit ručně nebo automaticky

- **Transparentní bridge** 
	- propojení na L2, které je pro jednotlivé uzly zcela **transparetní** (nevědí o něm)
	- **Nutnost automatického plnění** tabulky switche
	- Při přijetí rámce je do tabulky zaznamenána adresa odesílatele, port a čas přijetí
	- Následně switch prochází svoji tabulku - není-li tam příjemce pošle rámec v tabulce na všechny porty krom portu odesílatele

##### Navigace
Předchozí:  [[Počítačové sítě, jejich služby a architektury]]
Následující: [[Protokol IP - paket, adresy a podsítě, směrování]]
Celý okruh: [[2. Informační technologie]]