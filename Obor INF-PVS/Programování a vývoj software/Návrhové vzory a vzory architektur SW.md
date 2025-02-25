## Návrhové vzory architektur
- většinu problémů již někdo před námi řešil
- opravodvé problémy až při běhu aplikace
- ustálilo se několik osvědčených návrhových vzorů
- usnadní a urychlí návrh (ověřené, všichni to znají)
- aplikace možná na celý systém či jen částečně
#### Vrstvená architektura
- horizontální na sobě ležící vrstvy
- na vrstvách pod je závislá
- na vrstvách nad je nezásvislá
1) uzavřené vrstvy - implementace pouze pomocí nejbližší vrstvy, jako TCP/IP, kratší závislost
2) otevřené vrstvy - implementace pomocí kterékoliv nižší, horší údržba, nižšší režie => vyšší výkon
- specifikace problému obvykle definuje jen nejvyšší vrstvu
- nejnižší je logicky nejblíže HW/OS/knihovnám
- **výhody**
	- striktní rozdělení odpovědnosti
	- snadná testovatelnost
	- znovupoužitelnost
	- bezpečnost (přidání mezivrstev)
- **nevýhody**
	- nutné hlídat a dodržovat nezávislost
	- složitost komunikace
	- nižší výkon
#### Client-server
- vysokoúrovňová 2 vsrtvá architektura
- jsou úzce spjaté, komunikace je oboustranná
- klient - UI a UX, server - celá logika
- server musí vždy validovat získaná data od klienta
#### Event driven system
- události ... info o změně stavu
- může zajímat jiné části systému
- distribuovaný a asynchronní
- řídí dispečer a spouští callback
- publish-subsribe (vysílá se broadcast)
- např. GUI, sledování změn v DB, ...
- hodně možností jak události zpracovat
#### MVC - model view controller
- rozšířené pro GUI a webové appky
- striktní rozdělení odpovědností do 3 částí
- ![[Pasted image 20250223161747.png]]
#### MVP - model view presenter
- rozšíření MVC, zakazuje komunikace model-view
- ![[Pasted image 20250223161830.png]]
- každý view má vlastní presenter
#### MVVM - model view viewmodel
- viewmodel stojí mezi view a model
- view dostává notifikace od viewmodelu a na ty reaguje
- ![[Pasted image 20250223161853.png]]
#### SOA - service oriented architecture
- rozdělení na mírně nezávislé spolupracující služby
- služba zapouzdží funcionalitu a poskytne rozhraní
- bývají fyzicky odděleny
- např. webové služby, síťové služby
- bezstavovost
- klasicky výhody i nevýhody
#### Monolitická architektura
- SW je ucelený a pevně svázaný
- nízká režie => vyšší výkon
- vhodné pro malé projekty
- nedá se moc škálovat
- težká udržitelnost (technologie atd.)
#### Architektura mikroslužeb
- microservices
- velmi malé autonomní služby
- nezávislé (verze, technologie, umístění)
- fungují jako black boxy
- pro velké projekty (dobrá škálovatelnost)
- často komunikují pomocí HTTP
- trend dnešní doby
## Vytvářecí vzory
- většinově OOP
- vychází z reálného pohledu na svět
- **dessign patter** (návrhový vzor) ... způsob řešení opakujícího se problému v OOP
	- nejde o konkrétní kód, ale popis struktury
	- jejich znalost urychlí návrh OOP programů
- různá "velikost vzorů" (celé problémy i malé komponenty)
- definován pomocí
	1) **název** - zapamatovatelné ,krátké, usnadní přemýšlení, ustáleno praxí, vice ekvivalentních
	2) **popis problému** - vysvětlí problém a kontext
	3) **popis řešení** - vzor řešení (detailní a ucelené)
	4) **možné důsledky** - kompromisy při použití
- jsou mezi třídami a vzroy architektur
- dělení podle abstrakce - třídní a objektové
- podle účelu - vytvářecí, strukturální a vzory chování
- konkurentní vzory (paralelizační problémy)

- řeší vytváření nových instancí
- skrývají konkrétnost třídy, jak jsou třídy vytvářeny
- v compiletime nemusíme vědět jaké třídy konkrétně dostaneme
#### Abstract factory
- využívá se hodně
- vytvaří instance vzájemně souvisejících tříd, ale nemusíme specifikovat konkrétní třídy těchto objektů
#### Builder
- tolik se nepoužívá
- odděluje konstrukci objektů od jejich prezentace
#### Factory method
- vysoké použití
- interface pro tvorbu objektů, jehož potomci rozhodnou co se vytvoří
- při tom když třída neví jaké třídy objektů má vytvářet
- má několik součástí
	- product
	- concrete product
	- creator
	- concrete factory
