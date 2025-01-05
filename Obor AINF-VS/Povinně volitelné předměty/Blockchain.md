- **Blockchain** je **datová struktura pro realizaci distribuované účetní knihovny**.
- *Myšlenka blockchainu vznikla v roce 2008*, když někdo, který používal pseudonym **Satoshi Nakamoto**, publikoval bílou knihu s názvem *"Bitcoin: A Peer-to-Peer Electronic Cash System"*. Tato publikace byla zveřejněna na kryptografickém fóru. 
- První blockchain byl implementován jako součást kryptoměny Bitcoin, která byla spuštěna **v lednu 2009**.

- Jelikož sdílíme data, tak podle CAP teorému, musíme učinit volbu:
	- Typicky pro blockchain **zachováváme AP na úkol C**.

- Typy blockchainů:
	- **Veřejný**
	- **Privátní**
	- **Kontrolovaný**

## Základní myšlenka blockchain struktury
- Je to řetězec provázaných bloků.
- Každý blok obsahuje:
	- **Data** (záznamy, transakce, ...)
	- **Kryptografický hash dat**
	- **Kryptografický hash předchozích dat**
	- **Timestamp**
	- ...

- První blok v řetězci se nazývá **genesis block**

- **Hash dat zabezpečuje blok**:
	- Jelikož používáme **kryptografickou hashovací funkci**, tak jedna z její podmínek je, že mi malá změna v datech udělá velkou změnu po zahashování.
	- Takže *velmi snadná verifikace změny*.
- **Provázání bloků zabezpečuje blockchain**:
	- *Každý blok potvrzuje předešlé*.
	- Potvrzení spočívá v tom, že **máme vždy hash předešlého bloku** (odkaz).

- Každý uzel v síti si *udržuje vlastní kopii blockchainu* a *každý uzel může mít jinou kopii*, proto je **nutná shoda**.
- Stačí se nám **shodnout na jednom bloku**, protože se tím *shodneme na všech předešlých*.
- Na to však **nelze použít klasické algoritmy** (jako Paxos, Raft), protože v těchto algoritmech *má každý uzel jeden hlas a kdyby se připojilo hodně uzlů, tak by mohli vytvořit vlastní pravdu* (Sybil attack).

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