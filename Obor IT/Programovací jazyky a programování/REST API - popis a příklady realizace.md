- **REST API** (Representational State Transfer API) je architektonický styl pro vytváření síťových aplikací
- REST je způsob, jakým systémy mohou komunikovat přes HTTP podobně jako webové aplikace
- RESTful API používá standardní metody HTTP jako GET, POST, PUT, DELETE atd. k manipulaci s datovými zdroji

- Ilustrace architektury REST API:
![[REST API.png]]

## Popis:
1. **Zdroje (Resources)**: Každý zdroj má jedinečný identifikátor (URI), kterým je možné k němu přistupovat. Například, pokud máme databázi uživatelů, každý uživatel by mohl mít svůj unikátní URI jako `/users/{id}`.
2. **Operace (Operations)**: Klient může provádět operace nad zdroji pomocí standardních HTTP metod. GET pro čtení, POST pro vytvoření, PUT pro aktualizaci a DELETE pro smazání zdroje.
3. **Reprezentace (Representation)**: Data, která jsou posílána mezi klientem a serverem, jsou reprezentována v určitém formátu, jako je JSON, XML, HTML atd.
4. **Stav aplikace (Statelessness)**: Každá požadavek od klienta na server musí obsahovat všechny informace potřebné pro porozumění a zpracování tohoto požadavku. Server neuchovává žádný kontext o klientovi mezi jednotlivými požadavky.
5. **Jednotné rozhraní (Uniform Interface)**: Rozhraní mezi klientem a serverem by mělo být jednotné, aby bylo snadné pro klienty porozumět a používat. To zahrnuje standardní HTTP metody a formáty dat.

## Příklady:
1. **Webová aplikace s REST API**: 
	- Webová aplikace může mít REST API pro komunikaci s backendem. 
	- Např.  pro získávání informací o uživatelích, jejich příspěvcích a dalších dat.
2. **Mobilní aplikace s REST API**: 
	- Mobilní aplikace může komunikovat se vzdáleným serverem pomocí REST API. 
	- může posílat požadavky na server pro získání dat nebo aktualizaci informací.
3. **IoT zařízení s REST API**: 
	- IoT zařízení může poskytovat REST API pro vzdálený přístup a správu. 
	- Např. pro ovládání osvětlení, termostatu a dalších zařízení.
4. **Cloudová služba s REST API**: 
	- Cloudová služba může poskytovat REST API pro manipulaci s daty v cloudu. 
	- Např. pro nahrávání, stahování a správu souborů.
5. **E-commerce platforma s REST API**: 
	- E-commerce platforma může poskytovat REST API pro správu produktů, objednávek a plateb. 
	- To umožňuje vývojářům integrovat platformu s různými aplikacemi a službami.

## Příklad dotazu:
1. Získání informací o uživateli:
	```JSON
	GET /users/123 HTTP/1.1
	Host: api.example.com
	```
2. Přidání nového uživatele:
	```JSON
	POST /users HTTP/1.1
	Host: api.example.com
	Content-Type: application/json
	
	{
	  "name": "Jan Novak",
	  "email": "jan.novak@example.com"
	}
	```
3. Aktualizace uživatele:
	```JSON
	PUT /users/123 HTTP/1.1
	Host: api.example.com
	Content-Type: application/json
	
	{
	  "email": "novy.email@example.com"
	}
	```
4. Smazání uživatele:
	```JSON
	DELETE /users/123 HTTP/1.1
	Host: api.example.com
	```


##### Navigace
Předchozí:  [[Zpracování HTTP požadavků - předávání dat mezi webovým a aplikačním serverem, překlady realizace]]
Následující: [[JavaScript na webovém frontendu a jeho možnosti]]
Celý okruh: [[3. Programovací jazyky a programování]]