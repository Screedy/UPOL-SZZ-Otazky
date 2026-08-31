- **Problém shody** vyžaduje, aby skupina $n$ procesů/uzlů, přičemž každý z nich navrhne hodnotu, _dosáhla shody_ na **jediné** _společné hodnotě nebo rozhodnutí,_ i když některé _uzly selžou_ nebo jsou _zprávy doručovány se zpožděním_.
- Bez dosažení shody by různé uzly mohly považovat za správné různé hodnoty, což by vedlo k nekonzistenci systému.

> [!note]
> **Intuice:** Představ si, že 5 serverů distribuované databáze musí souhlasit s tím, jestli se transakce provede nebo zruší. Každý má svůj lokální pohled. Bez algoritmu pro shodu by mohlo dojít k tomu, že část serverů transakci potvrdí a část zruší — data by byla nekonzistentní.

- **Požadavky**:
  - **Agreement (Shoda)** – všechny korektní uzly rozhodnou stejnou hodnotu
  - **Validity (Platnost)** – rozhodnutá hodnota musí pocházet z některého z navržených návrhů
  - **Termination (Ukončení)** – každý korektní uzel se nakonec rozhodne (algoritmus nesmí čekat donekonečna)

> [!warning]
> **Kdy shoda nastane triviálně?**
>
> - **Bez chyb** (výpadků uzlů, ztracených zpráv) je **shoda triviální**. Všechny uzly si _pouze vymění své návrhy a zvolí stejný výsledek_ podle předem daného pravidla
> - Skutečná obtíž nastává až ve chvíli, kdy mohou _uzly nebo komunikace selhávat_.

### Typy modelů selhání

| Model | Chování uzlu | Detekce |
| --- | --- | --- |
| **Fail-stop** | Uzel se zastaví a už nic neposílá. | Spolehlivá |
| **Fail-silent** | Uzel se zastaví, ale není jisté, zda selhal nebo je jen pomalý. | Nespolehlivá |
| **Fail-noisy** | Uzel sice selže, ale stále může posílat chybné nebo nekonzistentní odpovědi. | Částečně možná |
| **Byzantine fault** | Uzel se může chovat zcela libovolně – posílat různým uzlům různé informace, lhát nebo jednat zákeřně. | Prakticky nelze jednoduše detekovat |

---

# 1. Flooding Consensus

- Flooding Consensus je jednoduchý algoritmus pro dosažení shody v distribuovaném systému při **Fail-stop** selháních.
- Je založen na principu **opakovaného zaplavování (flooding)** sítě informacemi, dokud _všechny aktivní uzly neobdrží stejné návrhy_ a _nemohou se shodnout na společném výsledku_.

## 1.1 Princip

1. Každý uzel má **svůj vlastní návrh hodnoty**.
2. V každém kole _odešle svůj návrh všem ostatním uzlům_.
3. _Přijme návrhy_ od ostatních uzlů.
4. Podle _deterministického pravidla vybere nový kandidátní návrh_ (všichni musí stejně).
5. Pokud **neobdržel informace od všech uzlů**, _pokračuje dalším kolem_.
6. Po _dostatečném počtu kol_ mají **všechny funkční uzly stejné informace** a _rozhodnou stejnou hodnotu_

![[019f769a-dcc9-7643-8d1b-9dcf78de4e0b.png]]

> [!warning]
> **Složitost:**
>
> - **Počet zpráv:** $O(n^2)$ za kolo, až $O(f \cdot n^2)$ celkem,$f$= počet selhání
> - **Počet kol:** $f + 1$ (nejhůře tolik kol, kolik selhání)
> - **Časová složitost:** $O(f+1)$ kol

## 1.2 Vlastnosti

- Velmi jednoduchý algoritmus, snadná implementace
- **Velké množství zpráv** (každý komunikuje s každým), vhodný pro menší distribuované systémy
- Předpokládá **Fail-stop** model selhání

---

# 2. Paxos

- Paxos je distribuovaný algoritmus pro dosažení **shody** mezi uzly i v případě, že některé z nich selžou. Je navržen pro **Fail-stop (i Fail-silent)** model selhání.
- Paxos využívá **hlasování většiny (majority quorum)**.

> [!info]
> Je základem mnoha produkčních systémů (Google Chubby, Apache Zookeeper)

## 2.1 Princip

- Paxos rozlišuje _tři logické roce_:
  
  - **Proposer (navrhovatel)** – _vytváří návrhy_ a snaží se prosadit určitou hodnotu
  - **Acceptor (akceptor)** – _přijímá_ nebo _odmítá_ návrhy
  - **Learner (pozorovatel)** – získává informaci o hodnotě, která byla přijata většinou.
  
  Jeden fyzický uzel může zastávat více rolí současně.

- Principy f_ungování algoritmu Paxos jsou komplexní_, ale **základní kroky** mohou být popsány následovně:

### 1. Fáze přípravy

- Proposer vytvoří **jedinečné číslo návrhu** (_proposal number_) a odešle zprávu **Prepare(n)** všem Acceptorům.
- Acceptor po přijetí zprávy:
  1. Porovná číslo návrhu _s nejvyšším číslem_, které dosud **slíbil přijmout**
  2. Pokud je nové číslo vyšší, odešle odpověď **Promise** a _zaváže se_, že již _nepřijme_ žádný návrh s _nižším číslem_
  3. Zároveň Proposerovi _sdělí_, zda už _v minulosti_ **přijal nějaký návrh** (přijal hodnotu ve fázi přijetí). Pokud ano, pošle jeho číslo a hodnotu.

