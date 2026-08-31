# 1. Globální stav

- **Globální stav** představuje _souhrnný stav_ distribuovaného systému _v určitém logickém okamžiku_. Je tvořen:
  - **lokálními stavy všech uzlů**,
  - **stavy všech komunikačních kanálů**
- **Znalost globálního stavu** je důležitá například _pro detekci deadlocku_, _detekci ukončení distribuovaného výpočtu_, _vytváření checkpointů_ nebo _obnovu systému po selhání_.

## 1.1 Lokální stav uzlu

- Lokální stav představuje _všechny informace_, které má **uzel v daném okamžiku k dispozici**. Typicky zahrnuje:
  - **hodnoty všech lokálních proměnných**,
  - **alokované zdroje** (otevřené soubory, zámky, …),
  - **stav vykonávání programu** (program counter, zásobník volání).

## 1.2 Stav komunikačních kanálů

- Součástí globálního stavu je také _stav komunikačních kanálů_. Ten tvoří zprávy, které již **byly odeslány**, ale ještě **nebyly doručeny** cílovému uzlu. Tyto zprávy označujeme jako **zprávy na cestě** (_messages in transit_).

> [!note]
> **_Intuitivně_** lze globální stav chápat jako _„snímek“ celého distribuovaného systému v jednom logickém okamžiku_, který zachycuje nejen stav jednotlivých uzlů, ale i všechny zprávy nacházející se právě na cestě mezi nimi.

## 1.3 Problém zachycení globálního stavu

- Určit _globální stav distribuovaného systému není jednoduché_.
- Pokud bychom postupně **_zjišťovali stav jednotlivých uzlů_**, _systém by mezitím dále pracoval_. Některé uzly by již _mohly odeslat nebo přijmout nové zprávy_, zatímco _jiné bychom ještě nezaznamenal_i. Výsledkem by mohl být **stav**, který ve skutečnosti **nikdy neexistoval**.

> [!info]
> _Například_ bychom mohli zaznamenat, že jeden _uzel již zprávu přijal_, ale u _druhého uzlu bychom ještě nezachytili její odeslání_. Takový globální stav by byl **nekonzistentní**.

- Je nutné zachytit takový stav systému, který _odpovídá skutečnému průběhu komunikace._ Takový stav označujeme jako **konzistentní globální stav**.

---

# 2. Řezy a konzistentní řezy

## 2.1 Řez (cut)

Řez v distribuovaném systému je rozdělení všech událostí v systému na dvě množiny:

- **minulost** — události, které se **„již staly"** (spadají do řezu),
- **budoucnost** — události, které se **„ještě nestaly"**.

> [!info]
> Na časovém diagramu lze _řez znázornit jako pomyslnou čáru procházející všemi uzly_. Události **nalevo** od řezu představují **minulost**, události **napravo budoucnost**.

- Ne každý řez však _odpovídá reálně možnému stavu systému_.

## 2.2 Konzistentní řez

- Řez je **konzistentní**, pokud **zachovává kauzální závislosti** mezi událostmi.

> [!warning]
> _Například pozor_:
>
> - Pokud řez obsahuje **přijetí zprávy**, musí obsahovat také její **odeslání**.
> - Naopak je možné, aby _řez obsahoval odeslání zprávy_, ale _nikoliv její přijetí_.

![[019f9987-3fa3-775c-aed2-30ab017f2e7f.png]]

## 2.3 Snapshot

**Snapshot** (nebo také **globální snímek**) distribuovaného systému je **globální stav** _odpovídající nějakému_ **konzistentnímu řezu**.

> [!danger]
> Snapshot **nemusí odpovídat jednomu skutečnému okamžiku reálného času**. Důležité však je, aby výsledný snapshot byl **logicky konzistentní**, tedy zachovával kauzální vztahy mezi událostmi.

