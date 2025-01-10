## Centralizované řešení
- Velmi jednoduchá myšlenka i provedení.
- Jeden uzel (**rozhodčí**) rozhoduje o výhradním přístupu ke sdílenému zdroji.

>[!Example] Postup:
>- Rozhodčí drží frontu žádostí.
>1. Zájemce $i$ pošle žádost.
>2. Rozhodčí potvrdí `OK`, je-li zdroj volný, jinak dá $i$ do fronty.
>3. Proces $i$ po dokončení práce pošle `RELEASE`.
>4. Rozhodčí pošle `OK` dalšímu ve frontě, nebo čeká na žádost.

- Rozhodčí může sehnat $\rightarrow$ to ostatní nepoznají.
- Rozhodčí může být přetížený (je to prostě bottleneck).

## Ricart-Agrawala algoritmus
- Byl navržen aby *umožnil procesům koordinovat svůj přístup ke sdíleným zdrojům*.
- Stačí nám **méně zpráv** (než u využití logických hodin) a **není potřeba FIFO komunikace**

- Každý proces **má logické hodiny**.
- Procesy si posílají $2$ typy zpráv:
	- **request**
	- **ack**

>[!Example] Postup:
>1. Proces $p_{i}$, který chce vstoupit **zašle `request`** $(p_{i}, t)$ **ostatním $p_{j}$**.
>2. Proces $p_{j}$ při přijetí $(p_{i}, t)$ pošle `ack` pokud **nechce vstoupit nebo $t$ je menší než logické hodiny procesu $p_{j}$**, jinak si **přidá $p_{i}$ do fronty**.
>3. Při přijetí $(N-1)$ `ack` zpráv, proces **vstoupí do kritické sekce**.
>4. Při výstupu proces $p_{i}$ **pošle `ack` všem ve frontě** čekajícím procesům.

![[MacBook-2025-01-10-002407@2x.png]]

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

---
*\*Toto je navíc z předchozího ročníku.*
## Logické hodiny
- Lamportovy logické hodiny mohou být využity pro *implementaci algoritmu vzájemného vyloučení v DS*.
- Každý proces **má logické hodiny**. 
- Všechny procesy si posílají 3 druhy zpráv.
	- **request**
	- **release**
	- **ack**

- **Request**:
	- Proces $p_{i}$ každému procesu *posílá zprávu* $(p_{i}, t)$ s hodnotou logických hodin $t$ (žádá o vstup) a **zprávu si uloží do fronty**.
	- *Při přijetí* request je $(p_{i}, t)$ *uloženo do fronty* a posláno **potvrzení ack**.
- **Release**:
	- *Proces každému procesu zasílá zprávu* (oznámení o výstupu), **při přijetí je** $(p_{i}, t)$ **smazáno z fronty**.
- **Ack**:
	- Potvrzení *request*.

>[!tip] Zvyšování hodin:
>- Každé volání request, release, ack $\rightarrow$ hodiny $+ 1$.

>[!text] Podmínka o vstup:
>- Proces vstoupí do kritické sekce pokud **má ve frontě `request` s hodnotou $t$**.
>- $t$ je menší než všechny ostatní `request` ve frontě.
>- Obdržel potvrzení od každého uzlu s hodnotou větší než $t$
>Všechny body musí platit.

>[!warning]
>Komunikace musí probíhat **FIFO**
