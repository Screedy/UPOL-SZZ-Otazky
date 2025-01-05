- Snapshot = Stav všech uzlů v komunikačním kanálu.
- V DS se termín "globální stav" obvykle odkazuje na *souhrn stavu všech uzlů* v daném distribuovaném prostoru.
- Je to abstrakce, která *reprezentuje aktuální stav systému z pohledu všech jeho částí a umožňuje sledovat celkový stav a události, které se v systému odehrávají*.
- Např. Kolik je v DS se třemi uzly tokenů? Odpověď může být: $(0, 1, 3)$

## Konzistentní řez a konzistentní snapshot
- **Konzistentní řez $C$**: **Pokud událost $b \in C \land a \rightarrow b$**, pak $a \in C$.
- **Postup výpočtu** v DS je **posloupnost konzistentních řezů**.
- **Konzistentní snapshot** je **zachycení stavu konzistentního řezu**.

![[MacBook-2025-01-05-002374@2x.png]]
- Cut $1$ je good.
- Cut $2$ není konzistentní, protože do něj nenáleží událost $h$ ($g$ závisí na $h$).

## Chandy-Lamport algoritmus
- Algoritmus využívající techniku *distribuovaný snímek*.
- Cílem je **zachytit konzistentní snímek stavu všech uzlů a komunikačních kanálů v systému**.

>[!Example] Postup algoritmus:
>- **Počáteční značení**:
>	- Uzel, který spouští detekci **vysílá značku** (market) **do systému**.
>	- Tato značka je označena jako počáteční značka pro distribuovaný snímek.
>- **Lokální snímek na každém uzlu**:
>	- Počáteční *značka putuje přes uzly a komunikační kanály systému*.
>	- Každý uzel, který obdrží značku, provede **lokální snímek svého stavu a stavu příchozích kanálů**.
>	- To zahrnuje *zaznamenání všech aktuálních událostí a hodnot proměnných*.
>	- Po provedení lokálního snímku každý uzel předává značku dál v systému.
>- **Získání snímků od ostatních uzlů**:
>	- *Každý uzel přijímá snímky od svých sousedů*.
>	- Tyto snímky jsou kombinovány s lokálním snímkem uzlu.
>- **Analýza snímků**:
>	- Po obdržení všech snímků *uzly analyzují své lokální snímky spolu s informacemi ze značky a snímků od ostatních uzlů*.
>	- Cílem je identifikovat konzistentní globální stav systému.

## Detekce ukončení: Dijkstra-Scholten algoritmus
- Algoritmus pro detekci ukončení v DS.
- Jeho célem je určit, *kdy všechny uzly v DS dokončili svůj běh* a *jsou v bezpečném stavu pro ukončení celého systému*.

>[!Example] Postup:
>- Posílají se dva typy zpráv - `SIGNAL` a `ACK`.
>- Každý uzel je **aktivní** (pracuje) **nebo pasivní**.
>- Každý uzel **eviduje svůj deficit**, což je **rozdíl mezi poslanými a přijatými `SIGNAL` a `ACK`** (na vstupu i na výstupu). Na začátku jsou *oba $0$*.
>- **Iniciátor** pošle `SIGNAL`.
>- Uzel pošle `ACK` pokud **deficit na vstupu je větší než $1$**, nebo **deficit na vstupu je $1$** a na **výstupu je $0$ a uzel je pasivní**.

## Distribuovaný commit
- **Operace je provedena na všech uzlech nebo na žádném** (např. transakce v distribuovaných databázích).
- **One-phase commit**:
	- *Koordinátor* **zahájí operaci** a řekne ostatním, **co mají udělat**.
	- Problém: **Chybí zpětná vazba**, pokud uzel nedokáže operaci provést, není koordinátor informován.
- **Two-phase commit**:
	- *Koordinátor* **pošle všem `VOTE-REQUEST`**.
	- **Uzel pošle `VOTE-COMMIT`**, pokud *je připraven provést commit*. Jinak `VOTE-ABORT`.
	- *Pokud koordinátor obdrží* **od všech `VOTE-COMMIT`**, pošle všem zprávu `GLOBAL-COMMIT`, jinak `GLOBAL-ABORT`.
	- Pokud uzel obdrží `GLOBAL-COMMIT` provede commit.
	- Problémy: Mnoho bodů selhání, řešení jsou časovače.
	- ![[MacBook-2025-01-05-002375@2x.png]]
	- Uzel, který **neobdrží `VOTE-REQUEST`** po **čase pošle `VOTE-ABORT`**.
	- Koordinátor ve stavu *wait* **po čase pošle `GLOBAL-ABORT**.
	- Uzel v ready stavu (čeká na koordinátora) má dvě možnosti:
		- **Blokovat** dokud **koordinátor nepošle zprávu**.
		- Po čase **kontaktovat jiný uzel** a zeptat se zda neobdržel `GLOBAL-*`
		- Pokud v tomto bodu *selže koordinátor*, pak **nekonečné blokování**.
- **Three-phase commit**:
	- ![[MacBook-2025-01-05-002376@2x.png]]
	- Navíc `PREPARE-COMMIT` zpráva.
		- Koordinátor ve stavu **`PRE-COMMIT`**, po čase může poslat `GLOBAL-COMMIT`.
		- Uzel ve stavu `READY` nebo `PRE-COMMIT` analogické jako u 2-fázového commitu, ale pokud je více jak polovina uzlů ve stavu `READY`, tak `VOTE-ABORT`.

## Odbočka: Zotavení z chyby
- **Zpětné zotavení**:
	- Postupné zaznamenávání checkpointů (log).
	- Při chybě návrat zpět.
- **Dopředné zotavení**:
	- Z chybového stavu přesun do nového nechybového stavu.
	- Je třeba znát možné příčiny chyby.

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FTolerance%20chyby%20v%20DS" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FReplikace%20a%20konzistence%20v%20DS" style="text-decoration: none;">
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