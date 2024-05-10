
## Architektura informačního systému
- je to **základní plán** pro **organizaci** a strukturování komponent informačního systému 
- zahrnuje hardware, software, data a procesy
- různé typy architektur jsou navrženy tak, aby vyhovovaly **specifickým potřebám organizací** a **technologickým požadavkům**
- vhodným **komunikačním** prostředkem mezi **vedením a projektanty**
- **minimalizuje** náklady na **chybně zadané projekty**

## Globální architektura
- hlavním modelem globální architektury je model **ICT** služeb
- zaměřuje se na **integraci a koordinaci dat**, **procesů** a **aplikací** napříč různými **geografickými a kulturními hranicemi**
- typy ICT služeb:
	1. **Informační služba**:
		- dodává **poskytovatel příjemci** požadovanou **informaci**
		- dodána **v požadovaném formátu**
	2. **Aplikační služba**:
		- předmětem funkcionalita **business aplikace** (účetnictví, mail, objednávky, ...)
		- často **SaaS** (Software as a Service) v podobě balíků služeb
	3. **Infrastrukturní služba**:
		- **vybudování** a **provoz**
		- **servery**, koncové stanice, LAN a WAN, OS, **komunikační služby**
	4. **Podpůrné služby**
		- služby potřebné pro zajištění ostatních služeb
		- **školení**, **implementace**, **help desk**
	5. **Smíšené**:
		- poradenství, ...

>[!Info]- Stavební bloky globální architektury
>![[MacBook-2024-05-08-001224.png]]
>- EIS - Executive IS
>	- podpora vrcholového řízení
>	- strategické řízení, marketing
>- DSS - Decision support system
>- MSI - Management IS
>	- taktické řízení, sumarizace, agregace, grafická podpora
>- KWS - Knowlage work system
>	- Expertní systémy
>- OIS - Office IS
>- EDI - Electronic Data Interchange
>- TPS - Transaction Processing System

## Vrstvená architektura
- běžný designový vzor, který **rozděluje aplikace na oddělené vrstvy**
- každá **vrstva** poskytuje **konkrétní funkcionalitu**
- umožňuje **lepší organizaci kódu**, **zjednodušuje údržbu** a **zlepšuje** možnosti **škálovatelnost systému**
- typicky do **tří vrstev**:
	1. **Prezenční vrstva**:
		- je odpovědná za **interakci s uživatelem**, **zobrazení dat** a **příjem uživatelských vstupů**
		- komunikuje s aplikační vrstvou
	2. **Aplikační vrstva**:
		- **zpracovává uživatelské vstupy**, provádí obchodní pravidla, a **řídí aplikaci**
		- identifikace, autorizace
		- komunikuje **s prezenční i datovou vrstvou**
	3. **Datová vrstva**:
		- zabývá se **ukládáním** a **načítáním dat** z **databází** nebo jiných úložišť

##### Navigace
Předchozí:  [[Základní pojmy informačních systémů - data, informace, informační systém]]
Následující: [[Tvorba informačních systémů - softwarový proces, metodika vývoje, analýza systému]]
Celý okruh: [[2. Informační technologie]]