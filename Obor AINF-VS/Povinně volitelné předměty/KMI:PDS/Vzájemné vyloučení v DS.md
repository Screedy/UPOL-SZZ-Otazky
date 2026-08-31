- V distribuovaných systémech je potřeba zajistit _vzájemné vyloučení při přístupu ke sdílenému zdroji_. To může být například:
  - Zápis do distribuované databáze
  - Úprava stejného souboru,
  - Přístup ke sdílenému zařízení
- Protože jednotlivé procesy **běží na různých uzlech** a **nesdílí společnou paměť**, _nelze použít klasické synchronizační mechanismy_. Místo nich se využívají **algoritmy** _založené na_ **výměně zpráv mezi uzly**.

> [!note]
> **Intuice:** Představ si 5 serverů, které chtějí upravit jeden sdílený konfigurační soubor na NFS. Bez koordinace mohou zapisovat najednou a soubor se poškodí. Jak to vyřešit bez centrálního zámku, který by byl single point of failure?

- **Předpoklady modelu** (platí pro všechny algoritmy, pokud není uvedeno jinak)
  - Asynchronní systém (žádné záruky o časování zpráv).
  - Zprávy se neduplikují ani nepoškozují — **spolehlivé kanály**.
  - Procesy selhávají pouze stylem **crash** (zastaví se), nikoliv byzantsky.
  - Každý proces _zná_ seznam všech _ostatních procesů_ (plně propojená síť).

---

# 1. Logické hodiny (Lamportův algoritmus)

- **Lamportův algoritmus** je jedním z prvních algoritmů pro řešení vzájemného vyloučení v distribuovaných systémech.
- Využívá **Lamportovy logické hodiny**, které zachovávají kauzalitu mezi událostmi a umožňují _jednoznačně seřadit požadavky na vstup ke sdílenému zdroji_.

## 1.1 Princip

- Každý proces si _udržuje_:
  - Lamportovy logické hodiny
  - Frontu požadavků seřazenou podle dvojice **(časové razítko, ID procesu)**
- Procesy mezi sebou komunikují pomocí tří typů zpráv:
  - **REQUEST** – žádost o vstup do kritické sekce,
  - **ACK** – potvrzení přijetí žádosti,
  - **RELEASE** – oznámení o opuštění kritické sekce.

### **1. Žádost o vstup (REQUEST)**

- Proces, který _chce vstoupit do kritické sekce_:
  - **Zvýší** své logické hodiny
  - Odešle zprávu **REQUEST (ID, časové razítko)** všem ostatním procesům
  - _Svůj požadavek_ zároveň **uloží** do vlastní fronty.

### **2. Přijmutí žádosti (ACK)**

- Nejprve **aktualizuje hodiny** podle pravidla $L=max(L,t_{zprávy})+1$
- **Uloží** požadavek do fronty
- **Zvýší** své logické hodiny
- **Odešle** ACK

### **3. Vstup do kritické sekce**

- Proces může vstoupit do kritické sekce _pouze když_:
  - **Jeho REQUEST** je _uložen ve frontě_
  - **Jeho požadavek** má **nejmenší** _časové razítko_ (případně při shodě rozhoduje ID procesu)
  - Obdržel potvrzení **ACK od všech ostatních procesů**

### **4. Opuštění kritické sekce (RELEASE)**

- **Zvýší** své logické hodiny
- **Odešle** RELEASE

### 5. Příjmutí uvolnění kritické sekce

- _Najde_ ve své frontě požadavek daného procesu
- **Odstraní ho z fronty**
- **Zkontroluje**, zda se _nyní na začátku fronty nenachází jeho vlastní požadavek_. Pokud ano a zároveň už má ACK od všech ostatních procesů, může vstoupit do kritické sekce.

> [!info]
> _Celkem je tedy potřeba_ **3(N − 1)** zpráv, kde **N** je počet procesů.

> [!danger]
> **KOMUNIKACE MUSÍ PROBÍHAT FIFO!**

## 1.2 Vlastnosti

- _Vysoký počet_ zpráv **3(N − 1)**
- Proces _musí čekat na potvrzení_ **od všech ostatních uzlů**
- Při _výpadku některého procesu_ může dojít k **blokování**
- **Vyžaduje FIFO komunikaci**, aby všechny procesy viděly požadavky ve stejném pořad

