- *(Mluví se zde o rozhodnutelných jazycích, protože jsou ve spojitosti s algoritmy, rekurzivní jazyk je to samé, ale se spojitosti s TS)*

## Částečně rozhodnutelný problém
- $ANO/NE$ problém $P$ je částečně rozhodnutelný, jestliže **existuje** algoritmus $A$, který pro každý vstup problému $P$:
	1) pokud je odpověď $ANO$, skončí a vydá odpověď $ANO$
	2) nebo pokud je odpověď $NE$, buď skončí s odpovědí $NE$ nebo je jeho běh nekonečný.
- Říkáme také, že algoritmus $A$ částečně rozhoduje problém $P$.

## Rozhodnutelný problém
- $ANO/NE$ problém $P$ je rozhodnutelný, jestliže **existuje** algoritmus $A$, který pro každý vstup problému $P$:
	1) pokud je odpověď $ANO$, skončí a vydá odpověď $ANO$
	2) nebo pokud je odpověď $NE$, skončí a vydá odpověď $NE$.
- Říkáme také, že algoritmus $A$ rozhoduje problém $P$.
- Rozhodnutelné problémy jsou podmnožinou částečně rozhodnutelných.

#### Doplňkový problém
- **Doplňkový problém** k $ANO/NE$ problému $P$ (označovaný $co-P$) je problém, který má stejné vstupy jako $P$, ale výstupy $ANO$, $NE$ jsou **prohozeny**.

>[!tip] Tvrzení
>Je-li problém $P$ rozhodnutelný, je i co-$P$ rozhodnutelný.

>[!info] Postova věta
>$ANO/NE$ problém $P$ je **rozhodnutelný** právě tehdy, když $P$ i co-$P$ **jsou částečně rozhodnutelné**.

>[!example] Důkaz Postovy věta
>- Hlavní myšlenka spočívá v tom, že ke dvěma algoritmům lze zkonstruovat algoritmus, který výpočty obou provádí "paralelně". Když takto "současně spustíme" algoritmus $A_{1}$, který částečně rozhoduje $P$, a algoritmus $A_{2}$, který částečně rozhoduje co-$P$, zaručeně dojde k situaci, kdy jeden z algoritmů skončí; když skončí $A_{1}$ s odpovědí $ANO$ (nebo $A_{2}$ s odpovědí $NE$), konbinovaný algoritmus skončí s odpovědí $ANO$, když skončí $A_{2}$ s odpovědí $ANO$ (nebo $A_{1}$ s odpovědí $NE$), kombinovaný algoritmus skončí s odpovědí $NE$.
>- Když je $P$ rozhodnutelný, pak je i co-$P$ rozhodnutelný; pak ovšem $P$ i co-$P$ jsou částečně rozhodnutelné.

##### Navigace
Předchozí:  [[Částečně rekurzivní a rekurzivní jazyky, jazyky a rozhodovací problémy]]
Následující: [[Uzávěrové vlastnosti jazyků TS]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]