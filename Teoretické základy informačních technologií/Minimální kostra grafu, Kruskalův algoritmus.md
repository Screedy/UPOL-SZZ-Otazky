### Příklad
- Máme za úkol propojit města $v_{1}, ..., v_{n}$ elektrickým vedením, a to tak, aby výstavba vedení byla co nejlevnější. Musíme tedy rozhodnout, mezi kterými městy máme natáhnout elektrické dráty tak, aby se elektřina mohla dostat z každého města do každého jiného města. Přitom víme, že mezi některými dvojicemi měst přímé propojení postavit nelze. Pokud města $v_{i}$ a $v_{j}$ propjit lze, známe náklady na výstavbu vedení mezi $v_{i}$ a $v_{j}$.

- **Kostra neorientovaného grafu $G$** je jeho **podgraf $G'$**, který je stromem a obsahuje **všechny vrcholy** grafu G.
- Je-li $w: E \rightarrow R^{+}$ hranové ohodnocení grafu $G = <V, E>$, nazývá se **kostra $G' = <V, E'>$ minimální kostra**, pokud má ze všech koster grafu $G$ nejmenší hodnotu $w(G')$, kde $w(G')= \sum_{\{u,v\} \in E'} w(\{u,v\})$

### Kruskalův Algoritmus
- **Vstup:**
	- Souvislý neorientovaný graf $G = <V, E>$ s $n$ vrcholy a $m$ hranami
	- Ohodnocení $w: E \rightarrow R^{+}$
- **Výstup:**
	- Množina hran $E' \subseteq E$ takový, že $G' = <V, E'>$ je minimální kostra grafu $G$
- **Postup:**
	1. Setřiď hrany vzestupně podle ohodnocení, tj. utvoř posloupnost $e_{1}, ..., e_{m}$ všech hran z $E$ tak, že $w(e_{1}) \leq ... \leq w(e_{m})$
	2. $E_{0} = \varnothing, i = 0$
	3. Dokud $E_{i}$ neobsahuje $n-1$ hran, prováděj:
		1. $i = i + 1$
		2. $E_{i} =$
			1. $E_{i-1} \cup \{e_{i}\}$ pokud $<V, E_{i-1} \cup \{e_{i}\}>$ neobsahuje kružnici
			2. $E_{i-1}$ v opačném případě
	4. $E' = E_{i}$

![[MacBook-2024-03-07-000799@2x.png | 500]]