- _Pořízení konzistentního snapshotu_ má v distribuovaných systémech řadu praktických využití:
  - **detekce deadlocku**, kdy lze ze snapshotu sestavit globální wait-for graf a hledat cyklické závislosti,
  - **detekce ukončení distribuovaného výpočtu**, kdy lze ověřit, že všechny uzly jsou pasivní a v síti nejsou žádné zprávy,
  - **checkpointing a obnova po selhání**, kdy se snapshot uloží jako konzistentní bod pro návrat systému,
  - **monitorování a ladění systému**, protože umožňuje analyzovat stav běžící distribuované aplikace.

---

# 3. Chandy-Lamportův algoritmus

- **Chandy–Lamportův algoritmus** je algoritmus určený k pořízení **konzistentního globálního snapshotu** distribuovaného systému _za jeho běhu_. Umožňuje zachytit lokální stavy všech uzlů i stav komunikačních kanálů, aniž by bylo nutné zastavit vykonávání systému.

> [!warning]
> Výsledkem algoritmu je **konzistentní globální stav**, který _zachovává kauzální vztahy mezi událostmi_ a _odpovídá konzistentnímu řezu_.

## 3.1 Předpoklady

- Aby algoritmus fungoval správně, musí být splněny následující podmínky:
- **Spolehlivé kanály** — zprávy se neztrácí a nepoškodí.
- **FIFO kanály** — zprávy na každém kanálu jsou doručovány ve stejném pořadí, v jakém byly odeslány. (Toto je klíčový předpoklad — bez FIFO kanálů algoritmus nefunguje!)
- Silně propojený graf komunikace (z každého uzlu je dosažitelný každý jiný).

## 3.2 Princip

> [!warning]
> Algoritmus využívá _speciální řídicí zprávu_ označovanou jako **marker**, která neslouží k přenosu dat, ale **pouze k vyznačení okamžiku**, od kterého se _pořizuje snapshot_.

### 1. Zahájení snapshotu

- Jeden z uzlů iniciuje vytvoření snapshotu.

1. Uloží svůj **lokální stav**
2. Odešle zprávu **MARKER** po všech svých odchozích komunikačních kanálech.
3. _Začne zaznamenávat všechny zprávy_ přicházející po svých příchozích kanálech.

### 2. Přijetí prvního markeru

- Pokud jiný uzel přijme marker poprvé:
  - Uloží svůj **lokální stav**,
  - Kanál, ze kterého marker přišel, označí jako **prázdný**,
  - Odešle marker po všech **svých odchozích kanálech**,
  - Z_ačne zaznamenávat zprávy_ přicházející po všech ostatních příchozích kanálech.

### 3. Zaznamenávání stavu kanálů

- Od okamžiku uložení svého lokálního stavu zaznamenává uzel _všechny zprávy přicházející po kanálech_, na kterých **ještě neobdržel marker**.
- Jakmile **marker** na některém z těchto kanálů dorazí, uzel zaznamenávání tohoto **kanálu ukončí**.
- Všechny zaznamenané zprávy (bez marker označení) představují **stav komunikačního kanálu**, tedy zprávy, které byly _při pořizování snapshotu právě na cestě mezi uzly_.

### 4. Dokončení snapshotu

- Snapshot je dokončen ve chvíli, kdy **každý uzel obdrží marker** na _všech svých příchozích kanálech_.
- Výsledný snapshot tvoří:
  - lokální stav všech uzlů,
  - stav všech komunikačních kanálů.
- Takto získaný snapshot odpovídá konzistentnímu globálnímu stavu systému.

## 3.3 Význam FIFO kanálů

- FIFO kanály zajišťují, že _marker nemůže předběhnout běžnou zprávu odeslanou dříve_.

## 3.4 Vlastnosti

- **Každým jednosměrným komunikačním kanálem projde právě jedna marker zpráva**, proto režie algoritmu roste lineárně s počtem komunikačních kanálů.
- **Vyžaduje spolehlivé FIFO komunikační kanál**
- **Nevyžaduje zastavení systému**

