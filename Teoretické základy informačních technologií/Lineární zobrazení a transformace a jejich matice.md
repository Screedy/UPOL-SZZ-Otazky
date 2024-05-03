### Lineární zobrazení - definice:
Nechť $\mathcal{V}=(V,+, \mathcal{T},\, \cdot\,)$ a $\mathcal{V}^{\prime}=\left(V^{\prime},+, \mathcal{T}, \, \cdot \,\right)$ jsou vektorové prostory nad číselným tělesem $\mathcal{T}$. Potom zobrazení $f: V \rightarrow V^{\prime}$ nazveme homomorfizmus vektorového prostoru $\mathcal{V}$ do vektorového prostoru $\mathcal{V}^{\prime}$, jestliže
1. $\forall \vec{u}, \vec{v} \in V ; f(\vec{u}+\vec{v})=f(\vec{u})+f(\vec{v})$,
2. $\forall c \in T, \vec{u} \in V ; f(c \vec{u})=c f(\vec{u})$.
##### Definice $9.2$
- **Bijektivní homomorfizmus** $\mathcal{V}$ na $\mathcal{V}^{\prime}$ se nazývá izomorfizmus $\mathcal{V}$ na $\mathcal{V}^{\prime}$.
- Řekneme, že vektorový prostor $\mathcal{V}^{\prime}$ je izomorfní $s$ vektorovým prostorem $\mathcal{V}$, existuje-li alespoň jeden izomorfizmus $\mathcal{V}$ na $\mathcal{V}^{\prime}$.


Definice 9.3 
Je-li $f$ homomorfizmus vektorového prostoru $\mathcal{V}$ do vektorového prostoru $\mathcal{V}^{\prime}$, pak jádrem homomorfizmu $f$ nazýváme množinu $\operatorname{Ker} f=\left\{\vec{u} \in V ; f(\vec{u})=\vec{o}^{\prime}\right\}$. 
(Symbol $\vec{o}^{\prime}$ označuje nulový vektor ve $\mathcal{V}^{\prime}$.)

*Obrazem homomorfizmu $f$ rozumíme množinu $\operatorname{Im} f=\{f(\vec{u}) ; \vec{u} \in V\}$.*

Věta $9.1$ 
Je-li f homomorfizmus $\mathcal{V}$ do $\mathcal{V}^{\prime}$, pak
- $f$ je injektivní, právě když $\operatorname{Ker} f=\{\vec{o}\}$;
- $f$ je surjektivní, právě když $\operatorname{Im} f=\mathcal{V}^{\prime}$;
- $f$ je izomorfizmus, právě když $\operatorname{Ker} f=\{\vec{o}\}$ a $\operatorname{Im} f=\mathcal{V}^{\prime}$.

Vĕta $9.2$ 
Nechť $\mathcal{V}, \mathcal{V}^{\prime}, \mathcal{V}^{\prime \prime}$ jsou vektorové prostory nad $\mathcal{T}, f$ homomorfizmus $\mathcal{V}$ do $\mathcal{V}^{\prime}, g$ homomorfizmus $\mathcal{V}^{\prime}$ do $\mathcal{V}^{\prime \prime}$. Potom složené zobrazení $f \circ g: V \rightarrow V^{\prime \prime}(t j . \forall \vec{u} \in$ $V ;(f \circ g)(\vec{u})=g(f(\vec{u})))$ je homomorfizmus $\mathcal{V}$ do $\mathcal{V}^{\prime \prime}$.

Věta 9.3 
Je-li $f$ izomorfizmus $\mathcal{V}$ na $\mathcal{V}^{\prime}$ pak zobrazení $f^{-1}: V^{\prime} \rightarrow V$ je izomorfizmem $\mathcal{V}^{\prime}$ na $\mathcal{V}$

Věta 9.4 
Jsou-li $\mathcal{V}$ a $\mathcal{V}^{\prime}$ vektorové prostory nad $\mathcal{T}$, je-li $f$ izomorfizmus $\mathcal{V}$ na $\mathcal{V}^{\prime}$ a je-li $\left\{\vec{u_1}, \ldots, \vec{u_n}\right\}$ báze prostoru $\mathcal{V}$, pak množina $\left\{f\left(\vec{u_1}\right), \ldots, f\left(\vec{u_n}\right)\right\}$ je bází prostoru $\mathcal{V}^{\prime}$.

---
Příklad 9.1 
Uvažujme zobrazení $f: \mathcal{R}^2 \rightarrow \mathcal{R}^2$ takové, že pro každý vektor $\left(x_1, x_2\right) \in$ $\mathcal{R}^2$ platí $f\left(\left(x_1, x_2\right)\right)=\left(2 x_1+x_2, x_1+x_2\right)$

