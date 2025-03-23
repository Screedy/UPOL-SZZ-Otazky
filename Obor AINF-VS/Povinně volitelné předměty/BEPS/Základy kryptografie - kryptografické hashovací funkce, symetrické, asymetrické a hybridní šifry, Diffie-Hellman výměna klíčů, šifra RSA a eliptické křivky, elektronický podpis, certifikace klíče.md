- **Kryptografie** = věda o **utajování** zpráv
- **Kryptoanalýza** = věda o **luštění šifrovaných** zpráv
- **Kryptologie** = věda zahrnující **kryptografii a kryptoanalýzu**

- Kryptografické metody zahrnují:
	- *Důvěrnost dat* - utajuje obsah komunikace
	- *Autentičnost zprávy* - příjemce může zjistit původ zprávy
	- *Neodmítnutelnost* - Odesílatel nemůže popřít, že zprávu odeslal
	- Integritu zprávy - příjemce může zjistit, jestli při přenosu nedošlo ke změně zprávy

## Terminologie
- **Otevřený text** = zpráva určená k odeslání
- **Šifrování** = proces úpravy otevřeného textu, který ukryje jeho obsah
- **Zašifrovaný text / kryptogram** = výsledek aplikace šifrování na otevřený text
- **Dešifrování** = opačný proces k šifrování
- **Šifrovací funkce** = matematická funkce provádějící dešifrování
- **Šifra** = společné označení pro šifrovací a dešifrovací funkci
- **Kanál** = komunikační spoj
- Kryptografický modul = zařízení zajišťující šifrování, dešifrování, podepisování, ...

## Omezené šifry
- Bezpečnost šifrování je **založena na utajení způsobu**, jakým šifra pracuje.
- Dnes se **nevyužívá**, z praktického pohledu nevýhodné.

## Šifry založené na klíči
- **Kerckhoffův princip**: Bezpečnost šifry **závisí pouze na utajení klíče**, nikoliv na utajení šifrovací a dešifrovací funkce.
	- *Princi šifry může být i zveřejněn.*

>[!Example] Proces
> ![[MacBook-2025-03-23-002734.png| 500]]
> - $M$ - *konečná* množina všech **zpráv**.
> - $C$ - *konečná* množina všech **zašifrovaných zpráv**.
> - $K$ - *konečná* množina všech **klíčů**.
> - $e: M \times K \rightarrow C$ - **šifrovací** funkce
> - $d: C \times K \rightarrow M$ - **dešifrovací** funkce
> ---
> Definice (Claude E. Shannon)
> 		- Šifra založená na klíči je pětice $\langle \mathcal{M}, \mathcal{C}, \mathcal{K}, e, d \rangle$ taková, že pro libovolný šifrovací klíč $k_{e} \in \mathcal{K}$ a jemu odpovídající dešifrovací klíč $k_{d} \in \mathcal{K}$ platí $$d(e(x,k_{e}),k_{d})=x$$ pro všechna $x \in \mathcal{M}$. Krátce budeme mluvit o šifře.
## Symetrické šifry
- **Klíče pro šifrování a dešifrování** jsou **identické** nebo **mezi nimi existuje jednoduchá vztah**.
- Alice a Bob **sdílí stejnou znalost** - **klíč**. Oba **umí šifrovat i dešifrovat**.

>[!Example] Postup:
>1. Alice a Bob se **domluví na klíči**.
>2. Alice **zašifruje** zprávu pomocí klíče.
>3. Šifrovaná zpráva může být poslána Bobovi přes *nezabezpečený komunikační kanál*.
>4. Bob **dešifruje** zprávu pomocí klíče.
> - Odesílatel i příjemce **musí udržovat klíč v tajnosti**, proto se často mluví o **šifrování s tajným klíčem** (private key cryptography).
> ![[MacBook-2025-03-23-002737.png]]

>[!success] Výhody:
>- Šifrování a dešifrování je **velmi rychlé**.

>[!fail] Nevýhody:
>- Bezpečnost
>	- Nebezpečí odhalení tajného klíče třetí stranou.
>- Velký počet klíčů, složitý key management
>	- Počet klíčů = počet všech komunikačních kanálů.
>	- Počet klíčů roste kvadraticky, $n$ uživatelů potřebuje $\frac{n*(n-1)}{2}$ klíčů.

## Klasické šifry
- Jedná se o **symetrické šifry**.
- Dva typy klasických šifer:
	- **Monoabecední**
		- Prvky množin $M$ a $C$ jsou **jednotlivé symboly abecedy**.
		- (symbol abecedy je vždy mapován šifrovací funkcí na jediný symbol)
	- **Polyabecední** 
		- Prvky množin $M$ a $C$ jsou **posloupnosti symbolů abecedy určité délky**.
		- (symbol abecedy je vždy mapován na jeden z několika symbolů)