---

# 4. Detekce ukončení — Dijkstra-Scholten algoritmus

- **Dijkstra–Scholtenův algoritmus** slouží k detekci ukončení distribuovaného výpočtu. Jeho cílem je určit okamžik, kdy všechny uzly dokončily svou práci a v komunikačních kanálech již nejsou žádné zprávy, které by mohly některý uzel znovu aktivovat.

### 4.1.1 Předpoklady

- Algoritmus předpokládá:
  - výpočet zahajuje **jeden iniciující uzel** (difúzní výpočet),
  - uzly spolu komunikují pomocí zpráv,
  - každý uzel je buď **aktivní** (vykonává práci), nebo **pasivní** (čeká na zprávu),
  - pasivní proces nepošle žádnou zprávu,
  - komunikační kanály jsou **spolehlivé**.

### 4.1.2 Princip

- Algoritmus využívá dva typy zpráv:
  - **SIGNAL** – zpráva, která aktivuje další uzel nebo mu předává práci,
  - **ACK** – potvrzení, že uzel dokončil svou práci a již není potřeba na něj čekat.
- Každý uzel si vede **deficit**, který vyjadřuje počet dosud nepotvrzených zpráv. Na začátku je deficit všech uzlů nulový.

#### 1. Zahájení výpočtu

- Iniciující uzel začne výpočet odesláním jedné nebo více zpráv **SIGNAL** ostatním uzlům. Tím se tyto uzly aktivují.

#### 2. Zpracování zpráv

- Aktivní uzel může provádět výpočet a podle potřeby odesílat další zprávy **SIGNAL**, kterými aktivuje další uzly.
- **Při přijetí zprávy se zvýší deficit**, protože přijatá práce ještě nebyla potvrzena.

#### 3. Odesílání potvrzení

- Jakmile uzel _dokončí svou práci_ a _již nečeká na dokončení práce uzlů_, které sám aktivoval, odešle odesílateli potvrzení **ACK**.
- Odesláním **ACK se deficit sníží**.

#### 4. Detekce ukončení

- Potvrzení **ACK** se postupně _vracejí zpět k iniciujícímu uzlu_.
- Jestliže iniciující uzel:
  - je pasivní,
  - jeho deficit je nulový,
  - obdržel všechna potřebná potvrzení,
- pak je **výpočet ukončen**. To znamená, že žádný uzel již nevykonává práci a v systému nezůstaly žádné nepotvrzené zprávy.

### 4.13 Vlastnosti

- **Režie algoritmu je nízká** – ke každé zprávě **SIGNAL** je odesláno nejvýše jedno potvrzení **ACK**, takže počet řídicích zpráv roste lineárně s počtem přenesených zpráv (**O(m)**, kde _m_ je počet aplikačních zpráv).
- Je určen pro **difúzní výpočty**
- Vyžaduje **spolehlivé komunikační kanály**
- **Netoleruje selhání uzlů**

---

# 5. Distribuovaný commit

- **Distribuovaný commit** je mechanismus, který zajišťuje, aby byla operace provedena **na všech zúčastněných uzlech, nebo na žádném z nich**.
- Používá se především u distribuovaných transakcí, kdy _jedna transakce zahrnuje více databází nebo více uzlů_.
- Cílem je zachovat **atomicitu** transakce – všechny uzly musí dojít ke stejnému rozhodnutí, zda změny provedou, nebo zruší.

## 5.1 One-Phase Commit (1PC)

- Jednofázový commit je _nejjednodušší způsob distribuovaného commitu_.
- **Koordinátor** odešle _všem uzlům požadavek na provedení operace_ a **předpokládá, že ji všechny úspěšně provedou**. Účastníci _neposílají žádné potvrzení ani nehlasují o tom, zda jsou připraveni operaci provést_.

### 5.1.1 Nevýhody

