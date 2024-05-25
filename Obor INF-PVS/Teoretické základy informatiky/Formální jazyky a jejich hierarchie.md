
## Abeceda a jazyk
### Abeceda
- libovolná konečná množina $\Sigma$, jejíž prvky nazýváme znaky abecedy
>[!Example] Příklad abecedy
>- množina $\set{a,b}$
>- množina $\set{0,1,...,9}$
>- množina $\varnothing$

### Slovo
- **Slovo $v$ nad abecedou** $\Sigma$ je libovolná konečná posloupnost znaků této abecedy
- **Počet členů** této posloupnosti značíme $|v|$ a nazýváme **délkou slova**
- **Počet výskytů** znaku $a$ ve slově $v$ značíme $\#_{a}(v)$
- Prázdné posloupnosti znaků odpovídá tzv. **prázdné slovo**
	- značíme $\epsilon$, které má nulovou délku
- Množina všech slov nad abecedou $\Sigma$ značíme $\Sigma^{*}$
- Množinu všech neprázdných slov $\Sigma^{+}$
>[!Example] Příklad
>- $\set{a}^{*} = \set{\epsilon,a,aa,aaa,aaaa,...}$
>- $\set{a}^{+} = \set{a}^{*}\\ \set{\epsilon}$
>- $\set{0,1}^{*} = \set{\epsilon,0,1,00,01,10,11,000,001,011,...}$
- Definitoricky dále klademe $\varnothing^{*}=\set{\epsilon}$ a $\varnothing^{+}=\varnothing$
- Na každé dvě slova $u, v$ lze aplikovat **binární operaci zřetězení**, která je definována $u.v=uv$
>[!Example] Příklad zřetězení slov
>- zřetězením slov $abba$ a $bba$ obdržíme slovo $abbabba$
- Operace zřetězení je **asociativní**
	- $u.(v.w)=(u.v).w$ pro libovolná slova $u,v,w$
- Déle $\epsilon$ se chová jako **jednotkový prvek**
	- $u.\epsilon = \epsilon.u = u$ pro libovolné $u$

- Pro snazší specifikaci jazyků je výhodné zavést **unární operaci $i$-té mocniny slova**, která je definovaná induktivně pro každé $i \in N_{0}$ takto:
	- Nechť $\Sigma$ je libovolná abeceda, $u \in \Sigma^{*}$ libovolní slovo. Pak
		- $u^{0}=\epsilon$
		- $u^{i+1}=u.u^{i}$

>[!Example] Příklad $i$-té mocniny slova
>- $(abc)^{3} = abcabcabc$

- Pro slova $u,v \in \Sigma^{*}$ platí:
	- $u=v$, právě když $|u|=|v|$ a zároveň $u_{i}=v_{i}$ pro všechna $i=1,...,|u|$

- Slovo $u$ je podslovem slova $v$, jestliže existují slova $x,y$ taková, že $v=x.u.y$
	- Pokud navíc $x=\epsilon$, říkáme že slovo $u$ je předponou (prefixem) slova $v$
- Je-li $y=\epsilon$ nazveme $u$ příponou (sufix) slova $v$

### Jazyk
- **Jazyk nad abecedou $\Sigma$** je libovolná množina slov nad $\Sigma$ (Jazyk nad $\Sigma$ je tedy právě podmnožina $\Sigma^{*}$)
>[!Example] Příklady
>- $\set{10,1,011101}$ je jazyk nad abecedou $\set{0,1}$
>- prázdná množina je jazyk nad libovolnou abecedou