### 2. Fáze přijetí

- Pokud proposer obdrží odpověď **Promise** od většiny Acceptorů, odešle zprávu **Accept(n, v)**
- Hodnota **v** se _určuje následovně_:
  
  - Pokud žádný Acceptor dosud **žádnou hodnotu nepřijal**, proposer _použije svou vlastní hodnotu_
  - Pokud některý Acceptor **již přijal jiný návrh**, proposer musí převzít **hodnotu z návrhu s nejvyšším číslem**, kterou obdržel v odpovědích.
  
  Acceptor přijme zprávu **Accept** pouze tehdy, pokud mezitím neslíbil přijmout návrh s vyšším číslem.

### 3. Fáze rozhodnutí

- Jestliže návrh **Accept(n, v)** přijme _většina Acceptorů,_ je hodnota **v** považována _za schválenou_.
- Learneři se o této skutečnosti dozvědí a mohou rozhodnutí předat ostatním částem systému.

> [!warning]
> **Tolerance: m** chyb v **2m + 1** uzlech (protože shoda je na rozhodnutí většiny)
>
> **Složitost:**
>
> - **Počet zpráv:** $O(n)$ za fázi
> - **Počet kol (round-trips):** 2 (Fáze 1 + Fáze 2)

## 2.2 Průběh algoritmu

### 2.2.1 Klasický průběh

- Rozdělení — Každý uzel má svoji roli

![[019f8033-da16-74f8-bee8-3ba9a6233c1d.png]]

- Rozdělení — Každý uzel je vším

![[019f8021-99c5-7408-838d-0f51b552748a.png]]

### 2.2.2 Výpadek Acceptora

![[019f8033-901a-7348-b189-31c36a276558.png]]

### 2.2.3 Výpadek Proposera

![[019f803e-c4e6-75fa-aad9-b40b28e3c552.png]]

### 2.2.4 Chyba: vznik livelock

```
P1 vybere n=1, pošle PREPARE(1) → acceptoři slíbí P1
P2 vybere n=2, pošle PREPARE(2) → acceptoři slíbí P2 (vyšší n!)
P1 pošle ACCEPT(1, "X") → acceptoři ZAMÍTNOU (slíbili n=2)
P1 zvýší n=3, pošle PREPARE(3) → acceptoři slíbí P3
P2 pošle ACCEPT(2, "Y") → acceptoři ZAMÍTNOU (slíbili n=3)
... (cyklí donekonečna)
```

> [!success]
> **Řešení:** Zvolit jednoho **lídra** (distinguished proposer), který jako **_jediný navrhuje_**.

## 2.3 Vlastnosti

- Toleruje výpadky uzlů
- Nevyžaduje centrální koordinátor
- Tvoří základ řady distribuovaných databází a úložišť
- Složitější implementace
- Větší komunikační režie (více fází)
- Při více současných proposerech může docházet k opakovanému zahajování hlasování (livelock), proto se v praxi často používá **Multi-Paxos**, kde je dlouhodobě zvolen jeden proposer (lídr)

---

# 3. Byzantská shoda

- _Shoda při byzantských chybách_ řeší problém, jak zajistit, aby _všechny korektně fungující uzly_ dospěly ke **stejnému rozhodnutí**, i když se _některé uzly_ chovají **libovolně nebo zákeřně**.

## 3.1 Princip (myšlenka)

- Na rozdíl od Paxosu nestačí _pouze přijmout návrh_. Každý uzel musí také **ověřit, co ostatní skutečně obdrželi**.
- Proto si uzly nejen _předávají původní zprávu_, ale následně si mezi sebou vyměňují i informace o tom, **jakou zprávu každý z nich obdržel**. Tím lze **odhalit uzel**, který různým příjemcům poslal různé hodnoty.

1. Odesílatel (například server) _rozešle svůj návrh_ všem uzlům.
2. Každý uzel si _návrh uloží_.
3. Uzly si mezi sebou **vzájemně rozešlou, jakou zprávu obdržely**.
4. Každý uzel vytvoří _tabulku přijatých hodnot_.
5. Podle většinového rozhodnutí **vyhodnotí správnou hodnotu**.
6. Pokud je potřeba, _výměna informací pokračuje dalším kolem_, dokud všechny korektní uzly **nedospějí ke stejné shodě**.

> [!warning]
> Pro **toleranci m** byzantských uzlů je potřeba alespoň **3m + 1 uzlů**
>
> Komunikace je **velmi náročná**, protože uzly si vzájemně ověřují přijaté informace (exponenciální) **Složitost:** Exponenciální — $O(n^{m+1})$ zpráv.

## 3.2 Vlastnosti

- Odolnost vůči zákeřným uzlům, zajišťuje správnou shodu i při byzantských chybách,
- Využívá se například v některých blockchainových systémech a kritických distribuovaných aplikacích (Hyperledger Fabric, Zilliqa)
- Velmi vysoká komunikační režie