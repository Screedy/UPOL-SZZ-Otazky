>[!info] Riceova věta
>- Každá netriviální vstupně/výstupní vlastnost programů je nerozhodnutelná.

- Upravit znění věty se dá např. takto:
	- Je-li $V$ netriviální vstupně/výstupní vlastností TS, pak je **nasledující problém nerozhodnutelný.**
	  
	  **Název**: Zjišťování vlastnosti $V$
	  **Vstup**: TS $M$
	  **Otázka**: Má $M$ vlastnost $V$?
- Věta mluví o **vstupně/výstupních vlastnostech** programů. Pro každý program $Pg$ si představme (obecně konečnou) **tabulku s dvěma sloupci:**
	- v prvním sloupci jsou všechny přípustně vstupy programu
	- v druhém sloupci je ke každému vstupu $w$ uveden příslušný výstup $Pg(w)$. 
		- V případě, že výpočet $Pg$ pro vstup $w$ je **konečný** jako výstup vydá $Pg(w)$, nebo znak $\vdash$ (nedefinováno) v případě, že výpočet $Pg$ na $w$ je **nekonečný**.

- Tabulka tedy zachycuje **\[částečné\] zobrazení vstupů na výstupu**, které $Pg$ realizuje; můžeme jí říkat $I/O$-tabulka ($I$=input, $O$=output).

- Každá vlastnost $V$ Turingových strojů **rozdělí množinu** všech TS **na dvě disjunktní podmnožiny**
	- množina strojů, která vlastnost $V$ **má**
	- množina strojů, která vlastnost $V$ **nemá**

- Vlastnost $V$ je **triviální**, jestliže je jedna z oněch dvou příslušných množin **prázdná** (tedy všechny stroje vlastnost $V$ mají nebo nemají)
- Vlastnost $V$ je **netriviální**, jestliže **ji alespoň jeden stroj má** a **alespoň jeden stroj nemá**

>[!info] Definice převeditelnosti
>- Mějme $ANO/NE$ problémy $P_{1}, P_{2}$. Řekneme, že problém $P_{1}$ **je algoritmicky převeditelný na problém $P_{2}$** ($P_{1} \leq_{m} P_{2}$), jestliže **existuje algoritmus $A$**, který pro libovolný vstup $w$ problému $P_{1}$ sestrojí vstup problému $P_{2}$, $A(w)$, přičemž platí, že odpověď na otázku problému $P_{1}$ pro vstup $w$ je $ANO$ **právě tehdy,** když odpověď na otázku problému $P_{2}$ pro vstup $A(w)$ je $ANO$.

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