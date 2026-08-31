> [!warning]
> **Velikostí vstupu TS** rozumíme _počet buněk_ (vstupní pásky), které _daný vstup zabírá_.
>
> **Velikostí paměti TS** $M$ _potřebné při výpočtu pro konkrétní vstup_ rozumíme číslo $p + 1$, kde $p$ je _maximální počet buněk_, jež jsou během výpočtu (nad daným vstupem) _navštíveny_.

- Abychom mohli porovnávat algoritmy z hlediska využité paměti, potřebujeme měřit množství paměti, které využívají během výpočtu. Tím se zabývá **paměťová složitost algoritmů**.

> [!success]
> **Paměťová složitost** **DTS** $M$ je funkce $S_M: \mathbb{N} \to \mathbb{N}$, kde $S_M(n)$ je _velikost potřebné paměti při výpočtu_ $M$ nad vstupem délky $n$ **v nejhorším případě** (worst case).
>
>
> Pro NTS jsou _definice analogické_.

- Prostorovou složitost formalizujeme pomocí tříd **DSPACE** a **NSPACE**, které omezují množství pracovní paměti použité deterministickým, resp. nedeterministickým Turingovým strojem.

- Formálně: pro funkci $f: \mathbb{N} \rightarrow \mathbb{N}$ definujeme třídy:
  - $\text{DSPACE}(f(n)) = \{ L(M)\ |\ M$ je DTS s paměťovou složitostí $O(f(n))\}$
  - $\text{NSPACE}(f(n))=\{ L(M)\ |\ M$ je NTS s paměťovou složitostí $O(f(n))\}$

> [!note]
> _Jak to správně říct_:
>
> Pro **paměťovou složitost** $S(n)$ definujeme $\text{DSPACE}(S(n))$ jako _množinu všech jazyků_ rozhodnutelných **deterministickým** Turingovým strojem, jehož _paměťová složitost_ je $O(S(n))$.

> [!danger]
> Při _měření prostorové složitosti_ se počítá pouze **pracovní paměť** Turingova stroje, _nikoliv vstupní páska_, která je určena _pouze pro čtení._

---

# 1. Třída $\text{PSPACE}$

> [!success]
> Třída $\text{PSPACE}$ je množina všech jazyků rozhodnutelných **DTS s polynomiální paměťovou složitostí**.
>
> $$
> \text{PSPACE}=\bigcup_{k>0}\text{DSPACE}(n^k)
> $$

> [!note]
> Jinými slovy, jazyk patří do $\text{PSPACE}$ právě tehdy, když _existuje DTS_, který jej rozhoduje a při výpočtu používá **nejvýše polynomiální množství pracovní paměti**.

> [!danger]
> Na rozdíl od časových tříd zde není _nijak omezen počet vykonaných kroků_. Algoritmus může běžet i **exponenciálně dlouho**, pokud během celého výpočtu nepřekročí povolenou velikost pracovní paměti.

---

# 2. Třída $\text{NPSPACE}$

> [!success]
> Třída $\text{NPSPACE}$ je množina všech jazyků rozhodnutelných **NTS s polynomiální paměťovou složitostí**
>
> $$
> \text{NPSPACE}=\bigcup_{k>0}\text{NSPACE}(n^k)
> $$

> [!danger]
> Na první pohled by se mohlo zdát, že stejně jako u tříd $\text{P}$ a $\text{NP}$ bude _nedeterminismus znamenat větší výpočetní sílu_. Překvapivě tomu tak není – **obě třídy jsou ve skutečnosti shodné**. Tento výsledek udává **Savitchova věta**.

---

# 3. Savitchova věta

> [!warning]
> **Prostorově zkonstruovatelná funkce** je funkce $f(n)$, pro kterou _existuje TS_, který **při vstupu délky** $n$ využije právě $O(f(n))$ pracovní paměti a _dokáže na pracovní pásce_ **vyznačit oblast o velikosti** $f(n)$. Jinými slovy, stroj _umí sám určit, kolik paměti má při výpočtu k dispozici._

> [!success]
> **Savitchova věta:**
>
> Nechť $s(n) \geq n$ je prostorově konstrovatelná funkce. Potom platí
>
> $$
> \text{NSPACE}(s(n)) \subseteq \text{DSPACE}(s(n)^2).
> $$

> [!note]
> **Intuice:** To znamená, že každý n_edeterministický algoritmus využívající prostor_ $f(n)$ **lze simulovat** _deterministicky_ za cenu **nejvýše kvadratického zvětšení spotřeby paměti**.
>
> To je dramatický kontrast s časem, kde nejlepší známá deterministická simulace NTS stojí **exponenciální** čas $\text{NTIME}(t) \subseteq \text{DTIME}(2^{O(t)})$. Tento rozdíl je jádrem otázky $\text P$ vs $\text{NP}$.

