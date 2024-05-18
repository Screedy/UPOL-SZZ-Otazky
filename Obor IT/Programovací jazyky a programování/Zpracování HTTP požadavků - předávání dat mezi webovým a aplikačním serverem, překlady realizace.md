- Zpracování HTTP požadavků je klíčovou součástí fungování webových aplikací. 
- Při komunikaci mezi webovým prohlížečem a aplikačním serverem se data přenášejí pomocí HTTP protokolu.

## HTTP Požadavek
- Webový prohlížeč (klient) pošle HTTP požadavek na určitou URL adresu na serveru.
- Požadavek obsahuje metodu (**GET**, **POST**, **PUT**, **DELETE** atd.) a další metadata jako hlavičky (headers) a tělo (body).

>[!Example] Příklad HTTP požadavku
>```HTTP
>GET /index.html HTTP/1.1
>Host: www.example.com
>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
>Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
>Accept-Encoding: gzip, deflate, br
>Accept-Language: en-US,en;q=0.9
>```
>- **Metoda:** GET - říká serveru, že chce získat obsah z dané URL adresy.
>- **URL:** `/index.html` - cílová adresa, ze které chce klient získat obsah.
>- **Verze HTTP:** HTTP/1.1 - verze HTTP protokolu.
>- **Hlavičky (Headers):**
> 	- **Host:** [www.example.com](http://www.example.com/) - označuje webovou stránku, ke které se klient připojuje.
> 	- **User-Agent:** Informuje server o typu a verzi prohlížeče, který klient používá.
> 	- **Accept:** Definuje typy obsahu, které klient akceptuje.
> 	- **Accept-Encoding:** Informuje server o kompresních algoritmech, které klient podporuje.
> 	- **Accept-Language:** Definuje preferovaný jazyk uživatele.

## Aplikační Server
- Aplikační server přijímá HTTP požadavek.
- Zpracovává požadavek a provádí odpovídající operace (např. dotazy do databáze, logiku aplikace).

## Zpracování požadavku
- Aplikační server zpracovává požadavek a generuje odpověď.
- Odpověď může být ve formě HTML stránky, dat ve formátu JSON nebo jiných formátech, v závislosti na požadavku.

## HTTP Odpověď
- Aplikační server odešle HTTP odpověď zpět klientovi.
- Odpověď obsahuje stavový kód (status code), který indikuje, zda byla žádost úspěšná či nikoliv, a také metadata a tělo odpovědi.

>[!Example] Příklad odpovědi
>```HTTP
>HTTP/1.1 200 OK
>Date: Fri, 15 Apr 2024 12:00:00 GMT
>Server: Apache/2.4.48 (Unix)
>Last-Modified: Thu, 14 Apr 2024 08:00:00 GMT
>Content-Length: 1245
>Content-Type: text/html
>
><!DOCTYPE html>
><html>
><head>
> 	<title>Example Page</title>
></head>
><body>
> 	<h1>Hello, world!</h1>
> 	<p>This is an example page.</p>
></body>
></html>
>```
>- **Stavový kód:** 200 OK - označuje, že požadavek byl úspěšně zpracován a že odpověď obsahuje požadovaný obsah.
>- **Datum:** Fri, 15 Apr 2024 12:00:00 GMT - datum a čas, kdy byla odpověď odeslána.
>- **Server:** Apache/2.4.48 (Unix) - označuje webový server, který zpracoval požadavek.
>- **Last-Modified:** Thu, 14 Apr 2024 08:00:00 GMT - označuje datum a čas poslední modifikace zdrojového souboru.
>- **Content-Length:** 1245 - délka obsahu odpovědi v bajtech.
>- **Content-Type:** text/html - označuje typ obsahu odpovědi.
>- **Tělo odpovědi:** Obsahuje HTML obsah stránky "index.html", který je zobrazen v prohlížeči. Obsahuje nadpis `<h1>` a odstavec `<p>` s jednoduchým textem.


### **Zobrazení v prohlížeči:**
- Webový prohlížeč obdrží odpověď a zobrazí ji uživateli.
- Pokud je odpověď HTML stránka, prohlížeč ji zobrazí uživateli. 
- Pokud je odpověď JSON, může být zpracována pomocí JavaScriptu a použita k dynamickému aktualizování obsahu stránky.

## Frameworky
- Překlady realizace HTTP požadavků mohou být realizovány pomocí různých technologií a frameworků v závislosti na potřebách aplikace. 
- Některé z populárních technologií pro zpracování HTTP požadavků jsou:
	- **Node.js s Express:** Pro vytváření webových serverů a API pomocí JavaScriptu.
	- **Django a Flask v Pythonu:** Frameworky pro vývoj webových aplikací a API v jazyce Python.
	- **Ruby on Rails:** Framework pro vývoj webových aplikací v jazyce Ruby.
	- **ASP.NET Core:** Framework pro vývoj webových aplikací v jazyce C#.

##### Navigace
Předchozí:  [[Architektura webové aplikace a problematika škálovatelnosti]]
Následující: [[REST API - popis a příklady realizace]]
Celý okruh: [[3. Programovací jazyky a programování]]