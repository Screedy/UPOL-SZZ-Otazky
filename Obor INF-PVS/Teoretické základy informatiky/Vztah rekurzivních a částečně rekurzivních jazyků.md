- (Mluví se zde o rozhodnutelných jazycích, protože jsou ve spojitosti s algoritmy, rekurzivní jazyk je to samé, ale se spojitosti s TS)

>[!info] Částečně rozhodnutelný
>- $ANO/NE$ problém $P$ je částečně rozhodnutelný, jestliže **existuje** algoritmus $A$, který pro každý vstup problému $P$, na něž je odpověď $ANO$, skončí a vydá odpověď $ANO$ a pro každý vstup problému $P$, na něž je odpověď $NE$, buď skončí s odpovědí $NE$ nebo **je jeho běh nekonečný**.
>- Říkáme také, že algoritmus $A$ částečně rozhoduje problém $P$.

>[!info] Rozhodnutelný
>- $ANO/NE$ problém $P$ je rozhodnutelný, jestliže **existuje** algoritmus $A$, který pro každý vstup problému $P$, na něž je odpověď $ANO$, skončí a vydá odpověď $ANO$ a pro každý vstup problému $P$, na něž je odpověď $NE$, skončí a vydá odpověď $NE$.
>- Říkáme také, že algoritmus $A$ rozhoduje problém $P$.

- Mějme $ANO/NE$ problém $P$. **Doplňkový problém k problému $P$**, označovaný co-$P$, je problém, který má stejné vstupy jako $P$, ale výstupy $ANO$, $NE$ jsou **prohozeny**.
	- (kde má $P$ odpověď $ANO$, má $P$ odpověď $NE$, a naopak)

- **Tvrzení:** Je-li problém $P$ rozhodnutelný, je i co-$P$ rozhodnutelný.
- **Postova věta:** $ANO/NE$ problém $P$ je **rozhodnutelný** právě tehdy, když $P$ i co-$P$ **jsou částečně rozhodnutelné**.
>[!example] Důkaz
>- ($P$ je rozhodnutelný $\Rightarrow$ $P$ i co-$P$ jsou částečně rozhodnutelné) Když je $P$ rozhodnutelný, pak je i co-$P$ rozhodnutelný; pak ovšem $P$ i co-$P$ jsou částečně rozhodnutelné
>- ($P$ i co-$P$ jsou částečně rozhodnutelné $\Rightarrow P$ je rozhodnutelný) Hlavní myšlenka spočívá v tom, že ke dvěma algoritmům lze zkonstruovat algoritmus, který výpočty obou provádí "paralelně". Když takto "současně spustíme" algoritmus $A_{1}$, který částečně rozhoduje $P$, a algoritmus $A_{2}$, který částečně rozhoduje co-$P$, zaručeně dojde k situaci, kdy jeden z algoritmů skončí; když skončí $A_{1}$ s odpovědí $ANO$ (nebo $A_{2}$ s odpovědí $NE$), konbinovaný algoritmus skončí s odpovědí $ANO$, když skončí $A_{2}$ s odpovědí $ANO$ (nebo $A_{1}$ s odpovědí $NE$), kombinovaný algoritmus skončí s odpovědí $NE$.

##### Navigace
Předchozí:  [[Částečně rekurzivní a rekurzivní jazyky, jazyky a rozhodovací problémy]]
Následující: [[Uzávěrové vlastnosti jazyků TS]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]