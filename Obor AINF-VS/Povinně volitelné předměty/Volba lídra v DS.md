- **Lídr** = *koordinátor, iniciátor* (jiná role než ostatní uzly).

- Uzly se **musí "domluvit"** kdo bude *lídr*.
- *Úzce souvisí se vzájemným vyloučením*:
	- Vzájemným vyloučením je možné zvolit lídra.
	- Lídr zajišťuje vzájemné vyloučení.

- Předpoklady:
	- Existuje *identifikátor* uzlu.
	- Uzly o sobě *navzájem vědí*.
	- Uzly mohou vypadnout.

## Bully algoritmus
- Cílem je *zvolit nejsilnější* (nejvyšší) *proces na základě jejich identifikátoru*.

- Detekce potřeby nového lídra:
	- Každý proces v DS *pravidelně kontroluje*, zda je *stávající lídr stále dostupný*.
	- Pokud proces zjistí, že **lídr nereaguje** (nekomunikuje), považuje to za detekci **potřeby nové volby lídra**.

>[!Example] Průběh:
>- Zahájení volby lídra:
>	- Proces, který zjistí nedostupnost lídra, začne volbu nového lídra tím, že **pošle žádost o volbu** `(ELECTION message)` všem procesům s **vyšším identifikátorem** než má sám.
>- Reakce ostatních procesů:
>	- Procesy, které *obdrží žádost o volbu*, mohou buď potvrdit, že **nejsou zájemci o stání se lídrem**, nebo **mohou začít sami volbu, pokud mají vyšší identifikátor**.
>- Vítězný proces:
>	- Proces s nejvyšším identifikátorem *mezi těmi, kteří obdrželi žádost o volbu*, se stane **novým lídrem**.
>	- Tento proces **zašle zprávu informující o svém vítězství** `(COORDINATOR, message)` **všem** ostatním procesům.
>- Aktualizace informací:
>	- Ostatní procesy **aktualizují své informace o aktuálním lídrovi** na základě nových zpráv.
>	- Pokud *některý z nich zjistí*, že má vyšší identifikátor než nový lídr, **může zahájit svou vlastní volbu**.
>
>![[MacBook-2025-01-10-002412.png]]


- Bully algoritmus funguje dobře v situacích, kdy **potřebujeme rychle zvolit nového lídra** v reakci na **výpadek stávajícího**.
- Časová složitost je $\mathcal{O}(n^{2})$, kde $n$ je počet procesů v systému.
	- Může být neefektivní ve velkých DS.

- Existuje i varianta, kdy se vybírá lídr s **nejnižším identifikátorem**. Poté se zprávy posílají všem co mají nižší identifikátor atd.

## Ring algoritmus
- Ring algoritmus pro volbu lídra v DS je založen na *kruhové topologii*.

>[!Example] Průběh:
>- Zahájení volby:
>	- Proces, který rozhodne, že je třeba **zahájit volbu lídra** (například po detekci výpadku stávajícího lídra), **pošle "lístek" se svým identifikátorem sousedovi**.
>- Předávání zpráv:
>	- Každý proces, *který obdrží "lístek"* a **porovná zda je jeho identifikátor větší než ten na lístku**.
>	- Pokud **ano, přepíše a pošle dál**, pokud ne *pošle pouze dál*.
>- Detekce vítěze:
>	- "Lístek" cirkuluje v kruhu, dokud *nenarazí na proces, který započal volby*.
>	- Tento proces pak **zprávu vyhodnotí a informuje všechny uzly o výsledku** (pošle další "lístek").
>- Potvrzení lídra:
>	- Každý proces přijímá příchod zprávy o novém lídrovi a **aktualizuje svůj stav** o **identifikátor nového lídra**.
>
>![[MacBook-2025-01-10-002413.png]]


- Opět existuje varianta, kdy se volí lídr s **nejnižším identifikátorem**.

## Raft algoritmus
- Moderní (2014) a *především jednoduchý algoritmus*, implementovaný v mnoha jazycích.
- Je založen na většinové shodě.
- Běžně se používá pro **replikaci dat**, avšak lze použít i pro samotnou volbu lídra.

- Stavy uzlů:
	- Leader, Následovník, Kandidát
- Term = Volební období.
- Split-vote = nikdo nezískal (restart, náhodné zpoždění)

