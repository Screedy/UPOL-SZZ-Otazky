### **Booleovské funkce**
- **Booleovská funkce s n argumenty** (n-ární booleovská funkce) je *libovolné zobrazení*, které *uspořádané n-tici hodnot 0 nebo 1 přiřadí hodnotu 0 nebo 1.*
- Každou booleovskou funkci f s n argumenty lze **zapsat v tabulce**
- Předpokládejme, že argumenty funkce f označíme $x_{1}, ..., x_{n}$, pak píšeme také $f(x_{1}, ..., x_{n})$

- Existuje právě $2^{2^{n}}$ booleovských funkcí s n argumenty

>[!Example] Všechny booleovské funkce jedné proměnné
>
>```js
>x₁| f₁  f₂  f₃  f₄ 
>------------------
> 0 | 0   0   1   1
> 1 | 0   1   0   1
> ```
> - Vidíme, že $f_{3}$ je pravdivostní funkce spojky negace, tj. $f_{3}(0)=1$ a $f_{3}(1)=0$.

>[!Example] Všechny booleovské funkce dvou proměnných
>```js
>x₁  x₂ | f₁  f₂  f₃  f₄  f₅  f₆  f₇  f₈  f₉  f₁₀ f₁₁ f₁₂ f₁₃ f₁₄ f₁₅ f₁₆
>--------------------------------------------------------------------------
>1   1  | 1   1   1   1   1   1   1   1   0    0   0   0   0   0   0   0                            
>1   0  | 1   1   1   1   0   0   0   0   1    1   1   1   0   0   0   0                           
>0   1  | 1   1   0   0   1   1   0   0   1    1   0   0   1   1   0   0                      
>0   0  | 1   0   1   0   1   0   1   0   1    0   1   0   1   0   1   0                             
>```
>
>- Vidíme, že 
>	- $f_{2}$ je pravdivostní funkce spojky disjunkce, 
>	- $f_{5}$ je pravidvostní funkce spojky implikace, 
>	- $f_{7}$ je pravdivostní funkce spojky ekvivalence, 
>	- $f_{8}$ je pravidovostní funkce spojky konjunkce.


### **Funkčně úplný systém**
- Množina booleovských funkcí $\{f_{1},\ ...\ ,f_{k}\}$ je **funkčně úplná**, pokud <u>každou</u> booleovskou funkci $f: \{0, 1\}^{n} \rightarrow \{0, 1\}$ lze **vyjádřit jako složení některých funkcí** z $\{f_{1},\ ...\ ,f_{k}\}$.
	- Jinými slovy, pokud máme **sadu logických operací**, a pomocí této sady můžeme **sestavit jakýkoli možný logický výraz**, je tato sada považována za **funkčně úplnou**.

- Řekneme, že **množina výrokových spojek je úplná** (tvoří úplný systém spojek), jestli je **funkčně úplná** množina jim odpovídajících booleovských funkcí.
- Každý úplný minimální systém spojek VL nazveme **bází**.

- Funkčně úplné množiny logických funkcí: $\{\neg,\land\}, \{\neg, \lor\}, \{\neg, \rightarrow\}, \{\uparrow\}, \{\downarrow\}$

  >[!Example] Důkaz
  >- Pomocí $\uparrow$ (resp. $\downarrow$) lze vyjádřit $\neg,\land, \lor$:
  >  Zřejmě $$(a \uparrow b) \leftrightarrow \neg(a \land b).$$
  >  Odsud:
  > 	 1. $\neg a \leftrightarrow \neg (a \land a) \leftrightarrow (a \uparrow a);$
  > 	 2. $(a \land b) \leftrightarrow \neg \neg (a \land b) \leftrightarrow \neg (a \uparrow b) \leftrightarrow ((a \uparrow b) \uparrow (a \uparrow b));$
  > 	 3. $(a \lor b) \leftrightarrow \neg \neg (a \lor b) \leftrightarrow \neg (\neg a \land \neg b) \leftrightarrow (\neg a \uparrow \neg b) \leftrightarrow ((a \uparrow a) \uparrow (b \uparrow b)).$
  > 
  > Podobně pro $\downarrow$.
  
  
##### Navigace
Předchozí: [[Výroková logika, formule, pravdivost, vyplývání]]
Následující: [[Úplné konjunktivní a disjunktivní normální formy]]
Celý okruh: [[Výroková logika, formule, pravdivost, vyplývání]]