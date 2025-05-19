- Slouží k nalezení *největšího společného dělitele*
- **Postup**
	1. Máme dvě čísla $a$ a $b$ ($a \geq b$).
	2. Dělíme $a$ číslem $b$ a najdeme zbytek $r$, tedy: $r=a \mod  b$
	3. Nahrazujeme $a$ hodnotou $b$ a $b$ hodnotou $r$.
	4. Opakujeme, dokud $r=0$. V tom okamžiku je $b$ výsledný **největší společný dělitel**.
- **Příklad**
	- Najdeme `gcd⁡(48,18)`
	1. $48÷18=2$ zbytek **12**, takže $48 \mod 18=12$.
	2. $18÷12=1$ zbytek **6**, tedy $18\mod 12=6$.
	3. $12÷6=2$ zbytek **0**, tedy $12\mod6=0$.
	4. Výsledek: **gcd⁡(48,18)=6**
- Časová složitost je $O(log(min(a,b)))$
- Často se používá v kryptografii

>[!tip] Věta - Bézoutova rovnost
> Nechť $a, b \in \mathbb{N}$. Pak existují čísla $x, y \in \mathbb{Z}$ taková, že $NSD(a, b) = ax + by$.
- Jinými slovy říká, že NSD dvou přirozených čísel lze zapsat jako *lineární kombinaci* s celočíselnými koeficienty. Tyto koeficienty můžeme získat použitím rozšířeného Euklidova algoritmu.
```python
# 01 rekurzivní 
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# 02 iterativní
def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a

# 03 rozšířený rekurzivní
def extended_gcd_recursive(a, b):
    if b == 0:
        return a, 1, 0  # NSD = a, x = 1, y = 0
    gcd, x1, y1 = extended_gcd_recursive(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
```
