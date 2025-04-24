- **Autentizace uživatele** = **proces ověření uživatele** (počítače), uživatel se prokazuje, že je to skutečně on
- **Autorizace uživatele** = **udělení konkrétních práv** uživateli po jeho autentizaci.

- Základní způsoby autentizace:
	- Uživatel zná něco (pseudo) unikátního, jako je například *heslo*, URL s hashem (ověření emailu)
	- Uživatel má něco *unikátního*, což může být například **soukromý klíč**, **telefon**, přístup k emailu
	- Biometrika uživatele jako například **otisk prstu, face id, ...**
		- Mezi "*biometriku*" počítače/aplikace by se mohlo dát zahrnout:
			- Digitální certifikáty
			- TPM (Trusted Platform Module) - speciální mikroprocesor navržený pro bezpečné kryptografické operace
			- Softwarové podpisy
			- Device identity - jedinečné identifikátory zařízení (MAC, sériová čísla, ...)

## Autentizace heslem
- Heslo = **tajná sekvence znaků**, kterou by měl znát **pouze uživatel**.
- Vlastnosti silného hesla:
	- **Délka**: Heslo by mělo mít aspoň 12 znaků. Delší hesla jsou obecně bezpečnější, protože jsou obtížnější k prolomení.
	- **Komplexita**: Heslo by mělo obsahovat kombinaci různých typů znaků:
		- Velká písmena (A-Z)
		- Malá písmena (a-z)
		- Číslice (0-9)
		- Speciální znaky (!, @, #, ...)
	- **Náhodnost**: Heslo by mělo být náhodné a nemělo by obsahovat snadnou hodnutelné informace, jako je jméno, datum narození nebo jednoduchá slova.
	- **Unikátnost**: Každý účet by měl mít své vlastní unikátní heslo.
		- Použití stejného hesla pro více účtů zvyšuje riziko, že pokud bude jedno heslo prolomeno, budou ohroženy i ostatní účty.
	- **Vyhnout se bězným frázím**: Hesla by neměla obsahovat bězné fráze, slova nebo vzory, které lze snadno uhodnout nebo prolomit pomocí slovníkových útoků 
		- např. "password", "123456", "qwerty"

## Password manager
- Správce hesel může generovat a uchovávat složitá hesla za vás, takže si nemusíte pamatovat každé jednotlivé heslo.
- Bezpečnost:
	- Silné šifrování: Kvalitní správci hesel používají silné šifrovací algoritmy (např. AES-256).
	- Zero-knowledge architektura: Mnoho správců hesel používá tzv. zero-knowledge architekturu, což znamená, že poskytovatel služby nemá přístup k vašim šifrovaným datům a nemůže vidět vaše hesla ani hlavní heslo.
- Rizika:
	- Výběr správného správce hesel.
	- Zabezpečení hlavního hesla.

## Jednorázová hesla
- *Problém je, pokud nám někdo odcizí heslo, tak jej může využívat dokud si toho nevšimneme a nezměníme*
- **Jednorázová hesla** (OTP - One-Time Passwords) jsou hesla, *která jsou platná pouze* **po dobu uživatelovi autentizace**, pro další autentizaci je vyžadováno jiné.

- Může být řešeno pomocí:
	- **Seznam jednorázových hesel**
	- **Rekurentní algoritmus** (S/KEY, OTP)
	- **Zaslání jednorázového hesla jiným kanálem** (SMS, email, telefon, ...)

## Rekurentní algoritmus
- Máme nějakou jednosměrnou funkci $f$ (často je používána hashovací funkce):
	- Musí být **snadné** vypočítat $f(x)$.
	- Musí být **velmi obtížné** najít takové $y$, že $y=f(x)$.
- $f^{n}(x)$ poté značí $n$-krát použití funkce $f$ s počátečním řetězcem $x$.
	- např. $f^{4}(x)=f(f(f(f(x))))$.

- Postup:
	- **Inicializace**:
		- Uživatel si **zvolí tajný řetězec seed**.
		- Uživatel si **zvolí čáslo** $n$ a **spočítá** $f^{n}(\text{seed})$ a dvojici $<n, f^{n}(\text{seed})>$ pošle autentizující aplikaci.
	- **Autentizace**:
		- Uživatel pošle serveru jméno (informaci o uživatelovi).
		- Server nalezne v db současné $n$ a **odešle uživateli** $n-1$.
		- Uživatel spočítá $f^{n-1}(\text{seed})$ a pošle jej serveru
		- Server **spočítá** $f(f^{n-1}(\text{seed}))$ a ověří, zda se rovná s $f^{n}$ v db.
		- Server **sníží** $n$ a předělá $f^{n}$ **na** $f^{n-1}$ v db.

## S/KEY
- **S/KEY** je systém jednorázových hesel.
- Vyvinut v 80. letech jako metoda autentizace uživatelů bez nutnosti přenášet nebo ukládat citlivé informace.
- Tento systém **využívá kryptografické hashovací funkce** (pouze MD4 - dnes už nedostatečná) a **rekurentní algoritmus** (je to konkrétní implementace rekurentního algoritmu) pro generování řady jednorázových hesel.
- **Tajné heslo** (seed) je *zkombinováno* s **náhodnou hodnotou nebo sekvencí** (sůl)
	- Tu zná uživatel i autentizační server.
	- Klient může mít stejný seed pro více serverů.
	- Parametry $n$ a *sůl* jsou **definovány serverem**.
- Výstup hashovací funkce dělí na poloviny a poté použije XOR.

## OTP
- Rozšiřuje S/KEY o **MD5** a **SHA1**, povinná je však pouze MD5, která v dnešní době **taky není bezpečná**.
- Definuje formát zpráv pro autentizační komunikaci.