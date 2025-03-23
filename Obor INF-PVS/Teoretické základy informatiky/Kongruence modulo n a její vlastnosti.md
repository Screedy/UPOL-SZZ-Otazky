>[!info] Definice
> Nechť $a,b \in \mathbb{Z}, n \in \mathbb{N}$. Řekneme, že dana čísla $a, b$ jsou **kongruentní modulo n**, jestliže $n \mid (a - b)$.
> 
> Značíme: $a \equiv b \space (mod \space n)$
- Jinými slovy to znamená, že jejich rozdíl je násobkem $n$
#### Vlastnosti kongruence modulo n
>[!tip] Věta
>Nechť $a,b \in \mathbb{Z}, n \in \mathbb{N}$. Pak jsou následující podmínky ekvivalentní:
> 1. $a \equiv b \space (mod \space n)$
> 2. existuje $k \in \mathbb{Z}$ takové, že $b = a - nk$
> 3. $a \mod n = b \mod n$

> [!tip] Věta
> Pro $n \in \mathbb{N}$ je relace kongruence modulo n ekvivalencí na $\mathbb{Z}$.
> 
> Tzn. je reflexivní, symetrická a trazitivní.

- Platí i **další vlastnosti**:
	- Předpoklad: $a,b, c, d \in \mathbb{Z}, n \in \mathbb{N}$
	1) sčítání: $a + c \equiv b + d \space (mod \space n)$
	2) odečítání: $a - c \equiv b - d \space (mod \space n)$
	3) násobení: $a \cdot c \equiv b \cdot d \space (mod \space n)$ *(**pozor** - dělení obecně neplatí)*
	4) umocnění: $a^k \equiv b^k \space (mod \space n)$, $k \in \mathbb{N}$
#### Zbytková třída modulo n ($\equiv_n$)
- Množina všech celých čísel, která při dělení přirozeným číslem $n$ dávají stejný zbytek po celočíselném dělení
- Např.
	- Třída obsahuje číslo $i \in \mathbb{Z}$ je značena $[i]_{\equiv_n}$
	- Platí: $i = \{j \mid j = i + kn, k \in \mathbb{Z} \}$
	- $[2]_{\equiv_5} = \{ ..., -8, -3, 2, 7, 12, ... \}$



