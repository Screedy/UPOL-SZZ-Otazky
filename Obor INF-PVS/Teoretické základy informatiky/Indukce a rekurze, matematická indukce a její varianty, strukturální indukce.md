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

- Můžeme definovat i číselné množiny
	- např. množina $L$ všech lichých čísel - pro $1 \in L$, pokud $n \in L$ pak $n+2 \in L$
- Taktéž i formule výrokové logiky (induktivně definovaná struktura)
	1) každý výrokový symbol $p$ je formule (atomická)
	2) jsou-li $\psi$ a $\phi$ formule, pak jsou i výrazy formule (složené)
		- $\neg\psi$
		- $\psi \wedge \phi$
		- $\psi \vee \phi$
		- $\psi \rightarrow \phi$
		- $\psi \leftrightarrow \phi$
- Sierpisnkého trojúhelníky
![[Pasted image 20250420134907.png]]
## Matematická indukce
- Umožňuje dokazovat tvrzení jako "pro každé přirozené číslo platí..."
>[!info] Princip indukce
> Pro každé $n \in N$ je dáno tvrzení $V(n)$, předpokládejme že platí
>> a) $V(1)$ - indukční předpoklad
>> b) pro každé $n \in N$: z $V(n)$ plyne $V(n+1)$ - indukční krok

![[Pasted image 20250420135224.png]]

#### Varianty důkazu matematickou indukcí
- Indukce nemusí začínat 1
- ![[Pasted image 20250420135725.png]]
#### Definice matematickou indukcí
- Třeba pro faktoriál (viz na začátku tohoto souboru)
- ![[Pasted image 20250420135853.png]]
## Strukturální indukce
- Jde o zobecnění matematické indukce
- Místo množiny $\mathbb{N}$ pracujeme s množinou $T$
- Množina $T$ je množina řetězců obvykle utvořena podle induktivních pravidel (např. výrokové formule)
- Např. důkaz pro stejných počet levých i pravých závorek ve výrokové formuli
	- ![[Pasted image 20250420140721.png]]
#### Definice strukturální indukcí
- Definujeme pro bazické prvky $T$ (předpoklad) a složené prvky $T$ (krok)
- Používá se pro: aritmetické výrazy, definici seznamů, definici stromů