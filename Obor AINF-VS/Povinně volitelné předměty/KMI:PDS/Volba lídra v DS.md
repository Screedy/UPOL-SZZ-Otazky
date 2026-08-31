- V distribuovaném systému často potřebujeme, aby měl **jeden uzel** speciální roli – **lídra** **(koordinátora)**. Ten například koordinuje přístup ke sdílenému zdroji, komunikuje s uživatelem, …
- Protože ale může lídr kdykoliv selhat, musí se uzly umět samy dohodnout na novém lídrovi. Tomuto procesu říkáme **volba lídra (Leader Election)**.

> [!note]
> **Intuice:** Distributed systémy nemají přirozeného koordinátora — každý uzel je „rovnocenný". Ale spousta algoritmů potřebuje koordinátora. Volba lídra je mechanismus, jak takového koordinátora demokraticky zvolit.

- **Předpoklady**:
  - Každý uzel má jednoznačný identifikátor (ID)
  - Uzly o sobě navzájem vědí (znají ostatní členy systému)
- Vlastnosti správného algoritmu volby lídra
  - **Safety (bezpečnost):** V každém okamžiku je **nejvýše jeden** lídr.
  - **Liveness (živost):** Algoritmus _vždy doběhne_ — lídr bude nakonec zvolen.
  - **Agreement (shoda):** _Všechny uzly se shodnou_ na totožnosti lídra.

---

# 1. Bully algoritmus

- Bully algoritmus slouží k **volbě nového lídra v distribuovaném systému**, _když původní lídr přestane odpovídat_ (například havaruje).
- Cílem je, aby se všechny uzly shodly na jednom novém koordinátorovi. Ve výsledku se **lídrem vždy stane uzel s nejvyšším identifikátorem (ID), který je právě funkční.**

## 1.1 Princip

1. Každý uzel _pravidelně kontroluje_, zda současný **lídr stále komunikuje**.
2. Pokud některý uzel zjistí, že _lídr neodpovídá, zahájí volby_. Pošle zprávu **ELECTION** všem uzlům, které mají **vyšší ID**, _než má on sám_.
3. Pokud některý z těchto uzlů odpoví, znamená to, že _existuje "silnější" kandidát_. Tento uzel následně sám _zahájí nové volby_ a **osloví pouze uzly s ještě vyšším ID**.
4. Celý proces se tak postupně _posouvá směrem k nejvyššímu ID v systému_.
5. Jakmile _žádný vyšší uzel neodpoví_, poslední aktivní uzel pozná, že _je nejvyšší_, **prohlásí se za nového lídra** a rozešle všem zprávu **COORDINATOR**, aby _oznámil výsledek voleb_. Ostatní uzly si následně _uloží jeho identifikátor jako nového koordinátora_.

> [!warning]
> **Složitost v nejhorším případě**:$O(n^2)$ zpráv. Nastane tehdy, když volby zahájí uzel s nejnižším ID.
>
> **Složitost v nejlepší případ:** $O(n)$ zpráv. Volby zahájí uzel hned pod nejvyšším ID.

## 1.2 Vlastnosti

- Jednoduchý algoritmus, rychle zvolí nového lídra
- Časová složitost je **O(n²)**, takže se nehodí pro velké distribuované systémy
- Předpokládá **úplný graf** — každý zná každého.

---

# 2. Ring algoritmus

- **Ring algoritmus** slouží k _volbě nového lídra v distribuovaném systému_, například po výpadku současného koordinátora.
- Uzly jsou uspořádány do **logického kruhu (ringu)** a každý uzel _komunikuje pouze se svým sousedem_.

## 2.1 Princip

1. Když některý uzel zjistí, že je _potřeba zvolit nového lídra_, **vytvoří zprávu** =**"lístek"** obsahující _své ID_ a _pošle ji svému sousedovi_.
2. Každý uzel, který zprávu obdrží, _porovná ID uvedené na lístku se svým vlastním_:
  - pokud je jeho ID **větší**, přepíše lístek svým ID,
  - pokud je jeho ID **menší nebo stejné**, nechá původní ID beze změny.
3. Poté zprávu pošle dál svému sousedovi.
4. Po jednom oběhu kruhu se _zpráva vrátí uzlu, který volbu zahájil_. Na lístku už bude **nejvyšší ID v celém systému**, tedy nový lídr.
5. Tento uzel následně rozešle druhou zprávu **oznamující výsledek voleb** všem ostatním uzlům. Ty si uloží identifikátor nového lídra.

> [!warning]
> **Časová složitost** :$O(n)$ zpráv. Celkem $\approx 2n$ zpráv.

## 2.2 Vlastnosti

- _Jednoduchý_ algoritmus
- Každý uzel komunikuje _pouze se svým sousedem_
- Vyžaduje **logickou kruhovou topologii**, při _změně nebo výpadku uzlu_ je potřeba _kruh znovu propojit_.

---

# 3. Raft

- _Moderní_ (2014) a především _jednoduchý_ algoritmus, založený na **většinové shodě**.

> [!info]
> Běžně se _používá_ **pro replikaci da**t, avšak lze _použít i pro samotnou volbu lídra._

## 3.1 Princip

