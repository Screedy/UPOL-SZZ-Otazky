- V dnešní době je již těžké vymezit co je webová aplikace a co ještě ne. 
- Původně byly www stránky statické a za webovou aplikaci se označovala j**akákoliv stránka obsahující script**. Dnes scripty používají **snad všechny** webové stránky. 
	- Proto je těžké určit hranici. 
- Většina webových aplikací ale využívá **kromě webového serveru** ještě **aplikační** a navíc například **databázi**. 
- Obecně můžeme říct, že webová aplikace označuje webové stránky, kde je **ve větší míře používán programový kód** na straně klienta nebo serveru.

---

- V dnešní době nemají ale webové aplikace podobu pouze dynamické webové stránky, ale mohou být realizovány jako **mobilní nebo desktopové aplikace**. 
- Poněkud přesněji je tedy možné webovou aplikaci vymezit jako aplikaci, která potřebuje pro neomezené fungování přístup k Internetu nebo jádro prohlížeče.

>[!Example] Statická webová stránka
>![[Statiická web stránka.png]]

>[!Example] Webová aplikace
>![[Webová aplikace.png]]

>[!success] Výhody webových aplikací
> - Dostupně po internetu - rychlé aktualizace, možnost vynucení aktualizace
> - Dobrá škálovatelnost - možno využít výkonu serverů a není omezena na zdroje zařízení
> - Multiplatformnost

>[!fail] Nevýhody
>- Bezpečnost - náročné na zajištění kvůli vzdálenému přístupu
>- Technologicky náročné - velké množství technologií, které je třeba ovládat

## Výčet technologií

### Front-end technologie
- Front-end technologie se zaměřují na vývoj části webové aplikace, se kterou interagují uživatelé.
- **HTML (HyperText Markup Language)**
	- Jazyk pro vytváření struktury webových stránek.
	- Umožňuje definovat různé prvky jako text, obrázky, odkazy, formuláře atd.
- **CSS (Cascading Style Sheets)**
	- Používá se pro stylování HTML dokumentů.
	- Umožňuje definovat layout, barvy, písma a další vizuální aspekty.
- **JavaScript**
	- Skriptovací jazyk pro vytváření interaktivních webových stránek.
	- Umožňuje manipulaci s DOM (Document Object Model), provádění asynchronních operací (AJAX) a mnoho dalšího.
- **Front-end frameworky a knihovny**
	- **React** - Knihovna pro budování uživatelských rozhraní
	- **Angular** - Framework pro vývoj webových aplikací
	- **Vue.js** - Progresivní framework pro budování uživatelských rozhraní

### Back-end technologie
- Back-end technologie se zaměřují na serverovou část webové aplikace, která zajišťuje logiku, databázové operace, autentizaci a další funkcionality.
- **Programovací jazyky**
	- **JavaScript (Node.js)** - JavaScript běžící na serveru, umožňuje vytvářet škálovatelné a rychlé aplikace.
	- **Python (Django, Flask)**
	- **PHP (Laravel)**
	- **Ruby (Ruby or Rails)**
- **Webové servery**
	- **Apache**
	- **Nginx**
- **Databáze**
	- **Relační databáze (SQL)** - MySQL, PostgreSQL, ...
	- **NoSQL databáze** - MongoDB, Redis, ...

### DevOps a nasazení
- DevOps praktiky a nástroje jsou důležité pro automatizaci, monitorování a správu aplikací po nasazení.
- **Kontinuální integrace a kontinuální nasazení (CI/CD)**
	- **Jenkins** - Automatizační server pro CI/CD
	- **GitLab CI/CD** - Integrované CI/CD v GitLab platformě
- **Kontejnerizace a orchestrace**
	- **Docker** - Platforma pro vytváření, nasazení a správu kontejnerů.
	- **Kubernetes** - Systém pro orchestrace kontejnerizovaných aplikací, umožňuje automatizaci nasazení, škálování a správu kontejnerů.
- **Cloudové služby**
	- **AWS (Amazon Web Services)** - Široká škála služeb pro hostování, databáze, úložiště a další.
	- **Microsoft Azure**
	- **GCP (Google Cloud Platform)**

### Bezpečnost
- Bezpečnost je klíčovou součástí vývoje webových aplikací, zahrnuje ochranu proti různým typům útoků a zajištění integrity a důvěrnosti dat.
- **Autentizace a autorizace**
	- **OAuth, OpenID** - Standardní protokoly pro autentizaci
- **Bezpečnostní praktiky**
	- **HTTPS** - Šifrování přenosu dat pomocí SSL/TLS.

##### Navigace
Předchozí:  [[Zařazení jazyka C mezi ostatní jazyky, výhody a nevýhody]]
Následující: [[Architektura webové aplikace a problematika škálovatelnosti]]
Celý okruh: [[3. Programovací jazyky a programování]]