- Jazyky mohou ovšem být i **nekonečné**
>[!Example] Příklad nekonečných jazyků
>- $\set{w \in \set{a,b}^{*}| \#_{a}(w)= \#_{b}(w)}$ je jazyk nad abecedou $\set{a,b}$ obsahující všechna slova, ve kterých se $a$ i $b$ vyskytují ve stejném počtu

## Operace nad jazyky
- Nechť $L$ je libovolný jazyk nad abecedou $\Sigma$ a $K$ libovolný jazyk nad abecedou $\Delta$.
- Jelikož $L$ i $K$ jsou množiny, můžeme aplikovat standarní množinové operace **sjednocení, průnik a rozdíl**. Výsledkem je vždy jazyk nad abecedou $\Sigma \cup \Delta$.
- Dále definujeme:
	- Zřetězení jazyků $K$ a $L$ je jazyk $K.L = \set{uv|u \in K, v \in L}$ nad abecedou $\Sigma \cup \Delta$.
		- Podle definice zejména platí $\varnothing .M = M.\varnothing = \varnothing$ a $\set{\epsilon}.M = M.\set{\epsilon} = M$ pro libovolný jazyk $M$. Operace zřetězení jazyků je také zřejmě **asociativní**
	- **$i$-tá mocnina jazyka $L$** je definována induktivně pro každé $i \in N_{0}$:
		- $L^{0}=\set{\epsilon}$
		- $L^{i+1} é L.L^{i}$
	 Zejména tedy $\varnothing^{0}=\set{\epsilon}, \varnothing^{i} = \varnothing$ pro libovolné $i \in N$ a $\set{\epsilon}^{i}=\set{\epsilon}$ pro libovolné $j \in N_{0}$
	- **Iterace jazyka $L$** je jazyk $L^{*}=\cup_{i=0}^{\infty} L^{i}$
	- **Pozitivní iterace jazyka $L$** je taky $L^{+}=\cup_{i=0}^{\infty} L^{i}$. Obecně není pravda, že $L^{+}=L^{*} \backslash \set{\epsilon}$
		- tato rovnost platí právě tehdy, když $L$ neobsahuje $\epsilon$
	- **Doplněk jazyka $L$** je jazyk co-L = $\Sigma^{*} \backslash L$
	- **Zrcadlovým obrazem** (též reverzí) **slova $x = a_{1},...,a_{n}$** nazýváme slovo $\omega^{R}=a_{n},...,a_{1}$. **Zrcadlový obraz jazyka $L$** definujeme jako $L^{R}=\set{\omega^{R}| \omega^{L}}$
	- **Substituce $f$** je zobrazení abecedy $\Sigma$ do podmnožiny $\Delta^{*}$
		- tj. přiřazuje každému $a \in \Sigma$ jazyk $f(a) \subseteq \Delta^{*}$. 
		- Zobrazení $f$ je rozšířeno na slova takto:
			- $f(\epsilon) = \epsilon$
			- $f(xa) = f(x).f(a)$
		 $f$ **rozšíříme na jazyk** tak, že pro každé $L \subseteq \Sigma^{*}$ klademe $f(L)=\cup_{x \in L} f(x)$.
	- Speciálním případem substituce je **homomorfismus $h$**, který definujeme jako substituci, u níž $h(a)$ obsahuje jediné slovo pro každé $a \in \Sigma$.
	- Je-li $h$ homomorfismus, pak definujeme **inverzní homomorfní obraz jazyka $L$** jako $h^{-1}(L)=\set{x|h(x) \in L}$ a **pro slova** definujeme inverzní homomorfismus jako $h^{-1}(w)=\set{x|h(x)=w}$.

## Konečná reprezentace jazyka
- Konečná reprezentace by měla být opět řetězcem symbolů (nad jistou abecedou), který budeme vhodně interpretovat tak, aby danému jazyku odpovídala nějaká, ne nutně jediná, konkrétní konečná reprezentace. Obráceně pak, aby každé konkrétní konečné reprezentaci odpovídal jediný konkrétní jazyk.
- Takovými reprezentacemi pro nás budou zejména tzv. gramatiky a automaty

### Gramatika
- **Gramatika $G$** je uspořádaná čtveřice $G=(N, \Sigma, P, S)$, kde:
	1. $N$ je neprázdná konečná množina neterminálních symbolů
	2. $\Sigma$ je konečná množina terminálních symbolů
		- platí $\Sigma \cap N = \varnothing$
		- Sjednocení $N$ a $\Sigma$ obdržíme množinu všech symbolů gramatiky, kterou obvykle označujeme symbolem $V$
	3. $P$ je konečná množina pravidel ve tvaru $P \subseteq V^{*}NV^{*} \times V^{*}$.
		- Pravidlo $(\alpha, \beta)$ obvykle zapisujeme ve tvaru $\alpha \rightarrow \beta$
	4. $S \in N$ je počáteční neterminál

- Podmínka kladená na tvar pravidel $\alpha \rightarrow \beta$ pouze požaduje, aby $a$ (levá strana pravidla) obsahovala **alespoň jeden** neterminál, na $\beta$ (pravou stranu pravidla) nejsou obecně kladeny žádné požadavky - speciálně, může být i prázdným slovem $\epsilon$
- **Relaci přímého obvození $\gamma \Rightarrow_{G} \sigma$** chápeme jako aplikaci konkrétního pravidla na řetězec $\gamma = \eta \alpha \rho$, jehož výsledkem je řetězec $\eta \beta \rho$, neboli: $\eta \alpha \rho \Rightarrow_{G} \eta \beta \rho$, kde $\eta, \rho \in V^{*}$ a $\alpha \rightarrow \beta$ je **právě aplikované pravidlo gramatiky $G$** 
	- (pokud je gramatika zřejmá z kontextu, pak můžeme označení $G$ u šipky vynechat)
- $\Rightarrow_{G}^{*}$ umožňuje při odvození aplikovat libovolný počet libovolných pravidel
- **Derivace** = proces, kdy na řetězec aplikujeme konečný počet kroků odvození
- $\Rightarrow_{lm}$ značí nejlevější derivaci - přepisujeme vždy podle nejlevějšího neterminálu 
	- analogicky $\Rightarrow_{rm}$ je nejpravější derivace
- Jazyk, který gramatika $G$ generuje, definujeme jako $L(G) = \set{w \in \Sigma^{*}| S \Rightarrow_{G}^{*}w}$
	- (řetězce v jazyce $G$ už neobsahují neterminály)

>[!Example] Příklad
>- Nechť $G = (\set{S,A,B}, \set{a,b}, P, S)$, kde 
>  $P = \{ S \rightarrow ABS,$
>  $\ \ \ \ \ \ \ \ \ \ S \rightarrow \epsilon,$
>  $\ \ \ \ \ \ \ \ \ \ AB \rightarrow BA,$
>  $\ \ \ \ \ \ \ \ \ \ BA \rightarrow AB,$
>  $\ \ \ \ \ \ \ \ \ \ A \rightarrow a,$
>  $\ \ \ \ \ \ \ \ \ \ B \rightarrow b \}$
>  - Pak např. $AaBAbBS$ je větná forma $G$, zatímco $ABb$ nikoliv.
>  - Jazyk $L(G)$ vypadá takto: $$L(G) = \set{u \in \set{a,b}^{*} | \#_{a}(u)=\#_{b}(u)}.$$

## Chromského hierarchie gramatik a jazyků
- Lingvista **Noam Chomsky** rozdělil gramatiky do čtyř skupin (typů) na základě různých omezení na tvar pravidel
- Jeho práce byla původně motivována úvahami o struktuře přirozeného jazyka, z dnešního pohledu má však především význam jako základní rozdělení gramatik podle jejich popisné síly.
- Chomského hierarchie rozlišuje **tyto čtyři (základní) typy gramatik:**

#### Typ 0
- Libovolná gramatika je gramatikou typu $0$
- Na tvar pravidel se nekladou žádné omezující požadavky
- Někdy se též taková gramatiky označují jako **gramatiky bez omezení či frázové gramatiky**

#### Typ 1
- Též **kontextová**, Context-Sensitive, CSG, méně často též *monoténní*
- Gramatika je typu $1$, jestliže pro každé její pravidlo $\alpha \rightarrow \beta$ platí $| \alpha | \leq | \beta |$ s eventuelní výjimkou pravidla $S \rightarrow \epsilon$, pokud se $S$ nevyskytuje na pravé straně žádného pravidla

#### Typ 2
- Též **bezkontextová**, Context-Free, CFG
- Gramatika je typu $2$, jestliže každé její pravidlo je tvaru $A \rightarrow \alpha$, kde $| \alpha | \geq 1$ s eventuelní výjimkou pravidla $S \rightarrow \epsilon$, pokud se $S$ nevyskytuje na pravé straně žádného pravidla

#### Typ 3
- Též **regulární**, pravolineární
- Gramatika je typu $3$, jestliže kažřdé její pravidlo je tvaru $A \rightarrow aB$ nebo $A \rightarrow a$ s eventuelní výjimkou pravidla $S \rightarrow \epsilon$, pokud se $S$ nevyskytuje na pravé straně žádného pravidla
---
- Hierarchie gramatik také určuje příslučnou hierarchii jazyků
- Z definice je patrné, že každý nový typ gramatiky v Chomského hierarchii je specifikován **zavedením dalších omezujících podmínek** na typ předchozí

>[!Example] Příklad
>- Každá regulární gramatika je také gramatikou bezkontextovou, kontextovou i typu $0$
>- Naopak to ovšem neplatí

>[!Info] Tvrzení
>- Nak abecedou $\set{a}$ existuje jazyk, který není typu $0$.
>- (Existuje nespočetně mnoho jazyků nad abecedou $\set{a}$, tedy je nelze vyjádřit konečnou reprezentací)

##### Navigace
Předchozí:  [[Geometrická interpretace určitého integrálu]]
Následující: [[Regulární jazyky (definice, uzávěrové vlastnosti)]]
Celý okruh: [[1. Teoretické základy informatiky]]