## Deterministický konečný automat
>[!info] Definice
>- **Deterministický konečný automat** $M$ je uspořádaná pětice $M = (Q, \Sigma, \delta, q_{0}, F)$, kde:
>	- $Q$ je neprázdná konečná množina stavů
>	- $\Sigma$ je konečná množina vstupních symbolů, nazývaná také vstupní abeceda
>	- $\delta$ je přechodová funkce ve stavu $\delta : Q \times \Sigma \rightarrow Q$
>	- $q_{0} \in Q$ je počáteční stav
>	- $F \subseteq Q$ je množina koncových/akceptujících stavů

- Takto definovaný atomat je deterministický, protože se v každém kroku výpočtu nachází právě v jednom stavu
- Abychom mohli definovat jazyk přijímaný daným DFA M, zavedeme rozšířenou přechodovou funkci $\hat{\delta}: Q \times E^{*} \rightarrow Q$, definovanou induktivně vzhledem k délce slova ze $\Sigma^{*}$:
	- $\hat{\delta}(q, \epsilon) = q$, pro každý stav $q \in Q$
	- $\hat{\delta}(q, wa) = \delta(\hat{\delta}(q,w)a)$

- Jazyk přijímaný DFA M, označovaný $L(M)$, je tvořen právě všemi takovými slovy, pod kterými automat přejde z počátečního stavu do některého z koncových stavů: $L(M) = \set{w \in \Sigma^{*} |\ \hat{\delta}(q_{0}, w) \in F}$
- Jazyk, který je rozpoznatelný DFA, nazveme regulární

>[!Example] Příklad DFA M a jeho další možné reprezentace
>- Nechť $\mathcal{M} = (\set{q_{0}, q_{1}, q_{2}}, \set{a,b}, \delta, q_{0}, \set{q_{2}})$ je $FA$, kde
>  $\ \ \delta (q_{0},a)=q_{1}\ \ \ \ \delta (q_{0}, b)=q_{2}$
>  $\ \ \delta (q_{1},a)=q_{2}\ \ \ \ \delta (q_{1}, b)=q_{0}$
>  $\ \ \delta (q_{2},a)=q_{0}\ \ \ \ \delta (q_{2}, b)=q_{1}$
>  Pak $L(\mathcal{M})=\set{w \in \set{a,b}^{*} |\ (\#_{a}(w)- \#_{b}(w)) \text{ mod } 3=2}$.
- Automat M je možné reprezentovat pomocí tabulky přechodové funkce:![[MacBook-2024-05-26-001341.png| 350]]
- Stavy automatu jsou vypsány v záhlaví řádků, vstupní symboly v záhlaví sloupců, přechodová funkce je určena obsahem vnitřních polí tabulky, počáteční stav je označen znakem $\rightarrow$ a koncové stavy znakem $\leftarrow$.
- Ještě přehlednější(a proto nejčastěji používaná) je reprezentace pomocí přechodového grafu, který pro automat $M$ vypadá takto:![[MacBook-2024-05-26-001342.png| 400]]
- Stavy odpovídají uzlům, přechodová funkce je znázorněna ohodnocenými hranami, vstupní abeceda je tvořena symboly, kterými jsou hrany ohodnoceny, počáteční stav je označen šipkou a koncové stavy jsou dvojitě zakroužkovány

- Nakonec ještě zmiňme reprezentaci výpočetním stromem. Kočen stromu odpovídá počátečnímu stavu. Z každého uzlu, který není listem vychází právě tolik hran ohodnocených symboly vstupní abecedy, kolik má odpovídající stav následníků (je-li tedy totální, pak právě tolik hran, kolik symbolů má vstupní abeceda). Jestliže nějaký stav odpovídá více uzlům, pak hrany vycházejí jen z jednoho z těchto uzlů.
- Výpočetním stromem lze reprezentovat jen ty automaty, kde každý stav je tzv. dosažitelný z počátečního stavu
- Výpočetní strom pro daný automat není určen jednoznačně - může se lišit dle toho, zda jej konstruujeme způsobem, který odpovídá například procházení do hloubky, nebo do šířky, či dalšími možnostmi. ![[MacBook-2024-05-26-001343.png]]

## Konstrukce konečných automatů
- Základním trikem, který dokáže zjednodušit návrh konečného automatu, je zavedení jisté pomocní struktury na stavech. Informaci, která je spojená s daným stavem, je účelné zachytit v jeho označení.
>[!Example] Příklad
>- Máme za úkol sestrojit automat rozpoznávající jazyk $$L=\set{w \in \set{a,b}^{*} |\ w \text{ obsahuje podslovo abaa}}$$![[MacBook-2024-05-26-001344.png]]

## Konečný nedeterministický automat
- Jediný rozdíl je v tom, že **nedeterministický** automat **nemusí mít pro daný stav a vstupní symbol určen následující stav jednoznačně**. Slovo $w$ bude akceptování, pokud alespoň jeden z možných výpočtů nad slovem $w$ skončí v koncovém stavu.

>[!info] Definice
>- **Nedeterministický konečný automat $M$** je **uspořádaná pětice $M=(Q, \Sigma, \delta, q_{0}, F)$**
>	- $Q$ je neprázdná konečná množina stavů
>	- $\Sigma$ je konečná množina vstupních symbolů, nazývaná také vstupní abeceda
>	- $\delta$ je přechodová funkce ve tvaru $\delta : Q \times \Sigma \rightarrow 2^{Q}$
>	- $q_{0} \in Q$ je počáteční stav
>	- $F \subseteq Q$ je množina koncových/akceptujících stavů

- Abychom mohli definovat jazyk přijímaný daným NFA M, zavedeme **rozšíčenou přechodovou funkci** $\hat{\delta}: Q \times \Sigma^{*} \rightarrow 2^{Q}$, definovanou induktivně vzhledem k délce slova ze $\Sigma^{*}$:
	- $\hat{\delta}(q, \epsilon)=\set{q}$, pro každý stav $q \in Q$
	- $\hat{\delta}(q, wa)=\cup_{p \in \hat{\delta}(q,w)} \delta (p,a)$
- Jazyk přijímaný NFA M je definován takto: $$L(M)=\set{w \in \Sigma^{*}|\ \hat{\delta}(q_{0}, w) \cap F \neq 0}$$
- Nedeterminismus je velmi silná popisný aparát, který často umožňuje zachytit strukturu jazyka elegantním a přirozeným způsobem.
>[!Example] Příklad
>- $L=\set{w \in \set{a,b}^{*} |\ w \text{ obsahuje podslovo abba nebo bab}}$
>- Navrhnout DFA, který rozpoznává $L$, není zcela triviální.
>- Naopak nederministický automat lze zkonstruovat snadno
>![[MacBook-2024-05-26-001345.png]]
- Nedeterminismus lze dobře využít jako popisný prostředek, nemá však vliv na výpočetní sílu konečných automatů. Ke každému nedeterministickému konečnému automatu totiž ve skutečnosti existuje ekvivalentní deterministický automat, který lze dokonce algoritmicky zkonstruovat.

##### Navigace
Předchozí:  [[Regulární jazyky (definice, uzávěrové vlastnosti)]]
Následující: [[Regulární výrazy, automaty s e-přechody]]
Celý okruh: [[1. Teoretické základy informatiky]]