>[!Example] Průběh:
>- Inicializace:
>	- Každý uzel v DS **začíná ve stavu "Follower"** (následovník).
>- Vyvolání voleb - následovník:
>	- zvýší svůj term,
>	- stane se kandidátem,
>	- hlasuje sám pro sebe,
>	- požádá o hlas všechny ostatní (zašle zprávu).
>- Uzel obdrží zprávu o hlas:
>	- Když *kandidát* (follower je podobný) *obdrží zprávu `RequestVote`*, zkontroluje, zda **je volební období žádajícího kandidáta větší než jeho vlastní**.
>	- Pokud je **období větší**, aktualizuje svoje období, přejde do stavu **následníka** a hlasuje pro kandidáta.
>	- Pokud je **term stejný nebo menší**, žádost o hlasování zamítne.
>- Výsledek:
>	- Vyhraje volby:
>		- kandidát dostane většinu hlasů,
>		- prohlásí se leaderem.
>	- Jiný kandidát se prohlásí leaderem (zpráva) a:
>		- má term větší nebo roven mému $\rightarrow$ návrat k následovnictví.
>		- má term menší než můj $\rightarrow$ odmítnu ho.
>	- Dlouho nevyhrává nikdo - **timeout** $\rightarrow$ restart voleb.

>[!text] Další pojmy:
>- Časový limit voleb:
>	- Každý uzel čeká na **náhodný** časový limit voleb. 
>	- Pokud uzel během tohoto časového limitu *neobdrží zprávu od lídra* nebo *jakéhokoli kandidáta*, přejde do **stavu "kandidát"** a **zahájí nové volební období**.
>- Heartbeats:
>	- Jakmile se uzel stane vůdcem, zasílá **periodicky zprávy** všem následovníkům, aby si **udržel své vedení** a zabránil zahájení nových voleb.
>- Ztráta lídra:
>	- Pokud *následovník neobdrží Heartbeat během určitého časového limitu*, **přejde do stavu kandidáta** a **zahájí nové volební období**.
>- Omezení volebního období:
>	- Každé nové **volební období** v Raft algoritmu **je vyhrazeno pro jednu volbu lídra.** To znamená, že každá volba lídra má svoje vlastní volební období.

![[MacBook-2025-01-10-002414.png]]

>[!fail] Problémy volby lídra:
>- V některých případech nechceme vybírat lídra pouze podle identifikátoru. Je nutné zohlednit i například:
>	- Polohu
>	- Výkon uzlu
>	- Latenci
>	- ...
>- Například v Ad-hoc sítích **chceme najít lídra s určitými parametry** (toho nejlepšího).

## Ad-hoc sítě
- **Ad-hoc síť** = bezdrátová a decentralizovaná síť na bázi P2P.

>[!Example] Postup:
>- Libovolný uzel (source) zahájí volby (pošle zprávu `ELECTION`)
>- Pokud uzel *obdrží `ELECTION` poprvé*, **udělá z odesílatele svého rodiče** a **pošle `ELECTION` všem sousedům** (kromě rodiče). Přijetí `ELECTION` potvrdí až, **dojde k potvrzení od sousedů**.
>- Pokud uzel *obdrží `ELECTION` od jiného uzle než od svého rodiče* **pouze ji potvrdí**.
>- **List potvrdí přijetí `ELECTION`** a **zašle informace o svých možnostech** (stav baterie, rychlost, ...) **rodiči**.
>- **Informace** (vždy nejlepší volba) se **propagují** sítí zpět k **source** uzlu.
>
>![[MacBook-2025-01-04-002365.png]]
>![[MacBook-2025-01-10-002415.png]]

## Odbočka: Broadcast
- **Broadcast představuje poměrně velkou zátěž** (velký počet zaslaných zpráv).
- Vhodné je použít například **Gossip protokol** (někdy také epidemic protokol)
	- Propagace:
		- Každý uzel *posílá zprávu náhodným uzlům*.
		- Po určitém počtu konverguje.
	- Agregace:
		- Každý uzel $P_{i}$ *si nastaví proměnnou $v_{i}$ na $0$ pouze $P_{1}$ nastaví $v_{1}$ na $1$*.
		- Když $P_{i}$ **konverguje** $P_{j}$ nastaví své **$v$ na $(v_{i} + v_{j}) / 2$**.
		- Z průměru hodnoty je možné odhadnout počet uzlů v síti.

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FVz%C3%A1jemn%C3%A9%20vylou%C4%8Den%C3%AD%20v%20DS" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FShoda%20v%20DS" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Následující otázka
            </button>
        </a>
    </div>
    <!-- Spodní tlačítko -->
    <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2F2.%20Povinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty" style="text-decoration: none;">
        <button style="padding: 15px 30px; background-color: #ADD8E6; color: black; border: none; border-radius: 5px; cursor: pointer; width: 43%;">
            Všechny otázky
        </button>
    </a>
</div>