## 3.1 Důkaz

_Vezměme libovolný jazyk_ $L \in \text{NSPACE}(s(n))$. Potom _existuje_ NTS $M$, který rozhoduje jazyk $L$ a používá prostor $f(n) \in O(s(n))$. _Naším cílem_ je sestrojit **deterministický** TS, který bude _rozhodovat stejný jazyk_ a bude používat pouze $O(f(n)^2)$ paměti, a tedy i $O(s(n)^2)$.

Navrhneme **deterministický algoritmus** `CAN-YIELD`, který má vstup `α, β` a `t`, kde `α, β` jsou _konfigurace_ stroje $M$ obsahující $f(n)$ políček pásky a `t` je _počet kroků_.  
Algoritmus rozhodne, zda-li se $M$ **může dostat z konfigurace** `α` **do konfigurace** `β` **s pomocí maximálně** `t` **kroků**.

- **Algoritmus** `CAN-YIELD(α, β, t)`
  1. Pokud $t=0$: zkontrolujeme, zda $\alpha = \beta$ (ANO = přijmi, NE = zamítni)
  2. Pokud $t=1$: ověříme, zda lze z konfigurace `α` přejít do konfigurace `β` jedním krokem podle přechodové funkce stroje $M$ (ANO = přijmi, NE = zamítni)
  3. Jinak: **iteruj přes všechny konfigurace** $\gamma$, které mohou vzniknout při využití nejvýše $f(n)$ buněk pracovní pásky. Pro každou konfiguraci $\gamma$ rekurzivně zavoláme rekurzivně zavoláme `CAN-YIELD(α, γ, ⌊t/2⌋)` a `CAN-YIELD(γ, β, ⌈t/2⌉)`. _Pokud_ **_obě_** _volání přijímají →_ **_přijmi_**.
  4. Jinak **zamítni.**
- **Vytvoříme TS** $N$, který pro vstup $w$ provede:
  - $\text{return }\text{CAN-YIELD}(C_{\text{start}}, C_{\text{finish}}, 2^{O(f(n))})$ (počet možných obsahů pásky $|Γ|^{f(n)}$, máme dva páskové symboly)

- **Paměťová složitost.**
  - **Jedna konfigurace zabírá** $O(f(n))$ **paměti.** _V jednom rekurzivním volání_ uchováváme **pouze** konfigurace $α, β, γ$ a parametr $t$, tedy _stále_ $O(f(n))$ _paměti_.
  - _Hloubka rekurze_ je:
    $$
    \log(2^{O(f(n))})=O(f(n)),
    $$
    
  - protože _při každém rekurzivním volání_ se parametr $t$ **dělí přibližně na polovinu**.
  - **Celková spotřeba paměti** je tedy
    $$
    O(f(n))⋅O(f(n))=O(f(n)^2).
    $$
    
  - Jelikož $f(n)∈O(s(n))$, dostáváme
    $$
    O(f(n)^2)⊆O(s(n)^2).
    $$
    

> [!warning]
> **Pozor**:
>
> _Proč může být výpočet dlouhý nejvýše_ $2^{O(f(n))}$_?_
>
> - Musel by navštívit jednu konfiguraci vícekrát → vznikl by cyklus

> [!note]
> **Intuice:** Místo procházení celého výpočetního stromu NTS _„rozděl a panuj"_ — hledáme _středový bod_ výpočtu, a pak rekurzivně _oba poloviční úseky_. **Neukládáme** celou cestu, jen aktuální vrstvu rekurze.

## 3.2 Hlavní důsledek Savitchovy věty

$$
\text{NPSPACE}=⋃_k \text{NSPACE}(n^k)⊆⋃_k \text{DSPACE}(n^{2k})=\text{PSPACE}
$$

Opačná inkluze $\text{PSPACE} \subseteq \text{NPSPACE}$ je triviální (DTS je speciální NTS). Tedy:

$$
\boxed{\text{PSPACE} = \text{NPSPACE}}
$$

> [!note]
> **Intuice:** Nedeterminismus **nepřidává žádnou sílu**, pokud je zdrojem paměť. Kvadrát polynomu je zase jen polynom — polynomiální třídy jsou vůči kvadratické ztrátě _„imunní“_.

---

# 4. Immermanova–Szelepcsényiho věta

> [!note]
> Nedeterministické _prostorové třídy_ jsou **uzavřené na doplněk**. (Deterministické jsou vždy uzavřené na doplněk)

> [!success]
> **Věta:** Pro $s(n) ≥ n$ platí $\text{NSPACE}(s(n)) = \text{coNSPACE}(s(n))$.