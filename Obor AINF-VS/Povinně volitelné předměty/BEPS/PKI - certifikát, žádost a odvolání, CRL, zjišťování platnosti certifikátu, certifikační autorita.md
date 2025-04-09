- PKI = soubor norem, které ošetřují práci s veřejnými klíči a certifikáty
	- Správa,
	- vydávání,
	- platnost,
	- podepisování,
	- ...

## Certifikát
- **Certifikát** = definovaná struktura, která obsahuje potřebné údaje pro certifikaci veřejného klíče.
	- Identifikační **údaje certifikované strany**.
	- Identifikační **údaje certifikační autority**.
	- Certifikovaný **veřejný klíč**.
	- Sériové číslo certifikátu.
	- **Doba platnosti**.
	- Vymezení způsobu použití.
- Struktura je popsána v Abstract Syntax Notation One.
	- ASN.1 je **standard pro popis struktury dat** nezávislým způsobem.
	- Použítán v telekomunikaci, počítačových sítích a kryptografie.
	- Umožňuje *definovat komplexní datové struktury* a poskytuje způsob, jak tyto struktury serializovat a přenášet mezi různými systémy a aplikacemi.

>[!Example] Nejběžnější kódovací pravidla
> - ASN.1 podporuje několik kódovaných pravidel definující, jak budou data **serializována pro přenos nebo ukládání**.
> 1. **BER (Basic Encoding Rules)**
> 	- Původní sada pravidel.
> 	- Poskytuje flexibilitu, ale může být neefektivní pro některé aplikace.
> 2. **DER** (Distinguished Encoding Rules)
> 	- Podmnožina BER, která poskytuje jednoznačné kódování, často používaná v digitálních certifikátech.
> 3.  **CER** (Canonical Encoding Rules)
> 	- Další podmožina BER s určitými omezeními pro jednoznačné kódování.
> 4. **PER** (Packed Encoding Rules)
> 	- Efektivní kódovací pravidla navržená pro minimalizaci velikosti přenášených dat.

### Popis položek
- **Verze** - *odvozena od verze X.509*
	- 1. verze - pouze základní položky.
	- 2. verze - položky `issuerUniqueID` a `subjectUniqueID`.
	- 3. verze dnes nejpoužívanější, možnost custom rozšíření.
- **Sériové číslo**
	- Nezáporné celé číslo.
	- Jednoznačné v rámci certifikační autority.
	- Obdoba rodného čísla.
	- Velikost do 20 B.
- **Podpisový algoritmus**
	- Specifikace, jakým algoritmem je certifikát podepsán.
- **Vydavatel**
	- Jedinečné jméno certifikační autority.
- Platnost
	- Po vypršení se již nepoužívá k podpisu a k šifrování.
	- Pro dešifrování a ověření podpisu i později.
- **Subjekt**
	- **Unikátní jméno** v rámci certifikační autority.
	- Sekvence relativních jmen:
		- C - countryName
		- ST - stateOrProvinceName
		- L - localityName
		- O - organizationName
		- CN - commonName
		- ...
- **Informace o veřejném klíči**
	- Použitý algoritmus veřejného klíče.
	- Jeho nastavení - např. u RSA délka klíče, n, e.
- **Rozšíření**
	- Trojice $\langle$identifikátor, kritičnost, hodnota$\rangle$
	- Kritickým rozšířením musí aplikace rozumět, jinak odmítnou certifikát.
	- **Basic Constraints**
		- Určuje, zda je certifikát certifikátem CA a omezení cesty certifikátu.
	- **Key Usage** a **Extended Key Usage**
		- Specifikuje účely, pro které může být veřejný klíč použit.
		- Např. digitální podpis, šifrování klíče.
	- **Subject Alternative Name**
		- Umožňuje specifikovat další identifikátory pro subjekt, jako je e-mail nebo IP.
	- **Authority Key Identifier**
		- Identifikuje veřejný klíč, který odpovídá soukromému klíči použitý k podpisu cerifikátu.
	- **Subject Key Identifier**
		- Identifikuje veřejný klíč předmětu.
	- **CRL Distribution Points**
		- Kde nalezneme seznam odvolaných certifikátů.

## Kvalifikovaný certifikát (QCA)
- QCA je **speciální typ** digitálního certifikátu umožňující splňovat **přísné požadavky stanovené právními a technickými normami**.
- Jsou vydávány **kvalifikovanými poskytovateli služeb vytvářejících důvěru** (QTSP - Qualified Trust Service Providers) a jsou určeny pro použití v **právně závazných digitálních transakcích**.
- Kvalifikovaný certifikát je považován za nejvyšší úroveň důvěryhodnosti mezi digitálními certifikáty.
- V ČR tři CA pro QCA - PostSignum, 1.CA, eldentity
- **Identifikační údaje**: jméno, příjmení, adresa, ...
- **Rozšíření**: titul, datum a místo narození, pohlaví, občanství, ...

## Odvolání platnosti certifikátu
- V případě **smazání či kompromitace** soukromého klíče je potřeba **zneplatnit certifikát**.
	- Smazání není tolik kritické.
	- Kompromitovaný soukromý klíč je potřeba odvolat co nejrychleji.

- Postup pro odvolání certifikátu:
	1. Kontaktujte certifikační autoritu (CA):
		- Většina CA má definované postupy pro odvolání certifikátů a poskytuje zákaznickou podporu, která pomůže s procesem.
	- **2a. Poskytněte identifikační údaje**
		- Při kontaktu s CA potřeba poskytnout identifikační údaje.
		- Ty prokážou, že jste oprávněný vlastník certifikátu.
	- **2b. Použijte revokační heslo nebo PIN**

## Certificate Revocation List (CRL)
- CRL je **seznam odvolaných certifikátů**.
- Je to **digitálně podepsaný** dokument vydávaný certifikační autoritou.
- Obsahuje **seznam digitálních certifikátů**, které byly **předčasně zneplatněny** (odvolány) před vypršením jejich platnosti.
- Umožňuje ověřovatelům zjistit, zda jsou certifikáty, které se pokoušejí ověřit, stále platné.

### Ověření platnosti certifikátu
- OCSP (Online Certificate Status Protocol) je klient-server protokol pro **ověřování stavu digitálních podpisů v reálném čase**.
- Efektivnější a flexibilnější alternativa k tradičním CRL.
- Je široce používán např. v HTTPS, e-mailových klientech a dalších bezpečnostních aplikacích.

>[!Example] Průběh
>- Dotaz:
>	- Číslo certifikátu
>	- Kontrolní součet jména CA
>	- Kontrolní součet veřejného klíče CA
>-  Odpověď:
>	- OCSP obálka
>	- Odpověď (kdo, čas, číslo, status)

## Žádost o certifikát
- Tři formy pro žádost o certifikát
	- RFC-1424: PEM, neujal se
	- RFC-2314: PKCS#10
	- RFC-2511: CRMF
- Nejčastěji používaný je **PKCS#10**
	- Vhodný pouze pro certifikáty schopné elektronického podpisu.

- Na žádost můžeme prohlížet jako na certifikát podepsaný "sám sebou"
- Podpisem **prokážeme držení soukromého klíče**. Nepodepsané žádosti jsou zahozeny.
