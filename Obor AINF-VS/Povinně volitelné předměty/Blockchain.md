## Distribuované transakce
- Transakce, která zahrnuje více uzlů v DS.
- Mezibankovná převod (různé systémy), zápis do více různých DB, ...
- Zaměřili jsme se na distribuované transakce.

## Distribuovaný commit
### One-phase commit:
- *Koordinátor* **zahájí operaci** a řekne ostatním, **co mají udělat**.
- Problém: **Chybí zpětná vazba**, pokud uzel nedokáže operaci provést, není koordinátor informován.

### Two-phase commit:
- *Koordinátor* **pošle všem `VOTE-REQUEST`**.
- **Uzel pošle `VOTE-COMMIT`**, pokud *je připraven provést commit*. Jinak `VOTE-ABORT`.
- *Pokud koordinátor obdrží* **od všech `VOTE-COMMIT`**, pošle všem zprávu `GLOBAL-COMMIT`, jinak `GLOBAL-ABORT`.
- Pokud uzel obdrží `GLOBAL-COMMIT` provede commit.

>[!fail] Problém:
> Mnoho bodů selhání, řešení jsou časovače.


![[MacBook-2025-01-13-002435.png]]
- Uzel, který **neobdrží `VOTE-REQUEST`** po **čase pošle `VOTE-ABORT`**.
- Koordinátor ve stavu *wait* **po čase pošle `GLOBAL-ABORT`**.
- Uzel v ready stavu (čeká na koordinátora) má dvě možnosti:
	- **Blokovat** dokud **koordinátor nepošle zprávu**.
	- Po čase **kontaktovat jiný uzel** a zeptat se zda neobdržel `GLOBAL-*`
	- Pokud v tomto bodu *selže koordinátor*, pak **nekonečné blokování**.

### Three-phase commit:
![[MacBook-2025-01-13-002436.png]]
- Navíc `PREPARE-COMMIT` zpráva.
	- Koordinátor ve stavu **`PRE-COMMIT`**, po čase může poslat `GLOBAL-COMMIT`.
	- Uzel ve stavu `READY` nebo `PRE-COMMIT` analogické jako u 2-fázového commitu, ale pokud je více jak polovina uzlů ve stavu `READY`, tak `VOTE-ABORT`.

## Blockchain
- **Blockchain** je **datová struktura pro realizaci distribuované účetní knihovny**.
- *Myšlenka blockchainu vznikla v roce 2008*, když někdo, který používal pseudonym **Satoshi Nakamoto**, publikoval bílou knihu s názvem *"Bitcoin: A Peer-to-Peer Electronic Cash System"*. Tato publikace byla zveřejněna na kryptografickém fóru. 
- První blockchain byl implementován jako součást kryptoměny Bitcoin, která byla spuštěna **v lednu 2009**.

- Jelikož sdílíme data, tak podle CAP teorému, musíme učinit volbu:
	- Typicky pro blockchain **zachováváme AP na úkol C**.

- Bitcoin, Ethereum, Dogecoin, ...
- Ale nejen kryptoměny:
	- DNS, IoT, lékařské záznamy, smart contracts, ...

- Jsou nejen veřejmé:
	- Nějaká míra centralizace, omezení přístupnosti nebo transparentnosti, ...
	- Privátní (centralizovaný)m
	- Hybridní (řízený důvěryhodným konsorciem, s autentizací)

### Bloky a jejich provázání
- Blockchain - řetězec (provázaných) bloků
- Blok obsahuje:
	- **Data** (transakce, záznamy, ...),
	- **Timestamp**,
	- **Hash dat** (většinou kryptografický),
	- **Hash předchozího bloku** (většinou kryptografický),
	- ...

- První blok v řetězci se nazývá **genesis block**
	- Jediný blok, který nemá předchozí hash block.

- **Hash dat zabezpečuje blok**:
	- Jelikož používáme **kryptografickou hashovací funkci**, tak jedna z její podmínek je, že mi malá změna v datech udělá velkou změnu po zahashování.
	- Takže *velmi snadná verifikace změny*.
	- Předchozí bloky *prakticky* nelze měnit.
- **Provázání bloků zabezpečuje blockchain**:
	- *Každý blok potvrzuje předešlé*.
	- Potvrzení spočívá v tom, že **máme vždy hash předešlého bloku** (odkaz).

- Každý uzel může mít vlastní kopii blockchainu.
- Stačí shoda jenom na jednom (posledním) bloku.

### Shoda, Pow
- Proof of Work.

