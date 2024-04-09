- Nechť V je množina výrokových symbolů, pak:
	- **literál** nad V = libovolný výrokový symbol z V nebo jeho negace
	- **úplná elementární konjunkce** nad V = libovolná konjunkce literálů, ve které se každý výrokový symbol z V vyskytuje právě v jednom literélu
	- **úplná elementární disjunkce** nad V = libilná disjunkce literélů, ve které se každý výrokový symbol z V vysksytuje právě v jednom literélu
	- **úplná konjunktivní normální forma** nad V = je *konjunkce úplných elementárních disjunkcí*
	- **úplná disjunktivní normální forma** nad V = je *disjunkce úplných elementárních konjunkcí*

	- **ÚDNF** se **nedá vytvořit** pokud se jedná o **kontradikci** a **ÚKNF** se **nedá vytvořit** pokud se jedná o **tautologii**

### Vytvoření ÚDNF
- Pro každý řádek tabulky odpovídající ohodnocení $e$, při kterém má funkce $f$ hodnotu **1** sestrojíme **ÚEK**, tak že
	- $p_{i}$ pro $e(p_{i})=1$
	- $\neg p_{i}$ pro $e(p_{i})=0$
- Výsledná ÚDNF je disjunkcí ÚEK z předchozího kroku

### Vytvoření ÚKNF
- Pro každý řádek tabulky odpovídající ohodnocení $e$, při kterém má funkce $f$ hodnotu 0 sestrojíme **ÚED**, tak že
	- $p_{i}$ pro $e(p_{i})=0$
	- $\neg p_{i}$ pro $e(p_{i})=1$
- Výsledná ÚKNF je konjunkcí ÚED z předchozího kroku
![[MacBook-2024-02-28-000760@2x.png | 500]]

##### Navigace
Předchozí: [[Booleovské funkce, funkčně úplné systémy]]
Následující: [[Množiny, množinové operace, potenční množina, kartézský součin, číselné množiny, spočetné a nespočetné množiny]]
Celý okruh: [[Výroková logika, formule, pravdivost, vyplývání]]