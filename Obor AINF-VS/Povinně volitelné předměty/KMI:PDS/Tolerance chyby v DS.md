- **Tolerance chyb** je _schopnost_ distribuovaného systému **zachovat správnou funkčnost a korektnost** (pracuje dle specifikace)  i **přes přítomnost chyb** nebo **selhání některých jeho částí** (uzlů, komunikačních kanálů, …)

- Obecně by měli distribuované systémy _tolerovat určité množství chyb_
- Při návrhu _distribuovaného systému odolného vůči chybám_ se snažíme **zajistit** zejména:
  - **Dostupnost (Availability)** — Podíl času, kdy je systém funkční a připraven vyřídit požadavky uživatelů. (Např. 99,9% dostupný)
  - **Spolehlivost (Reliability)** — Pravděpodobnost, že systém poběží bez poruchy po určitou dobu.
  - **Bezpečnost (Safety)** — Chyba nezpůsobí katastrofické nebo nekorektní chování systému.
  - **Udržovatelnost (Maintainability)** — Chyby lze snadno odhalit, opravit a systém obnovit.

---

# 1. Klasifikace chyb

- Chyby lze rozdělit podle několika hledisek.
- Například podle _doby trvání, způsobu projevu_ nebo _možnosti jejich detekce_

## 1.1 Podle doby trvání

| Typ | Popis | Příklad |
| --- | --- | --- |
| **Přechodná (transient)** | Objeví se jednou a zmizí | Kosmické záření překlopí bit v paměti |
| **Přerušovaná (intermittent)** | Chyba se periodicky objevuje a mizí | Uvolněný konektor |
| **Trvalá (permanent)** | Zůstává do opravy/výměny | Spálená síťová karta |

## 1.2 Podle způsobu projevu

- Tato klasifikace popisuje, **jak se chyba projeví během komunikace nebo činnosti uzlu**

### 1.2.1 Stop chyba (Pád, Crash failure)

- Uzel přestane fungovat a již neprovádí žádné operace.
- Do okamžiku selhání pracoval správně.

> [!info]
> **Příklad:** Server spadne kvůli výpadku napájení.

### 1.2.2 Chyba vynechání (Omission failure)

- Selhání poslání či přijetí zprávy.
- Příčinou může být například výpadek sítě nebo přeplněný buffer.

> [!info]
> **Příklad:** Zpráva se během přenosu ztratí.

### 1.2.3 Časovací chyba (Timing failure)

- Uzel odpoví správně, ale mimo požadovaný časový interval.

> [!info]
> **Příklad:** Odpověď přijde až po vypršení timeoutu.

### 1.2.4 Chyba odpovědi (Response failure)

- Uzel odpoví, ale vrátí nesprávnou hodnotu nebo provede chybný přechod mezi stavy.

> [!info]
> **Příklad:** Databázový server vrátí chybný výsledek výpočtu.

### 1.2.5 Byzantská chyba (Byzantine failure)

- Uzel se může chovat zcela libovolně.
- Může různým uzlům posílat odlišné informace, lhát nebo jednat zákeřně.
- Jde o nejobecnější model selhání.

> [!info]
> **Příklad:** Kompromitovaný server posílá každé replice jiná data.

## 1.3 Podle možnosti detekce selhání

- Možnost detekovat selhání závisí na typu distribuovaného systému.

### 1.3.1 Asynchronní systém

- _Nelze spolehlivě rozlišit_, zda **uzel selhal nebo je pouze pomalý**.
- Neexistuje známá horní mez doby přenosu zpráv. (komunikace probíhá bez nějakého pevného časového rámce)

### 1.3.2 Synchronní systém

- Existuje **časový rámec pro vykonání operací** a _doručení zpráv_
- Pokud uzel _neodpoví do této doby_, lze jej **považovat za selhaný**.

### 1.3.3 Částečně synchronní systém

- Využívá **heartbeat.**
- Pokud heartbeat chybí $k$ period → předpokládáme selhání

# 2. Modely chování selhaného uzlu

> [!note]
> **Poznámka:** Tyto modely popisují **předpokládané chování selhaného uzlu**, zatímco klasifikace v předchozí kapitole popisuje **způsob, jakým se selhání projeví**. Proto nejde o dvě konkurenční klasifikace, ale o dva různé pohledy na selhání.

| Model | Chování uzlu | Detekce |
| --- | --- | --- |
| **Fail-stop** | Uzel se zastaví a již nekomunikuje. Ostatní uzly jeho selhání spolehlivě rozpoznají. | Spolehlivá |
| **Fail-silent** | Uzel přestane komunikovat, ale není možné jednoznačně určit, zda selhal nebo je pouze pomalý. | Nespolehlivá |
| **Fail-noisy** | Uzel může stále komunikovat, ale posílá chybné nebo nekonzistentní odpovědi. | Částečně možná |
| **Byzantine** | Uzel se může chovat zcela libovolně a posílat různým uzlům různé informace. | Prakticky nelze jednoznačně detekovat |

# 3. Redundance

- **Základní nástroj** pro _konstrukci distribuovaných systémů s tolerancí chyb_

> [!info]
> **Princip:** Zaveď víc komponent, než je nezbytně nutné, aby systém přežil výpadek části z nich.

## 3.1 Typy redundance

- **Informační redundance**
  - Je záměrně zavedena za účelem _zvýšení spolehlivosti, bezpečnosti nebo odolnosti_ vůči chybám **v přenosu nebo zpracování informací**
  - Kontrolní součty, paritní bity, ECC paměť (Error Correcting Code), …
- **Časová redundance**
  - Spočívá v **opakovaném provedení stejné operace**, aby se eliminovaly přechodné chyby nebo zvýšila pravděpodobnost úspěšného dokončení.
  - Opětovné odeslání zprávy po timeoutu, opakování výpočtu, opakovaný pokus o připojení k serveru, …
- **Fyzická (hardwarová) redundance**
  - Spočívá v **duplikaci hardwarových prostředků**, takže při selhání jedné komponenty může její funkci převzít jiná.
  - Záložní servery, RAID pole, redundantní síťová připojení, dvojité napájecí zdroje, replikované uzly v distribuovaném systému.

## 3.2 k-tolerantní systém

- Systém je **k-tolerantní**, pokud dokáže správně fungovat i při selhání až **k uzlů**.
- Například:
  - **1-tolerantní** systém přežije výpadek jednoho uzlu.
  - **2-tolerantní** systém přežije výpadek dvou uzlů.

> [!info]
> **Příklad:** Máme cluster o pěti serverech. Pokud je navržen jako **2-tolerantní**, bude fungovat i při výpadku libovolných dvou serverů.

## 3.3 Organizace uzlů do skupin

- _Použití redundance_
- V distribuovaných systémech se pro zvýšení odolnosti často **sdružují uzly do skupin**
- Místo komunikace s jednotlivými uzly komunikuje aplikace **se skupinou jako celkem**, což vytváří abstrakci nad jednotlivými uzly.

> [!info]
> **Příklad:** Databáze může být replikována na třech serverech. Klient komunikuje s databázovou službou jako s jedním celkem, i když jsou data uložena na více uzlech. Pokud jeden server selže, ostatní nadále poskytují službu.