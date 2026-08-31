> [!warning]
> **DLT (Distributed Ledger Technology)** = distribuovaná účetní kniha.
>
> Obecný pojem pro systémy, kde _více nezávislých uzlů sdílí a udržuje shodnou kopii záznamů_ bez centrální autority.

- Představuje konkrétní implementaci **distribuované účetní knihy** **(Distributed Ledger Technology)**, ve které všechny zúčastněné uzly uchovávají vlastní kopii stejných dat.
- Díky tomu _není potřeba centrální autorita_, která by záznamy spravovala nebo ověřovala jejich správnost. Místo důvěry v jednu instituci je správnost dat zajištěna kombinací **kryptografických metod**, **mechanismů shody** a **replikace dat mezi uzly**.

- **Myšlenka** blockchainu _vznikla v roce 2008_, když někdo, který používal pseudonym **Satoshi Nakamoto**, publikoval bílou knihu s názvem **_"Bitcoin: A Peer-to-Peer Electronic Cash System"_**. Tato publikace byla zveřejněna _na kryptografickém fóru_.
- **První blockchain** byl _implementován jako součást kryptoměny Bitcoin_, která byla spuštěna **v lednu 2009**, jejímž cílem bylo _umožnit elektronické platby bez prostředníka_, například banky.
- Postupně se však začal _využívat i v dalších oblastech_, například pro _správu digitální identity_, _sledování původu zboží v logistice_, _ukládání zdravotnických záznamů_ nebo _provoz decentralizovaných aplikací_.

> [!info]
> Jelikož se jedná o distribuovaný systém _poskytující replikovaná dat_a, tak podle _CAP teorému, musíme uřinit volbu_. **_Typicky_** pro blockchain zachováváme **AP na úkor C**
>
> Dočasně tedy mohou **existovat konkurenční větve**, ale _pravidlo nejdelšího řetězu zajistí_, že se síť nakonec shodne. (větev, která má více bloků)

#### **Typy blockchainů**

- Blockchain lze rozdělit podle toho, **kdo může do sítě přistupovat a podílet se na ověřování transakcí**. Rozlišujeme tři základní typy:
  - **Veřejný**
    - Síť je otevřená **komukoliv**.
    - _Každý může číst data, připojit se jako uzel a podílet se na ověřování transakcí._
    - Typickými příklady jsou **Bitcoin** nebo **Ethereum**.
  - **Soukromý**
    - Síť spravuje **jedna organizace**, která rozhoduje o přístupu jednotlivých uživatelů.
    - Nabízí vyšší výkon, ale nižší míru decentralizace.
  - **Konsorciový (Hybridní)**
    - Blockchain je spravován **skupinou organizací** (konsorciem).
    - Představuje kompromis mezi veřejným a soukromým blockchainem a využívá se například v bankovnictví nebo logistice.

---

# 1. Datová struktura blockchainu

- Blockchain se skládá z jednotlivých **bloků**, které jsou _vzájemně propojeny do řetězce_ pomocí kryptografických hashů.
- Každý blok obsahuje dvě hlavní části: **hlavičku (Block Header)** a **data**

## 1.1 Hlavička bloku

- **Timestamp:** Časová značka vytvoření bloku
- **Hash aktuálního bloku:** Kryptografický hash obsahu bloku
- **Hash předchozího bloku:** Kryptografický hash předchozího bloku (tím vzniká řetězení)
- **Merkle root:** Hash reprezentující všechny transakce v bloku
- **Další metadata:** Nonce (při PoW), číslo bloku, obtížnost, verze protokolu, …

> [!warning]
> **Merkleův strom** je _stromová datová struktura_ (binární strom), ve které jsou všechny t_ransakce postupně hashovány_ a jejich hashe se _spojují až do jediného výsledného hashe_ nazývaného **Merkle root**. Ten je uložen v hlavičce bloku a umožňuje _rychle ověřit_, zda **nebyla některá z transakcí změněna**, aniž by bylo nutné kontrolovat celý blok.

## 1.2 Datová část

- Datová část obsahuje _seznam transakcí nebo jiných záznamů_, které mají být do blockchainu **trvale uloženy**.
- Obsah dat _závisí na konkrétní implementaci_ blockchainu

> [!info]
> **Genesis block** = první blok v řetězci. Nemá odkaz na předchozí blok. Obvykle je pevně zakódován v software.

