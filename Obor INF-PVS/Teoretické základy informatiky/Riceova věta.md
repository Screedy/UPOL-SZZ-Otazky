>[!info] Riceova věta
>- Každá netriviální vstupně/výstupní vlastnost programů je nerozhodnutelná.

- Upravit znění věty se dá např. takto: "Je-li $V$ netriviální vstupně/výstupní vlastností TS, pak je **nasledující problém nerozhodnutelný.**"
- Definice problému: 
	- **Název**: Zjišťování vlastnosti $V$
	 - **Vstup**: TS $M$
	 - **Otázka**: Má $M$ vlastnost $V$?
- Věta mluví o **vstupně/výstupních vlastnostech** programů, co to je?
## Vstupně/výstupní vlastnost (I/O vlastnost)
-  Pro každý program $Pg$ si představme (obecně konečnou) **tabulku s dvěma sloupci:**
	1) v prvním sloupci jsou všechny přípustně vstupy programu
	2) druhém sloupci je ke každému vstupu $w$ uveden příslušný výstup $Pg(w)$. 
		- V případě, že výpočet $Pg$ pro vstup $w$ je **konečný** jako výstup vydá $Pg(w)$, nebo znak $\vdash$ (nedefinováno) v případě, že výpočet $Pg$ na $w$ je **nekonečný**.
- Mají-li 2 TS stejnou I/O tabulku, pak oba musí onu vlastnost mít nebo oba nemít
## Triviální a netriviální vlastnosti
- Každá vlastnost $V$ TS rozdělí množinu všech TS **na dvě disjunktní podmnožiny**
	1) množina strojů, která vlastnost $V$ **má**
	2) množina strojů, která vlastnost $V$ **nemá**
- **Triviální vlastnosti $V$** ... alespoň jedna z oněch dvou množin je **prázdná** (všechny TS vlastnost $V$ mají nebo nemají)
- **Netriviální vlastnosti $V$** ... alespoň jeden stroj ji nemá a jeden má (množiny nejsou prázdné)
## Algoritmická převoditelnost
- Jde o relace $\leq_m$ (tzv. mapping reduction)
- Vztahuje se pouze na $ANO/NE$ problémy
- Řekneme, že problém $P_{1}$ **je algoritmicky převeditelný na problém $P_{2}$** ($P_{1} \leq_{m} P_{2}$), jestliže **existuje algoritmus $A$**, který pro libovolný vstup $w$ problému $P_{1}$ sestrojí vstup problému $P_{2}$, $A(w)$, přičemž platí, že odpověď na otázku problému $P_{1}$ pro vstup $w$ je $ANO$ **právě tehdy,** když odpověď na otázku problému $P_{2}$ pro vstup $A(w)$ je $ANO$.
- Matematicky: Existuje vyčíslitelná funkce $f:\Sigma^* \rightarrow \Sigma^*$ taková, že $\forall w \in \Sigma^*  : w \in L_1 \Leftrightarrow f(w) \in L_2$.
- Ke každému $ANO/NE$ problému náleží jazyk, takže $P_1 \leq_m P_2$ můžeme chápat jako $L_1 \leq_m L_2$

>[!Example] Důkaz Riceovy věty
>- Uvažujme libovolnou netriviální vstupně/výstupní vlastnost $V$ Turingový stroj. Nechť stroj $M_{1}$, který se **nezastaví na žádný vstup**, vlastnost $V$ nemá, a nechť stroj $M_{2}$ vlastnost $V$ má, nebo naopak. Takové dva stroje $M_{1}$ a $M_{2}$ **nutně musí existovat**.
>- Uvažme nyní instanci $M$, $w$ problému zastavení. Sestrojíme k ní stroj $M'$, který se chová takto: vstup $u$ nejprve ignoruje a simuluje stroj $M$ na $w$ (slovo $w$ má stroj $M'$ uloženo ve svém počátečním stavu). Pokud se tato **simulace zastaví**, tak $M'$ smaže vše zbylé po této simulaci a **pokračuje simulací stroje $M_{2}$ na vstupu $u$**.
>- Vidíme, že platí: pokud se $M$ zastaví na $w$, tak $M'$ **má stejně $I/O$ chování** (stejnou $I/O$ tabulku) **jako $M_{2}$**. Pokud se $M$ nezastaví na $w$, tak $M'$ **má stejné $I/O$ chování jako $M_{1}$**. Kdyby tedy vlastnost $V$ **byla rozhodnutelná**, byl by **rozhodnutelný i problém zastavení**
>	- (Kdyby byla, byť jen částečně rozhodnutelná, pak by HP i co-HP bylo částečně rozhodnutelné. Z čehož by vyplývalo, že HP je rozhodnutelné. Což je spor. Proto musí být vlastnost $V$ nerozhodnutelná.)
>- Ukázali jsme vlastně, že $HP \leq_{m} PV$ nebo $HP \leq_{m} \text{ co-}PV$ - o který z těchto případů se jedná, je určeno tím, žda stroj $M_{1}$ (který se nezastaví na žádný vstup) vlastnost $V$ nemá či má.

##### Navigace
Předchozí:  [[Uzávěrové vlastnosti jazyků TS]]
Následující: [[Složitost algoritmu (časová a paměťová)]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]