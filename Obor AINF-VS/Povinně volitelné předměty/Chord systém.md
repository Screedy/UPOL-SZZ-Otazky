## Chord systém
- = **Distribuovaná hashovací tabulka**
- Chord systém se používá pro organizaci a vyhledávání informací v distribuovaných systémech. 
- Navržen tak, aby poskytoval efektivní a spolehlivé řešení pro distribuované uchovávání a vyhledávání klíčů v síti. 
-  Původně navržen pro  peer-to-peer sítě, ale jeho koncepty jsou aplikovatelné i na jiné typy DS.

- Chord vytváří **kruhovou strukturu**, kde každý uzel (node) v síti má přiřazen jedinečný identifikátor (klíč). 
- Uzly jsou uspořádány do kruhu podle hodnot jejich identifikátorů. Identifikátor má $m$ bitů (obvykle $128$ nebo $160$) a celkově je poté v $2^{m}$ uzlů.

- Uzel s klíčem $k$ je spravován uzlem s klíčem $id$, kde $id \geq k$, tento uzel se nazývá `succ(k)` (successor)

- Hlavní úkol je pro $k$ efektivně najít `succ(k)`.

>[!Example]- Řešení:
>- Každý uzel má **Finger Table (FT)** obsahující $s$ záznamů ($s < m$).
>- Záznamy v tabulce pro uzel $p$ vypočítáme následovně: $$FT_{p}[i]=\text{succ}(p+2^{i-1})$$
>- Poté uzel $p$ předá dotaz na klíč k uzlu $q$ na indexu $j$ následovně:$$FT_{p}[j] \leq k < FT_{p}[j+1]$$
>	- pokud $p < k < FT_{p}[1]$, pak $q = FT_{p}[1]$ (je menší než první záznam v tabulce)
>	- pokud $p < k \text{ and } k > FT_{p}[s]$, pak $q = FT_{p}[s]$ (je větší než všechny záznamy v tabulce)
>![[MacBook-2025-01-03-002357.png]]

### Přidání uzlu do chord systému
- Proces, který **zahrnuje aktualizaci struktury kruhu a redistribuci odpovědnosti za klíče** tak, aby nový uzel byl začleněn do sítě.

>[!Example] Postup:
>1. Nový uzel $p$, který se chystá připojit k síti, vygeneruje svůj jedinečný identifikátor (klíč).
>2. Nový uzel musí najít svého "souseda" v kruhu Chord. tj. `succ(p+1)`. Často provedeno pomocí **vyhledávacího dotazu**.
>3. Každý uzel $q$ si drží aktualizovanou FT:
>	- $FT_{q}[1] = \text{succ}(q+1) - q$ ví, že první záznam odkazuje na následující uzel v kruhu.
>	- Každý uzel pravidelně ověřuje podmínku:
>		- $q = \text{pred}(\text{succ}(q+1))$
>		- **Pokud je nepravdivá**, pak $q < p < \text{succ}(q+1)$, je třeba nastavit $FT_{q}[1]=p$ (také je třeba ověřit, že $\text{pred}(p)=q$).
>		- Musím opravit zbytek $FT$ ($q$ musí najít $\text{succ}(k)$, $k = q + 2^{i-1}$)

### Smazání (výpadek, havárie) uzlu
- Každý uzel $p$ testuje, zde $\text{pred}(p)$ je naživu.
- Pokud $q$ aktualizuje spojení na dalšího souseda v kruhu a zjistí, že $\text{pred}(q+1)$ není nastaven, pak $\text{pred}(q+1) = q$.

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FReplikace%20a%20konzistence%20v%20DS" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FBlockchain" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Následující otázka
            </button>
        </a>
    </div>
    <!-- Spodní tlačítko -->
    <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2F2.%20Povinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty" style="text-decoration: none;">
        <button style="padding: 15px 30px; background-color: #ADD8E6; color: black; border: none; border-radius: 5px; cursor: pointer; width: 43%;">
            Všechny otázky
        </button>
    </a>
</div>