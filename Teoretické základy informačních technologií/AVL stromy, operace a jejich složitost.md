- Motivate: udržovat výšku s $n$ prvky omezenou na $O(\lg n)$ tak, aby složitost operací *(závislá lineárně na výšce stromu)* zůstala $O(\lg n)$. Jeden z přístupů vymysleli G. M. Adelson-Velskij a J. M. Landis v roce 1962 $\rightarrow$ **AVL stromy**

- Hlavní idea: 
	- Definujeme **vyváženost uzlu $u$** jako rozdíl výšky levého podstro u a výšky pravého podstromu tohoto uzlu. 
	- Strom je **přípustný (vyvážený)** pokud pro **každý uzel** $u$ ve stromu platí, že jeho vyváženost je $0, 1,$ nebo $-1$. 
	- Výšku **prázdného podstromu** definujeme rovnu $-1$.

- Věta: 
	- Výška přípustného stromu je **seshora omezena** $\frac{3}{2} \lg (n+1)$.
  Intuice důvodu: 
	  Pokusíme se namalovat přípustný strom, který má výšku $1, 2, ...,$ tak, aby obsahoval co nejméně uzlů 
	  tím bude funkce popisující výšku stromu v závislosti na počtu uzlů "nejvíce rostoucí" a najdeme tak vztak k Fibonacciho posloupnosti.
  $f(h) = f(h-1) - f(h-2) + 1$
  $f(0) = 1$
  $f(1) = 2$

<iframe width="690" height="385" src="https://www.youtube.com/embed/DB1HFCEdLxA?si=R0IPA6zVt48l5f0k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Operace s AVL stromy
- Operace `insert` a `delete` děláme jako u **binárního vyhledávacího stromu**. Problém ovšem je, že **tyto operace mohou strom učinit nepřípustným**![[MacBook-2024-03-12-000859@2x.png]]
- Pozorujeme, že přidáním nebo odebráním uzlu můžeme změnit vyváženost **pouze uzlů na cestě** od přidaného/smazaného uzlu **ke kořeni**. Je to proto, že pro ostatní uzly se výška jejich podstromu **nezmění**.
- **Drobnost k implementaci:** 
	- Do uzlu přidáme položku `bf`, ve které budeme udržovat vyváženost uzlu. 
	- Po změně ve stromu procházíme strom směrem od místa změny ke kořeni. 
	- Změní-li se výška některého podstromu uzlu, upravíme položku `bf` v tomto uzlu.
```C
struct node {
  left, //levy potomek
  right, //pravy potomek
  parent, //rodic
  key, //klic
  bf
  …
}
```
```C
struct tree {
  root, // koren
  …
}
```
- Je-li po změně `bf` rovno $2$ nebo $-2$, **musíme provést některou z rotací**
- Procházení můžeme ukončit, pokud se výška podstromu s kořenem $u$ nezmění. Pak se totiž nezmění výšky podstromu žádného z předků uzlu $u$, a tím se nezmění ani jejich položky `bf`
<iframe width="690" height="385" src="https://www.youtube.com/embed/JPI-DPizQYk?si=iRNlQAPzmjWLrA6p" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Rotace
- $x.\text{bf} == 2 \rightarrow y$ existuje
- Možnosti: $y.\text{bf} \in \{1, 0, -1\}$
- Značení:
	- $h(A)$ ... výška podstromu $A$
	- $h(x)$ ... výška podstromu s kořenem $x$
	- $\rightarrow$ ... odvodím

##### 1. případ - Pravá (Levá) rotace
- $A$ je o jedna větší než $B$ a $C$
  $y.\text{bf} == 1 \rightarrow \ \ \ h(A) = h(B) + 1$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(y) = h(A) + 1$
  $x.\text{bf} == 2 \rightarrow \ \ h(y) = h(C) + 2$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(A) = h(C) + 1$
  
  $h(x) = h(y) + 1 = h(A) + 2$

- Po rotaci: $h(y) = h(A) + 1$
  ![[MacBook-2024-03-12-000860@2x.png | 400]]
##### 2. případ - Pravá (Levá rotace)
- $C$ je o jedna menší než $A$ a $B$
  $y.\text{bf} == 0 \rightarrow \ \ \ h(A) = h(B)$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(y) = h(A) + 1$
  $x.\text{bf} == 2 \rightarrow \ \ h(y) = h(C) + 2$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(A) = h(C) + 1$
  
  $h(x) = h(y) + 1 = h(A) + 2$

- Po rotaci: $h(y) = h(A) + 2 = h(B) + 2$
  ![[MacBook-2024-03-12-000861@2x.png | 400]]