> [!danger]
> **Důsledek řetězení bloků:**
>
> Pokud útočník **změní data v bloku** $n$, změní se hash $H_n$. Tím přestane souhlasit `prev_hash` v bloku $n+1$, a _kaskádově se rozbijí všechny následující bloky_.

> [!warning]
> **Kryptografická hashovací funkce** převádí libovolně dlouhá vstupní data na **hash (otisk)** _pevné délky_.
>
> **Vlastnosti kryptografické hashovací funkce:**
>
> - **Deterministická** – stejný vstup vždy vytvoří stejný hash.
> - **Jednosměrná** – z hashe nelze zpětně získat původní data.
> - **Odolná vůči kolizím** – je velmi nepravděpodobné, že dva různé vstupy vytvoří stejný hash.
> - **Citlivá na změnu vstupu** – i malá změna dat způsobí výraznou změnu výsledného hashe

> [!info]
> Transakce jsou podepisovány **privátním klíčem** odesílatele. Kdokoli může ověřit podpis pomocí odpovídajícího **veřejného klíče**.

---

# 2. Algoritmy shody (konsenzus)

- Blockchain je _distribuovaný systém bez centrální autority_, proto musí existovat mechanismus, který zajistí, že se všechny **_uzly shodnou na stejné verzi_** blockchainu. K tomu slouží **algoritmy shody (konsenzuální algoritmy)**

## 2.1 Proof of Work (PoW)

- **Proof of Work** je algoritmus shody, ve kterém uzly (**těžaři**) soutěží o vytvoření nového bloku řešením výpočetně náročné kryptografické úlohy.

1. Těžař posbírá čekající transakce do kandidátního bloku.
2. Sestaví _hlavičku bloku_. Důležitou součástí je **nonce**.
3. Hledá _takovou hodnotu nonce_, aby _hash celé hlavičky splňoval_ **podmínku obtížnosti**
  - _U Bitcoinu konkrétně_: hash musí začínat $n$ nulovými bity (délka nulového prefixu se upravuje).
4. Protože hash je kryptograficky jednosměrný, nezbývá než **zkoušet nonce jednu po druhé** (brute force).
5. Kdo najde platný nonce první, **rozešle blok do sítě** a **získá odměnu**.
6. **Ověření je triviální:** Ostatní uzly spočtou jeden hash a zkontrolují, zda splňuje podmínku — $O(1)$.

**Výhody:**

- Vysoká bezpečnost
- Odolnost proti podvodům a manipulaci (útok vyžaduje > 50 % výpočetního výkonu sítě)

**Nevýhody:**

- Vysoká spotřeba energie,
- Nižší rychlost zpracování transakcí,
- Potřeba specializovaného výpočetního hardwaru.

## 2.2 Proof of Stake (PoS)

- **Proof of Stake** je algoritmus shody, ve kterém nové bloky nevytvářejí těžaři, ale **validátoři**. Ti uzamknou určité množství svých mincí (**stake**) jako záruku poctivého chování.

1. Validátor nabídne **zástavu** (stake) — zamkne určité množství vlastněné kryptoměny daného blockchainu.
2. Systém **vybere validátora** pro vytvoření dalšího bloku na základě kombinace faktorů:
  - Velikost zástavy (čím víc vsadíš, tím větší šance)
  - Dlouhodobá důvěryhodnost
  - Prvek náhody
3. Vybraný validátor sestaví blok a rozešle do sítě.
4. Ostatní validátoři **ověří platnost** bloku.
5. Pokud je blok platný → validátor získá **odměnu** (poplatky, nové prostředky).
6. Pokud validátor podvádí → **ztrácí zástavu** (slashing) a je penalizován.

> [!info]
> **Klíčová ekonomická logika:** Podvod vyžaduje vlastnit velké množství prostředků → útočník útočí sám na sebe (znehodnocuje měnu, ve které má vázaný majetek).

**Výhody:**

- Nízká spotřeba energie
- Vyšší rychlost zpracování transakcí
- Není potřeba specializovaný hardware

**Nevýhody:**

- Větší vliv mohou získat uživatelé s velkým množstvím mincí,
- Bezpečnost závisí na správném nastavení pravidel výběru validátorů a sankcí.

## 2.3 Další mechanismy shody

