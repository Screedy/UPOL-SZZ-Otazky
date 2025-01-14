## Synchronizace bez sdílené paměti
### Distribuovaný systém
- Lze chápat jako *speciální* případ paralelního.
- Obecně se jedná o **kolekci (autonomních) systémů**, které se **chovají jako jeden systém**.
- Mohou být na jednom uzlu/stroji, na LAN i WAN.

- Rozdíly oproti dosud uvažovaným paralelním systémům:
	- Absence synchronizace pomocí sdílené paměti.
	- Musíme však řešit **komunikaci mezi systémy** (komunikace je nespolehlivá, pomalá).
	- Absence synchronizace času.
	- ...

#### Architektura distribuovaných systémů
- Skládá se z:
	- **uzlů**
	- **propojení uzlů**
	- **API** (umožňuje komunikaci mezi různými komponentami a poskytuje standardizovaný způsob, jakým mohou aplikace nebo služby vzájemně interagovat)
- Typy architektur:
	- Layer-based
		- Systém rozdělený do logických vrstev.
		- Vrstvy odděleny (nezávislé) a komunikují mezi sebou (API).
		- TCP/IP, MVC, ...
	- Services-oriented
		- Snaha o znovupoužitelnost komponent jako služeb.
		- Služby mohou běžet na různých strojích, vystavují rozhraní (API).
		- Vysoká modularita a dobrá škálovatelnost.
	- Event-based architecture
		- Centrální prvek jsou události a jejich průběh systémem.
		- Komponenty asynchronně produkují a konzumují události.
		- Chytrá domácnost, IoT, Kafka, ...
- Organizace distribuovaného systému:
	- **klient-server**
	- **peer-to-peer**

#### Klient-server
- Klienti požadují službu od serverů.
- Servery služby nabízejí.

- Jeden uzel může být pro někoho server a pro někoho klient.
- Typicky (ale není to nutnost) po síti.
- Request-response (požadavek-odpověď) komunikace.
- Např. webové služby, souborové servery, email servery, ...

#### Struktura peer-to-peer
- Označení typu počítačových sítí, ve které spolu komunikují přímo jednotliví klienti
- Každý uzel má stejnou roli i odpovědnost.
- Každý uzel zná své sousedy.
- Plně decentralizované a snadno škálovatelné.
- Např. Torrenty

### Komunikace
- V distribuovaných sítích existuje několik způsobů komunikace mezi uzly nebo komponentami systému. 
- Způsob komunikace může záviset na **architektuře** distribuovaného systému, **potřebách aplikace** a **požadovaných vlastnostech**.

- **Remote Procedure Call** (RPC)
- **Message-Oriented Communication** (MOC)
- **Inter Process Communication** (IPC)
- **Multicast** a **broadcast**

#### RPC
- Je mechanismus umožňující **volání procedur** nebo funkcí, které běží na vzdáleném počítači či uzlu, tak, **jako by byly volány lokálně**.
- Velmi komplikované - volaná procedura **nemá přístup** k aktuálnímu **stavu** volajícího. Proto je jej potřeba **předat** volanému.

>[!text] Hlavní myšlenka:
>- Volající netuší, že volá proceduru vzdáleného objektu.
>- Z jeho pohledu normální lokální volání a čeká na výsledek.
>- *Middleware* volajícího předhodí obrys vzdáleného objektu - **stub**.
>- A vyvolá metodu stubu $\rightarrow$ middleware zařídí komunikaci:
>	1. Vytvoří zprávu s požadavkem včetně argumentů,
>	2. vykomunikuje s OS odeslání zprávy serveru,
>	3. počká na odpověď,
>	4. rozbalí odpověď,
>	5. vrátí výsledek volajícímu.

>[!fail] Problémy RPC
>- Předávání parametrů (marshalling/unmarshalling)
>- Zpráva je posloupnost bytů - jak ji interpretovat?
>- Endianita

- Varianty RPC:
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

### Message-Oriented Communication (MOC)
#### Roura (pipe)
- Jednosměrné spojení výstupu procesu a vstupu jiného procesu.
- Funguje na principu **FIFO**.
- Pro komunikaci v obou směrech jsou potřeba dvě potrubí, jedno pro každý směr.
- Některé jazyky mají i **duplexní roury** (např. Python)

- Existují dvě hlavní kategorie rour:
	- **Nepojmenované** - Vytváří se dynamicky **v rámci procesu a jeho potomků**. Vhodné pro komunikaci mezi příbuznými procesy.
	- **Pojmenované** - Existují **samostatně**. Jsou vhodné pro komunikaci mezi nezávislými procesy.

#### Fronta zpráv (message queue)
- Centrální místo pro výměnu zpráv.
- Perzistentní, oboustranné.
- Posílá a přijímá zprávy daných typů.
- Např. RabbitMQ

#### Message broker
- Centrální místo pro výměnu zpráv.
- Obecné zprávy (procesy více typů).
- Rozumí typu zpráv.
- Analyzuje zprávu, nějak ji zpracuje a potom na to zareaguje.
- Např. Apache Kafka

#### Síťové sokety
- Síťové sockety jsou rozhraním, umožňující aplikacím vytvářet komunikační kanály pro přenost dat přes síť.
- Proces komunikace pomocí síťových socketů může být rozdělen do několika kroků:
	1. **Vytvoření socketu**
	2. **Navázání spojení** (pouze pro klienta)
		- Pokud jde o komunikaci typu klient-server, klientový socket se snaží navázat spojení se serverovým socketem.
	3. **Naslouchání na serverovém socketu** (pouze pro server)
		- Čeká na příchozí požadavky na připojení od klientů.
	4. **Přijetí připojení** (pouze pro server)
	5. **Přenos dat**
	6. **Uzavření spojení**

>[!Example]- Večeřící filozofové - distribuované řešení
>- Potřeba změnit zadání, jinak nelze distribuovaně řešit
>- **Vidličky = procesy**
>	- Komunikace mezi vidličkou a sdílenými filozofy.
>- **Filozofové mezi sebou dokáží mluvit.**
>	- Každý filozof dostane jednu špinavou vidličku.
>	- Když chce jíst potřebuje další vidličku od souseda, pošle mu zprávu s žádostí o vidličku.
>	- Pokud filozof obdrží žádost, vidličku si nechá pokud je čistá, jinak ji vyčistí a pošle (žádost si pamatuje)
>	- Když se filozof nají, vidličky jsou špinavé (pošle ji jedné zapamatované žádosti)

### Inter-Process Communication
- Komunikace mezi procesy na stejném stroji.
- Lze uvažovat vše zmíněné:
	- Sdílené paměť, synchronizační primitiva, roury, fronty, RPC
- Většinou není perzistentní, nejsou problémy sítě.
- Procesy mohou sdílet stav.

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

---
*\*Toto je navíc z předchozího ročníku.*

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