- příklad intel procesory
	![[Pasted image 20231219084619.png]]
	
#### Prototype
- střední
- specifická instance třídy
- nový objekt se vytvoří klonováním prototypu
#### Singleton
- dost se používá
- třída pouze s jedinou instancí (globálně dostupná)
- chceme, aby danou funkcionalitu měla pod kontrolou jen 1 instance
	- např. logger, přístup do DB, plánovač v OS
- konkrétní implementaci je nejlepší nechat přímo na třídě (globální proměnná není moc dobrá)
- `private konstruktor`
## Strukturální vzory
- jak jsou třídy a objekty složeny do sebe
- využívají dědičnost
#### Adapter (Wrapper)
- vyšší použití
- konvertuje rozhraní navzájem nekompatabilních tříd
- příklad celkem triviální
- součásti
	- target - definice rozhraní v dané doméně
	- client - volá nekompatabilní rozhraní
	- adaptee - nekompatabilní rozhraní
	- adapter - překladač
- důsledky - kolik práce dělá? volá jen metody nebo i další práce?
#### Bridge
- střední
- odděluje rozhraní a implemetaci objektu
#### Composite
- vyšší
- uspořádá objekty do stromové struktury a s tou se pak dá pracovat jako s jediným objektem
#### Decorator
- střední
- dynamicky rozšiřuje funkcionalitu objektu
- znám z Pythonu
#### Facade
- vysoká
- třídá vytvářející rozhraní pro celý subsystém (rozhraní vyšší úrovně)
- taková rozhraní pro rozhraní
- proč? potřebujeme komunikovat se všemi třídami v subsystému
- důsledky - odstínění komponent subsystému (=> menší závislost)
#### Flyweight
- nízká
- efektivní správa více objektů s podobnou strukturou, sdílení dat
#### Proxy
- vyšší
- objekt zajišťující přístup k jinému objektu (deleguje to)
## Vzory chování
- rozdělují zoodpovědnost
- řeší komunikaci mezi objekty
- tzv. control flow (téžké sledovat za běhu)
- třídní a objektové vzory
#### Chain of responsibility
- nízké
- předání požadavku do řetězce objektů
#### Interpreter
- nízká
- interpretace vět jednoduhcého jazyka
#### Mediator
- nižší
- komunikace mezi 2 třídami (komunikují přes prostředníka)
#### Observer (pozorovatel)
- objektový
- 1:N - při změně stavu 1 objektu informauje ostatní
- proč? systém se musí udržovat v konzistentním stavu
	- tabulka s daty -> změna dat -> nutné změnit zobrazení, o kterém data ale neví
1) **subject** - zná pozorovatele, rozhraní pro přihlášení a odhlášení odběru změn
2) **observer** - definuje rozhraní pro informování o změně
3) **concreteSubject** - uložení sledovaného stavu, inforamuje o změně
4) **concreteObserver** - zná pozorovaný objekt (a udržuje si jeho stav), reaguje na změny
		![[Pasted image 20231119205029.png]]
- funguje jako broadcast
- nevýhoda: pozorovatelé se neznají -> kaskáda změn
#### Iterator (cursor, enumerator)
- objektový
- poskytuje sekvenční procházení datové struktury
- vše pak můžeme procházet stejným způsobem a nemsuíme řešit zda jde o strom, list nebo tečkové páry
1) **concreteIterator** - implementace rozhraní, udržuje aktuální pozici
2) **aggregate** - rozhraní pro vytvoření objektu Iterator
3) **concreteAggregate** - konkrétní datová struktura, umožňuje sekvenční průchod
#### Strategy
- zapouzdří algoritmy a umožní uživateli libovolně rozhodovat, který vybere (jsou vzájemně zaměnitelné)
#### Command
- zapouzdří operaci, aby šla později zavolat a zároveň si pamatoval režijní informace
- odděluje zadání požadavku a jeho vykonání
#### Visitor
- definování nové operace třídě bez její úpravy
#### Memento
- řeší uchování vnitřního stavu objektu, tak abychom se do něj mohli později napříkald vrátit
- neporušuje zpouzdření
- např. pro operaci undo