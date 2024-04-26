
- Číselné soustavy jsou metody reprezentace čísel pomocí sady symbolů.
- Různé číselné soustavy mají různé základy (**radix**), které určují počet **unikátních symbolů** a číslic použitých v systému.

### Desítková soustava
- Člověk pro reprezentaci dat používá desítkovou soustavu. 
- Číslice $0$ až $9$
- Každé číslo může být reprezentováno jako součet mocninné řady desítkového základu, například: $(1024)_{10} = 1 \cdot 10^{3} + 0 \cdot 10^{2} + 2 \cdot 10^{1} + 4 \cdot 10^{0}$

### Dvojková soustava (binární)
- Základní soustava používaná v počítačích.
- Elektromechanické a elektronické součásti: nejsnadnější realizovatelné $2$ stavy pro $2$ hodnoty, symboly (číslice) $0$ a $1$ (digitální začízení/elektronika)
- Každé číslo je vyjádřeno jako součet mocninné řady základu 2, například:$(11)_{10} = (1011)_{2} = 1 \cdot 2^{3} + 0 \cdot 2^{2} + 1 \cdot 2^{1} + 1 \cdot 2^{0}$

## Osmičková soustava
- Číslice 0-7 
- Je často používána v informatice pro zjednodušení binárních zápisů, protože každé osmičkové číslo odpovídá právě třem binárním číslicím.

## Šestnáctková soustava
- Používá šestnáct symbolů (0-9 a A-F).
	- A až F reprezentují čísla 10 až 15.
- Používána v informatice pro efektivní reprezentaci binárních dat, protože každé hexadecimální číslo odpovídá právě čtyřem binárním číslicím.

## Převody mezi soustavami

### Z desítkové na dvojkovou $(156)_{10}$
- Proces, kdy dělíme číslo základem dvojkové soustavy a zaznamenáváme zbytky. Postup opakujeme dokud nedosáhneme nuly. Zbytky poté čteme od posledního k prvnímu:
1. **Dělení čísla 156 základem 2**:
    - 156 děleno 2 je 78, zbytek je 0.
    - 78 děleno 2 je 39, zbytek je 0.
    - 39 děleno 2 je 19, zbytek je 1.
    - 19 děleno 2 je 9, zbytek je 1.
    - 9 děleno 2 je 4, zbytek je 1.
    - 4 děleno 2 je 2, zbytek je 0.
    - 2 děleno 2 je 1, zbytek je 0.
    - 1 děleno 2 je 0, zbytek je 1.
2. **Zaznamenání zbytků a čtení od spodu**:
    - Zbytky: 0, 0, 1, 1, 1, 0, 0, 1
    Binární číslo: **10011100**
3. Tedy $(156)_{10} = (10011100)_{2}$. 

### Z dvojkové na desítkovou $(10011100)_{2}$
- Proces, při kterém přiřazujeme každé číslici binárního čísla váhu založenou na její pozici.
- Váha je dána mocninou základu 2, přičemž exponent se zvyšuje s každou pozicí zprava doleva, začínající od nuly.
- Pro bin. číslo $(10011100)_{2}$:
	- Pozice 0: $0 \cdot 2^{0} = 0 \cdot 1 = 0$
	- Pozice 1: $0 \cdot 2^{1} = 0 \cdot 2 = 0$
	- Pozice 2: $1 \cdot 2^{2} = 1 \cdot 4 = 4$
	- Pozice 3: $1 \cdot 2^{3} = 1 \cdot 8 = 8$
	- Pozice 4: $1 \cdot 2^{4} = 1 \cdot 16 = 16$
	- Pozice 5: $0 \cdot 2^{6} = 0 \cdot 32 = 0$
	- Pozice 6: $0 \cdot 2^{7} = 0 \cdot 64 = 0$
	- Pozice 7: $1 \cdot 2^{8} = 1 \cdot 128 = 128$
	- $128 + 16 + 8 + 4 = (156)_{10}$
