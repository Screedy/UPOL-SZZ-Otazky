- Systém je soubor vzájemně propojených prvků, které spolu interagují a vykazují určitou organizovanou strukturu
- Jedná se o entitu, která má vymezené hranice a může existovat ve svém okolí
- Systém přijímá vstupy, zpracovává je a generuje výstupy

>[!Example] Nákres systému
>![[Systém-nákres.png]]

## Struktura
- je definována množinou všech prvků a vazeb mezi prvky
- **Prvky systému:**
	- elementární, dále nedělitelné části systému
- **Subsystémy:**
	- podmnožina prvků systému
	- obvykle můžeme brát jako samostatný systém se specifickou charakteristikou

## Hranice
- uzavírá systém nebo odděluje více systémů
- dělíme na:
	1. prostorová hranice (fyzická)
	2. logická hranice (hranice při informačních systémech)

## Okolí
- entita nacházející se za hranicemi systému
- ovlivňují systém přes vstupy
- systém je ovlivňuje přes výstupy

## Vstup a výstup
- Systém interaguje s okolím pomocí **vstupů** a **výstupů**.
- **Vstup systému** - množina vazeb či proměnných, pomocí kterých **okolí působí na systém**.
- **Výstup systému** - množina vazeb či proměnných, pomocí kterých **systém působí na okolí**.

## Vlastnosti systému
- **Dynamika (chování)**:
	- Projev dynamiky systému (**schopnost** vyvolat **změnu** v systému).
	- Schopnost systému se měnit a přizpůsobovat se v čase.
	- Např. změna stavu systému
- **Stav systému**:
	- Souhrn hodnot jeho atributů, vlastností, které lze pozorovat v daný časový okamžik za přesně definovaných podmínek 
	- Např. Žárovka - stav rozsvícená/zhasnutá, při přívodu el. energie
- **Událost**:
	- **Změna hodnoty** některého atributu (nebo prvku) systému, případně jejich **vyloučení/přidání** do systému. 
	- Nebo také **změna propojení prvků** systému.
- **Stabilita**:
	- Schopnost systému **udržet si nezměněné chování i přes působení okolí**, změně vstupů a přes působení procesů probíhajících uvnitř systémů. 
- **Adaptabilita**:
	- Schopnost systému se přizpůsobit změnám v okolí nebo v samotném systému.
- **Komplexnost**:
	- Míra složitosti systému, často určena počtem a typem prvků a vazeb mezi nimi.
- **Redundance**:
	- Přítomnost nadbytečných prvků nebo kapacit, které zvyšují spolehlivost systému.
## Klasifikace Systému

### Otevřenost

1. **Otevřený systém**:
	- Dochází k **výměně informací s okolím**, zpracovává **nečekané vstupní hodnoty**. 
	- Snaží se **reagovat** tak, aby byla **zachována jejich existence**.
2. **Uzavřený systém**:
	- Systém je zcela **izolovaný**. 
	- Nemá **žádné** vazby s okolím.

### Kauzalita
- **Deterministické systémy**:
	- **Řídí** se jasně danou **množinou pravidel**, jejich chování je **jednoznačně určeno aktuálním stavem** a **vstupy systému**.
- **Nedeterministické systémy**:
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