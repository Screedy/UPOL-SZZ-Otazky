na základě WWW služby
- popisuje prohlížení, ukládání a odkazování navzájem provázaných hypertextových dokumentů uložených v síti.
- uživatelé kteří jsou v této síti si mohou dokumenty prohlížet
### Komunikace po síťi
- **klient-server** architektura
- webová stránka umístěna na **webovém serveru**
- adresy web stránky - **Uniform Resource Location (URL)**
- pro komunikaci serveru a klienta **HTTP(S)** protokol
#### Protokol HTTP(S)
- pro výměnu dat **mezi klientem** a **webovým serverem**
- **HTTP** - Hypertext Transfer Protocol
- **HTTPS** - zabezpečená varianta HTTP

>[!Example] Požadavek HTTP
>```HTTP
>GET /pozadovana-stranka HTTP/1.1
>Host: www.example.cz
>Connection: keep-alive
>User-Agent: Mozilla/5.0
>Accept-Language: cs
>```

>[!Example] Odpověď
>```HTTP
>HTTP/1.1 200 OK
>Date: Thu, 13 Jul 2305 12:34:56 GMT
>Server: Apache/2.4.10 (Debian)
>Content-Type: text/html; charset=UTF-8
>
>data
>```

- **data** - **zdrojový kód** stránky
- **status** - je číselné **značení odpovědi** jestli proběhla správně a informuje o vzniklé situaci:
	- $200$ - OK
	- $301$ - soubor permanentně přesunut
	- $302$ - soubor dočasně přesunut
	- $404$ - soubor nenalezen
	- $410$ - soubor odstraněn
	- $418$ - I'm a teapot
	- $500$ - chyba serveru
#### Uniform Resource Location(URL)
- představuje adresu souboru v síti
>[!Example] Příklad
>```HTTP
>http://www.example.cz/adresa/index.html
>```
>![[url_parts.png| 500]]
>*url*^[https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2022/07/the-structure-of-a-url.webp]

- **první část** - protokol
- **druhá část**- doménové jméno serveru (DNS) - můžeme psát IP - pokud nemá registrované doménové jméno
- **třetí část**- cesta k souboru na serveru a soubor
- . - kořenová adresa
- možnost adresovat soubory na lokálním PC: `C:\muj-web\index.html`

>[!info] Absolutní vs Relativní adresování
>- **absolutní** - jsou cesty které označuj **úplné adresy** které vedou na daný soubor
> 	- `http://www.example.cz/adresa/index.html`
> - **relativní** - adresa souboru k aktuální adrese stránky ve které je použit
> 	- `./index.html`

### Co je webová stránka?
- dříve dokument v síti internet
- dnes těžko definovat (i mobilní nebo desktop aplikace)
- **statické** a **dynamické** webové stránky

>[!Example] Statická stránka
>- tvořena statickým obsahem (dokumenty, obrázky, etc) které je vrácen web serverem
>![[static-page.png|400]]
>*static page*^[https://teleporthq.io/blog/content/images/2022/04/what-is-a-static-site-1.png]

>[!Example] Dynamická stránka
>- dynamický stránka je vytvářena při každém dotazu
>- web aplikace - stránky používají ve větší míře skriptovací jazyk
>- ![[dynamic-page.png|400]]
>- *dynamic page*^[https://teleporthq.io/blog/content/images/2022/04/what-is-a-dynamic-site-1.png]

### Webové technologie
#### Klientské technologie
- technologie na straně klienta (běží)
- **HTML** - struktura, **CSS** - vzhled, **JavaScript** - interakce a manipulace
#### Serverové technologie
- technologie běžící na serveru
- **webový server**, **databázový server**, **aplikační server**
#### Webové standarty
- konsorcium W3C  - vydává specifika popisující webové technologie
- **pouze recommended** $\rightarrow$ pouze doporučení, **prohlížeč může implementovat jinak**


>[!summary] V kostce
> ##### 1. Komunikace v síti:
> - Využití protokolů jako **HTTP(S)** pro **výměnu dat** mezi klientem (webový prohlížeč) a serverem.
> - Adresace zdrojů pomocí URL (Uniform Resource Locator).
> ##### 2. Klientské (Frontend) technologie:
> - **HTML (Hyper Text Markup Language)**: Definuje strukturu webové stránky.
> - **CSS (Cascading Style Sheets)**: Určuje styl a vzhled prvků na stránce.
> - **JavaScript**: Zajišťuje interaktivitu stránky tím, že umožňuje dynamické změny na klientově straně.
> ##### 3. Serverové (Backend) technologie:
> - **Webové servery** jako Apache nebo Nginx, které zpracovávají požadavky na straně serveru.
> - **Aplikační servery** a **databáze** (např. MySQL, MongoDB), které spravují logiku aplikací a úložiště dat.
> - **Skriptovací jazyky na straně serveru** jako PHP, Python, Ruby, které generují dynamický obsah na stránkách.
> ##### 4. Webové standardy a specifikace:
> - Spravovány organizacemi jako W3C (World Wide Web Consortium), které definují standardy pro technologie jako HTML, CSS a JavaScript.
> ##### 5. Statické vs. dynamické stránky:
> - Statické stránky poskytují pevný obsah, který se nemění.
> - Dynamické stránky generují obsah na základě interakcí uživatele nebo serverových procesů.


##### Navigace
Předchozí:  [[IPv6 - vlastnosti, paket, adresy]]
Následující: [[Syntaxe a sémantika HTML a CSS]]
Celý okruh: [[2. Informační technologie]]