Pro libovolné $\left(x_1, x_2\right),\left(y_1, y_2\right) \in \mathcal{R}^2$ a $c \in \mathcal{R}$ platí $f\left(\left(x_1, x_2\right)+\left(y_1, y_2\right)\right)=f\left(\left(x_1+\right.\right.\left.\left.y_2\right),\left(x_1+x_2\right)+\left(y_1+y_2\right)\right)=\left(2 x_1+x_2, x_1+x_2\right)+\left(2 y_1+y_2, y_1+y_2\right)=$$=f\left(\left(x_1, x_2\right)\right)+f\left(\left(y_1 y_2\right)\right) f\left(c\left(x_1, x_2\right)\right)=f\left(\left(c x_1, c x_2\right)\right)=\left(2 c x_1+c x_2, c x_1+c x_2\right)=c\left(2 x_1+x_2, x_1+x_2\right)=c f\left(\left(x_1, x_2\right)\right)$ tedy $f$ je homomorfizmus $\mathcal{R}^2$ do $\mathcal{R}^2$.

Nechť $\left(x_1, x_2\right) \in \mathcal{R}^2$ je takový vektor, že $f\left(\left(x_1, x_2\right)\right)=\vec{o}$, tj. platí
$$
2 x_1+x_2=0, \quad x_1+x_2=0
$$
Potom $x_1=x_2=0$, tedy $\left(x_1, x_2\right)=\vec{o}$, a to znamená, že Ker $f=\{\vec{o}\}$, neboli že $f$ je injektivní.

Ukážeme ještě, že pro každý vektor $\left(y_1, y_2\right) \in \mathcal{R}^2$ existuje $\left(x_1, x_2\right) \in \mathcal{R}^2$, který je jeho vzorem v homomorfizmu $f$. Pro takový $\left(x_1, x_2\right)$ musí platit $f\left(\left(x_1, x_2\right)\right)=\left(y_1, y_2\right)$, tedy
$$
y_1=2 x_1+x_2, \quad y_2=x_1+x_2 .
$$
Odtud dostáváme
$$
x_1=y_1-y_2, \quad x_2=2 y_2-y_1,
$$
a snadno se přesvědčíme, že opravdu platí $\left(y_1, y_2\right)=f\left(y_1-y_2, 2 y_2-y_1\right)$. Homomorfizmus je tedy surjektivní.
Celkově proto dostáváme, že $f$ je izomorfizmem $\mathcal{R}^2$ na $\mathcal{R}^2$.

---

Příklad $9.2$ 
Označme $g$ zobrazení $\mathcal{R}^3$ do $\mathcal{R}^4$ takové, že pro každý vektor $\left(x_1, x_2, x_3\right) \in$ $\mathcal{R}^3$ platí $g\left(\left(x_1, x_2, x_3\right)\right)=\left(x_1, x_1, x_2, x_3\right)$.
Podobně jako v př́́kladu $9.1$ snadno dokážeme, že $g$ je homomorfizmus $\mathcal{R}^3$ do $\mathcal{R}^4$.
Jestliže pro $\left(x_1, x_2, x_3\right) \in \mathcal{R}^3$ platí $g\left(\left(x_1, x_2, x_3\right)\right)=\vec{o}$, pak $x_1=x_2=x_3=0$, tedy $\left(x_1, x_2, x_3\right)=\vec{o}$. To znamená, že Ker $f=\{\vec{o}\}$, neboli že $g$ je injektivní.

Dále platí, že $\operatorname{Im} g=\left\{\left(x_1, x_1, x_2, x_3\right) ;\left(x_1, x_2, x_3\right) \in \mathcal{R}^3\right\}$, tedy $\operatorname{Im} g$ je vlastní podmnožinou $\mathcal{R}^4$. Proto $g$ není surjektivní, což znamená, že není ani izomorfizmus.

Příklad 9.3 
Uvažujme zobrazení $h: \mathcal{R}^2 \rightarrow \mathcal{R}$ takové, že $h\left(\left(x_1, x_2\right)\right)=\left(x_1+x_2\right)$.
Přímým výpočtem můžeme ověřit, že $h$ je homomorfizmus $\mathcal{R}^2$ do $\mathcal{R}$.
Jestliže pro $\left(x_1, x_2\right) \in \mathcal{R}^2$ platí $h\left(\left(x_1, x_2\right)\right)=\vec{o}$, pak $x_1+x_2=0$, neboli Ker $h=$ $\left\{\left(x_1, x_2\right) \in \mathcal{R}^2 ; x_1=-x_2\right\}$, a tedy $h$ není injektivní, proto není ani izomorfizmem.
Homomorfizmus $h$ je ale surjektivní, protože pro každý $x \in \mathcal{R}$ platí $(x)=h((x, 0))$.

---


##### Navigace
Předchozí:  [[Soustavy lineárních rovnic, Frobeniova věta, Gaussova eliminační metoda, Cramerovo pravidlo]]
Následující: [[Funkce jedné reální proměnné, základní vlastnosti]]
Celý okruh: [[1. Teoretické základy informačních technologií]]