>[!Example] Jak funguje:
>- Vytvoření nového validního bloku vyžaduje velké množství práce.
>1. Zájemce posbírá transakce do bloku.
>2. Sestaví základ bloku.
>3. Musí blok doplnit tak, aby vyřešil nějakou výpočetně náročnou hádanku.
>4. Hádanka má upravitelnou obtížnost (dle aktuálních možností sítě).

- Kdo to zvládne první, získává odměnu za blok (poplatky, nové prostředky, ...)
- Ověření validity bloku (výsledku hádanky) musí být triviální.
- Změna bloku = přepočítání všech dalších bloků $\rightarrow$ nereálné.

>[!fail] Problémy:
>spotřeba, pooly, rychlost

- Např. Bitcoin a délka nulového prefixu hashe.

### Shoda, PoS
- Proof of Stake.
- Problémy PoW $\rightarrow$ místo práce zástava.

>[!Example] Jak funguje:
>- Vytvoření nového bloku vyžaduje (relativně) velkou zástavu.
>1. Zájemce (validátor) nabídne zástavu (kryptoměnu daného blockchainu).
>2. Systém vybere zájemce
>	- Podle velikosti zástavy,
>	- podle dlouhodobé důvěryhodnosti,
>	- s prvkem náhody.
>3. Vítěz posbírá transakce do bloku a připojí jej do sítě.
>- Ostatní validátoři ověří plastnosti bloku ($\rightarrow$ odměna).
>	- OK: Vítěz získává odměnu za blok.
>	- KO: Vítěz ztrácí zástavu, je penalizován v síti.

- Podvod vyžaduje mít hodně prostředků $\rightarrow$ útok na sebe sama.

>[!fail] Problém:
>Potenciální centralizace bohatství (a moci).

### Shoda, další
- Delegated PoS
- Proof of Authority
- Proof of Elapsed Time
- Practical Byzantine Fault Tolerance

### Hrozby
- 51% útok - ovládnutí většiny v síti.
- Sybil(a) útok - vydávání se za více účastníků.
- Eclipse útok - oddělení uzlu.
- Chyby v chytrých smlouvách (smart contracts) - zneužití bugu.
- Fyzická/linková vrstva - útok na podpurné vrstvy.
- Kryptografie - aktuálně kvantové počítače a SHA-256.
- DDoS - přetížení sítě.
- Sociální inženýrství - útoky na uživatele obecně.

## Bitcoin
- První úplná implementace DLT.
- Alternativa k fiat měnám.
- Fixní počet 21,000,000 BTC
- 1 BTC = $10^{8}$ Satoshi (lze rozdělit).
- Na začátku byla odměna 50 BTC v bloku.
	- Halving každých 210.000 bloků.
- Hashovací funkce SHA-256
- **Privátní klíč** podepisuje transakce
- **Veřejný klíč** ověřuje
- Velikost bloku do 1MB (dnes už 4MB)
- PoW: Doplnit blok o nonce(číslo), aby hash měl prefix $0^{n}$.
- Délka prefixu $n$ je nastavitelná.

## Ethereum
- "Druhá nejvýznamnější" kryptoměna.
- Záměr: Blockchain může poskytovat více než jen měnu (smart contracts).
- Nemá limit, ale má jiné nástroje pro omezení inflace.
- Hash: **Keccak-256** (modifikace SHA-3).
- **Primární klíč** podepisuje.
- **Veřejný klíč** ověřuje.
- Původně PoW, paměťově náročné operace.
- Nyní PoS. Snížení spotřeby o 99%.
- Podporuje smart contracts:
	- součástí je EVM (Ethereum Virtual Machine)
	- Vlastní bytekód, Turingovsky úplný.
	- Jazyky: Solidity, vyper
	- V transakci očekává vstup a platbu.


<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FChord%20syst%C3%A9m" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Následující otázka
            </button>
        </a>
    </div>
    <!-- Spodní tlačítko -->
    <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2F2.%20Povinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty" style="text-decoration: none;">
        <button style="padding: 15px 30px; background-color: #ADD8E6; color: black; border: none; border-radius: 5px; cursor: pointer; width: 43%;">
            Všechny otázky
        </button>
    </a>
</div>

---
*\*Shoda, bitcoin jak byla probírána s panem doktorem Trnečkou.*

### Shoda
- **Practical Byzantine Fault Tolerance** je algoritmus navržený pro *dosažení tolerance Byzantských chyb v DS*. Tato tolerance je klíčová v situacích, kdy některé komponenty systému mohou selhat nebo **jednat zákeřně**.