- Dělení podle způsobu šifrování:
	- Blokové šifry
	- Proudové šifry

### Posunovací šifra
- **Monoabecední šifra**.
- Písmeno abecedy je mapováno na jiné písmeno téže abecedy, které je posunuté o určitý počet pozic.
- Počet posunutí je dán **klíčem**.

>[!Example] Definice
>Nechť $\mathcal{M} = \mathcal{C} = \mathcal{K} = \mathbb{Z}_{26}$ . Pro $k \in \mathcal{K}$ definujeme šifrovací funkci $$e(x,k)=x+k$$ a dešifrovací funkci $$d(y,k)=y-k.$$

- **Kryptoanalýza** je založená na **exhaustive key search** (hrubá síla).
- Existuje pouze *26 různých klíčů* (anglická abeceda).
- Šifra **není bezpečná**.

### Afinní šifra
- **Monoabecední šifra**.
- Písmeno abecedy je mapováno na jiné písmeno téže abecedy

>[!Example] Definice
>Nechť $\mathcal{M} = \mathcal{C} = \mathbb{Z}_{26}$, $\mathcal{K} = \{\langle a, b \rangle \in \mathbb{Z}_{26} \times \mathbb{Z}_{26} | \text{gcd}(a,26)=1 \}$. Pro $k = \langle a,b \rangle \in \mathcal{K}$ definujeme šifrovací funkci $$e(x,k)=ax+b,$$ a dešifrovací funkci $$d(y,k)=a^{-1}(y-b).$$

- Ve zbytkových třídách (modulární aritmetika) lze určit inverzní prvek tak, že hledáme číslo, které když vynásobíme s daným číslem, dá výsledek 1 modulo $n$.
- Existuje $312$ různých klíčů.
	- To je pořád málo.

### Substituční šifra
- **Monoabecední šifra**.
- Písmeno abecedy je mapováno na jiné písmeno téže abecedy podle zvolené permutace této abecedy.

>[!Example] Definice
>Nechť $\mathcal{M} = \mathcal{C} = \mathcal{Z}_{26}$, $\mathcal{K} = \{ \pi | \pi \text{ je permutace }  \mathbb{Z_{26}}\}$. Pro $\pi \in \mathcal{K}$ definujeme šifrovací funkci $$e(x, \pi) = \pi(x),$$ a dešifrovací funkci $$d(y, \pi) = \pi^{-1}(y).$$

- Existuje asi $4 * 10^{26}$ různých klíčů (26!), nemůžeme použít hrubou sílu.
- Přesto to **není bezpečná šifra**.
	- Kryptoanalýza se provádí s využitím jiných metod.

### Vigenerova šifra
- **Polyabecední šifra**.
- Prvky $M$ jsou $m$-tice písmen abecedy.
- **Klíčem** je také $m$-tice písmen abecedy.
- Písmeno abecedy může být mapovánoo na jedno z $m$ písmen téže abecedy.
	- (pokud předpokládáme, že klíč je složen z $m$ různých písmen)

>[!Example] Definice
>Nechť $\mathcal{M} = \mathcal{C} = \mathcal{K} = \mathbb{Z}^{m}_{26}$, $m \in \mathbb{N}$. Pro klíč $k = \langle k_{1}, ..., k_{m} \rangle \in \mathcal{K}$ definujeme šifrovací funkci $$e(x,k) = \langle x_{1} + k_{1}, ..., x_{m} + k_{m} \rangle ,$$ a dešifrovací funkci $$d(y, k) = \langle y_{1}-k_{1}, ..., y_{m}-k_{m} \rangle$$ pro všechny $x = \langle x_{1}, ..., x_{m} \in \mathcal{M}, y= \langle y_{1}, ..., y_{m} \rangle \in \mathcal{C}$.

- Existuje $26^{m}$ **různých klíčů délky $m$**, stále to však **není bezpečná šifra**.
- Kryptoanalýza se provádí pomocí Kasiského a Friedmannova testu.

## Kryptoanalýza klasických šifer
- Kryptoanalýza se liší v *závislosti na typu informace, kterou má útočník k dispozici*.
- Poté mluvíme o útočích:
	1. **Ciphertext only attack**
		- Zná zašifrovanou zprávu.
	2. **Known plaintext attack**
		- Zná původní zprávu a její odpovídající zašifrovanou zprávu.
	3. **Chosen plaintext attack**
		- Získal dočasný přístup ke kryptografickému modulu, který realizuje šifrování.
		- (může si vybrat libovolnou zprávu a tu pak zašifrovat)
	4. **Chosen ciphertext attack**
		- Získal dočasný přístup ke kryptografickému modulu, který realizuje dešifrování.
		- (může si vybrat libovolný kryptogram a ten pak dešifrovat)
- Ve všech případech je snahou najít klíč.

