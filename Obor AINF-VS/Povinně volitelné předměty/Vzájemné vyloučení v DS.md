## Logické hodiny
- Lamportovy logické hodiny mohou být využity pro *implementaci algoritmu vzájemného vyloučení v DS*
- Každý proces **má logické hodiny**. Všechny procesy si posílají 3 druhy zpráv.
	- **request**
	- **release**
	- **ack**

- **Request**:
	- Proces $p_{i}$ každému procesu *posílá zprávu* $(p_{i}, t)$ s hodnotou logických hodin $t$ (žádá o vstup) a **zprávu si uloží do fronty**.
	- *Při přijetí* request je $(p_{i}, t)$ *uloženo do fronty* a posláno **potvrzení ack**.
- **Release**:
	- *Proces každému procesu zasílá zpravů* (oznámení o výstupu), **při přijetí je** $(p_{i}, t)$ **smazáno z fronty**.
- **Ack**:
	- Potvrzení *request*.

>[!text] Zvyšování hodin:
>- Každé volání request $\rightarrow$ hodiny $+ 1$.
>- Každé volání release  $\rightarrow$ hodiny $+ 1$.
>- Každé volání ack  $\rightarrow$ hodiny $+ 1$.

>[!text] Podmínka o vstup:
>- Proces vstoupí do kritické sekce pokud **má ve frontě request s hodnotou $t$**.
>- $t$ je menší než všechny ostatní request ve frontě.
>- Obdržel potvrzení od každého uzlu s hodnotou větší než $t$
>Všechny body musí platit.

>[!warning]
>Komunikace musí probíhat FIFO

## Ricart-Agrawala algoritmus
- Byl navržen aby *umožnil procesům koordinovat svůj přístup ke sdíleným zdrojům*.
- Stačí nám **méně zpráv** (než u využití logických hodin) a **není potřeba FIFO komunikace**

- Každý proces **má logické hodiny**.
- Procesy si posílají $2$ typy zpráv:
	- **request**
	- **ack**

>[!Example] Postup:
>1. Proces $p_{i}$, který chce vstoupit **zašle request** $(p_{i}, t)$ **ostatním $p_{j}$**.
>2. Proces $p_{j}$ při přijetí $(p_{i}, t)$ pošle ack pokud **nechce vstoupit nebo $t$ je menší než logické hodiny procesu $p_{j}$**, jinak si **přidá $p_{i}$ do fronty**.
>3. Při přijetí $(N-1)$ ack zpráv, proces **vstoupí do kritické sekce**.
>4. Při výstupu proces $p_{i}$ **pošle ack všem ve frontě** čekajícím procesům

>[!fail] Problém:
>- **$N$ bodů selhání**
>	- Lze vyřešit opakovaným posíláním zprávy, kdy odesílatel po neobdržení odpovědí usoudí, že proces selhal.
>- **Vyžaduje multicast komunikaci**
>	- Nevhodné pro rozsáhlé systémy, protože je potřeba evidence.

## Token-ring algoritmus
- Algoritmus využívající princip tokenu - *speciální zpráva, která obíhá mezi uzly*.
- Tento token určuje, který proces má aktuálně právo vstoupit do kritické sekce.

- Inicializace:
	- Každý uzel v systému má určený *identifikátor* a zná seznam všech uzlů v DS.
	- Tyto uzly jsou **uspořádány do logického kruhu** (obecně nezávislé na fyzické topologii).

- Token:
	- Token je **speciální zpráva**, která obíhá mezi uzly v kruhové síti.
	- Kdo má token, **může vstoupit do kritické sekce**.

- Vstup do kritické sekce:
	- Když token dorazí k uzlu, který si přeje vstoupit do kritické sekce, může vstoupit do této části kódu.
	- Během této doby **ostatní uzly nemohou vstoupit** do kritické sekce, protože token se nachází v rokou uzlu, který je právě v této sekci.

- Opuštění kritické sekce:
	- Když proces dokončí svou činnost v kritické sekci, předá token dalšímu uzlu v prstenci.

- Kruhový pohyb tokenu:
	- Token pokračuje v obíhání v kruhu.
	- Uzly, které si nepřejí vstoupit do kritické sekce, pouze **předávají token dál**.

>[!fail] Problémy:
>- Ztráta tokenu
>- Udržování topologie

- Je důležité poznamenat, že toto řešení funguje dobře pro malé a střední sítě. Může mít problémy s výkonem a efektivitou ve velkých systémech.

## Decentralizované řešení
- Každý zdroj je replikován $N$ krát. Přitom **každá replikace má svého koordinátora**.
- Pokud chce proces vstoupit do kritické sekce, **pošle zprávu každému koordinátorovi** (tedy $N$ zpráv).
- **Koordinátor** může poslat **pouze jedno potvrzení**, pokud *dostane více žádostí, ignoruje je*.
- Pokud **proces dostane nadpoloviční počet potvrzení**, může vstoupit do kritické sekce.
- Po vystoupení z kritické sekce, *informuje všechny, že odešel a může se znovu hlasovat*.

## Odbočka: Total-order multicast
- Mechanismus pro distribuovaný multicast, který zajišťuje **doručení zpráv všem uzlům ve správném pořadí**.
- Může být použit k implementaci vzájemného vyloučení v DS.

- V total-order multicast systému jsou **zprávy odesílány všem uzlům** a **každý uzel obdrží zprávy ve stejném pořadí**.
	- Tímto způsobem se zajišťuje, že **každý uzel vidí stejnou posloupnost zpráv**.

- Označování zpráv:
	- Každá zpráva odeslaná do systému je označena *identifikátorem* $t$, který ukazuje **na její pořadí v rámci posloupnosti zpráv**.
	- To umožňuje jednotlivým *uzlům identifikovat a udržovat sled pořadí zpráv*.

- Vzájemné vyloučení:
	- Při implementaci vzájemného vyloučení pomocí total-oder multicast **označí každý uzel v systému zprávu před vstupem do kritické sekce** a **pošle tuto označenou zprávu ostatním uzlům pomocí total-order multicast**.
	- Každý uzel obdrží označenou zprávu ve stejném pořadí, což umožní všem uzlům vědět, kdy byl daný uzel ve své kritické sekci.

- Čekání na potvrzení:
	- Procesy po odeslání označené zprávy *čekají na potvrzení ostatních uzlů*, že **zpráva byla doručena**
	- Tím se zajistí, že *ostatní uzly mají informace o vstupu do kritické sekce*.

- Vstup do kritické sekce:
	- Jakmile proces **obdrží potvrzení od všech ostatních** uzlů, *může vstoupit do kritické sekce*.
	- V tomto okamžiku ostatní uzly také vědí, že tento uzel je v kritické sekci.

- Oznámení výstupu z kritické sekce:
	- Když proces opouští kritickou sekci, může opět odeslat označenou zprávu, tentokrát s informací o výstupu z kritické sekce.

- Doručení označené zprávy o výstupu:
	- Total-order multicast zajistí správné doručení označené zprávy o výstupu ze sekce do všech uzlů.

- Čekání na potvrzení výstupu:
	- Stejně jako při vstupu do kritické sekce *může proces čekat na potvrzení od ostatních uzlů*, že označená zpráva o výstupu byla doručena.

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FKoordinace%20%C4%8Dasu%20v%20DS" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FVolba%20l%C3%ADdra%20v%20DS" style="text-decoration: none;">
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