| Mechanismus | Princip | Poznámky |
| --- | --- | --- |
| **Delegated PoS (DPoS)** | Držitelé mince volí malou skupinu validátorů; váha hlasu podle majetku | Rychlejší, ale více centralizované |
| **Proof of Authority (PoA)** | Předvybraná důvěryhodná skupina validátorů | Centralizace autority; vhodné pro privátní blockchainy |
| **Proof of Elapsed Time (PoET)** | Důvěryhodný HW (Intel SGX) generuje náhodné čekací doby | Nutný důvěryhodný HW; robustní systém práce s časem |
| **PBFT (Practical BFT)** | Klasický BFT protokol aplikovaný na blockchain | Toleruje byzantské uzly; problém se škálováním ($O(n^2)$ zpráv) |

---

# 3. Bitcoin

- Bitcoin je první a nejznámější kryptoměna, která byla představena v roce **2009** osobou nebo skupinou vystupující pod pseudonymem **Satoshi Nakamoto**. Jeho hlavním cílem je umožnit bezpečné elektronické platby bez potřeby centrální autority, například banky. Bitcoin využívá algoritmus **Proof of Work**, při kterém těžaři ověřují transakce a vytvářejí nové bloky.

---

# 4. Ethereum

- Ethereum je blockchainová platforma spuštěná v roce **2015**, která kromě kryptoměny **Ether (ETH)** umožňuje spouštění **chytrých kontraktů (smart contracts)** a decentralizovaných aplikací (dApps). Na rozdíl od Bitcoinu není určena pouze pro převod digitálních měn, ale umožňuje vytvářet a provozovat vlastní aplikace. Od roku 2022 využívá algoritmus **Proof of Stake**, který nahradil původní Proof of Work.

---

# 5. Bezpečnost a hrozby

| **Hrozba** | **Popis** | **Obrana** |
| --- | --- | --- |
| **51% útok** | Útočník ovládne většinu výpočetního výkonu (PoW) nebo většinu stake (PoS) a může měnit pořadí transakcí nebo provést **double spending**. | Decentralizace sítě, vysoké náklady na útok. |
| **Sybil útok** | Útočník vytvoří mnoho falešných identit a snaží se získat větší vliv v síti. | PoW a PoS vyžadují skutečné zdroje (výpočetní výkon nebo stake), ne pouze nové identity. |
| **Eclipse útok** | Útočník izoluje uzel od zbytku sítě a předkládá mu nepravdivé informace nebo falešný řetězec. | Připojení k více různým uzlům a náhodný výběr peerů. |
| **Chyby v chytrých kontraktech** | Programátorské chyby mohou umožnit zneužití kontraktu. | Testování, bezpečnostní audity a formální verifikace. |
| **Útoky na síťovou komunikaci** | Odposlech nebo manipulace s přenášenými daty mezi uzly. | Šifrování komunikace (např. TLS). |
| **Kryptografické hrozby** | Budoucí prolomení současných kryptografických algoritmů (např. kvantovými počítači). | Vývoj a nasazení postkvantové kryptografie. |
| **DDoS útok** | Zahlcení sítě velkým množstvím požadavků nebo transakcí. | Transakční poplatky, omezení počtu požadavků (rate limiting). |
| **Sociální inženýrství** | Podvodné e-maily, falešné peněženky nebo phishing zaměřený na uživatele. | Opatrnost uživatelů a jejich vzdělávání. |

---

# 6. Blockchain a Byzantská shoda

- Blockchain je v podstatě **řešení Byzantské shody v otevřeném prostředí** (permissionless).
- Klasická Byzantská shoda vyžaduje $n \geq 3f + 1$ pro toleranci $f$ byzantských selhání.
- Blockchain dosahuje lepšího poměru díky **ekonomickým pobídkám** — útočník riskuje reálné zdroje:
  - PoW: útok vyžaduje > 50 % výpočetního výkonu → $n > 2f$
  - PoS: útok vyžaduje > 50 % stake + riskuje slashing

| Vlastnost | Tradiční BFT (PBFT) | Nakamotův konsenzus (PoW) |
| --- | --- | --- |
| **Prostředí** | Permissioned (známí účastníci) | Permissionless (kdokoli) |
| **Tolerance chyb** | $n \geq 3f + 1$ | $n > 2f$ (ekonomická cena) |
| **Finalita** | Deterministická (okamžitá) | Pravděpodobnostní |
| **Škálovatelnost** | Špatná ($O(n^2)$ zpráv) | Dobrá (globální broadcast) |
| **Propustnost** | Vysoká (tisíce tx/s) | Nízká (jednotky tx/s u BTC) |
| **Spotřeba energie** | Minimální | Extrémní |

---