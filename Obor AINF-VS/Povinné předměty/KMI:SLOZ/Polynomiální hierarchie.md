> [!info]
> Třída $\text{NP}$ odpovídá na otázky typu:
>
> - “**_Existuje_** řešení splňující podmínku?“
> - Např. Problém $\text{CLIQUE}$— Existuje v grafu klika velikost $\ge k$? (Existuje množina vrcholů velikosti $k$ tvořící kliku)
>
> Třída $\text{coNP}$ odpovídá na otázky typu:
>
> - “**_Pro všechna_** řešení platí podmínka?“
> - Např. Problém $\text{coCLIQUE}$— Neexistuje v grafu klika velikost $\ge k$? (Pro všechny množiny vrcholů velikosti $k$ platí, že netvoří klikou)
>
> Můžeme se ptát ale na složitější otázky:
>
> - **“Existuje** $x$, takové že **pro všechna** $y$ platí nějaká vlastnost?”
> - Např. Problém $\text{EXACT-CLIQUE}$ _— Má největší klika v grafu_ $G$ **_přesně_** $k$ _uzlů?_ _(_Existuje klika velikosti k, přičemž každá jiná klika má velikost nejvýše k.)
> - Musíme navíc ověřit, že **žádná** klika nemá víc než $k$ uzlů → zdá se těžší než $\text{NP}$

- Polynomiální hierarchie _slouží ke klasifikaci problémů,_ které jsou **_„obtížnější než_** $\text{NP}$ **_“_**, ale stále _řešitelné v polynomiálním čase_ s vhodným oraclem.

---

# 1. Třídy $\Sigma_k^p$ a $\Pi_k^p$

> [!success]
> Pro $k \ge 1$ řekneme, že jazyk $L$ patří do třídy $\Sigma_k^p$, pokud existuje **DTS** $M$ s **polynomiální časovou složitostí** a **polynom** $q$ tak, že
>
> $$
> x \in L \Lrarr (\exists u_1)(\forall u_2)(\exists u_3)...(Q_ku_k)\ M(x,u_1,u_2, ..., u_k)=1
> $$
>
> kde
>
> - pro **liché** $i$ je $Q_i=\exists$
> - pro **sudé** $i$ je $Q_i = \forall$
> - pro všechna $i=1,...,k$ platí $|u_i|< q(|x|).$

> [!danger]
> **Proč deterministický TS?**
>
> $M$ **deterministický Turingův stroj**, který běží v polynomiálním čase.  
> Veškerá "nedeterminističnost" je _přesunuta do kvantifikátorů_ před vstupy $u_i$  
> Stroj $M$ _pouze polynomicky ověřuje_ (verifikátor)

> [!success]
> _Analogicky definujeme_ **třídu** $Πₖᵖ$
>
> $$
> x ∈ L ⟺ (∀u₁)(∃u₂)(∀u₃)…(Qₖuₖ) M(x, u₁, …, uₖ) = 1
> $$
>
> tedy **první kvantifikátor je univerzální** a _ostatní se opět pravidelně střídají_.

> [!info]
> Platí proto $Πₖᵖ = coΣₖᵖ$ (doplněk třídy $Σₖᵖ$).

## **1.1** Bezprostřední důsledky

| Tvrzení | Zdůvodnění |
| --- | --- |
| $\Sigma_1^p = \mathrm{NP}$ | Definice s jedním $\exists u_1$ je přesně definice polynomiální verifikovatelnosti. |
| $\Sigma_i^p \subseteq \Sigma_j^p$ pro $i \leq j$ | Na konec přidáme **fiktivní kvantifikátory**, jejichž řetězce stroj $M$ prostě **ignoruje**. |
| $\mathrm{EXACT\text{-}CLIQUE} \in \Sigma_2^p$ | Viz kvantifikátorový zápis v úvodu |

---

# 2. Charakterizace pomocí ATS

> [!success]
> ATS $M$ je $\Sigma_k\text{-stroj}$, pokud pro každý vstup a každou výpočetní větev platí:
>
> - výpočet lze rozdělit do **nejvýše** $k$ **intervalů**,
> - v každém intervalu jsou **jen univerzálně** nebo **jen existenčně** alternující konfigurace,
> - **první interval** obsahuje **existenční** alternující konfigurace.
>
> _Analogicky_ $\Pi_k\text{-stroj}$ začíná **univerzálním** intervalem.

