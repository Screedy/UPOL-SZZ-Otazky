- Tolerance chyb v DS se zabývá **schopností systému udržet svou funkčnost** a **korektnost i přes přítomnost chyb** nebo **selhání některých jeho částí**.
- Cílem je zajistit, aby systém i přes chyby v jednotlivých uzlech nebo komponentách fungoval spolehlivě, udržoval konzistentní stav a poskytoval očekávané služby.

- Selhání uzlů nebo komunikačního kanálu vede k chybám.
- Obecně by měli DS tolerovat určité množství chyb.

>[!Example] Základní koncepty, které požadujeme od našeho systému:
>- **Dostupnost** - dostupnost systému v čase
>- **Spolehlivost** - doba běhu bez chyb
>- **Bezpečnost** - nedojde ke katastrofickému selhání při chybě
>- **Udržovatelnost** - jak snadno lze odstranit chyby

## Klasifikace chyb
### Z pohledu serveru

| chyba           | popis                                           |
| --------------- | ----------------------------------------------- |
| stop chyba      | server se vypne, až do chyby funguje správně    |
| chyba vynechání | selhání poslání či přijetí zprávy               |
| chyba časování  | odpověď není doručena v daném časovém intervalu |
| chyba odpovědi  | odpověď je nesprávná                            |
| libovolná chyba | (Byzantská) libovolná odpověď v libovolném čase |
### Selhání uzlu
- V **asynchronních systémech** je **obtížné přímo určit, že nastala chyba**.
	- Zejména pokud dojde k něčemu, *co by mohlo být vnímáno jako běžné zpoždění nebo ztráta zprávy*.
	- Komunikace probíhá bez nějakého pevného časového rámce a tudíž detekce chyby může být komplikovaná.
- V **synchronních systémech** existuje **časový rámec pro vykonání operací a doručení zpráv**.
	- *Selhání uzlu může být detekováno, pokud nedojde k očekávané akci v daném časovém rámci.*
	- Například, pokud uzlu trvá příliš dlouho zpracování nebo odeslání zprávy, může být považováno za selhání.
- **Částečně-synchronní systémy** jsou jako **synchronní systémy bez omezení času.**
	- Pro synchronizace se využívají **časovače**.
	- Částečně synchronní systémy jsou často *využívány v odvětvích, kde je potřeba nějaká synchronizace*, ale **úplně synchronní systémy by byly příliš restriktivní nebo nemožné**.

### Způsob jakým se chyba projevuje
- **Fail-stop**:
	- Okamžité ukončení a spolehlivá detekce chyby.
	- (Tento termín se vztahuje na chování, kdy uzel, který selže, přestane pracovat, přestane vracet výsledky nebo nereaguje na žádné další požadavky).
- **Fail-noisy**:
	- Okamžité ukončení a nespolehlivá detekce chyby.
	- (Fail-noisy odkazuje na chování, kdy uzel selže, ale může stále produkovat nekonzistentní nebo chybné výsledky. Uzel může například vracet nesprávné odpovědi, generovat chybná data nebo se chovat nespolehlivě).

## Redundance
- **Základní nástroj** pro konstrukci distribuovaných systémů s tolerancí chyb.
Druhy redundance:

| Druh                  | Popis                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Informační redundance | Je záměrně zavedena za *účelem zvýšení spolehlivosti, bezpečnosti nebo odolnosti vůči chybám* v **přenosu nebo zpracování inforací** (například paritní bity, kontrolní součty, duplikace dat, ...)                         |
| Časová redundance     | Je využíván v různých oblastech, kde **opakování časových vzorků nebo operací může přinést nějaký užitek**, zejména v kontextu spolehlivosti, bezpečnosti nebo odolnosti vůči chybám (například opětovné odvysílání zprávy) |
| Fyzická redundance    | Týká se **opakování nebo zdvojení fyzických prvků nebo komponent v systému** s cílem *zvýšit spolehlivost, dostupnost nebo odolnost vůbec chybám* (například záložní uzly, servery, napájení, propojení, RAID, ...)         |
- Systém je **$k$-tolerantní** pokud **přežije výpadek $k$ uzlů**.

>[!Example] Použitím redundance:
>- Zavádíme abstrakci (komunikujeme se skupinou na místo jednoho uzlu)
>- Skupiny jsou dynamické (mohou vznikat, zanikat, uzly odchází, přichází nebo mohou být součástí více skupin)
>- Organizace uvnitř skupiny, může být rozdílná podle potřeb.

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FShoda%20v%20DS" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FGlob%C3%A1ln%C3%AD%20stav%20v%20DS" style="text-decoration: none;">
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