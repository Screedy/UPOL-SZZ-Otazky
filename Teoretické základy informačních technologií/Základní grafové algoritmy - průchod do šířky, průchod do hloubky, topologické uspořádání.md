### Průchod grafu
- Pro graf $G$ a počáteční vrchol $s$, chceme *systematicky navštívit všechny vrcholy dosažitelné z $s$*, každý z nich **právě jednou.**
- Vrchol $v$ je dosažitelný z $s$, pokud existuje cesta z $s$ do $v$.

#### Průchod do šířky a jeho vlastnosti
- **Vstup:**
	- Graf $G=(V, E)$
	- Vrchol $s \in V$
- *Projdeme vrcholy do kterých existuje cesta z $s$*
- Pomocné informace pro uzly **v polích** velikost $\mid V \mid$, na *indexu $i$* je informace k uzlu $i$:
	- **color:** barva uzlu, je to jedna z hodnot `white`, `gray`, `black`
	- **d:** *nejkratší vzdálenost od $s$* (vzdálenost je měřena jako počet hran ležících na cestě, $\mathbb{N}$ nebo $\infty$
	- **parent:** rodič uzlu ve stromu, který průchodem vytváříme, nebo `nil`
#### Implementace
- Předpokládáme, že samotný **graf** je struktura s položkami
	- **V:** množina vrcholů grafu (vhodně reprezentovaná)
	- **adj:** reprezentace grafu pomocí seznamů sousedů

```C
proc bfs(G, s)
  foreach u in G.V - {s} // pres vrcholy grafu mimo s
    color[u] = white
    d[u] = ∞
    parent[u] = nil
  
  color[s] = gray
  d[s] = 0
  parent[s] = nil
  Queue Q // fronta
  
  enqueue(Q,s)
  
  while !empty(Q)
    u = dequeue(Q)
    
    foreach v in G.adj[u] // pres sousedy vrcholu u
	    if color[v] == white
	      color[v] = gray
	      d[v] = d[u] + 1
	      parent[v] = u
	      enqueue(Q, v)
	    color[u] = black
```
#### Analýza algoritmu
- **Postupně objevujeme uzly:**
	- Neobjevené uzly mají barvu `white`
	- Objevené uzly, o kterých nevíme, že mají objevené sousedy, mají barvu `gray`
	- Objevené uzly, o kterých víme, že mají pouze objevené sousedy, mají barvu `black`
- **Složitost:**
	- Každý uzel je do fronty vložen pouze jednou (vkládáme pouze `white` uzly, uzel je po vložení přebarven na `gray`)
	- Uzly do fronty vkládáme a z fronty je odebíráme v konstantním čase. Proto je složitost práce s frontou $O(\mid V \mid)$
	- U každého uzlu po jeho odebrání z fronty projdeme seznam jeho sousedů. Víme ale, že součet délek seznamů v `adj` je $O(\mid E \mid)$. Proto procházení seznamů zabere $O(\mid E \mid)$ času
	- **Celkem je tedy složitost $O( \mid V \mid + \mid E \mid)$**

<iframe width="690" height="385" src="https://www.youtube.com/embed/HZ5YTanv5QE?si=vHtZX2LIAytCaoBM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### BFS(s) hledá uzly v pořadí podle vzdálenosti od $s$
- **Definice:** Nejkratší vzdálenost $\delta (u, v)$ z uzlu $u$ do uzlu $v$ je **nejmenší počet hran,** které má nějaká cesta z $u$ do $v$. 
- Pokud cesta z $u$ do $v$ **neexistuje**, pak $\delta (u,v) = \infty$.

#### Korektnost BFS
- **Věta:** Nechť $G = (V, E)$ je orientovaný nebo neorientovaný graf a $s \in V$. Potom na konci běhu algoritmu $\text{bfs}(G, s)$ pro každý uzel $v \in V$ platí:
	- $d[v] = \delta(s,v)$
	- Existuje-li cesta z $s$ do $v$, pak je `color[v]` rovno `black`
	- Existuje-li cesta z $s$ do $v$, pak je cesta, kterou sestavíme tak, že vezmeme nejkratší cestu z $s$ do `parent[v]` a připojíme k ní hranu `(parent[v], v)`, **nejkratší cestou z $s$ do $v$**

#### BFS sestaví strom
- Předpokládejme, že máme (orientovaný nebo neorientovaný) graf $G = (V, E)$ a uzel $s \in V$ a provedeme `bfs(G, s)`. Potom uvažujeme neorientovaný graf $G' = (V', E')$, kde 
	- $V' = \{v \in V \mid d[v] \neq \infty\}$
	- $E' = \{\{v, u\} \mid \text{parent}[u] = v\}$
- $G'$ je strom s kořenem $s$: z principu algortmu `bfs` plyne, že $\mid V' \mid = \mid E' \mid +\ 1$ *(s přidáním každého uzlu mimo $s$ do fronty vytvoříme jednu hranu z $E'$)* a $G'$ je souvislý *(z každého uzlu $v \in V'$ vede cesta do $s$, je to nejkratší cesta nalezená `bfs`)* Uzel $s$ jako jediný nemá rodiče.

