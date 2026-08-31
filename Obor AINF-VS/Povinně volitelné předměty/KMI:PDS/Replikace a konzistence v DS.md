- **Replikace** je _vytváření a udržování více kopií stejných dat nebo služby na různých uzlech distribuovaného systému_. Tyto kopie se označují jako **repliky**.
- Replikace představuje formu **redundance**, protože _stejná data jsou uložena na více místech_. Oproti běžné redundanci však přináší i **další výhody**, například _geografická dostupnost_, _rozložení zátěže_ (load balancing), _nižší latence pro klienty blíže k replice_.
- **Důvody replikace:**
  - **Zvýšení spolehlivosti (reliability)** — při výpadku jednoho uzlu jsou data stále dostupná na ostatních replikách
  - **Zvýšení výkonu** — čtecí požadavky lze rozdělit mezi více uzlů a snížit tak jejich zatížení.
  - **Zvýšení dostupnosti (availability)** — systém může obsluhovat požadavky i při výpadku části uzlů.
  - **Nižší latence** — klient komunikuje s geograficky nejbližší replikou

> [!danger]
> **Problém:** Replikace přináší jednu zásadní nevýhodu – **je potřeba zajistit, aby všechny repliky obsahovaly stejná data**.

> [!info]
> _Příklady replikace v praxi_
>
> - **Cache** — lokální kopie vzdálených dat; nejjednodušší forma replikace.
> - **CDN (Content Delivery Network)** — obsah webových stránek je uložen na serverech po celém světě, takže uživatel stahuje data z nejbližší lokality.
> - **DNS** — hierarchicky replikovaná databáze doménových jmen.
> - **Distribuované databáze** — PostgreSQL streaming replication, CockroachDB, Cassandra využívají replikaci pro zvýšení dostupnosti a odolnosti vůči chybám

---

# 1. Modely konzistence

- Konzistence určuje, **jakým způsobem se změny dat šíří mezi replikami** a **jaké hodnoty mohou klienti při čtení získat**.
- Jednotlivé modely se liší tím, jak přísně vyžadují shodu mezi replikami.

> [!warning]
> Obecně platí, že **čím silnější konzistence je požadována, tím více synchronizace mezi uzly je potřeba**, což zvyšuje latenci a snižuje výkon systému.

## 1.1 Silná konzistence (Linearizovatelnost)

- Silná konzistence zajišťuje, že všechny operace se chovají tak, **jako by existovala pouze jedna společná kopie dat**.
- Jakmile je _zápis potvrzen_, všechny _následující čtecí operace_ **musí vrátit novou hodnotu** bez ohledu na to, ze které repliky klient čte.
- **Příklad:**
  - Klient A zapíše $x = 1$ v čase $t_1$, potvrzení dostane v $t_2$.
  - Klient B čte $x$ v čase $t_3 > t_2$→ musí dostat $x = 1$.
  - Pokud B čte mezi $t_1$ a $t_2$, může dostat starou nebo novou hodnotu, ale jakmile jednou nová hodnota „prosvitne", stará se už nesmí vrátit.

## 1.2 Sekvenční konzistence

- Sekvenční konzistence vyžaduje, aby všechny operace proběhly v **jednom společném pořadí**, které je stejné pro všechny uzly. Na rozdíl od linearizovatelnosti však **nemusí odpovídat skutečnému času**, ale musí zachovat pořadí operací každého jednotlivého uzlu.
- To znamená, že _dvě operace různých klientů mohou být v globálním pořadí prohozeny_, i když jedna z nich ve skutečnosti proběhla dříve.
- **Příklad:**
  - Klient A provede dva zápisy: nejprve $x = 1$ a poté $x = 3$.
  - Mezitím klient B zapíše hodnotu $x = 2$.
  - Systém může určit globální pořadí operací například jako $x = 2 \rightarrow x = 1 \rightarrow x = 3$ nebo $x = 1 \rightarrow x = 2 \rightarrow x = 3$ nebo $x = 1 \rightarrow x = 3 \rightarrow x = 2$.
  - Vždy však musí být zachováno pořadí operací každého jednotlivého klienta. Proto zápisy **klienta A** _musí být vždy ve stejném pořadí_ ($x = 1 \rightarrow x = 3$).

## 1.3 Kauzální konzistence

- Kauzální konzistence zachovává **příčinné souvislosti mezi operacemi**.Pokud jedna _operace vznikla jako_ **_důsledek_** _jiné operace_, musí všechny uzly **vidět nejprve příčinu** a _teprve potom následek_.Naopak operace, které spolu **nijak nesouvisejí**, mohou _jednotlivé uzly vidět v různém pořadí_.
- **Příklad:**
  - Klient A zapíše hodnotu $x = 1$.
  - Klient B přečte hodnotu $x = 1$ a na základě této informace zapíše $y = 2$.
  - Klient C následně přečte hodnotu $y = 2$→ musí zároveň vidět také $x = 1$, protože zápis $y = 2$ vznikl jako důsledek zápisu $x = 1$.

