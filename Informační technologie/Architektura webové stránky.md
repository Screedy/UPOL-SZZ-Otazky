### 1. Komunikace v síti:
- Využití protokolů jako HTTP(S) pro výměnu dat mezi klientem (webový prohlížeč) a serverem.
- Adresace zdrojů pomocí URL (Uniform Resource Locator).
### 2. Klientské (Frontend) technologie:
- **HTML (Hyper Text Markup Language)**: Definuje strukturu webové stránky.
- **CSS (Cascading Style Sheets)**: Určuje styl a vzhled prvků na stránce.
- **JavaScript**: Zajišťuje interaktivitu stránky tím, že umožňuje dynamické změny na klientově straně.
### 3. Serverové (Backend) technologie:
- **Webové servery** jako Apache nebo Nginx, které zpracovávají požadavky na straně serveru.
- **Aplikační servery** a **databáze** (např. MySQL, MongoDB), které spravují logiku aplikací a úložiště dat.
- **Skriptovací jazyky na straně serveru** jako PHP, Python, Ruby, které generují dynamický obsah na stránkách.
### 4. Webové standardy a specifikace:
- Spravovány organizacemi jako W3C (World Wide Web Consortium), které definují standardy pro technologie jako HTML, CSS a JavaScript.
### 5. Statické vs. dynamické stránky:
- Statické stránky poskytují pevný obsah, který se nemění.
- Dynamické stránky generují obsah na základě interakcí uživatele nebo serverových procesů.

---

- na základě WWW služby
	- popisuje prohlížení, ukládání a odkazování navzájem provázaných hypertextových dokumentů uložených v síti.
	- Uživatelé kteří jsou v této síti si mohou dokumenty prohlížet

### Komunkace po síťi

- klient-server architektura
- webová stránka umístěna na webovém serveru
- adresy web stránky - **Uniform Resouce Locationn (URL)**
- pro komunikaci serveru a klienta HTTP(S) protokol

#### Protokol HTTP(S)

- pro výměnu dat mezi klientem a webovým serverem
- HTTP - Hyper Transfer Protocol
- HTTPS - zabezpečená varienta HTTP
- požadavek:
	- ![[req.png]]
- odpověd:
	- ![[res.png]]
	- **data** - zdrojoví kód stránky
	- **status** - je číselné značení odpovědi jestli proběhla správně a informuje o vzniklé situaci
		- 200 - OK
		- 301 - soubor permanentně přesunut
		- 302 - soubor dočasně přesunut
		- 404 - soubor nenalezen
		- 410 - soubor odstraněn
		- 500 - chyba serveru

#### Uniform Resource Location(URL)

- představuje adresu souboru v síťi
$$http://www.example.cz/adresa/index.html.$$
- první část - protokol
- druhá - doménové jméno serveru (DNS) - můžeme psát IP - pokud nemá registrované doménové jméno
- třetí - cesta k souboru na servru a soubor
- . - kořebá adresa
- možnost adresovat soubory na lokálním PC

**Absolutní vs Realtivní adresování**

- absolutní - jsou cesty které označuj úplné adresy které vedou na daný soubor
- relativní - adresa souboru k aktuální adrese stránky ve které je použita

### Co je webová stránka?

- dříve dokument v síti internet
- dnes těžko definovat (i mobilní číi deskotp app)
- statické a dynamické web stránky

#### Statická stránka

- tvořena statickým obsahem (dokumenty, obrazky, etc) které je vrácen web servrem.
![[static.png]]

### Dynamická stránka

- dynamický stránka je vytvářena při každém dotazu. 
- web aplikace - stránky používajíc ve větší míře skriptovací jazyk
![[dynamic.png]]

### Webové technologie

#### Klientské technologie

- tetchnologie na straně klienta (běží)
- HTML - struktura, CSS - vzhled, JavaScript - interakce a manipulace

#### Serverové technologie

- technologie běžící na serveru
- weboví server, databázoví server, aplikační server

#### Webové standarty

- konsorcium W3C  - vydává specifika popisující webové technologie
- pouze recommended -> pouze doporučení, prohlížeč může implementovat jinak

##### Navigace
Předchozí:  [[IPv6 - vlastnosti, paket, adresy]]
Následující: [[Syntaxe a sémantika HTML a CSS]]
Celý okruh: [[2. Informační technologie]]