#### Průchod do hlouby a jeho vlastnosti
- **Uzly mají položku pro barvu**, podobně jako u průchodu do hloubky. Možné barvy jsou opět `white`, `gray` a `black`
- Dále si pro každý uzel budeme **zaznamenávat čas**, kdy byl navštíven poprvé a změnil barvu z `white` na `gray`. K tomu použijeme **položku $d$.** Dále **zaznamenáme čas, kdy byl uzel navštíven podruhé,** k tomu použijeme **položku f**
- Čas budeme udržovat pomocí **globální proměnné `time`**, kterou na začátku nastavíme na $0$, a na vhodných místech inkrementujeme
```python
proc dfs(G)
  foreach u in G.V
    color[u] = white
    parent[u] = nil
  time = 0
  foreach u in G.V
    if color[u] == white
    dfs-visit(G,u)
```
```c
proc dfs-visit(G, u)
  time = time + 1
  d[u] = time  // prvni navsteva uzlu u
  color[u] = gray
  foreach v in G.adj[u] // navstivime vsechny nenavstivene sousedy u
    if color[v] == white
      parent[v] = u
      dfs-visit(G,v)
  color[u] = black
  time = time + 1
  f[u] = time   // druha navsteva uzlu u
```
- **Složitost:**
	- Proceduru `dfs-visit` voláme **pro každý uzel právě jednou**
	- V rámci tohoto volání procházíme seznam sousedů. Součet délek všech seznamů sousedů je omezen $\Theta (\mid E \mid)$.
	- Zbytek procedury je v konstantním čase.
	- **Celkem je tedy složitost $O(\mid E \mid + \mid V \mid)$**

#### DFS sestaví les
- Předpokládejme, že proběhl `dfs` pro graf $G$. Definujeme graf $G' = (V', E')$
	- $V' = V$
	- $E' = \{\{ u, v\} \mid \text{parent[u]} = v\}$
- $G'$ **je tvořen množinou stromů**, je to tzv. les. *Zdůvodnění je analogické tomu u `bfs`*. Stačí si všimnout, že `dfs-visit(G,u)` sestaví strom s kořenem $u$
- $G'$ může být i jenom strom (= les s jedním stromem), například když je $G$ **souvislý neorientovaný graf**
- **Lemma 4.** Po provedení `dfs` pro každý uzel $u$ platí $d[u] \leq f[u]$
- Důkaz. Mezi první a druhou návštěvou uzlu vždy **alespoň jednou inkrementujeme proměnnou `time`**

<iframe width="690" height="385" src="https://www.youtube.com/embed/Urx87-NMm6c?si=RtpuEeavhTJ645sF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Topologické uspořádání
- Orientovaný graf bez cyklů budeme nazývat `dag`. (to je zavedená anglická zkratka pojmu **directed acyclic graph**)
- Topologické uspořádání *dag*u $G = (V, E)$ je **lineární uspořádání vrcholů** grafu takové, že **pokud $(u,v) \in E,$** pak $u$ je v tomto uspořádání před $v$![[MacBook-2024-03-14-000883@2x.png]]
#### Algoritmus topol
- Inicializujeme prázdný seznam uzlů
- Spustíme upravený průchod do hloubky. Úprava spočívá v tom, že vždycky, když nastavujeme $f[u]$ pro uzel $u$, připojíme $u$ na začátek seznamu
- Po skončení průchodu obsahuje seznam uzly uspořádané sestupně podle hodnot položky $f$.

- Složitost:
	- Vkládání uzlu na začátek seznamu je v konstantním čase a vkládáme $\mid V \mid$ uzlů. To je jediná práce navíc oproti průchodu do hloubky. Proto je složitost $O(\mid V \mid + \mid E \mid)$

##### Navigace
Předchozí:  [[Hashovací tabulky, metody řešení kolizí]]
Následující: poslední
Celý okruh: [[1. Teoretické základy informačních technologií]]