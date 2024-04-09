### Strom a kořenový strom
- **Strom** je souvislý neorientovaný graf bez kružnic
- Graf je **souvislý**, pokud mezi libovolnou dvojicí různých uzlů **existuje cesta**
- Graf **obsahuje kružnici**, pokud existuje **tah**, ve kterém je první a poslední vrchol totožný a jinak jsou všechny vrcholy vzájemně různé

- **Kořenový strom** = jeden uzel je označen jako kořen $\rightarrow$ tím ve stromu získáme směr *(dolů)* ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe2QKxWSfdAG82iQL59uh34Vh7jU6cRD-ohU97Gc0FEAQuRfmikIxmLjbNXLTnz5WSgL6oChXlcr6XjmvCWyjIGOO-sYURX0Lo15Fl75zY04VG1AYK-WzsaNfmZl1BOfCGtQnQJGdvdbN5gukBjeFs?key=1oMgW2MUuii1DDrztmo2_Q)

### Binární vyhledávací stromy a operace s nimi
- **Binární (kořenový) strom**, kde v uzlech jsou uloženy další údaje, zejména však **klíč v položce key**
- Udržujeme **explicitní pointery na potomky a rodiče**: *left* na *levého potomka* (levý podstrom), *right* na *pravého potomka* (pravý podstrom), *p* na rodiče
- Pro každý vrchol $x$ v tomto stromu platí: Pokud je vrchol $y$ v levém podstromu vrcholu $x$, pak $y.\text{key} < x.\text{key}$. Pokud je $y$ v pravém podstromu vrcholu $x$, pak $y.\text{key} > x.\text{key}$
- Implementace:
```
struct node {
  left, //levy potomek
  right, //pravy potomek
  p, //rodic
  key //klic
  …
}

struct tree {
  root, // koren
  …
}
```

### Operace s binárními stromy
#### Průchod stromem
```
//navštíví všechny vrcholy podstromu s kořenem x
proc in-order-walk(x) 
  if x != nil
    in-order-walk(x.left)
    process(x)
    in-order-walk(x.right)**
```
- $\Theta (n)$ (analogie průchodu do hloubky)

#### Vyhledávání
- Porovnávám klíč s klíčem vrcholu, **podle výsledku** pokračuji do levého nebo do pravého podstromu
```
// rekurzivní verze
proc tree-search(x,k)                O(h),
  if x == nil or k == x.key          nejhůře O(n), nejlépe O(lg n)
    return x
  if k < x.key
    return tree-search(x.left, k)
  else
    return tree-search(x.right, k)
```
```
// iterativní verze
proc tree-search-iterative(x,k)       O(h)
  while x != nil and k != x.key       nejhůře O(n), nejlépe O(lg n)
    if k < x.key
      x = x.left
    else
      x = x.right
  return x
```

#### Hledání minimum, maximum
```
proc tree-minimum(x)               O(h)
  while x.left != nil nejhůře      O(n), nejépe O(lg n)
    x = x.left
  return x
```
```
proc tree-maximum(x)               O(h)
  while x.right != nil nejhůře     O(n), nejépe O(lg n)
    x = x.right
  return x
```

#### Hledání Pořádkového následníka a pořádkového předchůdce
- **Pořádkový následník uzlu $x$** je *uzel*, který má **v množině $\{z \mid z.\text{key} > x.\text{key}\}$ nejmenší klíč.** Pokud je tato *množina prázdná,* pořádkový následník $x$ neexistuje.

- **Pořádkový předchůdce je duální pojem** (otočíme znaménka porovnání), operace jeho nalezení a důkaz správnosti je analogický
![[MacBook-2024-03-12-000858@2x.png]]
```
proc tree-successor(x)
  // pripad 1
  if x.right != nil
  return tree-minimum(x.right)

  // pripad 2
  y = x.p
  while y != nil and x = y.right
    x = y
    y = y.p
  return y
```

#### Přidání uzlu `Insert`
- Idea: Hledáme jako při vyhledávání. Přidáme na místo, kde by bylo vyhledávání neúspěšné
- Složitost: $O(h)$
- Tvar a výška stromu závisí na pořadí, ve kterém je vkládáme
```
proc insert(T, z)
  y = nil
  x = T.root
  
  while x != nil
    y = x // po dokonceni iterace je vzdy y rodicem x
    if z.key < x.key
      x = x.left
    else
      x = x.right
      
  z.p = y
  if y == nil
    T.root = z // T byl pred pridanim prazdny
  else if z.key < y.key
    y.left = z
  else 
    y.right = z
```
#### Odebrání uzlu `Delete`
- Smazání uzlu $z$ ze stromu
	- $z$ nemá potomky ($z$ je list) $\rightarrow \Theta (1)$
	- $z$ má jednoho potomka $\rightarrow \Theta (1)$
		- $z$ má dva potomky $\rightarrow \Theta (1) + \Theta (h)$
```
proc transplant(T, u, v)
  if u.p == nil
    T.root = v
  else if u == u.p.left
    u.p.left = v
  else
    u.p.right = v
  if v != nil
    v.p = u.p

proc tree-delete(T,z)
  if z.left == nil
    transplant(T, z, z.right)
  else if z.right == nil
    transplant(T, z, z.left)
  else
    y = tree-minimum(z.right) // najdu poradkoveho následovníka
    if y.p != z // pořádkový následovník není potomek
      transplant(T, y, y.right) // nahradím y pravým podstromem
      y.right = z.right
      y.right.p = y
    transplant(T,z,y) // nahradim podstrom z, y
    y.left = z.left
    y.left.p = y
```
