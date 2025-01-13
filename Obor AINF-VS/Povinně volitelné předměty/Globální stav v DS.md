- **Lokální stav procesu** = hodnoty proměnných, alokované zdroje, stav vykonávání programu.
- **Globální stav DS** = lokální stav všech procesů DS a stavy všech kanálů mezi nimi.
- **Řez** = rozdělení události v systému na dvě skupiny.
	- Ty co se již staly a ty co se ještě nestaly.

- Snapshot = Globální stav DS v daném okamžiku.
	- Stav (konzistentního) řezu.

## Konzistentní řez a konzistentní snapshot
- **Konzistentní řez $C$**: **Pokud událost $b \in C \land a \rightarrow b$**, pak $a \in C$.
- **Postup výpočtu** v DS je **posloupnost konzistentních řezů**.
- **Konzistentní snapshot** je **zachycení stavu konzistentního řezu**.
![[MacBook-2025-01-13-002433.png|500]]
- c1 je nekonzistentní, c2 je konzistentní řez.

## Chandy-Lamport algoritmus
- Algoritmus využívající techniku *distribuovaný snímek*.
- Slouží k výpočtu snapshotu.

>[!Example] Postup algoritmu:
>1. Iniciátor uloží svůj stav, pošle zprávu s markerem (snapshot request).
>2. Proces obdrží zprávu s markerem:
>	1. Poprvé: 
>		- Uloží svůj stav. 
>		- Uloží příchozí kanál (ze kterého market přišel) jako prázdný (zprávy přijaté po marketu nejsou součástí snímku).
>		- Pošle market zprávy všem ostatním procesům přes své výstupní kanály.
>	1. Jindy: Uloží stav na kanálu.
>3. Proces s markerem dostane zprávu bez markeru
>	- Musí být z okamžiku před snapshotem,
>	- přepošle ji iniciátorovi, aby ji přidal

- FIFO kanály (jinak problém)

## Dijkstra-Scholten algoritmus
- Algoritmus pro detekci ukončení výpočtu.
- Jeho cílem je určit, *kdy všechny uzly v DS dokončili svůj běh* a *jsou v bezpečném stavu pro ukončení celého systému*.
- V síti buduje kostru (podobné volbě leadera v ad-hoc síti).
- Posílají se dva typy zpráv - `SIGNAL` a `ACK`.

>[!Example] Princip:
>- Každý uzel je **aktivní** (pracuje) **nebo pasivní**.
>- Každý uzel **eviduje svůj deficit**, což je **rozdíl mezi poslanými a přijatými `SIGNAL` a `ACK`** (na vstupu i na výstupu). Na začátku jsou *oba $0$*.
>- **Iniciátor** pošle `SIGNAL`.
>- Uzel pošle `ACK` pokud **deficit na vstupu je větší než $1$**, nebo **deficit na vstupu je $1$** a na **výstupu je $0$ a uzel je pasivní**.
>![[MacBook-2025-01-13-002434.png|350]]


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