---

# 2. Ricart–Agrawalův algoritmus

- **Ricart–Agrawalův algoritmus** je distribuovaný algoritmus pro řešení vzájemného vyloučení, který _vychází z Lamportova algoritmu_. Stejně jako Lamport **využívá logické hodiny** k určení pořadí požadavků, ale zvyšuje efektivitu tím, že **nevyžaduje zprávy** **RELEASE**. Místo toho proces _odkládá odpovědi ostatním procesům_, dokud neopustí kritickou sekci.

## 2.1 Princip

- Každý proces si udržuje:
  - Lamportovy logické hodiny
  - Stav procesu:
    - **RELEASED** – proces o kritickou sekci neusiluje
    - **WANTED** – proces žádá o vstup do kritické sekce
    - **HELD** – proces je v kritické sekci
  - Seznam **odložených odpovědí**
  - **Časové razítko** _vlastního REQUEST_
- Procesy mezi sebou komunikují pomocí dvou typů zpráv:
  - **REQUEST** – žádost o vstup do kritické sekce
  - **REPLY** – souhlas se vstupem do kritické sekce

### 1. Žádost o vstup (REQUEST)

- Proces, který **chce vstoupit do kritické sekce**:
  - **Nastaví** svůj stav na **WANTED**
  - **Zvýší** své logické hodiny
  - **Odešle** zprávu **REQUEST (ID, časové razítko)** všem ostatním procesům
  - **Uloží** si své časové razítko
  - **Čeká** na **REPLY od všech ostatních procesů**

### 2. Přijetí žádosti

- Nejprve **aktualizuje hodiny** podle pravidla $L=max(L,t_{zprávy})+1$
- Poté nastane jedna ze tří situací:
  - **Proces nechce vstoupit do kritické sekce (RELEASED)**
    - _Okamžitě_ **odešle** REPLY
  - **Proces je v kritické sekci (HELD)**
    - **Neodešle** REPLY
    - **Uloží** požadavek mezi odložené odpovědi
  - **Proces také žádá o vstup (WANTED)**
    - **Porovná** časové razítko svého a příchozího REQUEST
    - Pokud má _příchozí REQUEST_ **vyšší prioritu**, **odešle REPLY**
    - Pokud má **vyšší prioritu** _vlastní REQUEST_, **odloží REPLY** až do opuštění kritické sekce

### 3. Vstup do kritické sekce

- Proces může vstoupit do kritické sekce **pouze když**:
  - Obdržel REPLY **od všech ostatních procesů**

### 4. Opuštění kritické sekce

- **Nastaví** svůj stav na **RELEASED**
- **Projde** seznam odložených odpovědí
- **Odešle REPLY** všem procesům, kterým byla odpověď odložena

> [!info]
> _Celkem je tedy potřeba_ **2(N − 1)** zpráv, kde **N** je počet procesů.
>
> **Není potřeba** FIFO komunikace.

## 2.2 Vlastnosti

- Menší počet zpráv než u Lamportova algoritmu
- Proces **stále musí čekat** na odpověď _od všech ostatních procesů_
- **Výpadek** jednoho procesu _může zablokovat celý algoritmus_

---

# 3. Token Ring

- **Token Ring** je distribuovaný algoritmus pro řešení vzájemného vyloučení založený na předávání **jediného speciálního oprávnění – tokenu**. Proces může vstoupit _do kritické sekce pouze tehdy, pokud vlastní token_. Díky tomu je automaticky zajištěno, že ve _stejný okamžik může být v kritické sekci pouze jeden proces_.

## 3.1 Princip

- Všechny procesy jsou logicky uspořádány do **kruhu (ringu)**.
- V systému existuje **právě jeden token**, který se neustále předává mezi sousedními procesy.
- Token představuje **oprávnění ke vstupu do kritické sekce**.

### 1. Přijetí tokenu

- Proces **převezme token** od svého předchůdce v kruhu.

### 2. Rozhodnutí o vstupu do kritické sekce

