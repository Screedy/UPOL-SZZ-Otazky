## Synchronizace bez sdílené paměti
### Distribuovaný systém
- Distribuovaný systém lze chápat jako *speciální* případ paralelního.
- Obecně se jedná o **kolekci autonomních systémů**, které se **chovají jako jeden systém** (systémy mohou však být i na jednom uzlu).

- Alternativní popis: *Soubor nezávislých, autonomních výpočetních elementů propojených komunikační sítí. Výpočetní elementy komunikují formou posílání zpráv za účelem formy spolupráce.*

- Vznikají nám nové problémy (jiná architektura, než byla doteď)
	- Absence synchronizace pomocí sdílené paměti. Musíme však řešit **komunikaci mezi systémy** (komunikace je nespolehlivá, pomalá)

#### Architektura distribuovaných systémů
- Skládá se z:
	- **uzlů**
	- **propojení uzlů**
	- **API** (umožňuje komunikaci mezi různými komponentami a poskytuje standardizovaný způsob, jakým mohou aplikace nebo služby vzájemně interagovat)
- Typy architektur:
	- Layer-based (TCP/IP, MVC, ...)
	- Services-oriented
		- object-based
		- resource-based
		- event-based
		- blockchain
- Organizace distribuovaného systému:
	- **klient-server**
	- **peer-to-peer**

#### Struktura peer-to-peer
- Označení typu počítačových sítí, ve které spolu komunikují přímo jednotliví klienti
- Topologie sítě:
	- Strukturovaná - **ring**, **tree**, **grid**, ... (např. Chord, distribuovaná hash tabulka)
	- Nestrukturovaná - struktura není pevně dána, neudržitelné s rostoucí velikostí
	- Hybridní - **kombinace** klient-server a peer-to-peer (např. BitTorrent)

### Komunikace
- V distribuovaných sítích existuje několik způsobů komunikace mezi uzly nebo komponentami systému. Způsob komunikace může záviset na **architektuře** distribuovaného systému, **potřebách aplikace** a **požadovaných vlastnostech**.

- **Remote Procedure Call** (RPC)
- **Zasílání zpráv, Inter Process Communication** (IPC)
	- výrazně jednodušší a běžné
	- různé implementace
	- různé modely
		- request-reply
		- publisher-subscriber
		- pipeline

#### RPC
- Je mechanismus umožňující **volání procedur** nebo funkcí, které běží na vzdáleném počítači či uzlu, tak, **jako by byly volány lokálně**
- Velmi komplikované - volaná procedura **nemá přístup** k aktuálnímu **stavu** volajícího. Proto je jej potřeba **předat** volanému. Například pomocí pointeru.
- Aktuální stav třeba převést do zaslatelné podoby - pojmy **marshaling** a **unmarshaling**
>[!tip] Marshaling a unmarshaling
>Procesy převodu dat na formát vhodný pro přenost (marshaling) a zpětný proces převodu těchto dat z formátu přenosu do interní reprezentace (unmarshaling)

- Varianty:
	- **Synchronní RPC:**
		- V synchronním RPC čeká volající proces (klient) na odpověď ze vzdáleného procesu (serveru) po dobu trvání RPC. 
		- Klient je **blokován**, dokud server nevrátí výsledek volané procedury.
	- **Asynchronní RPC**:
		- Asynchronní RPC umožňuje klientovi pokračovat v práci bez čekání na dokončení vzdáleného volání. 
		- Klient může poslat RPC na server, pokračovat ve svém běhu a později získat výsledek, když je k dispozici.
	- **Jednosměrné RPC:**
		- Klient nečeká na potvrzení, což může být problematické pokud není komunikace spolehlivá.
	- **Multicast RPC**:
		- Při použití multicastu jsou zprávy odeslány všem uzlům ve specifické multicastové skupině, což umožňuje efektivní komunikaci s více uzly současně.

#### Pipes
- *Nejjednodušší forma IPC*
- Potrubí je primitivní mechanismus, který vytváří spojení mezi dvěma procesy.
- Jedná se o **nejčastěji unidirekční**, což znamená, že data mohou proudit pouze jedním směrem.
- Pro komunikaci v obou směrech jsou potřeba dvě potrubí, jedno pro každý směr.
- Některé jazyky mají i **duplexní pipes** (např. Python)

- Existují dvě hlavní kategorie potrubí:
	- **Nepojmenované** - Vytváří se dynamicky **v rámci procesu a jeho potomků**. Vhodné pro komunikaci mezi příbuznými procesy.
	- **Pojmenované** - Existují **samostatně**. Jsou vhodné pro komunikaci mezi nezávislými procesy.