##### 3. případ
- $B$ je o jedna větší než $A$ a $C$
  $y.\text{bf} == -1 \rightarrow \ \ \ h(B) = h(A)+1$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(y) = h(B) + 1$
  $x.\text{bf} == 2 \rightarrow \ \ h(y) = h(C) + 2$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(B) = h(C) + 1$
  
  $h(x) = h(y) + 1 = h(B) + 2$

- Nemůžeme použít pravou rotaci, protože po přepojení je $B$ o dva větší než $A$.![[MacBook-2024-03-13-000868@2x.png | 500]]
- $x. \text{bf} == 2 \rightarrow$ $y$ existuje
  $y. \text{bf} == -1 \rightarrow$ $z$ existuje
  
  $z.\text{bf} == 1 \rightarrow \ \ \ h(B) = h(C)+1$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(z) = h(B) + 1$
  $y.\text{bf} == -1 \rightarrow \ \ h(z) = h(A) + 1$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(A) = h(B)$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(y) = h(B) + 2$
  $x.\text{bf} == 2 \rightarrow \ \ h(y) = h(D) + 2$
  $\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ h(B) = h(D)$

- $C$ je o jedna menší než $A, B$ a $D$
- Po rotaci: $h(z) = h(B) + 2$
  ![[MacBook-2024-03-13-000869@2x.png | 500]]

### Rotace přehled
#### Jednoduché rotace (pravá a levá)
![[MacBook-2024-03-13-000870@2x.png]]

#### Dvojitá rotace (levo pravá)
![[MacBook-2024-03-13-000871@2x.png]]

### Dvojitá rotace (pravo levá)
![[MacBook-2024-03-13-000872@2x.png]]


### Přidání - $O(\lg n)$
- Provedeme vkládání jako v binárním vyhledávacím stromě. 
- Poté jdeme po cestě od rodiče přidaního uzlu do kořene a upravujeme položky $\text{bf}$. ($u$ je aktuální uzel, u kterého jsme provedli úpravu $b$)

1. Pokud je po úpravě $u.\text{bf}$ rovno $0$, algoritmus přidání končí
2. Pokud je po úpravě $u.\text{bf}$ rovno $-2$ nebo $2$, vybereme správnou rotaci, provedeme ji a algoritmus končí 
	- Můžeme algoritmus ukončit protože jsme museli použít rotaci, která sníží výšku stromu, který měl před rotací kořen $u$. 
	- Přidáním uzlu jsme ovšem předtím výšku stromu s kořenem $u$ zvýšili o 1, rotací jsme ji pak snížili o 1, má tedy stejnou výšku jako před přidáním
3. Pokud je po úpravě $u.\text{bf}$ rovno $-1$ nebo $1$, zvýšili jsme výšku podstromu a musíme tedy pokračovat s úpravou položky $\text{bf}$ u rodiče uzlu $u$.
```C
proc avl-insert(T, x)
  tree-insert(T, x)
  z = x;
  u = x.p;
  while u != nil
    // updatujeme bf
    if z == u.left then u.bf += 1
    if z == u.right then u.bf -= 1
  
    if u.bf == 0 then return // tady muzeme skoncit

    if u.bf == -2 or u.bf == 2 //sníží výšku stromu
      // vyber a proved správnou rotaci
      return

    z = u
    u = u.p
```

### Odebrání - $O(\lg n)$
- Provedeme odebrání **jako v binárním vyhledávacím stromě**. 
- Poté jdeme od uzlu vybraného *podle následujícího postupu* ke kořeni a upravujeme položku $\text{bf}$
- **Postup výběru uzlu**:
	- V případě, že odebíraný uzel nemá dva potomky, vybereme jeho rodiče
	- V případě, že odebraný uzel má dva potomky, vybereme rodiče jeho pořádkového následníka. Pokud je tímto rodičem přímo odebáraný uzel, vybereme místo toho rodiče odebíraného uzlu
- Označme $u$ jako *aktuální uzel*, u kterého jsme provedli úpravu $\text{bf}$
	- Pokud je po úpravě $u.\text{bf}$ rovno $-2$ nebo $2$, vybereme správnou rotaci. Pokud rotace zmenší výšku stromu, pokračujeme k úpravě $\text{bf}$ u rodiče uzlu $u$. Jinak, pokud víme, že se nezmenšila výška podstromu s kořenem $u$, algoritmus končí.
<iframe width="690" height="385" src="https://www.youtube.com/embed/PBkXmhiCP1M?si=YqbX1UZoWyiCCCvx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### Navigace
Předchozí:  [[Binární vyhledávací stromy, operace a jejich složitosti]]
Následující: [[B stromy, operace a jejich složitost]]
Celý okruh: [[1. Teoretické základy informačních technologií]]