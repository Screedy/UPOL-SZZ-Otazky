- **Alternující Turingův stroj** (**ATS**) je _zobecněním NTS._ Zatímco u NTS stačí, _aby existovala jedna přijímající výpočetní věte_v, ATS umožňuje **dva druhy větvení**:
  - **existenciální** $(\exists)$– stačí, aby uspěla _alespoň jedna větev_,
  - **univerzální** $(\forall)$– musí uspět _všechny větve_.

> [!success]
> **Alternující Turingův stroj** je NTS $M$ s množinou stavů $Q,$ obohacený o funkci
>
> $$
> \sigma:Q \rightarrow \set{\lor,\land}
> $$
>
> která _každému stavu přiřadí jeho typ_:
>
> - $\sigma(q)=\lor$— **existenčně alternující stav**,
> - $\sigma(q)=\land$— **univerzálně alternující stav**.

- Přijetí není (obecně) definováno _pomocí jediné výpočetní větve_, ale **rekurzivně nad celým výpočetním stromem**.

> [!success]
> O konfiguraci $c$ se stavem $q$ řekneme, že je **A-přijímající**, pokud $q$ **není zamítací stav** a dále platí alespoň jedna z podmínek:
>
> 1. $q$ je přijímající stav
> 2. $\sigma(q)=\lor$ a **existuje alespoň jedna konfigurace** $c'$, která je z $c$ dosažitelná pomocí jednoho kroku a je _A-přijímající_ (existenčně alternující konfigurace)
> 3. $\sigma(q)=\land$ a **všechny konfigurace**, které jsou dosažitelné z $c$ pomocí jednoho kroku jsou _A-přijímající_. (univerzálně alternující konfigurace)
>
> ATS $M$ **přijímá řetězec** $x,$ pokud je _počáteční konfigurace pro_ $x$ _A-přijímající_.

> [!note]
> **Intuice**:
>
> _Existenciální stav_ odpovídá _logickému OR_. Stačí najít jednu úspěšnou možnost
>
> _Univerzální stav_ odpovídá _logickému AND_. Musí uspět všechny možnosti
>
> **Každý nedeterministický TS je ATS**, ve kterém jsou **všechny stavy existenční**.

---

# 1. Časová a paměťová složitost ATS

> [!success]
> **Časová složitost ATS** $M$ je funkce $T:\mathbb{N} \to \mathbb{N}$, kde $T(n)$ je _nejvyšší počet provedených instrukcí_, který ATS může provést _na každé výpočetní větvi_ _nad vstupem délky_ $n$ v **nejhorším případě**.
>
> **Paměťová složitost** **ATS** $M$ je funkce $S: \mathbb{N} \to \mathbb{N}$, kde $S(n)$ je _velikost potřebné paměti,_ kterou ATS může používat _na každé výpočetní větvi nad vstupem délky_ $n$ **v nejhorším případě**.

---

# 2. Alternující třidy složitosti

> [!success]
> Definujeme:
>
> $\text{ATIME}(T(n)) = \{ L(M)\ |\ M$ je ATS s časovou složitostí z $O(T(n))$}
>
> $\text{ASPACE}(S(n)) = \{ L(M)\ |\ M$ je ATS s paměťovou složitostí z $O(S(n))$}

> [!note]
> _Jak to správně říct_:
>
> Pro **paměťovou složitost** $S(n)$ definujeme $\text{ASPACE}(S(n))$ jako _množinu všech jazyků_ rozhodnutelných **ATS**, jehož _časová složitost_ je $O(S(n))$.

---

# 3. Věta o vztahu standardním třídám

> [!info]
> **Věta:** Pro $t(n) \geq n$ a $s(n) \geq \log n$ platí:
>
> |     | Inkluze |
> | --- | --- |
> | (i) | $\text{ATIME}(t(n)) \subseteq \text{DSPACE}(t(n))$ |
> | (ii) | $\text{DSPACE}(s(n)) \subseteq \text{ATIME}(s²(n))$ |
> | (iii) | $\text{ASPACE}(s(n)) \subseteq \text{DTIME}(2^{O(s(n))})$ |
> | (iv) | $\text{DTIME}(t(n)) \subseteq \text{ASPACE}(\log t(n))$ |

