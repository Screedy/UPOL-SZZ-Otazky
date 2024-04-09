### Hledání nejkratší cesty a Dijkstrův algoritmus
- Dijkstrův algoritmus je jeden z nejznámějších algoritmů hledání nejkratší cesty

- Algoritmus pracuje následovně
- **Na vstupu** je neorientovaný graf $G = <V, E>$, jeho hranové ohodnocení $w: E \rightarrow R*$ a vrchol $s \in V$
- **Výstupem** algoritmu je pro každý vrchol $v \in V$ číslo $d(v)$, které je vzdáleností z $s$ do $v$.
- Algoritmus **používá proměnné** $A, N, d, m$, přitom $A$ a $N$ označují množiny vrcholů, $d$ označuje funkci přiřazující vrcholům kladná reálná čísla a $m$ označuje nezáporné reálné číslo.

- V každém kroku algoritmu je pro vrchol $v$ \in V$ hodnota $d(v)$ rovna délce nejkratší zatím nalezené cesty z $s$ do $v$.

- **Na začátku** se nastaví $d(s) = 0$ a $d(v) = \infty$ pro ostatní vrcholy $v \neq s$. Hodnota $d(v) = \infty$ znamená, že žádná cesta do $v$ zatím nebyla nalezena. Tato hodnota se pak u vrcholů, do kterých existuje cesta z $s$, v průběhu výpočtu zmenšuje, v každém kroku obsahuje délku nejkratší zatím nalezené cesty z $s$ do $v$, a na konci délku nejkratší cesty z $s$ do $v$. U vrcholů $v$, do kterých cesta z $s$ nevede, zůstává $d(v) = \infty$. Množina $A$ se na začátku nastaví na $A = V$. Během výpočtu obsahuje $A$ ty vrcholy $v$, pro něž zatím nebyla stanovena konečná hodnota $d(v)$ (tj. $d(v)$ byla stanovena, ale v dalším výpočtu se ještě může změnit). 
- **Algoritmus opakuje následující krok:** zjistí nejmenší hodnotu $d(v)$ vrcholů z $A$. Množinu vrcholů $v$ z $A$ s touto nejmenší hodnotou označí $N$. Z množiny $A$ vyjme všechny vrcholy $v$, pro které je $d(v)$ nejmenší. Vrchol $v$ se tedy odstraní z $A$ a vloží do $N$, právě když $d(v) = min{d(u) \mid u \in A}$. Každý takový vrchol $v$ je pak považován za vrchol, pro nějž byla nalezena nejkratší cesta z $s$ do $v$, délkou této cesty je $d(v)$, a kratší cesta do $v$ se v dalších krocích algoritmu už nehledá (to je zajištěno tím, že se vrchol odstranil z $A$). Vložení vrcholu $v$ do $N$ znamená, že $v$ je považován za vrchol, přes který může do zbývajících vrcholů $u$ množiny $A$ vést kratší cesta, než je dosud nalezená nejkratší cesta do $u$. V tomto smyslu je tedy každý vrchol $v$ z $N$ kandidátem na zlepšení hodnoty $d(u)$. Algoritmus toto možné zlepšení prověří pro vrcholy $u$ z $A$, do kterých vede z $v$ hrana. Algoritmus tedy pro každý $v \in N$ a pro každý $u \in A$, pro který existuje hrana $\{v, u\} \in E$, porovná hodnotu $d(v) + w(\{v, u\})$ (délka možné cesty z s do u, která vede přes v) s hodnotou $d(u)$ (délka dosud nejkratší nalezené cesty z $s$ do $u$). Je-li $d(v) + w(\{v, u\}) < d(u)$(tj. cesta přes v je kratší), změní se hodnota $d(u) na d(u) = d(v) + w(\{v, u\})$. Algoritmus se pak vrátí ke kroku 2. V něm se ověří, zda je v $A$ ještě nějaký vrchol $v$ s hodnotou $d(v) < \infty$. Pokud ano, znamená to, že v $A$ se nacházejí kandidáti na zlepšení hodnot $d(u)$ a pokračuje se znovu jako výše, tedy stanovením nové množiny $N$ , odebráním vrcholů z $A$ a tak dále. Pokud ale v $A$ žádný vrchol $v$ s hodnotou $d(v) < \infty$ není, algoritmus skončí. Na konci je množina $A$ buď prázdná, a to tehdy, když ke všem vrcholům z $s$ cesta existuje, nebo je neprázdná, a obsahuje jen vrcholy $v$ s hodnotou $d(v) = \infty$. Vrcholy s hodnotou $d(v) = \infty$ jsou právě ty, ke kterým z s neexistuje cesta.

### Algoritmus
- **Vstup:** Graf $G = <V, E>$, vrchol $s \in V$, hranové ohodnocení $w: E \rightarrow R^{+}$
- **Výstup:** Hodnota $d(v)$ pro každý $v \in V$, $d(v)$ je délka nejkratší cesty z $s$ do $v$
- **Proměnné:** Funkce $d: V \rightarrow R^{+}$, číslo $m \in R^{+}$, množiny $A, N \in V$
- **Postup:**
	1. $d(s) = 0$; pro každý $v \in V - \{s\}: d(v):= \infty ; A = V$
	2. Pokud existuje $v \in A$ takový, že $d(v) \neq \infty$, skonči
	3. $m = min\{d(v) \mid v \in A\}, N= \{ v \in A \mid d(v)=m \}, A = A - N$
	4. Pro všechny $v \in N, u \in A$ takové, že $\{v,u\} \in E$ jestliže $d(v) + w(\{v,u\}) < d(u),$ pak $d(u)=d(v)+w(\{v,u\});$ pokračuj krokem $2.$


