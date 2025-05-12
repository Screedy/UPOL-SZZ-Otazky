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

## RSA
- **Rivest Shamir Adleman** (tvůrci)
- **Asymetrická šifra**
- Dle délky klíče je považována za velmi bezpečnou.
- Použití:
	- Bezpečná výměna tajných klíčů pro symetrické šifrování
	- Digitální podpis

### Generování soukromého a veřejného klíče (příjemce)
1. Zvolí se **dvě různá prvočísla $p$ a $q$**
	- Přibližně **stejně** velká
	- Typická velikost 1024 - 3072 bitů nebo i více.
2.  Vypočítá se **součin** $n=p*q$, platí $\varphi (n) = (p-1) * (q-1)$
	- *Eulerova funkce $\varphi : \varphi (n)$ je počet přirozených čísel menších než $n$ a nesoudělných s $n$.*
3. Náhodně se **zvolí** $e \in \{1,2, ..., \varphi (n) - 1\}$ tak, **aby** $\text{gcd}(e, \varphi (n)) = 1$
	- $e$ se nazývá **veřejný exponent**
	- Často se volí $e=3$.
4. Pomocí rozšířeného Euklidova algoritmu **vypočítáme inverzi** $e \text{ modulo } \varphi (n)$, označíme $d=e^{-1} \text {mod} \varphi (n)$.

- $k_{e} = \langle e, n \rangle$ reprezentuje **veřejný klíč**.
- $k_{d} = d$ reprezentuje **soukromý klíč**.
- Čísla $p, q$ se mohou odložit (nejsou potřeba), ale **NIKDY** se **nesmí zveřejnit**.

### Šifrování a dešifrování
- Otevřený text $n \in M$ se rozdělí na číselné bloky $x_{i}$ tak, aby $x_{i} < n$$.
- Šifrování:
	- $e(x_{i}, k_{e}) = x^{e}_{i} \text{ mod } n$
- Dešifrování:
	- $d(y_{i}, k_{d}) = y^{d}_{i} \text{ mod } n$

>[!Example] Příklad
>1. otevřený text $m = 688232687966668003$
>2. $p=47$, $q=71$, $n=p*q=3337$
>3. zvolíme $e=79$, $79$ není soudělné s $(p-1)*(q-1) = 3220$
>4. $d$ vypočítáme jako inverzní prvek k $79$ v $(\mathbb{Z}_{3320},*)$, tzv. $d=1019$
>5. otevřený text $m$ rozdělíme do bloků $$
\begin{aligned}
m_{1} &= 688 \\
m_{2} &= 232 \\
m_{3} &= 687 \\
m_{4} &= 966 \\
m_{5} &= 688 \\
m_{6} &= 003
\end{aligned}
$$ tak, aby $m_{i} < n = 3337$.
> - Šifrování 1. bloku: $c_{1} = 688^{79} \text{ mod } 3337 = 1570$.
> 	- Podobně pro další bloky.
> - Celkem získáme šifrovanou zprávu $$c = 1570\ 2756\ 2091\ 2276\ 2423\ 158$$
>   Dešifrování 1. bloku: $m_{1} = 1570^{1019} \text{ mod } 3337 = 688$.
> 	- Podobně pro další bloky.

### Praktické aspekty
- **Generování velkých prvočísel**
	- Pro výpočet modulu $n$ potřebujeme dvě velká prvočísla
	- Princip:
		- Náhodně vygenerujeme číslo příslušné délky
		- Provedeme text prvočísel
	- Problémy:
		- Kolik čísel musíme vygenerovat, abychom narazili na prvočíslo?
			- Náhodně vygenerované číslo $p$ mezi $1$ a $N$ je prvočíslo s pravděpodobností přibližně $\frac{1}{\text{ln}N}$
		- Jak efektivně provést text prvočíselnosti?
			- Fermatův test, ASK, ...
