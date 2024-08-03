### Příklad
- Máme za úkol propojit města $v_{1}, ..., v_{n}$ elektrickým vedením, a to tak, aby výstavba vedení byla co nejlevnější. Musíme tedy rozhodnout, mezi kterými městy máme natáhnout elektrické dráty tak, aby se elektřina mohla dostat z každého města do každého jiného města. Přitom víme, že mezi některými dvojicemi měst přímé propojení postavit nelze. Pokud města $v_{i}$ a $v_{j}$ propojit lze, známe náklady na výstavbu vedení mezi $v_{i}$ a $v_{j}$.

- **Kostra neorientovaného grafu $G$** je jeho **podgraf $G'$**, který je **stromem** a obsahuje **všechny vrcholy** grafu $G$.
- Je-li $w: E \rightarrow \mathbb{R}^{+}$ **hranové ohodnocení** grafu $G = <V, E>$, nazývá se **kostra $G' = <V, E'>$ minimální kostra**, pokud má ze všech koster grafu $G$ nejmenší hodnotu $w(G')$, kde $w(G')= \sum_{\{u,v\} \in E'} w(\{u,v\})$

### Kruskalův Algoritmus
- **Vstup:**
	- Souvislý neorientovaný graf $G = <V, E>$ s $n$ vrcholy a $m$ hranami
	- Ohodnocení $w: E \rightarrow \mathbb{R}^{+}$
- **Výstup:**
	- Množina hran $E' \subseteq E$ takový, že $G' = <V, E'>$ je minimální kostra grafu $G$
- **Postup:**
	1. Setřiď hrany vzestupně podle ohodnocení, tj. utvoř posloupnost $e_{1}, ..., e_{m}$ všech hran z $E$ tak, že $w(e_{1}) \leq ... \leq w(e_{m})$
	2. $E_{0} = \varnothing, i = 0$
	3. Dokud $E_{i}$ neobsahuje $n-1$ hran, prováděj:
		1. $i = i + 1$
		2. $E_{i} = \cases{E_{i-1}\ \cup \set{e_{i}} \text{ pokud } <V, E_{i-1}\ \cup \set{e_{i}}> \text{neobsahuje kružnici} \\ E_{i-1} \text{ v opačném případě}}$ 
	4. $E' = E_{i}$

> [!Example]- Příklad
>```mermaid
>graph LR
>A -- "2" --- B;
>A -- "3" --- D;
>A -- "3" --- C;
>B -- "4" --- C;
>C -- "1" --- E;
>B -- "3" --- E;
>C -- "5" --- D;
>D -- "7" --- F;
>E -- "8" --- F;
>F -- "9" --- G;
>```
>
>```mermaid
>graph LR
>A -- "2" --- B;
>A -- "3" --- D;
>A -- "3" --- C;
>B -- "4" --- C;
>C -- "1" --- E;
>B -- "3" --- E;
>C -- "5" --- D;
>D -- "7" --- F;
>E -- "8" --- F;
>F -- "9" --- G;
>
>linkStyle 4 stroke:Red;
>```
>```mermaid
>graph LR
>A -- "2" --- B;
>A -- "3" --- D;
>A -- "3" --- C;
>B -- "4" --- C;
>C -- "1" --- E;
>B -- "3" --- E;
>C -- "5" --- D;
>D -- "7" --- F;
>E -- "8" --- F;
>F -- "9" --- G;
>
>linkStyle 4 stroke:Red;
>linkStyle 0 stroke:Red;
>```
>...
>```mermaid
>
>graph LR
>A -- "2" --- B;
>A -- "3" --- D;
>A -- "3" --- C;
>B -- "4" --- C;
>C -- "1" --- E;
>B -- "3" --- E;
>C -- "5" --- D;
>D -- "7" --- F;
>E -- "8" --- F;
>F -- "9" --- G;
>
>linkStyle 4 stroke:Red;
>linkStyle 0 stroke:Red;
>linkStyle 1 stroke:Red;
>linkStyle 2 stroke:Red;
>linkStyle 7 stroke:Red;
>linkStyle 9 stroke:Red;
>```
>- Minimální kostra grafu:
>```mermaid
>
>graph LR
>
>A -- "3" --- D;
>D -- "7" --- F;
>F -- "9" --- G;
>A -- "3" --- C;
>C -- "1" --- E;
>A -- "2" --- B;
>
>linkStyle default stroke:Red;
>```


<iframe width="690" height="385" src="https://www.youtube.com/embed/71UQH7Pr9kU?si=siVilj3MfpqRVJ2z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### Navigace
Předchozí:  [[Hledání nejkratší cesty, Dijkstrův algoritmus]]
Následující: [[Stromy, kořenové stromy, vztahy mezi výškou, počtem vrcholů, počtem listů]]
Celý okruh: [[1. Teoretické základy informačních technologií]]