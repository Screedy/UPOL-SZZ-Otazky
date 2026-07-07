## 1. PPM (Prediction by Partial Matching)

### 1.1 **Popis a principy**

- **PPM** je _adaptivní kontextová kompresní metoda_, která modeluje pravděpodobnosti výskytu symbolů na základě předchozího kontextu.

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů ze zdrojové abecedy
> - Číslo $K\ ...$maximální délka kontextu
>
> **Výstup**:
>
> - Pravděpodobnostní model (odhad pravděpodobností symbolů pro daný kontext)

**1.1.1 Kontextová metoda**

- Statistické metody (Huffman, aritmetické kódování) typicky pracují s **pravděpodobnostním modelem bez kontextu** — předpokládají, že výskyt symbolu je nezávislý na okolních symbolech.
- Ve skutečných datech **výskyt symbolu závisí na předchozích symbolech**.
- **Kontextové metody** tuto závislost explicitně modelují pomocí **Markovova modelu** $k$**-tého řádu**
  - Pravděpodobnost symbolu je podmíněna posloupností $k$bezprostředně předchozích symbolů (= **kontext délky** $k$).
  - Čím přesněji model predikuje další symbol, tím kratší kód mu může přiřadit → **vyšší míra komprese**.

> [!success]
> **Formálně:** Kontext délky$k$symbolu$a$na pozici$j$: $c_k = a_{j-k} a_{j-k+1} \dots a_{j-1}$
>
> **Podmíněná pravděpodobnost**: $P(a \mid c_k)$

> [!info]
> **Příklad:** Na vstupu `barbaraabarboraubaru`. Po kontextu `ba` vždy následuje `r`.
>
> $P(r \mid ba)$ je vysoká → symbol `r` v tomto kontextu _dostane krátký kód_.

**1.1.2 Klíčové principy PPM**

- Je adaptivní protože nezjišťuje kontexty dané délky _pro všechny symboly_, ale pouze pro ty, **co jsou na vstupu**.
- Metoda udržuje **průběžné (adaptivní) odhady** podmíněných pravděpodobností $P(a \mid c_k)$pro kontexty délek $k = K, K-1, \dots, 0, -1$.

**Escape mechanismus**

- Využívá se speciálního **escape symbolu ε**, který značí, že _symbol na vstupu_ se _v aktuálním kontextu ještě nevyskytl_.

**Kontext** $c_{-1}$**(kontext délky -1)**

- Představuje „nouzový" kontext pro **první výskyt** symbolu.
- Všechny symboly mají počáteční četnost $n(a \mid c_{-1}) = 1$→ _uniformní rozložení_.

---

### 1.2 Pseudokód

```
while načti ze vstupu symbol a ∈ A do:
  k ← k_max ← min{K, počet dosud načtených symbolů − 1} // Vezmi menší, K = max kontext
  while k ≥ 0 AND n(a|c_k) = 0 do: // Můžeme zkrátit kontext a symbol se ještě nevyskytl
      zapiš na výstup kód symbolu ε v kontextu c_k
      k ← k − 1
  zapiš na výstup kód symbolu a v kontextu c_k
  aktualizuj n(a|c_l) ← n(a|c_l) + 1 pro všechny kontexty c_l, k_max ≥ l ≥ 0 symbolu a
```

- Pokud se symbol $a$v kontextu$c_k$dosud **nevyskytl**, _zapíše se escape_ ε a _přejde se na kratší kontext_ $c_{k-1}$; to se opakuje, dokud se$a$v **některém kontextu najde** nebo se **nedosáhne kontextu** $c_{-1}$.

---

### 1.3 Příklad tvorby pravděpodobnostního modelu

![](/api/files/019c95c6-5820-757d-a43f-a09203fb1ecf/MacBook-2026-02-25-004175@2x.png)

---

### 1.4. Dekódování PPM

```
k ← k_max ← 0   //Obě proměnné nastavit na 0
while načti ze vstupu a dekóduj kód symbolu a ∈ A|c_k v kontextu c_k do:
    if a = ε:           
        k ← k − 1       // Přejdi na kratší kontext
    else:
        zapiš na výstup symbol a
        aktualizuj n(a|c_l) ← n(a|c_l) + 1 pro kontexty c_l, k_max ≥ l ≥ 0 symbolu a
        k ← kmax ← min{K, počet dekódovaných symbolů}
```

- Dekodér postupuje **stejně jako kodér**: začíná v _nejdelším kontextu_, při _escape přechází na kratší_.

---

### 1.5 Odhady pravděpodobností

Pro každý kontext $c_k$a symbol $a_i$z abecedy kontextu $A|c_k \subseteq A \cup {\varepsilon}$:

$$
f(a_i \mid c_k) = \frac{n(a_i \mid c_k)}{\sum_{j=1}^{|A|c_k|} n(a_j \mid c_k)}
$$

kde $n(a_i \mid c_k)$je počet výskytů symbolu $a_i$v kontextu $c_k$.

> [!note]
> **Intuice**: Pravděpodobnost symbolu v daném kontextu se odhaduje jako podíl počtu jeho výskytů po daném kontextu a celkového počtu výskytů všech symbolů v tomto kontextu.

---

### 1.6 Volba maximální délky kontextu $K$

- Vyšší$K\text{.}$Čím vyšší kontext, tím bývá **přesnější předpověď**. _Vyšší pravděpodobnost → lepší komprese_. ALE _dlouhé kontexty_ jsou **v textu vzácné**. Musíme _častěji používat escape symbol_.
- **V praxi:** $K = 5$nebo $K = 6$pro textová data.

---

### 1.6 Datová reprezentace — trie

Četnosti $n(a \mid c_k)$pro všechny kontexty se ukládají v $n\text{-ární stromu}$$T = \langle V, E \rangle$, kde $n = |A|$(velikost abecedy):

- **Vnitřní uzly** odpovídají symbolům kontextu $c_k$: uzel pro symbol $a_{-i}$ kontextu $c_k = a_{-k} \dots a_{-1}$.
- **Listové uzly** ukládají četnosti $n(a \mid c_{k_{max}})$pro symboly $a \in A$.
- Hrany vedou od symbolů kontextu k dalším symbolům/listům.
- **Suffix linky** $s(v(a \mid c_k)) = v(a \mid c_{k-1})$: umožňují rychlý přechod na kratší kontext.
- Pro každý symbol na vstupu se přidá$0$až$K+1$uzlů.![](/api/files/019ec802-4c28-70fc-ada6-24727a4e39aa/obrazek.png)

---

### PAQ

- PAQ je _pokročilá kontextová kompresní metoda_ vycházející z principů PPM. Na rozdíl od PPM _není omezena pouze na kontext tvořený bezprostředně předcházejícími symboly_, ale kombinuje více modelů využívajících různé typy kontextů (context mixing). Může například zohledňovat předchozí bity, znaky, sousední prvky multimediálních dat nebo vybrané dřívější části souboru. Díky kombinaci těchto predikcí dosahuje **velmi vysoké komprese**, avšak za _cenu vyšších nároků na paměť a výpočetní výkon_.