>[!Example] Základní princip fungování:
>- **Role uzlů**:
>	- **Klienti**:
>		- Klienti jsou entitami, které *iniciovaly transakce a chtějí je provést v DS*.
>	- **Uzly**:
>		- Uzly, které udržují kopie stavu systému a *spolupracují na dosažení shody ohledně transakcí*.
>- Fáze algoritmu:
>	- **Fáze pre-prepare**:
>		- Klient pošle *žádost o transakci primárnímu uzlu*.
>		- Ten pošle **ostatním `PRE-PREPARE` zprávu** spolu s **next-sequence number** (NSN) a daným požadavkem.
>	- **Fáze prepare**:
>		- Uzel obdrží `PRE-PREPARE` zprávu a **přijme** ji pokud **neobdržel žádnou další zprávu s daným NSN** a pošle `PREPARE` zprávu ostatním uzlům.
>	- **Fáze commit**:
>		- Uzel čeká až obdrží **nadpoloviční většinu `PREPARE`** a *následně pošle `COMMIT` zprávu*.
>		- Poté čeká na **nadpoloviční většinu `COMMIT` zpráv** a *následně provede požadavek*.
>		- Nakonec pošle `REPLY` klientovi.

>[!fail] Problémy:
>- Při vytvoření nového bloku je tento blok *broadcastem* poslán všem uzlům.
>- Každý uzel si blok *přidá do svého blockchainu*.
>- **Může dojít ke kolizi** - **uzel obdrží více různých bloků**.
>	- *Dojde k větvení*, což lze vyřešit, že **uzel náhodně vybere nejdelší větev**.
>- Nyní *může dojít k livelocku*, protože přidání bloku je rychlejší než jeho poslání do sítě, což lze **vyřešit časovačem**.
>- **Ale jakou dobu vybrat** - čím delší, tím méně větvení, ale pomalejší přidání bloku.
>
> - A co když uzel bude **"podvádět"** a neustále, bez ohledu na časovač, přidávat bloky?
> 	- Existují **nějaké hw řešení**, ale ty jsou *nedostatečné*.
> 	- Takže potřebujeme **zpomalit vytvoření samotného bloku**.
> 		- Na vytvoření bloku musíme **vyřešit složitý matematický problém**.
> 		- Potřebujeme **ale snadnou verfikaci**, že problém byl správně vyřešen.
> 		- Tohle se běžně označuje jako **proof-of-work**.

## Bitcoin
- V bloku jsou uloženy transakce
	- **Zjednodušeně**: kdo, komu, kolik.
	- V bloku *je minimum informací*, kompletní data jsou uložena centrálně.
	- **Asymetrické šifrování** (Eliptické křivky):
		- Bitcoin využívá asymetrického šifrování založeného na eliptických křivkách.
		- Každý účastník sítě má dva klíče: veřejný a soukromý.
		- Veřejný klíč se používá k vytvoření adresy peněženky.
		- Soukromý klíč slouží k podepisování transakcí.
	- **Veřejný klíč = peněženka**
		- Veřejný klíč je veřejně sdílená adresa peněženky, kterou může kdokoli znát.
		- Peněženka je v podstatě kombinací veřejného klíče a privátního klíče.
		- Kdo zná váš veřejný klíč, může vám poslat Bitcoin.
	- **Digitální podpis pro verifikaci**:
		- Při provedení transakce je třeba ji digitálně podepsat.
		- To znamená použití soukromého klíče k vytvoření digitálního podpisu.
		- Tento digitální podpis spolu s veřejným klíčem (adresou peněženky) umožňuje ostatním členům sítě ověřit, že transakce byla skutečně provedena majitelem příslušné peněženky.

- Bitcoin blockchain jsou *všechny transakce od samotného počátku*.
- **Mining** je *vytvoření nového bloku* za pomoci **proof-of-work**.

### Vytvoření bloku
- **Umístění transakcí do bloku, přidání odkazu a ověření podmínke**.
- Cílem je *uhodnout jaké data* (nonce) *přidat k datům nové transakce*, aby výsledný **hash** měl na začátku aspoň $p$ nul.
	- $p$ určuje **obtížnost**, která se mění každých 2016 bloků.
- Přidáním bloku se *získá odměna*, což jsou nové bitcoiny.
- Blok je považován za potvrzený, pokud jej **potvrzuje $3$ a více bloků**.

## Další informace
- Alternativní algoritmy:
	- proof-of-stake
	- proof-of-space
	- proof-of-authority
	- proof-of-elapsed-time
	- ...
- Minimální škálovatelnost počtu transakcí za sekundu