- V systému existují _tři možné role uzlu_:
  - **Follower (následovník)** – běžný uzel, který pouze čeká na pokyny od lídra.
  - **Candidate (kandidát)** – uzel, který se snaží stát lídrem.
  - **Leader (lídr)** – koordinuje celý systém.
- Každé volby probíhají v určitém **Termu (volebním období)**.
  - Každé nové volby znamenají nový **Term**.
  - V jednom **Termu** může být zvolen nejvýše jeden **Leader**.
  - Pokud uzel obdrží zprávu s vyšším **Termem**, pozná, že jeho informace jsou zastaralé, přejde do stavu **Follower** a přijme novější stav systému.
- Každý **Follower** má nastavený **Election Timeout**, tedy **náhodně zvolený časový interval**, po který _čeká na zprávu od Leadera_. Náhodná délka timeoutu snižuje pravděpodobnost, že _více uzlů zahájí volby současně_.
- Zvolený **Leader** pravidelně rozesílá zprávy **Heartbeat**, kterými ostatním uzlům oznamuje, že **je stále aktivní**. Dokud **Followers** tyto zprávy _přijímají, nové volby nespouštějí_.

**Postup**:

1. Po spuštění systému jsou _všechny uzly ve stavu_ **Follower**.
2. Pokud některému **Followerovi** vyprší **Election Timeout** a neobdržel žádný **Heartbeat**, předpokládá _selhání_ **Leadera**. Přepne se do stavu **Candidate**, zvýší číslo **Termu**, hlasuje sám pro sebe a _rozešle ostatním uzlům zprávu_ **RequestVote**, ve které je _žádá o jejich hlas_.
3. Každý **Follower** po přijetí zprávy **RequestVote** rozhodne, zda kandidátovi udělí svůj hlas. V jednom **Termu** může _hlasovat pouze jednou_.
4. Jakmile **Candidate** získá _hlasy od většiny uzlů_, stává se **Leaderem**.
5. Nově zvolený **Leader** začne pravidelně rozesílat **Heartbeat** zprávy. Tím _ostatním uzlům potvrzuje, že je stále aktivní_.
6. Pokud **Heartbeat** přestanou přicházet, některému **Followerovi** opět vyprší **Election Timeout** a celý proces voleb začne znovu v novém **Termu**.

![[019f7539-03b3-700d-9ed7-d65bf9410a29.png]]

> [!warning]
> **Složitost zpráv na kolo:** $O(n)$
>
> **Počet kol:** Typicky 1. Při split-vote se opakuje (náhodné timeout minimalizuje opakování)
>
> **Heartbeat overhead:** $O(n)$ zpráv na každý heartbeat interval

## 3.2 Vlastnosti

- Používá _demokratické hlasování_
- Běžně používaný v **praxi**
- Kromě volby lídra řeší i _replikaci dat a dosažení shody_
- Při rozdělení sítě _nemusí být možné zvolit lídra_, pokud žádná část nezíská většinu

---

# 4. Algoritmus pro ad-hoc sítě

- Slouží k volbě uzlu, který bude dočasně koordinovat činnost ostatních uzlů v **ad-hoc síti**, tedy _síti bez pevné infrastruktury_.
- Vybírá se uzel, který je pro roli lídra **nejvhodnější** podle **předem zvolených kritérií** (latence, výkon, zdroje).

## 4.1 Princip

- _Libovolný uzel_ (source) zahájí volbu a _rozešle svým sousedům zprávu_ **ELECTION**.
- Pokud uzel obdrží zprávu **ELECTION poprvé**, označí odesílatele jako svého **rodiče** **(parent)**. Následně přepošle zprávu **ELECTION** všem svým sousedům kromě rodiče a čeká na potvrzení od nich.
- Pokud uzel později obdrží stejnou zprávu **ELECTION** _od jiného souseda než svého rodiče_, pouze její přijetí _potvrdí_, ale dále ji již nešíří.
- Jakmile uzel obdrží _potvrzení od všech sousedů_, vytvoří **seznam potvrzení** a **připojí informace o svých vlastnostech** (například stav baterie, výkon, rychlost nebo jiná kritéria důležitá pro volbu lídra). Tyto informace odešle svému rodiči.
- Každý rodič _shromáždí informace od svých potomků_, vybere vždy **nejlepšího kandidáta** podle zvolených kritérií a _tuto informaci pošle dále_ směrem ke svému rodiči.
- Nakonec se všechny informace _dostanou zpět_ k uzlu **source**, který obdrží **nejlepšího kandidáta** z celé sítě a _vyhlásí jej jako nového_ **Leadera**.

> [!info]
> **Výsledná struktura:** Vzniká **spanning tree** (kostra grafu) — kořen je iniciátor, listy jsou okrajové uzly.

![[019f7549-b076-7738-8d96-f6b99f510ebc.png]]

> [!warning]
> **Složitost**: $O(E)$ zpráv, kde $E$ je počet hran grafu (každou hranou projde ELECTION a ACK)

## 4.2 Vlastnosti

- Kandidáti jsou **všichni uzly** — vyhraje _ten s nejlepšími vlastnostmi_
- Vhodné pro _dynamické sítě a mobilní sítě_, přizpůsobuje se aktuálním podmínkám v síti
- Je potřeba _pravidelně zjišťovat informace o uzlech_, což vytváří **komunikační režii**
- Při častých změnách topologie může být _nutné opakovat volbu lídra_