> [!info]
> **Věta (charakterizace přes ATS):**
>
> $\Sigma_k^p = \set{ L(M)\ |\ M \text{ je } \Sigma_k\text{-stroj s polynomickou časovou složitostí }}$

> [!warning]
> **Důkaz:**
>
> **(** $⇒$ **) Z definice pomocí kvantifikátorů sestrojíme ATS**
>
> - Nechť $L\in \Sigma_k^p$.  
>   Z definice tedy _existuje DTS M s polynomiální časovou složitostí a polynom_ $q$, že $x \in L \Lrarr (\exists u_1)(\forall u_2)(\exists u_3)...(Q_ku_k)\ M(x,u_1,u_2, ..., u_k)=1$
> - ATS nejprve **vygeneruje všechny řetězce** $u_1,u_2, ..., u_k$
>   - pokud _je kvantifikátor_ $\exists$, použije _existenční alternaci_,
>   - pokud _je kvantifikátor_ $\forall$, použije _univerzální alternac_i.
> - Po vygenerování už _pouze deterministicky simuluje stroj_ $M$ _na vstupu_ $(x,u_1,…,u_k)$
> - Protože _každý řetězec_ $u_i$ má **polynomiální délku** a $M$ běží **v polynomiálním čas**e, běží v _polynomiálním čase i celý AT_S.
>
> ($⇐$ **) Z ATS vytvoříme kvantifikátorovou definici**
>
> - Nechť nyní $L$ rozpoznává _polynomiální_ $\Sigma_k\text{-stroj} \ A$
> - Výpočet **každé větve** lze rozdělit _do_ **nejvýše** $k$ _bloků_ alternací.
> - Protože $A$ _běží v polynomiálním čase_, existuje _tedy polynom_ $q$ tak, že _každý z intervalů_ obsahuje **nejvíce** $q(|x|)$ **konfigurací**.
> - Nedeterministické volby, které _určují konkrétní výpočetní větev_ lze tedy _pro každý interval reprezentovat řetězcem_ **délky maximálně** $q(|x|)$
> - Sestrojíme deterministický TS $M$, který dostane _vstup_ $(x,u_1,…,u_k)$ a simuluje činnost $A$ pro x. Výpočetní větev vybírá podle $u_1,…,u_k$
> - Přijímá pokud $A$ se dostane do A-přijímající konfigurace.
> - Dostáváme tedy $x \in L \Lrarr (\exists u_1)(\forall u_2)(\exists u_3)...(Q_ku_k)\ M(x,u_1,u_2, ..., u_k)=1$

---

# 3. Polynomiální hierarchie $\text{PH}$

> [!success]
> **Polynomiální hierarchie** je sjednocení všech tříd $\Sigma_k^P$
>
> $$
> \text{PH}=⋃_{i \ge1}\Sigma_i^P
> $$

> [!info]
> **Věta:**  
> **(a)** Pro $k \ge 1$ platí $\Sigma_k^p ∪ \Pi_k^p \sube \Sigma^p_{k+1} ∩ \Pi^p_{k+1}.$  
> **(b)** $\text{PH} \sube \text{PSPACE}.$

> [!warning]
> **Důkaz**:
>
> **(a)** Do definice $\Sigma_k^p$ i $\Pi_k^p$ lze **přidat kvantifikátor navíc** (na začátek nebo konec), jehož řetězec stroj $M$ **ignoruje**.
>
> **(b)** Jazyky z $\text{PH}$ mají **konstantní** počet alternací,$\mathrm{PSPACE}=\mathrm{APTIME}$ připouští **polynomiální** počet alternací. Konstanta $\leq$ polynom, tedy $\Sigma_k \text{-stroj}$ je speciální případ polynomiálního ATS.

> [!info]
> **Věta (o kolapsu polynomiální hierarchie):**  
> **(a)** Pokud $P = NP,$ pak $P=PH.$  
> **(b)** Pro $i \ge 1:$ pokud $\Sigma_i^p=\Pi_i^p,$ pak $PH=\Sigma_i^p.$

