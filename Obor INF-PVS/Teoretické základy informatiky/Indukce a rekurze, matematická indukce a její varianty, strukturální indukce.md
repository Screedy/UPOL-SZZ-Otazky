## Indukce a rekurze
- Jedná se o dva provázané jevy
- Použití: důkazy, algoritmy, definice
- **indukce** ... od menšího k většímu (definujeme první krok)
- **rekurze** ... od velkého k malému (limitní ukončující podmínka)
#### Faktoriál
1) Rekurzivní výpočet
```python
def fact_1(n):
	if n == 1:
		return 1
	else: 
		return n * fact_1(n-1)
```
2) Induktivní výpočet
```python
def fact_2(n):
	res = 1
	while (n > 1):
		res *= n
		n--
	return res
```

- Popis faktoriálu matematicky
$$
f(n)=
\begin{cases}
1 & \text{pokud } n = 1, \\
n\ \cdot f(n-1) & \text{pokud } n > 1.
\end{cases}
$$
- Můžeme definovat i číselné množiny
	- např. množina $L$ všech lichých čísel - pro $1 \in L$, pokud $n \in L$ pak $n+2 \in L$
- Taktéž i formule výrokové logiky (induktivně definovaná struktura)
	1) každý výrokový symbol $p$ je formule (atomická)
	2) jsou-li $\psi$ a $\phi$ formule, pak jsou i výrazy formule (složené)
		- $\neg\psi$
		- $\psi \wedge \phi$
		- $\psi \vee \phi$
		- $\psi \Rightarrow \phi$
		- $\psi \Leftrightarrow \phi$
- Sierpisnkého trojúhelníky
![[Pasted image 20250420134907.png]]

## Matematická indukce
- Umožňuje dokazovat tvrzení jako "pro každé přirozené číslo platí..."
>[!info] Princip indukce
> Pro každé $n \in N$ je dáno tvrzení $V(n)$, předpokládejme že platí
>> a) $V(1)$ - indukční předpoklad
>> b) pro každé $n \in N$: z $V(n)$ plyne $V(n+1)$ - indukční krok

#### Důkaz principu indukce
- Provedeme ho sporem. Předpokládejme, že princip indukce neplatí, tj. existuje tvrzení $V(\cdot)$ splňující:
	1. $V(1)$
	2. pro každé $n \in \mathbb(N):$ z $V(n)$ plyne $V(n+1)$
- Ale pro nějaké $n' \in \mathbb(N)$  tvrzení $V(n')$ neplatí.
- Označme 
$$K = \{ m \in \mathbb{N} \ | \ V(m) \ \text{neplatí} \} $$
- $K$ je prázdná (neboť $n' \in K$). $K$ má tedy nejmenší prvek $k$ a ten je různý od $1$ (protože $V(1)$ platí). Pak tedy $k - 1 \notin K$, tedy $V(k-1)$ platí. Z indukčního kroku plyne, že platí i $V(k)$, tedy $k \notin K$, což je spor s $k \in K$. $\square$
#### Varianty důkazu matematickou indukcí
- Indukce nemusí začínat 1
- ![[Pasted image 20250420135725.png]]
#### Definice matematickou indukcí
- Třeba pro faktoriál (viz na začátku tohoto souboru)
>[!info] Věta 8.9.
> **Věta:** Nechť je dána množina $V$, prvek $a \in V$ a funkce $G: \mathbb{N} \times V \rightarrow V$. Pak existuje právě jedna funkce $F: \mathbb{N} \rightarrow V$, pro kterou platí:
>> 1. $F(1) = a,$
>> 2. pro každé $n \in \mathbb{N}$: $F(n+1)=G(n,F(n))$
>

## Strukturální indukce
- Jde o **zobecnění matematické indukce**
- Místo množiny $\mathbb{N}$ pracujeme s množinou $T$
- Množina $T$ je množina řetězců obvykle utvořena podle induktivních pravidel (např. výrokové formule)
- Např. důkaz pro stejných počet levých i pravých závorek ve výrokové formuli
	- ![[Pasted image 20250420140721.png]]
#### Definice strukturální indukcí
- Definujeme pro bazické/atomické prvky z $T$ (předpoklad) a složené prvky $T$ (krok)
- Používá se pro: aritmetické výrazy, definici seznamů, definici stromů