### Frekvenční analýzy
- Frekvenční analýza je založena na **přirozeném rozdílném výskytu znaků** v jazyce.
- Máme **zjištěné frekvence výskytu písmen** podle jazyka.
- Existuje i vylepšení, kde bere v potaz i závislosti výskytu písmen na základě předchozího písmena.

## Asymetrické šifrování
- **Klíče** pro šifrování a dešifrování **nejsou stejné**.
	- **Šifrovací klíč** = veřejný klíč
	- **Dešifrovací klíč** = soukromý klíč
- Vztah mezi soukromým a veřejným klíčem (jednosměrnost):
	- **Soukromý** $\rightarrow$ **veřejný**, je jednoduše vypočitatelné
	- **Veřejný** $\rightarrow$ **soukromý**, nelze jednoduše odvodit

- **Soukromý klíč** je držen v **tajnosti**, **veřejný klíč** může být **veřejně distribuován**.
	- V tomto případě mluvíme o šifrování s veřejným klíčem. (public-key cryptography)

>[!Example] Příklad
>- Šifrování založené na zavazadlovém problému, diskrétním logaritmu, eliptických křivkách, RSA, ...
>- Postup:
>	1. Příjemce vytvoří soukromý klíč a veřejný klíč
>	2. Soukromý klíč uschová příjemce v tajnosti, veřejný zveřejní
>	3. Odesílatel zašifruje zprávu pomocí veřejného klíče a pošle příjemci
>	4. Příjemce dešifruje zprávu pomocí soukromého klíče
>![[MacBook-2025-03-23-002738.png]]

>[!success] Výhody
>- Bezpečnější
>- Není složitá správa klíčů

>[!fail] Nevýhody
>- Pomalejší 

## Hybridní šifrování
- Kombinuje symetrické a asymetrické šifrování
- Odstraňuje nevýhody obou předešlých metod
- Šifrování je ve své podstatě symetrické, asymetrické šifrování je použito při distribuci tajného klíče
- Například SSL a TLS
![[MacBook-2025-03-23-002739.png]]

## Blokové šifry - DES a AES, jejich aplikace (vedlejší otázka)
- Soudobé **symetrické šifry**.
- Jsou to také **iterační blokové šifry**.

- Operace zvyšující bezpečnost kryptosystémů
	- Konfúze = operace, která se snaží skrýt vztah mezi kryptogramem a použitým klíčem
	- Difúze = znak otevřeného textu by měl ovlivňovat co nejvíce znaků kryptogramu $\Rightarrow$ změna jednoho bitu otevřeného textu vede v průměru ke změně poloviny bitů v kryptogramu

### DES
- **Data Encryption Standard**
- Symetrický blokový šifrovací algoritmus, který byl *standardizován* v roce 1977 **národním institutem standardů a technologie** (NIST) v USA.
- DES byl široce používán pro šifrování dat, ale dnes je **považován za zastaralý** kvůli své relativně malé klíčové délce a zranitelnosti vůči útokům

- **Bloková šifra**:
	- DES šifruje data v blocích o délce 64b.
- **Délka klíče**:
	- DES používá 56b klíč pro šifrování
	- Celkový klíč má délku 64b, ale 9b jsou kontrolní bity pro paritu a nejsou použity pro šifrování.
- **Struktura**:
	- DES používá **tzv. Feistelovu síť**, která rozděluje blok dat na dvě poloviny a pak opakovaně aplikuje šifrovací funkci na jednu polovinu a výsledky kombinuje s druhou polovinou.
- **Počet kol**:
	- DES provádí 16 kol šifrování, což zahrnuje permutace a substituce založené na klíči.

### AES
- Advanced Encryption Standard
- Symetrický blokový šifrovací algoritmus, který byl standardizován v roce 2001 jako náhrada za DES.
- AES je navržen tak, aby byl bezpečný a efektivní jak pro softwarové, tak pro hardwarové implementace.

- **Bloková šifra**:
	- AES šifruje **data v blocích o délce 128b**.
- **Délka klíče**:
	- AES podporuje klíče o délce 128b, 192b a 256b, čímž poskytuje různou úroveň zabezpečení.
- **Struktura**:
	- AES standard je založen na šifře Rijndael.
	- Implementace použitím polynomiální aritmetiky nad prvočíselnými tělesy.
- **Počet kol**:
	- AES provádí 10 kol pro 128b klíče,
	- 12 kol pro 192b klíče,
	- 14 kol pro 256b klíče.

- Šifra byla navržena pro snadnou implementaci na 8b procesorech.
- **Dnešní využití**:
	- WiFi encryption standard WPA2, WPA3 (AES-256)
	- SSH
	- Skype (rip)
	- SSL/TLC
	- Šifrovací algoritmy pro pevné disky
	- IPSec
	- Signal Protocol
	- Implementace přímo v HW