- Funguje na principu **FIFO**.

#### Fronta zpráv
- Fronta zpráv umožňuje *asynchronní komunikaci mezi komponentami systému*.
- Výměna zpráv probíhá přes centrální místo, které **udržuje zprávy dokud nejsou zpracovány**.
- Je možná **oboustranná komunikace**.

#### Síťové sokety
- Síťové sockety jsou rozhraním, umožňující aplikacím vytvářet komunikační kanály pro přenost dat přes síť.
- Proces komunikace pomocí síťových socketů může být rozdělen do několika kroků:
	1. **Vytvoření socketu**
	2. **Navázání spojení** (pouze pro klienta)
		- Pokud jde o komunikaci typu klient-server, klientový socket se snaží navázat spojení se serverovým socketem.
	3. **Naslouchání na serverovém socketu** (pouze pro server)
		- Pokud jde o serverový socket, ten čeká na příchozí požadavky na připojení od klientů.
	4. **Přijetí připojení** (pouze pro server)
	5. **Přenost dat**
	6. **Uzavření spojení**

>[!Example] Večeřící filozofové - distribuované řešení
>- Potřeba změnit zadání, jinak nelze distribuovaně řešit
>- **Vidličky = procesy**
>	- Komunikace mezi vidličkou a sdílenými filozofy.
>- **Filozofové mezi sebou dokáží mluvit.**
>	- Každý filozof dostane jednu špinavou vidličku.
>	- Když chce jíst potřebuje další vidličku od souseda, pošle mu zprávu s žádostí o vidličku.
>	- Pokud filozof obdrží žádost, vidličku si nechá pokud je čistá, jinak ji vyčistí a pošle (žádost si pamatuje)
>	- Když se filozof nají, vidličky jsou špinavé (pošle ji jedné zapamatované žádosti)

### Asynchronní programování
- Nejedná se o paralelní programování, kód se ve skutečnosti vykonává **sériově**.
- **Umožňuje efektivnější využití času v aplikacích**, zejména v situacích, kdy je čekání na dokončení operací neefektivní.
- Např. v kontextu webových služeb, síťové komunikace, GUI, ...

- Asynchronní programování umožňuje spouštět operace, které trvají delší dobu, bez blokování hlavního vlákna. Místo čekání na dokončení operace může hlavní vlákno pokračovat v provádění dalších úloh.
- Asynchronní programování je často spojeno **s neblokujícím vstupně-výstupním zpracováním**. To umožňuje programu pokračovat v provádění dalších úloh, zatímco čeká na dokončení operací I/O.

- **Synchronizace na úrovni funkcí**. V mnoha případech jsou asynchronní operace řízeny *callback funkcemi*. Callback je funkce, která je spuštěna po dokončení asynchronní operace.

### Korutiny
- Korutiny jsou programovacím konceptem, který umožňuje řízení průběhu programu tak, aby mohl být dočasně přerušen a později obnovem, aniž by byl ztracen aktuální stav.

- Kokutiny mohou být **kooperativní** nebo **preemptivní**. 
	- V kooperativním modelu je odpovědnost za přerušení a obnovení korutiny na programátorovi.
	- V preemptivním modelu může být přerušení prováděno automaticky systémem, například po uplynutí časovače.

- Kličové slovo `yield` je klíčovým prvkem v korutinách a indikuje místo, kde bude korutina dočasně přerušena a její aktuální stav bude vrácen volajícímu kódu. Při obnovení korutiny bude pokračovat od místa, kde byla posledně přerušena.

### Generátory
- Generátor je *speciální druh korutiny nebo funkce*, která umožňuje **postupné generování hodnot a udržuje svůj stav mezi voláními**.
- Generátor je pohodlným způsobem, jak vytvářet iterovatelné sekvence, aniž by bylo nutné ukládat všechny hodnoty do paměti najednou.
- V mnoha programovacích jazycích jsou generátory implementovány pomocí klíčových slov jako je `yield`

>[!Example] Příklad v jazyce Python
>```Python
>def generator():
>	yield 1
>	yield 2
>	yield 3
>	
># Vytvoření generátoru
>gen = generator()
>
># Iterace přes generátor
>for hodnota in gen:
>	print(hodnota)
>```

### Nativní korutiny
- Nativní korutiny *jsou přímo podporovány v jádře programovacího jazyka nebo runtime prostředí*.
	- To znamená, že nemusíme používat knihovny nebo dodatečné moduly pro vytváření a správu korutin.
- Nativní korutiny obvykle nabízejí *efektivní správu paměti*, což může být důležité při manipulaci s velkým množstvím korutin.

