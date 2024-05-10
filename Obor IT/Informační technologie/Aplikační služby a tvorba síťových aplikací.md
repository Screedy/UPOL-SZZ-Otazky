## Aplikační vrstva
![[MacBook-2024-04-18-001039.png| 500]]
- Nejvyšší vrstva TCP/IP architektury

- Je tvořena aplikační protokoly.
	- Každý implementuje nějakou službu nebo její část.
	- Protokoly většinou nemají nic společného.

### DHCP (Dynamic Host Configuration Protocol)
- Aplikační protokol, který zajišťuje službu automatické konfigurace hostitelského uzlu v počítačové síti.
- Poskytuje síťové údaje potřebné pro připojení uzlu do počítačové sítě.
- Klient-server služba. 
	- Klient - udp/68
	- Server - udp/67

- Postup získání adresy:
	1. Klient nejprve odešle pomocí broadcast DHCP discover zprávu.
		- DHCP zpráva musí být vložena do UDP datagramu, který je následně vložen do IP paketu. Klient tedy musí vyplnit IP adresu odesílatele a příjemce tohoto paketu. 
		- Adresu odesílatele nastaví na 0.0.0.0 a příjemce na 255.255.255.255.
	2. Server odešle DHCP offer zprávu, ve které nabídne klientovi konfigurační údaje.
		- Údaje jsou po určitou dobu serverem blokovány a nejsou nabízeny nikomu dalšímu.
		- Pokud zprávu klient neobdrží, opakuje 4x odeslnání DHCP discover zprávy s prodlevou 2s. Pokud ji stále neobdrží následuje 5 minutová pauza.
	3. Pokud klient obdrží DHCP offer zprávu, zašle DHCP request zprávu. Tou si zažádá o nabídnutou konfiguraci.
	4. Server po obdržení DHCP request zprávy začle DHCP ack zprávu. Po obdržení klient získává údaje pro síťovou konfiguraci a tu následně provede.

### SSH (Secure shell)
- Služba SSH je služba vzdáleného přihlášení
- Používá port tcp/22.
- Je realizována pomocí protokolu SSH-2. Ten se skládá z:
	- SSH-TRANS (transportní protokol) - vytváří bezpečné připojení pomocí TCP a zajišťuje šifrování a integritu dat
	- SSH-AUTH (autentizační protokol) - zajišťuje autentizaci klienta vůči serveru
	- (SSH-CONN) - (spojovací protokol) - slouží pro správu bezpečných spojení
	- aplikační protokol - popisuje vyměňovaná data
- První tři části je možné použít samostatně a bezpečným kanálem vyměňovat data jiných aplikačních protokolů (SSH tunelování)

### HTTP (Hypertext Transfer Protocol)
- Je to základní protokol, který se využívá pro přístup ke službě WWW.
- Umožňuje zobrazit webové stránky (dokumenty v síti Internet) a posílat požadavky na webové stránky
- Verze:
	- HTTP/1 (už se nepoužívá)
	- HTTP/1.1
	- HTTP/2
	- HTTP/3 (HTTP over QUIC)

- Obecně není šifrovaný. Běžně se pro jeho šifrování používá **SSL/TLS**. Takto šifrovaný HTTP protokol označujeme jako **HTTPS**.

- Protokol **HTTP/1.1** je:
	- čistě textový protokol 
	- vytváří perzistentní spojení 
	- je založen na klient-server architektuře
	- využívá tcp/80 a tcp/443 (HTTPS)

- HTTP je bezstavový protokol (neuchovává informace o klientovi). 
	- Toto je nevhodné.
	- Stav byl do protokolu dodán v podobě cookies. To jsou malé textové soubory uložené na klientovi.

- Při použití HTTP protokolu si mezi sebou klient a server vyměňují HTTP zprávy (request a response).![[MacBook-2024-04-18-001040.png]]

#### Request zpráva
![[MacBook-2024-04-18-001041.png| 600]]

#### Response zpráva
![[MacBook-2024-04-18-001042.png]]

### Elektronická pošta
- Realizována jako klient-server architektura.
![[MacBook-2024-04-18-001043.png]]
- Alice bude chtít poslat mail Bobovi:
	- Alice použije poštovního klienta (aplikaci). 
		- UA - User Agent
		- Umožňuje posílat a přijímat e-maily.
	- Jakmile je e-mail vytvořen, Alice jej odešle. O odeslání se stará Message Transfer Agent (MTA), který je součástí UA. Ten pomocí Extended Simple Mail Transfer Protocol (ESMTP) pošle zprávu mail serveru Alice.
		- Přesněji řečeno: MTA klient, který je součástí Alicina UA, pošle e-mail MTA serveru, který je součástí Alicina mail serveru.
	- Mail server Alice e-mail dále zpracovává. Mohou nastat dva případy:
		1. Bob používá stejný mail server. Mail se zařadí do odpovídajícího mail boxu (poštovní schránky).
		2. Bob používá jiný mail server. E-mail je zařazen do fronty zpráv a následně využije MTA pro přepravu e-mailu na Bobův mail server. 
	- Bobův mail server přijme e-mail a začadí jej do odpovídajícího mail boxu.

- Pokud si Bob bude chtít vyzvednout poštu:
	- Použije svého klienta (aplikaci).
	- O přístup do mail boxu se stará číst klienta, která se označuje Message Access Agent (MAA). MAA, který je realizován jako klient-server služba, pomocí Internet Mail Access Protocol 4 (IMAP4) přistoupí k Bobovu mail boxu a stáhne jeho obsah do Bobova poštovního klienta.

#### Struktura e-mailu
![[MacBook-2024-04-18-001044.png| 400]]

## Tvorba síťových aplikací
- Operační systém na požádání aplikace přiděluje síťový socket. Pomocí socketu aplikace může posílat a přijímat data (Socket API).
- Programátor obvykle potřebuje využívat pouze služby transportní vrstvy.

- Scháma Socket API:![[MacBook-2024-04-18-001045.png]]
- Při vytvoření socketu (funkce `socket()`) se specifikuje typ síťové adresy a transportní protokol
- Sockety podporují různé síťové adresy, například IPv4 adresy se zpřístupňují volbou `AF_INET`.
- Základní typy socketů:
	- `SOCK_STREAM` (TCP)
	- `SOCK_DGRAM` (UDP)
	- `SOCK_SEQPACKET` (SCTP)
	- `SOCK_RAW`(Manuální konstrukce)

- Konkrétní IP adresa a port se nastavují již vytvořenému socketu pomocí funkce `bind()`. 
	- Pokud není specifikován port, je určen OS.
- Komunikace pomocí TCP využívá funkci `connect()` pro navázání spojení. Následně jsou využívány funkce `send()` a `recv()`.
- Komunikace pomocí UDP využívá funkce `sendTo()` a `recvFrom()`.
##### Navigace
Předchozí:  [[Systém DNS]]
Následující: [[Bezpečnost počítačových sítích]]
Celý okruh: [[2. Informační technologie]]