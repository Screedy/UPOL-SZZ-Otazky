- Shoda se stává důležitá v DS, kde *různé části systému mohou udržovat kopie dat a informací*.
- Shoda je proces, kdy se všechny uzly v systému dohodnou na společném rozhodnutí nebo hodnotě.
- Je potřeba zajistit, aby **všechny kopie byly v souladu**.

- Shoda v systémech bez selhání, je velmi **jednoduchá** zjistit.

## Skupiny
- Zavedení redundance.
- Úlohu uzlu převezme skupina uzlů.

>[!text] Protokol primární-záloha
>- Hierarchická skupina.
>- Pracuje primární (zápisy).
>- Výpadek primárního $\rightarrow$ záloha převezme roli.
>![[MacBook-2025-01-10-002416.png|200]]

>[!text] Protokol replikovaného zápisu
>- *Plochá* skupina.
>- Všichni stejná role.
>- Nemají kritický bod.
>- **Nutná** koordinace.
>![[MacBook-2025-01-10-002417.png]]
## Shoda v systémech s možností selhání

### Flooding consensus
- *Algoritmus sloužící k dosažení shody v DS*.
- Jedná se o jednoduchý přístup, kde **každý uzel systému periodicky rozesílá svůj stav nebo informace o změnách všem ostatním uzlům** ve svém okolí.
- Tento proces se nazývá "**flooding**" (případně "epidemic dissemination").
- Fail-stop (ví kdo vypadl a umí s tím pracovat)

>[!Example] Postup:
>- V každém kole si **aktivní uzly vymění své návrhy**.
>- Každý uzel z návrhu **deterministicky zvolí volbu**.
>- Pokud někdo nedostane některou odpověď, začne nové kolo.
>- Všichni dostanou všechny odpovědi $\rightarrow$ volba $\rightarrow$ konec.
>
>![[MacBook-2025-01-10-002418.png]]

### Paxos
- Algoritmus pro *dosažení shody v DS*, i když se **jednotlivé uzly mohou chovat nespolehlivě** (např. mohou selhat nebo se zpozdit).

>[!text] Předpoklady:
>- Máme **částečně synchronní** či **zcela asynchronní** DS, který **nemá libovolné** (byzantské) **chyby**.
>- Spoje mohou být *nespolehlivé*.
>- Operace jsou *deterministické*.
>- Chybné zprávy **lze detekovat** (Fail-stop).

- Shoda je **rozhodnutí většiny**.
- Tolerance $m$ chyb v $2m+1$ uzlech.

- *Principy fungování algoritmu Paxos jsou komplexní, ale základní kroky mohou být popsány následovně:*

>[!Example] Zjednodušený Paxos algoritmus:
>- Fáze přípravy (Prepare Phase):
>	- Proposer vyšle požadavek na acceptory s návrhem čísla (proposal number).
>	- Číslo přípravy se skládá z **dvou čísel**:
>		- Číslo instance
>		- Unikátní identifikátor uzlu
>	- Uzly odpovídají s **informace o nejvyšším čísle přípravy**, které dosud viděly a s hodnotou, pokud již nějakou mají.
>- Fáze přijetí (Accept Phase):
>	- Pokud uzel **obdrží dostatek odpovědí ve fázi přípravy**, pokračuje fází přijetí.
>	- Uzel požádá ostatní uzly o *přijetí navrhované hodnoty a informace o čísle přípravy*.
>	- Uzly odpovídají buď **potvrzením**, že hodnota byla přijata, nebo **odmítnutím s informacemi** o nejvyšším čísle přípravy, které dosud viděly.
>- Fáze rozhodnutí (Decision Phase):
>	- Pokud uzel **obdrží dostatek potvrzení ve fázi přijetí**, může **rozhodnout o hodnotě**, kterou předložil.
>	- Pokud uzel obdrží odmítnutí nebo nedostatek potvrzení, musí **zahájit nový pokus o dosažení shody** s novým číslem přípravy.
>
>![[Pasted image 20250113172915.png]]

>[!fail] Možné chyby:
>>![[MacBook-2025-01-04-002369.png]]
>>- Pokud **selže uzel přijímající návrh**, nic se neděje, **dokud funguje většina**.
>
>>![[MacBook-2025-01-04-002370.png]]
>>- Pokud selže **navrhující uzel před návrhem**, jeho **roli převezme jiný uzel**.
>
>>![[MacBook-2025-01-04-002371.png]]
>>- Pokud **selže navrhující uzel v průběhu fáze přijetí**, jiný uzel **převezme jeho roli** a v případě, že *existuje alespoň jedna informace o návrhu* (zpráva `accept()`), **převezme ji**.
>
>>- Funguje i v případě, že více uzlů zahájí návrh, můžu ale dojít k livelocku. To se řeší volbou lídra (např. Bully, Raft, ...)

## Raft algoritmus
- Fail-noisy model.
- Shoda v DS ve formě replikovaného logu operací.
- "*Moderní", často používaný. 'Náhrada Paxosu', který je hodně komplikovaný.
- Stavy uzlů:
	- Lídr, následovník, kandidát.
- https://raft.github.io

>[!Example]- Příklad
><iframe width="660" height="385" src="https://www.youtube.com/embed/IujMVjKvWP4?si=SuU_M1C4-iHu7W0H" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FVolba%20l%C3%ADdra%20v%20DS" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FTolerance%20chyby%20v%20DS" style="text-decoration: none;">
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