> [!warning]
> Důkaz:
>
> 1. $\text{ATIME}(t(n)) \subseteq \text{DSPACE}(t(n))$
>   - ATS lze simulovat DTS _pomocí procházení výpočetního stromu_ (rekurzivně)
>   - V každém volání si **nepamatuje celou konfiguraci**, ale _posloupnost voleb vedoucí k ní._
>   - Pro univerzální uzly **musí uspět všechna** rekurzivní volání.
> 2. $\text{DSPACE}(s) \subseteq \text{ATIME}(s^2)$
>   - Každý deterministický výpočet používající prostor $s(n)$ lze převést na alternující výpočet s kvadratickým časem. Myšlenka důkazu využívá rekurzivní ověřování dosažitelnosti konfigurací (podobně jako u Savitchovy věty)
>   - Procedura `can-yield(α, β, m)` se realizuje pomocí alternujícího algoritmu
>     - Existenciální alternací se vybere $\gamma$
>     - Univerzální alternací poté provedeme rekurzivní volání
> 3. $\text{ASPACE}(s(n)) \subseteq \text{DTIME}(2^{O(s(n))})$
>   - Alternující prostor lze simulovat deterministicky v exponenciálním čase.
>   - _Počet konfigurací využívajících prostor_ $s(n)$ je **nejvýše** $2^{O(s(n))}$,
>   - Deterministický algoritmus _projde celý výpočetní graf_.
> 4. $\text{DTIME}(t(n)) \subseteq \text{ASPACE}(\log t(n))$
>   - Deterministický čas lze simulovat alternací s logaritmickou pamětí.
>   - ATS zkontroluje tableau DTS přes rekurzivní proceduru, která si _pamatuje jen indexy políček._

## 3.1 Důsledky

> [!info]
> _Definujeme_:
>
> $\text{APTIME} = \bigcup_{k>0 } \text{ATIME}(n^k)$ (alternace v polynomiálním čase) $\text{PSPACE} = \bigcup_{k>0} \text{DSPACE}(n^k)$ (deterministický polynomiální prostor)
>
> - $\subseteq:$ z (i), $\text{APTIME}(n^k) \subseteq \text{DSPACE}(n^k) \subseteq \text{PSPACE}.$
> - $⊇:$ z (ii), $\text{DSPACE}(n^k) \subseteq \text{ATIME}(n^{2k}) \subseteq \text{APTIME}$
>
> $$
> \boxed{\text{APTIME} = \text{PSPACE}}
> $$

---

# 4. ATS a polynomiální hierarchie

- Pokud omezíme počet střídání mezi existenčními a univerzálními stavy, dostaneme charakterizaci polynomiální hierarchie.

> [!success]
> ATS $M$ je $\Sigma_k\text{-stroj}$, pokud pro každý vstup a každou výpočetní větev platí:
>
> - výpočet lze rozdělit do **nejvýše** $k$ **intervalů**,
> - v každém intervalu jsou **jen univerzálně** nebo **jen existenčně** alternující konfigurace,
> - **první interval** obsahuje **existenční** alternující konfigurace.
>
> _Analogicky_ $\Pi_k\text{-stroj}$ začíná **univerzálním** intervalem.

---

# 5. Duální ATS

> [!success]
> K ATS $M$ sestrojíme duální ATS $\overline{M}$ tak, že:
>
> 1. **prohodíme alternace u stavů**
> 2. **prohodíme přijímací a zamítací stav.**

> [!info]
> **Věta:** Nechť $M$ je ATS, který vždy zastaví, a $N$ je k němu duální ATS. Pak
>
> $$
> L(N)=\overline{L(M)}.
> $$

> [!info]
> **Důsledek**:$Πₖᵖ = coΣₖᵖ$