## 1.4 Eventuální konzistence

- Eventuální konzistence představuje _nejslabší běžně používaný model konzistence_.
- Po provedení zápisu _nemusí všechny repliky obsahovat novou hodnotu_ **_okamžitě_**. Pokud však _již neproběhnou žádné další změny_, všechny repliky se **po určité době** _shodnou na stejném stavu_.
- Klient tedy může po určitou dobu číst zastaralá data.
- **Příklad:**
  - Klient A zapíše hodnotu $x = 20$ na jednu repliku.
  - Klient B krátce poté čte hodnotu $x$ z jiné repliky → může ještě dostat starou hodnotu $x = 15$.
  - Po určité době se změna rozšíří na všechny repliky.
  - Pokud již neproběhnou žádné další zápisy, všechny repliky se nakonec shodnou na hodnotě $x = 20$

### 2.6 Přehled modelů konzistence (od nejsilnější po nejslabší)

| Model | Garance | Cena | Příklad systému |
| --- | --- | --- | --- |
| **Linearizovatelnost** (silná) | Globální pořadí respektující reálný čas | Nejvyšší latence, nutná synchronizace | Spanner (Google TrueTime) |
| **Sekvenční konzistence** | Globální pořadí respektující programové pořadí | Vysoká, ale bez nutnosti přesných hodin | Zookeeper |
| **Kauzální konzistence** | Kauzálně závislé operace ve správném pořadí | Střední — vyžaduje sledování kauzality (vektorové hodiny) | COPS, MongoDB |
| **Eventuální konzistence** | Repliky se nakonec shodnou | Nejnižší latence, nejvyšší dostupnost | Cassandra, DynamoDB, DNS |

---

# 2. Metody replikace

- Replikaci lze _realizovat několika způsoby_. Jednotlivé metody se liší způsobem, _jakým jsou_ **_změny_** _mezi replikami_ **_šířeny_**, _jak rychle jsou_ **_potvrzovány_** a _jak se systém chová při_ **_výpadku_** _některého uzlu_.

## 2.1 Primary-Backup

- V systému existuje **jeden primární uzel (Primary nebo Leader)** a jeden nebo více **záložních uzlů (Backup nebo Follower)**.
- Veškeré **zápisy** provádí _pouze primární uzel_. Ten následně _změny přenese na záložní uzly_. Klienti mohou **číst buď pouze** _z primárního uzlu_ (silnější konzistence), nebo _i ze záloh_ (vyšší výkon, ale možnost zastaralých dat).
- **Výpadek primárního** → Záloha převezme roli (failover, potřeba zjistit)
- **Varianty:**
  - **Synchronní replikace** — primární _čeká na potvrzení od všech zálo_h → silná konzistence, vyšší latence.
  - **Asynchronní replikace** — primární _potvrdí klientovi okamžitě_, _zálohy dostanou data později_ → nižší latence, ale při výpadku primárního mohou být ztraceny posledních zápisy.

## 2.2 Replikovaný zápis (Replicated Write / Active Replication)

- Všechny _uzly mají stejnou roli_ a _provádějí stejné operace_.
- Aby všechny repliky skončily ve stejném stavu, musí všechny bezchybné uzly vykonávat **stejné operace ve stejném pořadí**. Toho se obvykle dosahuje pomocí **total-order multicast** nebo _některého z konsenzuálních protokolů_.
- **Výhoda:** _Nemá single point of failure_, žádný kritický bod.
- **Nevýhoda:** _Nutná koordinace_ — všechny bezchybné procesy musí vykonat stejné operace ve stejném pořadí

## 2.3 Řetězová replikace (Chain Replication)

- _Repliky jsou uspořádány_ do **řetězce**.
- _První_ uzel se označuje jako **hlava (Head)** a _poslední_ jako **ocas (Tail)**.
  - Všechny **zápisy** vstupují do systému **přes hlavu**
  - _Změny postupně procházejí_ celým řetězcem
  - **Ocas potvrzuje zápis klientovi** (potvrzení = zápis je na všech replikách)
  - **Čtení** probíhá pouze z **ocasu**, protože obsahuje _již potvrzená data_
- **Vlastnosti:**
  - **Silná konzistence** — čtení z ocasu vrací vždy potvrzená data.
  - _Koncepčně jiná než primary-backup_: nemáme leadera v tradičním smyslu.
  - Při čtení _reaguje ocas rovnou_ (nemusí komunikovat s ostatními).
- **Tolerance chyb (fail-stop model):**
  - Selhání hlavy → náhrada následníkem v řetězu.
  - Selhání ocasu → náhrada předchůdcem.
  - Selhání uzlu uprostřed → řeší centrální správcovský uzel (překlenutí řetězu).
  - **Centrální správcovský uzel musí být sám replikován**!