- Pokud proces **nepotřebuje** vstoupit do kritické sekce:
  - **Okamžitě předá token** následujícímu procesu.
- Pokud proces **potřebuje** vstoupit do kritické sekce:
  - **Ponechá si token**
  - **Vstoupí** do kritické sekce.

### 3. Opuštění kritické sekce

- Po dokončení práce:
  - **Opustí** kritickou sekci.
  - **Předá token** následujícímu procesu v kruhu.

## 3.2 Vlastnosti

- _Jednoduchý_ princip
- _Malá komunikační režie_ (předává se pouze token)
- **Ztráta tokenu** způsobí _zastavení algoritmu_, dokud není vytvořen nový token,
- **Při výpadku procesu** může dojít _k přerušení kruhu_,
- Proces může **čekat dlouho na token**, i když _ostatní procesy kritickou sekci nepotřebují_

---

# 4. Decentralizované řešení

- **Centralizované řešení** vzájemného vyloučení je založeno **na jednom koordinátorovi**, který _rozhoduje o vstupu procesů do kritické sekce_. Jeho nevýhodou je, že představuje _jediný bod selhání_ a může se stát _úzkým hrdlem systému_.
- **Decentralizované řešení** proto _rozděluje rozhodování_ mezi **více koordinátorů**. Každý koordinátor může _v jeden okamžik udělit souhlas pouze jednomu procesu_. Proces může _vstoupit do kritické sekce_ až po **získání většiny hlasů** od těchto koordinátorů.

## 4.1 Princip

- V systému existuje **více koordinátorů** (hlasujících uzlů).
- Každý koordinátor:
  - může udělit souhlas pouze **jednomu procesu**,
  - si pamatuje, komu svůj hlas udělil.
- Proces musí získat **většinu hlasů** **(kvórum)**, aby mohl vstoupit do kritické sekce.

### 1. Žádost o vstup

- Proces, který **chce vstoupit do kritické sekce**:
  - **Odešle** REQUEST všem koordinátorům.

### 2. Rozhodnutí koordinátora

- Pokud koordinátor **ještě nikomu hlas neudělil**:
  - **Odešle** GRANT (souhlas) žadateli.
  - **Zapamatuje si**, kterému procesu hlas udělil.
- Pokud koordinátor **už hlas udělil jinému procesu**:
  - Novou žádost **ignoruje**.

### 3. Vstup do kritické sekce

- Proces může vstoupit do kritické sekce **pouze když**:
  - **Získal většinu hlasů (kvórum)** od koordinátorů.

### 4. Opuštění kritické sekce

- Po dokončení práce proces:
  - **Odešle RELEASE** všem koordinátorům.

### 5. Uvolnění hlasu

- Po přijetí **RELEASE** koordinátor:
  - **Uvolní svůj hlas**

## 4.2 Vlastnosti

- **Odolnější** _vůči výpadku_ **jednoho** uzlu
- _Není potřeba komunikovat se všemi procesy_, komunikace probíhá **pouze s koordinátory**
- Při výpadku většího počtu koordinátorů nemusí být možné získat kvórum

---

# 5. Total-order multicast

- **Total-order multicast** je _komunikační mechanismus_, který zajišťuje, že _všechny procesy doručí multicastové zprávy_ **ve stejném pořadí**.
- Díky tomu mají všechny uzly **konzistentní pohled na posloupnost událostí**

## 5.1 Princip

- Proces odešle zprávu všem členům skupiny (multicast).
- Systém každé zprávě určí **globální pořadí** (například pomocí sekvenčních čísel nebo koordinátora).
- Všechny procesy doručují zprávy **výhradně podle tohoto pořadí**.
- Pokud některá zpráva dorazí dříve, ale není na řadě, proces ji dočasně **uloží do fronty**.
- Zpráva je předána aplikaci až tehdy, když jsou doručeny všechny předcházející zprávy.

## 5.2 Vlastnosti

- Všechny uzly mají _konzistentní pořadí zpráv_
- Eliminuje nekonzistentní stavy _způsobené různým pořadím doručení_
- **Vyšší komunikační režie**
- **Větší zpoždění**, protože některé zprávy musí čekat na správné pořadí
- **Složitější implementace**