- **Rychlé umocnění**
	- Jedná se o **zásadní problém**, jelikož bez rychlého umocnění by bylo šifrování RSA nepoužitelné.
	- Pro urychlení se používá vhodná kombinace násobení (MUL) a výpočtu druhé mocniny (SQ)

### Bezpečnost RSA (vedlejší otázka)
- Bezpečnost RSA je založena na předpokladu, že problém faktorizace IFP je pro velké moduly obtížný.

>[!tip] IFP
>- Faktorizace IFP (Integer Factorization Problem) je matematický problém spočívající v rozložení celého čísla na součin prvočísel.

- Nevíme však přesně, do jaké třídy složitosti tento problém spadá.
- Předpokládá se, že je v **NP-úplný**.

#### Útok pomocí postranního kanálu
- **Postranní kanál** je nežádoucí způsob výměny informací mezi zařízením (nebo programem implementující šifru) a jeho okolím.
- Postranní kanály se dají použít k prolomení RSA, aniž bychom se pokoušeli o faktorizaci.
- Při šifrování v HW mohou být postranní kanály (spotřeba, zvuk, teplo, ...)
- Tyto projevy můžeme změřit a na jejich základě odhadnout část soukromého klíče.

---
## Kryptografické hashovací funkce
- **Kryptogragická hashovací funkce** je **zobrazení** $\text{hash: } X \rightarrow Y$, kde:
	- $x \in X$ je **zpráva** (soubor) libovolné délky
	- $y \in Y$ je posloupnost znaků **pevné délky** nazývaná *hashovací hodnota*

- **Základní vlastnosti:**
	1. Hashovací funkce je **deterministická**.
	2. Hashovací funkce je **jednosměrná**.
	3. Jediným způsobem, jak získat hashovanou hodnotu $\text{hash}(x)$ pro zprávu $x$ je vyhodnocení funkce $\text{hash}$ pro $x$.
	4. **Lavinový efekt**: náhodná nebo záměrná (i velmi malá) změna zprávy na vstupu **výrazně změní** hashovanou hodnotu.

- **Podmínky kladené na bezpečnost hasnovací funkce**:
	- **Odolnost vůči získání vzoru**
		- Pro zadanou hasnovanou hodnotu $y$, je velmi obtížné najít zprávu $x$ tak, že $y = \text{ hash}(x)$
	- **Odolnost vůči získání jiného vzoru**
		- Pro zadanou zprávu $x_{1}$ je velmi obtížné najít takovou zprávu $x_{2} \neq x_{1}$ tak, že $\text{hash}(x_{1}) = \text{ hash}(x_{2})$
	- **Odolnost vůči kolizi**
		- Je velmi obtížné nalézt jakékoliv $x_{1} \neq x_{2}$, any $\text{hash}(x_{1}) = \text{ hash}(x_{2})$

- **Analogie k otisku prstu**
	- Otisk prstu je snadné pořídit.
	- Máme-li otisk prstu, je nemožné z něj rekonstruovat jeho nositele.
	- Máme-li konkrétního člověka, je nemožné najít jiného člověka se stejným otiskem.
	- Je nemožné najít jakékoliv dva lidi, kteří by měli stejný otisk.

### Použití
- Ověření integrity souboru
- Ověření hesla
- Digitální podpis

### Implementace
- MD5 - Message-Digest algorithm 5
	- Délka hashované hodnoty je 128b.
	- Nesplňuje podmínku odolnosti vůči kolizím (byl proveden collision attack)
		- Roku 2006 byl publikován efektivní algoritmus pro hledání kolizí
	- Dnes se používá pouze pro ověřování integrity souborů
- SHA-1 - Secure Hash Algorithm
	- Délka hashované hodnoty je 160b.
	- V roce 2005 byla publikována první známá kolize SHA-1 v praxi.
		- Od té doby byly objeveny další útoky a kolize.
		- Postupem času se stává čím dál snazší generovat kolize pro SHA-1 pomocí pokročilých výpočetních metod.
