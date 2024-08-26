>[!tip]- Pravidlo součtu a součinu, binomická věta
>- Pravidlo součtu a součinu:
>	- **Pravidlo součtu**: Lze-li úkol $A$ provést $m$ způsoby a úkol $B$ n způsoby, přičemž žádný z $m$ způsobů provedení úkolu $A$ není totožný s žádným z $n$ způsobů provedení úkolu $B$, pak provést úkol $A$ nebo úkol $B$ lze **$m + n$** způsoby
>	- **Pravidlo součinu**: Lze-li úkol $C$ rozložit na po sobě následující úkoly $A$ a $B$ a lze-li úkol $A$ provést $m$ způsoby a úkol $B$ $n$ způsoby, pak úkol $C$ lze provést $m*n$ způsoby
>- **Binomická věta**
>	- $(a+b)^{n} = \sum^{n}_{k=0} \binom{n}{k} a^{n-k}b^{k}$
>	- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
>	- Pro $n=3$: $$(a+b)^{3}= \binom{3}{0}a^{3}b^{0}+ \binom{3}{1}a^{2}b^{1}+ \binom{3}{2}a^{1}b^{2}+ \binom{3}{3}a^{0}b^{3}$$

### Permutace
- **Permutace $n$ (navzájem různých) objektů** je libovolné seřazení těchto objektů, tj. seřazení od prvního k $n$-tému. 
- Počet permutací $n$ objektů značíme $P(n)$.
- Vzoreček: $P(n) = n!$
- Důkaz vzorečku:
	- Jedno, ale libovolné, seřazení dostaneme tak, že vybereme $1.$ prvek *(lze provést $n$ způsoby)*, poté vybereme $2.$ prvek *(to lze provést $n-1$ způsoby)*, poté vybereme $3.$ prvek *(to lze $n-2$ způsoby)*, ..., nakonec vybereme $n$-tý prvek *(to lze provést jedním způsobem)*. Podle pravidla součinu lze takový výběr provést **$n * (n-1) * (n-2) * ... * 1 = n!$** způsoby. Tedy **$P(n) = n!$**.

#### Permutace s opakováním
- Seřazujeme-li objekty, z nichž některé jsou stejné
- Je dáno **$n$ objektů rozdělených do $r$ skupin**, které mají po řadě **$n_{1}, ..., n_{r}$ objektů**. Objekty v každé ze skupin jsou **navzájem nerozlišitelné.** Každé seřazení těchto $n$ objektů se nazývá **permutace s opakováním** (daným parametry ($n_{1}, ..., n_{r}$)). Počet takových permutací **značíme $P(n_{1}, ..., n_{r})$**.
- Vzoreček: **Pro $n_{1} + ... + n_{r} = n$ je $P(n_{1}, ..., n_{r}) = \frac{n!}{n_{1} * ... * n_{r}}$**

### Variace
- Je dáno $n$ (navzájem různých) objektů a číslo $r \leq n$. **Variace $r$ (objektů) z $n$ (objektů)** je **libovolný výběr $r$ objektů z daných $n$ objektů**, ve kterém <u>záleží na pořadí</u> vybíraných objektů. 
- Počet takových variací značíme $V(n,r)$.
- Vzoreček: **$V(n,r) = n * (n-1) * ... * (n-r+1)$**.
- Důkaz vzorečku:
	- Každá variace je dána tím, jaké objekty jsou na $1., 2., ..., r$-tém místě. Objekt na $1.$ místě lze zvolit $n$ způsoby *(vybíráme z n objektů)*, objekt na $2.$ místě pak $n-1$ způsoby *(vybíráme z $n-1$ objektů, protože jeden objekt je už na $1.$ místě)*, ..., objekt na $r$-tém místě lze vybrat $n-r+1$ způsoby *(tolik objektů kolik zbývá ještě k výběru)*. Podle pravidla součinu je tedy celkový počet takto provedených výběrů, tj. **počet všech variací, $n * (n-1) * ... * (n-r+1)$**.
- Možná variace vzorečku: **$V(n,r) = \frac{n!}{(n-r)!}$**
- Důkaz možné variace vzorečku: $\frac{n!}{(n-r)!} = \frac{n*(n-1)*...*(n-r+1)*(n-r)*...*1}{(n-r)*...*1} = n * (n-1) * ... * (n-r+1) = V(n,r)$ 

#### Variace s opakováním
- Výběry, ve kterých se prvky mohou opakovat, nazýváme variace s opakováním.
- Jsou dány objekty $n$ různých typů. Objektů každého typu je <u>neomezeně mnoho</u> a jsou navzájem nerozlišitelné. **Variace $r$ (objektů) z $n$ (objektů) s opakováním** je libovolný výběr $r$ objektů z daných objektů $n$ typů, ve kterém záleží na pořadí vybíraných objektů. Počet takových variací značíme $\stackrel{\_\_}{V}(n,r) = n^{r}$.

### Kombinace
- Je dáno $n$ (*navzájem různých*) objektů a číslo $r \leq n$. **Kombinace $r$ (objektů) z $n$ (objektů)** je **libovolný výběr $r$ objektů z daných $n$ objektů**, ve kterém <u>nezáleží na pořadí</u> vybraných objektů. Počet takových kombinací značíme $C(n,r)$
- Vzoreček: $C(n,r) = \binom{n}{r} = \frac{n!}{(n-r)!*r!}$
- Důkaz vzorečku: Víme, že $V(n,r) = \frac{n!}{(n-r)!}$. Uvědomme si, že každé kombinaci $r$ z $n$ odpovídá tolik variací $r$ z $n$, kolika způsoby lze uspořádat $r$ vybraných objektů *(u kombinace záleží jen na vybraných objektech, ne na jejich uspořádání, kdežto u variace záleží i na jejich uspořádání)*. Existuje $r!$ způsobů, jak uspořádat $r$ objektů. Je tedy **počet kombinací $r$ z $n$ krát počet uspořádání $r$ objektů = počet variací $r$ z $n$** $\binom{n}{r} * r! = V(n,r)$.
- Odtud $\binom{n}{r} = \frac{V(n,r)}{r!} = \frac{n!}{(n-r)!*r!}$.

#### Kombinace s opakováním
- Výběr, ve kterém nezáleží na pořadí prvků a ve kterém se prvky mohou opakovat, se nazývá kombinace s opakováním.
- Jsou dány objekty $n$ různých typů. Objektů každého typu je <u>neomezeně mnoho</u> a jsou navzájem *nerozlišitelné*. **Kombinace $r$ (objektů) z $n$ (objektů) s opakováním** je **libovolný výběr $r$ objektů z daných objektů $n$ typů**, ve kterém <u>nezáleží na pořadí</u> vybíraných objektů. Počet takových kombinací značíme $\stackrel{\_\_}{C}(n,r)$.
- Vzoreček: $\stackrel{\_\_}{C}(n,r) = \binom{n+r-1}{n-1} = \binom{n+r-1}{r}$.

##### Navigace
Předchozí:  [[Uspořádání, Hasseovy diagramy]]
Následující: [[Pravděpodobnost, Laplaceova definice, pravděpodobnostní prostor, náhodná veličina, střední hodnota]]
Celý okruh: [[1. Teoretické základy informačních technologií]]