> [!warning]
> **Důkaz**:
>
> Indukcí.

> [!note]
> **Co to tvrdí:** Kdykoliv se dvě sousední vrstvy _„slijí"_ ($Σᵢᵖ = Πᵢᵖ$), celá hierarchie kolabuje na tuto úroveň — všechny vyšší vrstvy jsou nadbytečné. Stejně tak pokud $\text P = \text{NP}$, celá hierarchie se _„zhroutí"_ na $\text P$
>
> - **Kolaps by byl dramatický** — znamenal by, že složité problémy hierarchie mají jednoduché algoritmy.
> - Proto věříme, že $\text P ≠ \text{NP}$ a hierarchie je skutečně nekonečná — jinak by měla celá složitostní teorie jiný tvar.

---

# 4. Úplné problémy pro jednotlivé úrovně

- Každá úroveň polynomiální hierarchie má _své vlastní úplné problémy_, které reprezentují **nejtěžší problémy dané třídy** — každý jiný problém z téže třídy na ně lze _převést polynomiální redukcí_ $\leq_p$

> [!success]
> Nejprve zavedeme **pomocný** **(umělý)** **jazyk**
>
> Pro _přirozené_ $k$ definujeme jazyk
>
> $$
> H_k=\set{M\#x\#^m\ |\ M(m,k)\text{-přijímá } x \text{ a jeho počáteční stav je existenčně alternující}}
> $$
>
> kde $(m,k)\text{-přijetí} \ x$ je definováno takto:
>
> - Ve výpočetním stromu ATS $M$ pro vstup $x$ **zkrátíme větve**, na kterých je provedeno více než $m$ kroků nebo které obsahují více než $k$ intervalů alternace, tak, aby měly nejvýše $m$ kroků a nejvýše $k$ intervalů alternace (v jedné z možností nastane rovnost).
> - Na takto ořezaný strom aplikujeme **běžnou definici A-přijímání**.

> [!note]
> **Intuice:** $H_k$ je $\Sigma_k\text{-verze}$ problému zastavení s časovým limitem

> [!info]
> **Věta:** $H_k$ je $\Sigma_k^p\text{-úplný}.$

---

# 5. Oracle stroje a alternativní definice hierarchie

> [!warning]
> **Oracle pro jazyk** $L$ je externí zařízení, které v **jednom kroku** rozhodne, zda $x \in L$.
>
> $M^B$ rozhodující $A$ znamená **Turingovskou redukci** $A \leq_T B$.

> [!success]
> Pro jazyk $B$
>
> $$
> P^B=\set{L(M)\ |\ M \text{ je DTS s pol. čas. slož. a přístupem k oracle pro } B}\\ NP^B=\set{L(M)\ |\ M \text{ je NTS s pol. čas. slož. a přístupem k oracle pro } B}
> $$
>
> Pro **množinu jazyků** $\mathcal{L}$:
>
> $$
> P^{\mathcal{L}}=⋃_{L \in \mathcal{L}}P^L,\ \ \ \ \ NP^{\mathcal{L}}=⋃_{L \in \mathcal{L}}NP^L
> $$

## 5.1 Rozdíl $\le_p$ a $\le_T$

- $L_1 \le_p L_2$ **implikuje** $L_1 \le_T L_2$ (many-one je speciální případ: spočítám $f(x),$ položím jeden dotaz, odpovím shodně).
- Opačně to neplatí: $\text{SAT} \le_T \overline{\text{SAT}}$ triviálně (položím dotaz a **odpověď obrátím**), zatímco $\text{SAT} \le_p \overline{\text{SAT}}$ by implikovalo $NP=coNP.$
- **Proč:** Turingovská redukce může orákulum volat vícekrát a hlavně **negovat odpověď**. Many-one ne — proto je citlivá na doplňky.

## 5.2 Oracle charakterizace hierarchie

> [!success]
> $NP_1 = NP, \ \ \ \ NP_{k+1 }= NP^{NP_k} \Rightarrow \boxed{NP_k=\Sigma_k^p}$