- SHA-2
	- Následní SHA-1
	- Obsahuje skupiny algoritmů SHA-224, SHA-256, SHA-384 a SHA-512

### Hashovací funkce pro hesla
- Většina předchozích navržena s ohledem na efektivní výpočet pro velké vstupy.
- Vznik speciálních hashovacích funkcí pro hashování hesel.
- Využívají:
	- Záměrného zpomalení
	- Sůl jako další argument
	- Často iterativní výpočet

- Implementace:
	- PBKDF2 (Password-Based Key Derivation Function 2)
		- Kryptografická funkce určená k odvození hashované hodnoty z hesla
		- Odolná vůči útokům hrubou silou.
		- Bere jako vstup heslo, sůl (náhodný řetězec použitý k posílení hesla) a parametry algoritmu (počet iterací a velikost odvozeného klíče)
		- Následně použije iterativní proces s použitím kryptografické hashovací funkce (např. SHA-256, SHA-512) k odvození hashované hodnoty.

## Prolomení hashovacích funkcí (vedlejší otázka)
- Prolomení hashovací funkce znamená **nalezení kolize** nebo **reverzního mapování** pro danou funkci.
	- To by umožnilo útočníkovi vytvořit dvě různé vstupy s identickým hashem nebo získat původní vstup z daného hashe.
- Existuje několik způsobů, jak se může útočník pokusit prolomit hashovací funkci:

1. **Brute Force Attack**
	- Útočník může zkoušet různé kombinace vstupních hodnot, dokud nenajde takovou, která má stejný hash jako cílový.
	- Postup může být časově náročný.
2. **Dictionary Attack**
	- Útočník může použít předem vytvořený seznam běžných hesel nebo možných vstupních hodnot.
	- Zkouší, zda některý z nich vytváří požadovaný hash.
3. **Rainbow Table Attack**
	- Útočník může použít předpočítané tabulky obsahující páry vstupních hodnot a jejich odpovídajících hashů.
	- Pokud útočník získá hash, může ho porovnat s tabulkou a zjistit odpovídající vstupní hodnotu.
	- Účinný proti slabým nebo běžným hashovacím funkcím.
4. **Collision Attack**
	- Útočník může aktivně hledat dvě různé vstupní hodnoty, který mají stejný hash.
	- Tento typ útoku je náročný a vyžaduje pokročilé kryptoanalytické techniky.
	- Pokud úspěšný, může vytvoření falešných dat nebo dokonce vyvrácení integrity systému.
5. **Využití slabostí v hashovací funkci**
	- Pokud jsou nalezeny slabiny v algoritmu hashovací funkce, může útočník využít těchto slabostí k získání požadovaných vstupů nebo kolizí.

## Digitální podpis

## Podepisování
1. Ze zprávy se **vytvoří hash**.
	- Kvůli efektivitě, integritě, ...
2. Hash se *zašifruje* pomocí **soukromého klíče**.
	- Je potřeba šifry, která to umožňuje (např. RSA)
3. Zašifrovaný hash se přiloží ke zprávě a je odeslán.
	- Potřeba zveřejnit veřejný klíč.

### Ověření podpisu
1. Příjemce oddělí zašifrovaný hash od zprávy.
2. Hash se *dešifruje* pomocí *veřejného klíče* podepisujícího.
3. Příjemce *porovná* hash zprávy a *dešifrovaný* hash.
4. Pokud se rovnají, vlastník soukromého klíče podepsal dokument v daném znění.

![[MacBook-2025-04-09-002868.png| 500]]

### Podvržení veřejného klíče
- Problém může nastat v distribuci veřejného klíče.
- Pokud by byl **distribuován spolu** se zprávou/souborem, mohl by jej někdo po cestě změnit.
	- *Man In The Middle attack* (MITM).
- Problém vyřeší **certifikace veřejného klíče** *"vyšší autoritou"*.
