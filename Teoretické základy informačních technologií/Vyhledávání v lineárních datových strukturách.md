- **Datové struktury** = **Způsob uložení entit**, které se vyskytují v programu **do paměti**
	- **entita** = jakákoliv přesně definovaná množina dat

- **Lineární datové struktury**
	- Prvky jsou **seřazeny do posloupnosti** (má smysl uvažovat o pořadí prvků)
	- U každého prvku **známe předka a následníka** (pokud existují)

### Pole
- Prvky jsou v paměti uspořádány **za sebou**
- K prvkům přistupujeme pomocí **indexu** v čase $\Theta (1)$ (konstantním čase)
- Má **fixní velikost** (alternativa dynamické pole)
- Všechny prvky jsou **stejného typu**
- ![[MacBook-2024-03-12-000854@2x.png | 400]]

- Výpočet přístupu k $i$-tému prvku:
	- $\text{adresa začátku} + (\text{velikost prvku} * \text{index})$ 

```C
struct array-set{
  data, //pole prvků node
  top, //index místa pro zápis
  cap //velikost pole data
}

//nebezpečí overflow
proc insert(AS, x)          Θ(1)
  AS.data[AS.top] = x 
  AS.top += 1**

//nebezpečí underflow
proc delete(AS, i)          Θ(1)
  AS.top -= 1  
  AS.data[i] = AS.data[AS.top] 
```

![[MacBook-2024-03-12-000855@2x.png]]

### Vyhledávání v nesetřízeném a setřízeném poli
#### 1. V nesetřízeném poli
```C
proc search(A,k)
  for i = 0; i < n; i++
      if A[i].key == k then return i
  return -1
```
- Zrychlení drobným trikem, za cenu zmenšení kapacity o $1$:
```C
proc search-alt(A,k)
  AS.data[AS.top] = k
  for i = 0; true; i++
      if AS.data[i].key == k then return i
```

- Složitost `search(A,k)`
	- Sledujeme počet porovnání v závislosti na velikosti pole $A$
	- **Nejhorší případ** = Prvek s klíčem $k$ se v $A$ nenachází. Projdeme celé pole a složitost je $\Theta (n)$
	- **Průměrný případ** = Pokud se prvek s klíčem $k$ v poli $A$ nachází, pak je počet porovnání $\frac{1 + 2 + 3 + 4 + ... + n}{n} = \frac{n \times (n+1)}{2n} = \frac{n+1}{2}$
		- *předpokládáme, že všechny prvky v poli vyhledáváme stejně často*

#### 2. V setřízeném poli
- Předpokládejme, že **klíče** bereme z **úplně uspořádané množiny** (čísla, lexikálně uspořádané řetězce, ...)
- Při neúspěšném vyhledávání v setřízeném poli potřebujeme nejhůře tolik porovnání, jako při vyhledávání v nesetřízeném poli, jsou ale případy, kdy potřebujeme méně
```C
proc search(A,k)
  for i = 0; i < n and A[i].key <= key; i++
      if A[i].key == k then return i
  return -1
```
- **Složitost** = **V nejhorším případě** *(Kdy je vyhledávaný prvek na konci pole, nebo je větší než všechny ostatní prvky v poli)* je stále $\Theta (n)$

##### Binární vyhledávání
- Idea:
	- Při **hledání prvku s klíčem $k$** se podíváme na prostřední prvek pole $A$, řekněme, že je na indexu $s$. 
	- Pokud je`k == A[s].key` vyhledávání **je úspěšné**. 
	- Pokud`k < A[s].key`, rekurzivně vyhledáváme v části pole ohraničeném indexy $0,s-1$. 
	- Pokud`k > A[s].key`, vyhledáváme v části pole ohraničeném indexy $s+1, n-1$.
- Složitost $\Theta (\log n$)
```C
proc binary-search(A,k)
   l = 0
   p = n - 1

   while l <= p 
      s = floor((l + p)/ 2) 
      if A[s].key == k then return s 
      if A[s].key > k 
         p = s - 1 
      else 
         l = s + 1 

   return -1
```

Strom vyhledání:
![[MacBook-2024-03-12-000856@2x.png | 500]]

### Interpolační vyhledávání
- Algoritmus je **vylepšením binárního vyhledávání** pro případy, kdy jsou hodnoty v seznamu nejen seřazené, ale **zároveň rovnoměrně rozložené**.
- Složitost $\Theta (\log \log n)$
- V nejhorším případě ovšem může být složitost až $O(n)$. Aby se zabránilo nejhoršímu případu, je možné **kombinovat interpolační** vyhledávání **s binárním vyhledáváním** *(například střídat vždy jeden krok interpolačního vyhledávání a jeden binárního vyhledávání)*
>[!Example] Příklad
>Tuto metodu intuitivně používají lidé *například při vyhledávání ve slovníku - odhadnou, kde by přibližně mohlo hledané heslo být* (např. heslo začínající písmenem "K" bude pravděpodobně někde před polovinou slovníku) a *otevřou slovník na odhadnutém místě. Podle odchylky postupují dopředu nebo dozadu o menší nebo větší počet stránek.* Jako příklad budeme uvažovat seznam čísel $1, 2, 3, ..., 1000$. Pokusíme se najít prvek $125$. Pokud bychom hledali pomocí binárního vyhledávání, prvním testovaným prvkem by bylo číslo $500$, poté číslo $250$ a nakonec námi hledané číslo $125$. Interpolační vyhledávací algoritmus odhadne pozici a přímo přejde na prvek $125$.

<iframe width="690" height="385" src="https://www.youtube.com/embed/DlCPTPQD6Mw?si=F7EWoP8TXvEkq4Vv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Fibonacciho posloupnost vyhledávání
- **Fibonacciho posloupnost vyhledávání** je *vyhledávací algoritmus, který funguje na principu binárního vyhledávání*, ale místo dělení pole na dvě stejně velká podpole se pole dělí na dvě podpole, jejichž velikost odpovídá dvěma po sobě jdoucím číslům Fibonacciho posloupnosti.

- Algoritmus začne s celým polem a dvěma ukazateli: *jeden na začátku pole a druhý na konci pole.* Poté se vypočte nejbližší číslo Fibonacciho posloupnosti, které je větší nebo rovno velikosti pole. *Toto číslo určuje délku prvního podpole.* Algoritmus porovná hledanou hodnotu s prvkem na konci tohoto podpole. Pokud je hledaná hodnota menší, pole se zmenší na první polovinu, jinak se pole zmenší na druhou polovinu. *Tento postup se opakuje, dokud se hledaná hodnota nenajde nebo dokud se pole nezmenší na velikost jednoho prvku.*

- Fibonacciho vyhledávání má složitost $O (\log n)$, což z něj dělá rychlejší než lineární vyhledávací algoritmy, ale pomalejší než binární vyhledávání. Jeho výhoda spočívá v tom, že je efektivní pro velká pole, zejména pokud jsou data uložena v pomalé paměti, protože algoritmus umožňuje minimalizovat počet přístupů k paměti. Fibonacciho vyhledávání se však v praxi často nepoužívá, protože je složitější než binární vyhledávání a jeho výhody jsou často zastíněny moderními vyhledávacími algoritmy s ještě lepšími výsledky.

##### Navigace
Předchozí:  [[Pořádkové statistiky]]
Následující: [[Binární vyhledávací stromy, operace a jejich složitosti]]
Celý okruh: [[1. Teoretické základy informačních technologií]]