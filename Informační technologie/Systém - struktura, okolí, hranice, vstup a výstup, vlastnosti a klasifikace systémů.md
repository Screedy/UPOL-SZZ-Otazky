- Systém je skupina objektů, které se navzájem ovlivňují za účelem splnit nějaký cíl.

>[!Example] Nákres systému
>![[Systém-nákres.png]]
## Prvky
- **Prvky systému** - **elementární**, dále **nedělitelné** části systému
- **Subsystém** - podmnožina prvků systému, kterou můžeme hodnotit jako **samostatný systém**

## Okolí a Hranice
- **Hranice** odděluje 2 nebo více systémů. 
	- Může být **prostorová** (fyzická) nebo **logická** (hranice IS).
- **Okolí** systému je **zdrojem podnětů** pro systém samotný. 

## Vstup a výstup
- Systém interaguje s okolím pomocí **vstupů** a **výstupů**.
	- **Vstup systému** - množina vazeb či proměnných, pomocí kterých **okolí působí na systém**.
	- **Výstup systému** - množina vazeb či proměnných, pomocí kterých **systém působí na okolí**.

## Vlastnosti systému
- **Chování**:
	- Projev dynamiky systému. 
	- **Dynamika** je **schopnost** vyvolat **změnu** v systému. 
	- Např. změna stavu systému
- **Stav systému**:
	- Souhrn hodnot jeho atributů, vlastností, které lze pozorovat v daný časový okamžik za přesně definovaných podmínek 
	- Např. Žárovka - stav rozsvícená/zhasnutá, při přívodu el. energie
- **Událost**:
	- **Změna hodnoty** některého atributu (nebo prvku) systému, případně jejich **vyloučení/přidání** do systému. 
	- Nebo také **změna propojení prvků** systému.
- **Stabilita**:
	- Schopnost systému **udržet si nezměněné chování i přes působení okolí**, změně vstupů a přes působení procesů probíhajících uvnitř systémů. 
## Klasifikace Systému

### Otevřenost

- **Otevřený**:
	- Dochází k **výměně informací s okolím**, zpracovává **nečekané vstupní hodnoty**. 
	- Snaží se **reagovat** tak, aby byla **zachována jejich existence**.
- **Uzavřený**:
	- Systém je zcela **izolovaný**. 
	- Nemá **žádné** vazby s okolím.

### Kauzualita
- **Deterministický**:
	- **Řídí** se jasně danou **množinou pravidel**, jejich chování je **jednoznačně určeno aktuálním stavem** a **vstupy systému**.
- **Nedeterministický**:
	- **Řízeny náhodou**. 
	- Chování více dáno **pravděpodobností než jistotu**.
### Stav
- **Dynamické**:
	- Pamatuje si **vnitřní stav**. 
	- Výstup záleží i na vnitřním stavu systému.
- **Statické**:
	- Výstup závisí **pouze** na vstupu. 

### Časová klasifikace

- **Diskrétní**: Časová množina je **spočetný soubor časových okamžiků**.
- **Spojité**: Časová množina je **interva**l.

##### Navigace
Předchozí:  [[Klientský JavaScript]]
Následující: [[Základní pojmy informačních systémů - data, informace, informační systém]]
Celý okruh: [[2. Informační technologie]]