- Koordinátor neví, zda _jsou všechny uzly schopné operaci provést_
- _Při selhání některého uzlu_ může být operace provedena pouze na části systému
- **Nezaručuje atomické provedení distribuované transakce**

> [!danger]
> Proto se v praxi pro distribuované transakce téměř nepoužívá.

## 5.2 Two-Phase Commit (2PC)

- Před samotným provedením operace ověří, zda jsou _všechny uzly připraveny transakci dokončit_.
- V algoritmu vystupují dvě role:
  - **koordinátor**, který řídí průběh transakce,
  - **účastníci (participanti)**, kteří transakci provádějí.

- Algoritmus probíhá ve dvou fázích.

### 1. fáze – Hlasování

- Koordinátor odešle všem účastníkům zprávu **VOTE-REQUEST** s dotazem, _zda jsou připraveni provést commit_.
- Každý účastník **zkontroluje**, _zda může transakci dokončit_.
  - Pokud ano, odešle **VOTE-COMMIT**. **Má stav READY**
  - Pokud ne, odešle **VOTE-ABORT**.

### 2. fáze – Rozhodnutí (Commit/Abort)

- Po obdržení všech hlasů koordinátor rozhodne o výsledku.
  - Pokud všichni hlasovali **VOTE-COMMIT**, odešle zprávu **GLOBAL-COMMIT** a všechny uzly transakci provedou.
  - Pokud alespoň jeden uzel hlasoval **VOTE-ABORT**, odešle **GLOBAL-ABORT** a všechny uzly transakci zruší.

### 5.2.1 Vlastnosti 2PC

- Zajišťuje atomické provedení distribuované transakce,
- Všechny uzly skončí se stejným výsledkem (commit nebo abort),
- Vyžaduje koordinátora, který řídí celý průběh transakce,
- Je **blokující** – pokud koordinátor selže po první fázi, mohou účastníci zůstat ve stavu čekání, dokud nebude koordinátor obnoven.

## 5.3 Three-Phase Commit (3PC)

- Three-Phase Commit rozšiřuje Two-Phase Commit o **třetí fázi**, která _snižuje riziko zablokování systému při selhání koordinátora_.

- Algoritmus probíhá ve třech krocích.

### 1. fáze – Hlasování

- Koordinátor odešle všem účastníkům dotaz, zda mohou transakci provést.
- Účastníci odpoví:
  - **VOTE-COMMIT**– jsou připraveni transakci provést, (stav **READY**)
  - **VOTE-ABORT**– transakci provést nemohou.

### 2. fáze – Příprava

- Pokud všichni odpověděli **VOTE-COMMIT**, koordinátor odešle zprávu **PRE-COMMIT**.
- Účastníci přejdou do připraveného stavu (**PRECOMMIT)** a potvrdí, že jsou připraveni dokončit transakci. (V této fázi ještě samotný commit neproběhne)

### 3. fáze – Commit

- Po obdržení všech potvrzení koordinátor odešle zprávu **COMMIT**.
- Všechny uzly provedou transakci a přejdou do konečného stavu.

### **5.3.1 Řešení problémů**

- **Koordinátor vypadne, účastník v READY:** Domluva s ostatními. Většina v READY → bezpečně ABORT (nikdo ještě nemohl commitovat).
- **Koordinátor vypadne, účastník v PRECOMMIT:** Domluva s ostatními. Většina v PRECOMMIT → mohou bezpečně COMMIT (víme, že všichni hlasovali COMMIT).
- **Následovník vypadne v PRECOMMIT:** Koordinátor čeká, pak COMMIT (po zotavení následovníka ten dokončí commit, protože byl v PRECOMMIT).

### 5.3.2 Vlastnosti

- Snižuje riziko zablokování při selhání koordinátora,
- Vyžaduje více zpráv a delší dobu komunikace než 2PC,
- Předpokládá časové limity (timeouty) a částečně synchronní systém,
- Ani 3PC nezaručuje správnou funkci při síťové partition nebo obecně v plně asynchronním systému