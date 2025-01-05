- Shoda se stává důležitou otázkou v distribuovaných prostředích, kde *různé části systému mohou udržovat kopie dat a informací*.
- Je potřeba zajistit, aby **všechny tyto kopie byly v souladu**.

- Shoda v systémech bez selhání, je velmi **jednoduchá** zjistit.

## Shoda v systémech s možností selhání
- Fail-stop (silná podmínka)
	- Využití algoritmu Flooding consensus nebo Paxos

### Flooding consensus
- *Algoritmus sloužící k dosažení shody v DS*.
- Jedná se o jednoduchý přístup, kde **každý uzel systému periodicky rozesílá svůj stav nebo informace o změnách všech ostatních uzlů** ve svém okolí.
- Tento proces se nazývá "**flooding**" (případně "epidemic dissemination").

>[!Example] Postup:
>- V každém kole si **aktivní uzly vymění své návrhy**.
>- Každý uzel **deterministicky zvolí volbu**.
>- *Pokud uzel neobdrží informace od všech ostatních* posun do **dalšího kola**
>
>![[MacBook-2025-01-04-002367@2x.png]]

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
>	- Každý uzel, který chce navrhnout hodnotu začne **fázi přípravy** tím, že **požádá ostatní uzly o schválení čísla přípravy**.
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
>![[MacBook-2025-01-04-002368@2x.png]]

>[!fail] Možné chyby:
>>![[MacBook-2025-01-04-002369@2x.png]]
>>- Pokud **selže uzel přijímající návrh**, nic se neděje, **dokud funguje většina**.
>
>>![[MacBook-2025-01-04-002370@2x.png]]
>>- Pokud selže **navrhující uzel před návrhem**, jeho **roli převezme jiný uzel**.
>
>>![[MacBook-2025-01-04-002371@2x.png]]
>>- Pokud **selže navrhující uzel v průběhu fáze přijetí**, jiný uzel **převezme jeho roli** a v případě, že *existuje alespoň jedna informace o návrhu* (zpráva `accept()`), **převezme ji**.
>
>>- Funguje i v případě, že více uzlů zahájí návrh, můžu ale dojít k livelocku. To se řeší volbou lídra (např. Bully, Raft, ...)

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