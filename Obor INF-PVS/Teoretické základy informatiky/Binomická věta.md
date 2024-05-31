>[!info] Definice
>- Pro reálná čísla $a, b$ a nezáporní celé číslo $n$ je $$(a+b)^{n} = \sum_{k=0}^{n} \binom{n}{k} a^{n-k}b^{k}$$

>[!Example] Důkaz
>- **Důkaz matematickou indukcí**
>1. Pro $n=1$ platí $$(a+b)^{1} = \binom{1}{0}a + \binom{1}{1}b = a+b$$
>2. Předpokládejme, že věta platí pro nějaké $n = k$, platí tedy $$(a+b)^{k} = \binom{k}{0} a^{k} + \binom{k}{1} a^{k-1}b + \binom{k}{2} a^{k-2}b^{2} + ... + \binom{k}{k-1} ab^{k-1} + \binom{k}{k} b^{k}$$
>- Za tohoto předpokladu dokážeme, že věta platí také pro $n = k+1$.
>- Víme, že $$(a+b)^{k+1} = (a+b) \cdot (a + b)^{k}$$ Podle indukčního předpokladu můžeme výraz $(a + b)^{k}$ rozvinout podle binomické věty: $$(a+b)^{k+1} = (a+b) \cdot [\binom{k}{0} a^{k} + \binom{k}{1}a^{k-1}b + \binom{k}{2} a^{k-2}b^{2} + ... + \binom{k}{k-1}ab^{k-1} + \binom{k}{k}b^{k}]$$ Po roznásobení dostáváme: $$(a+b)^{k+1} = \binom{k}{0}a^{k+1} + \binom{k}{1} a^{k}b+ \binom{k}{2} a^{k-1}b^{2} + ... + \binom{k}{k-1} a^{2}b^{k-1} + \binom{k}{k} ab^{k} + \binom{k}{0}a^{k}b + \binom{k}{1} a^{k-1}b^{2} + \binom{k}{2} a^{k-2}b^{3} + ... + \binom{k}{k-1} ab^{k} + \binom{k}{k} b^{k+1}$$ Odpovídající členy sečteme: $$(a+b)^{k+1} = \binom{k}{0} a^{k+1} + [\binom{k}{1}+\binom{k}{0}]a^{k}b+[\binom{k}{2} + \binom{k}{1}] a^{k-1}b^{2} + ... + [\binom{k}{k} + \binom{k}{k-1}] ab^{k} + \binom{k}{k}b^{k+1}$$ Pro sečtení čísel v hranatých závorkách využijeme vlastnost kombinačních čísel $$\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}$$ $$(a+b)^{k+1} = \binom{k}{0} a^{k+1} + \binom{k+1}{1}a^{k}b + \binom{k+1}{2}a^{k-1}b^{2} + ... + \binom{k+1}{k} ab^{k} + \binom{k}{k} b^{k+1}$$ Protože platí $\binom{k}{0} = 1 = \binom{k+1}{0}$ a také $\binom{k}{k} = 1 = \binom{k+1}{k+1}$, dostáváme binomickou větu pro $n = k+1$: $$(a+b)^{k+1} = \binom{k+1}{0}a^{k+1}+ \binom{k+1}{1} a^{k}b + \binom{k+1}{2} a^{k-1}b^{2} + ... + \binom{k+1}{k} ab^{k} + \binom{k+1}{k} b^{k+1}$$ Tím je platnost binomické věty dokázána.

##### Navigace
Předchozí:  [[Stromy, kořenové stromy, vztahy mezi výškou, počtem vrcholů, počtem listů]]
Následující: [[Princip inkluze a exkluze]]
Celý okruh: [[1. Teoretické základy informačních technologií]]