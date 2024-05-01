### **Booleovské funkce**
- **Booleovská funkce s n argumenty** (n-ární booleovská funkce) je *libovolné zobrazení*, které *uspořádané n-tici hodnot 0 nebo 1 přiřadí hodnotu 0 nebo 1.*
- Každou booleovskou funkci f s n argumenty lze **zapsat v tabulce**
- Předpokládejme, že argumenty funkce f označíme $x_{1}, ..., x_{n}$, pak píšeme také $f(x_{1}, ..., x_{n})$

- Existuje právě $2^{2^{n}}$ booleovských funkcí s n argumenty
![[MacBook-2024-02-28-000757@2x.png | 500]]
![[MacBook-2024-02-28-000758@2x.png | 500]]

### **Funkčně úplný systém**
- Množina booleovských funkcí $\{f_{1},\ ...\ ,f_{k}\}$ je **funkčně úplná**, pokud <u>každou</u> booleovskou funkci $f: \{0, 1\}^{n} \rightarrow \{0, 1\}$ lze **vyjádřit jako složení některých funkcí** z $\{f_{1},\ ...\ ,f_{k}\}$.
	- Jinými slovy, pokud máme **sadu logických operací**, a pomocí této sady můžeme **sestavit jakýkoli možný logický výraz**, je tato sada považována za **funkčně úplnou**.

- Řekneme, že **množina výrokových spojek je úplná** (tvoří úplný systém spojek), jestli je **funkčně úplná** množina jim odpovídajících booleovských funkcí.
- Každý úplný minimální systém spojek VL nazveme **bází**.

- Funkčně úplné množiny logických funkcí: $\{\neg,\land\}, \{\neg, \lor\}, \{\neg, \rightarrow\}, \{\uparrow\}, \{\downarrow\}$
  ![[MacBook-2024-02-28-000759@2x.png | 650]]
##### Navigace
Předchozí: [[Výroková logika, formule, pravdivost, vyplývání]]
Následující: [[Úplné konjunktivní a disjunktivní normální formy]]
Celý okruh: [[Výroková logika, formule, pravdivost, vyplývání]]