- **Nevýhoda:** Jeden pomalý uzel degraduje celý systém (latence závisí na nejpomalejším článku řetězu)

## 2.4 Replikace pomocí konsenzu (Raft, Paxos)

- **Raft**
  - Moderní protokol pro shodu v DS ve formě replikovaného logu operací.
  - Všechny uzly ve skupině udržují replikovaný **log operací**.
    - Klient odešle požadavek leaderovi.
    - Leader zapíše operaci do svého logu.
    - Operaci odešle followerům.
    - Followeri zápis uloží a odešlou potvrzení.
    - Jakmile leader obdrží potvrzení od většiny uzlů (kvóra), označí operaci jako potvrzenou (commit).
    - Leader potvrdí úspěšné provedení klientovi.
- **Paxos** — starší, obecnější, ale komplikovanější. Prakticky ekvivalentní, ale obtížněji srozumitelný.
- Oba zajišťují **silnou konzistenci** za cenu majority kvóra.

---

# 3. CAP teorém

- Brewer, 2000; formální důkaz Gilbert & Lynch, 2002
- **CAP teorém** říká, že distribuovaný systém _nemůže při výpadku komunikace mezi uzly_ **současně zaručit všechny tři** následující **vlastnosti**:
  - **Consistency (C) – konzistence**
  - **Availability (A) – dostupnost**
  - **Partition tolerance (P) – odolnost vůči rozdělení sítě**
- Z těchto tří vlastností lze současně zaručit **nejvýše dvě**.

### Consistency (C)

- Po provedení zápisu všechny následující čtecí operace vracejí stejnou, aktuální hodnotu bez ohledu na to, ze které repliky klient čte.

### Availability (A)

- Každý funkční uzel vždy odpoví na požadavek klienta.

### Partition tolerance (P)

- Systém zůstává funkční i v případě, že mezi některými uzly dojde k přerušení komunikace (vzniknou izolované části)

## 3.1 Kombinace vlastností

### 3.1.1 CP (Consistency + Partition tolerance)

- Důležitější jsou **správná data**
- Při rozdělení sítě může _být část systému nedostupná_
- **Příklady:**
  - ZooKeeper,
  - HBase.

### 3.1.2 AP (Availability + Partition tolerance)

- Důležitější je **nepřetržitá dostupnost systému**
- Klient může dočasně získat neaktuální data
- **Příklady:**
  - Cassandra
  - DynamoDB
  - DNS

### 3.1.3 CA (Consistency + Availability)

- Současně zajišťuje **konzistenci i dostupnost**
- Předpokládá, že _nedochází k rozdělení sítě_
- _V distribuovaných systémech není dosažitelná_, protože tam musíme počítat s partition.
- **Příkladem** může být databáze běžící na jediném serveru.

---

# 4. PACELC teorém

- **PACELC teorém** _rozšiřuje CAP teorém_.
  - **Pokud dojde k rozdělení sítě (Partition)**, volíme mezi:
    - **Availability (A)** – dostupností
    - **Consistency (C)** – konzistencí
  - **Jinak (Else)**, když síť funguje správně, volíme mezi:
    - **Latency (L)** – nízkou odezvou
    - **Consistency (C)** – konzistencí

> [!note]
> **Jinými slovy**: CAP řeší, co dělat při výpadku sítě, zatímco PACELC popisuje kompromisy i během běžného provozu.

- **Příklady:**
  - PostgreSQL (distribuovaný): **PC/EC** — vždy konzistence, i za cenu latence.
  - Cassandra: **PA/EL** — vždy dostupnost a nízká latence.

---

# 5. CALM teorém

- **CALM (Consistency As Logical Monotonicity)** teorém říká, že:

> [!success]
> Pokud je **výpočet monotónní,** lze _dosáhnout správného výsledku_ **bez koordinace** mezi uzly**.** Pokud **monotónní není,** je **koordinace nutná.**

- Monotónní operace jsou takové, při kterých přidávání nových informací **nemění dříve získané výsledky**.

> [!info]
> **Příklad**: Přidávání do seznamu, sjednocení množin, grow-only counter, …

- Nemonotónní operace mohou po příchodu nových dat změnit dřívější výsledek.

> [!info]
> **Příklad**: maximum/minimum, množinový rozdíl, mazání prvků, …

## 5.1 Význam pro praxi

- CALM dává **teoretický základ pro CRDT** (Conflict-free replicated data type) — datové struktury, které jsou monotónní a tedy konzistentní bez synchronizace.
- Pokud víme, že naše _operace jsou monotónní_, **můžeme je bezpečně replikovat bez konsenzu** → vysoká dostupnost, nízká latence.

---