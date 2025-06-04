## Dokazatelnost VL
>[!tip] Odvozovací pravidlo Modus Ponens
>- **Odvozovací pravidlo** = předpis pomocí nějž ze vstupních formulí odvozujeme další formule $$MP: \frac{\phi, \phi \Rightarrow \psi}{\psi}$$
>- Z formulí $\phi$ a $\phi \Rightarrow \psi$ odvodíme formuli $\psi$
>- Např. $\neg q$ vzniká z použitím **MP** z formulí $p \Rightarrow r$ a $(p \Rightarrow r) \Rightarrow \neg q$

>[!info] Axiomy VL
>- **Axiomy** = formule, které automaticky přijímáme jako "platné"
>- Axiomy popisují vlastnosti logických spojek a jejich vzájemný vztah
>- **Axiomová schémata:**
>	- (A1): $\phi \Rightarrow (\psi \Rightarrow \phi)$
>	- (A2): $(\phi \Rightarrow (\psi \Rightarrow \chi)) \Rightarrow ((\phi \Rightarrow \psi) \Rightarrow (\phi \Rightarrow \chi))$
>	- (A3): $(\neg \psi \Rightarrow \neg \phi) \Rightarrow (\phi \Rightarrow \psi)$
### Důkaz, syntaktické vyplývání

> [!info] Definice důkazu formule
> - **Důkaz formule $\psi$ z množiny formulí $T$** je libovolná posloupnost formulí $\psi_{1},...,\psi_{n}$ taková, že $\psi_{n} = \psi$ a každá $\psi_{i} (i = 1, ..., n)$:
>>- je **axiomem**
>>- nebo **náleží do $T$**
>>- nebo **vzniká** z předchozích formulí důkazu **pomocí odvozovacího pravidla MP**
>>- tedy existují indexy $j, k < i$ tak, že $\psi_{k}$ je formule ve tvaru $\psi_{j} \Rightarrow \psi_{i}$
>- **Formule $\psi$ je dokazatelná z $T$** (zapisujeme $T \vdash \psi$), pokud existuje důkaz formule $\psi$ z $T$. Pokud $\vdash \psi$, pak říkáme, že $\psi$ je **dokazatelná**
- **Dokazatelnosti** budeme také říkat **syntaktické vyplývání**, abychom tím zdůraznili, že jde o protějšek sémantického vyplývání
	- $T \vDash \psi$ ... **sémantické** vyplývání (pravdivost)
	- $T \vdash \psi$ ... **syntaktické** vyplývání (dokazatelnost)

>[!tip] Tvrzení
>- Pro každou množinu formulí $T$ a formule $\psi, \phi$ platí, že z $T \vdash \psi \Rightarrow \phi$ a $T \vdash \psi$ plyne $T \vdash \phi$.

>[!tip] Věta
>- Pro každou formuli $\psi$ platí $\vdash \psi \Rightarrow \psi$.
>- *Neboli že plyne z prázdné množiny.*

>[!tip] Lemma monotonie dokazatelnosti (MD)
>- Nechť $T$ a $S$ jsou množiny formulí a $\psi, \phi$ jsou formule. 
>- Pak platí: Pokud $T \vdash \psi$ a pro každou $\phi \in T$ máme $S \vdash \phi$, pak $S \vdash \psi$.
> - Z platnosti $\vdash \phi$ jednoduše odvodíme $T \vdash \phi$

>[!tip] Věta o dedukci (VoD)
>- Pro každou množinu formulí $T$ a formule $\psi, \phi$ platí:
>- $T \vdash \psi \Rightarrow \phi$, právě když $T, \psi \vdash \phi$.

>[!info] Spornost a bezespornost
>- Množina formulí $T$ se nazývá **sporná** (nekonzistentní), jestliže je z ní dokazatelná jakákoliv formule. 
>- Není-li $T$ sporná (tedy existuje formule, která není z $T$ dokazatelná), nazývá se **bezesporná** (konzistentní)

>[!tip] Věta o důkazu sporem
>- Nechť $T$ je množina formulí, nechť $\psi$ je libovolná formule. Pak platí: $T \vdash \psi$, právě když $T \vdash \neg \psi$ je **sporná množina**.
>- *Předpokládáme neplatnost tvrzení a dojdeme ke sporu, čímž dokážeme platnost daného tvrzení.*

>[!tip] Věta o důkazu rozborem případů
>- Pro množinu formulí $T$ a formule $\psi, \phi, \chi$ platí $T, \psi \lor \phi \vdash \chi$, právě když $T, \psi \vdash \chi$ a $T, \phi \vdash \chi$

>[!tip] Věta o neutrální formuli
>- Pro množinu formulí $T$ a formule $\psi$ a $\phi$ platí $T \vdash \phi$, právě když $T, \psi \vdash \phi$ a $T, \neg \psi \vdash \phi$.

>[!tip] Věta o korektnosti
>- Pro libovolnou množinu formulí $T$ a formuli $\psi$ platí, že je-li $T \vdash \psi$, pak $T \vDash \psi$.
>- Speciálně tedy, každá dokazatelná formule je tautologií

>[!info] Churchovo lemma (ChL)
>- Pro libovolnou formuli $\psi(p_{1}, ... p_{n})$ platí $p^{e}_{1}, ... ,p^{e}_{n} \vdash \psi^{e}$

>[!info] Věta o úplnosti, slabá verze
>- Pro libovolnou konečnou množinu $T$ formulí a formuli $\psi$ platí, že z $T \vDash \psi$ plyne $T \vdash \psi$.
>	- Speciálně, každá pravdivá formule je dokazatelná

##### Navigace
Předchozí:  [[Výroková logika, jazyk, formule, pravdivost, vyplývání, tautologie, základní syntaktické a sémantické pojmy výrokové logiky]]
Následující: [[Syntax a sémantika predikátové logiky]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky|1. Teoretické základy informatiky]]