## Návrh paralelních programů
- Když chceme sekvenční úlohu přepsat na paralelní, obvykle postupujeme:
	1. Nejprve vyřešíme úlohu sekvenčně.
	2. Poté uděláme dekompozici sekvenční úlohy na paralelně vykonávané úlohy.
	3. Definujeme závislosti mezi úlohami.
	4. Je potřeba provést analýzu závislostí (dependency graph)

- Jsou dva typy dekompozice:
	1. **Dekompozice úloh** - rozložím na menší nezávislé paralelní úlohy
	2. **Dekompozice dat** - rozdělím data na nezávislé části, které pak zpracuji paralelně

>[!info] Fosterova metodologie
>- Vytvořil postup návrhů paralelních programů.
>
> Postup:
> 1. Rozdělení na menší části (dekompozice)
> 2. Zabezpečení komunikace mezi částmi
> 3. Aglomerace (spojování částí do logických celků)
> 4. Mapování (technická realizace)

## Chord systém
- = **Distribuovaná hash tabulka**
- Chord systém se používá pro organizaci a vyhledávání informací v distribuovaných systémech. Je navržen tak, aby poskytoval efektivní a spolehlivé řešení pro distribuované uchovávání a vyhledávání klíčů v síti. 
- Chord byl původně navržen pro použití v prostředí peer-to-peer sítí, ale jeho koncepty jsou aplikovatelné i na jiné typy distribuovaných systémů.

- Chord vytváří **kruhovou strukturu**, kde každý uzel (node) v síti má přiřazen jedinečný identifikátor (klíč). Uzly jsou uspořádány do kruhu podle hodnot jejich identifikátorů. Identifikátor má $m$ bitů (obvykle $128$ nebo $160$) a celkově je poté v $2^{m}$ uzlů.

- Uzel s klíčem $k$ je spravován uzlem s klíčem $id$, kde $id \geq k$, tento uzel se nazývá `succ(k)` (successor)

- Hlavní úkol je pro $k$ efektivně najít `succ(k)`.

>[!Example]- Řešení:
>- Každý uzel má **Finger Table (FT)** obsahující $s$ záznamů ($s <leq m$).
>- Záznamy v tabulce pro uzel $p$ vypočítáme následovně: $$FT_{p}[i]=\text{succ}(p+2^{i-1})$$
>- Poté uzel $p$ předá dotaz na klíč k uzlu $q$ na indexu $j$ následovně:$$FT_{p}[j] \leq k < FT_{p}[j+1]$$
>	- pokud $p < k < FT_{p}[1]$, pak $q = FT_{p}[1]$ (je menší než první záznam v tabulce)
>	- pokud $p < k \text{and} k > FT_{p}[s]$, pak $q = FT_{p}[s]$ (je větší než všechny záznamy v tabulce)
>![[MacBook-2025-01-03-002357@2x.png]]

### Přidání uzlu do chord systému
- Přidání uzlu do Chord systému je proces, který **zahrnuje aktualizaci struktury kruhu a redistribuci odpovědnosti za klíče** tak, aby nový uzel byl začleněn do sítě.

>[!Example] Postup:
>1. Nový uzel $p$, který se chystá připojit k síti, vygeneruje svůj jedinečný identifikátor (klíč).
>2. Nový uzel musí najít svého "souseda" v kruhu Chord. tj. `succ(p+1)`. Často provedeno pomocí **vyhledávacího dotazu**. Nový uzel může začít hledání od některého existujícího uzlu v síti.
>3. Každý uzel $q$ si drží aktualizovanou FT:
>	- $FT_{q}[1] = \text{succ}(q+1) - q$ ví, že první záznam odkazuje na následující uzel v kruhu.
>	- Každý uzel pravidelně ověřuje podmínku:
>		- $q = \text{pred}(\text{succ}(q+1))$
>		- **Pokud je nepravdivá**, pak $q < p < \text{succ}(q+1)$, je třeba nastavit $FT_{q}[1]=p$ (také je třeba ověřit, že $\text{pred}(p)=q$).
>		- Musím opravit zbytek $FT$ ($q$ musí najít $\text{succ}(k)$, $k = q + 2^{i-1}$)

### Smazání (výpadek, havárie) uzlu
- Každý uzel $p$ testuje, zde $\text{pred}(p)$ je naživu.
- Pokud $q$ aktualizuje spojení na dalšího souseda v kruhu a zjistí, že $\text{pred}(q+1)$ není nastaven, pak $\text{pred}(q+1) = q$.

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FProst%C5%99edky%20pro%20synchronizaci%20vl%C3%A1ken" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FKoordinace%20%C4%8Dasu%20v%20DS" style="text-decoration: none;">
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