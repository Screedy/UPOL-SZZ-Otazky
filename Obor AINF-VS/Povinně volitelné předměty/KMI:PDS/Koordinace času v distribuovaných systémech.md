> [!warning]
> V mnoha případech je potřeba _koordinace na základě času_. Typicky jsou to _úlohy_, kde je **potřeba časové razítko**. (Nejčastěji na určení správného určení pořadí událostí)

- V distribuovaném systému má však **každý uzel své vlastní hodiny**, které se však můžou navzájem rozcházet u mnoha důvodů. Například:
  - Nepřesnost křemenných oscilátorů (nejčastější důvod)
  - Změna teploty
  - Stárnutí hardwaru
  - Kolísání napájení
  - Výrobní odchylky

> [!danger]
> **Zásadní omezení: čas nelze vrátit zpět.**
>
> - Pokud zjistíme, že naše hodiny “moc dopředu”, **nemůžeme je prostě nastavit dozadu**. To by způsobilo, že by _dvě různé události dostaly stejný timestamp_ nebo by _novější událost vypadala jako starší_
> - Místo toho hodiny **zpomalíme**

- Existují _dvě hlavní skupiny řešení:_
  - **Synchronizace fyzického času**
    - Snažíme se, aby všechny _počítače ukazovali přibližně stejný čas._
  - **Synchronizace logického času**
    - Nezajímá nás skutečný čas, zajímá nás, která _událost nastala dříve_

---

# 1. Synchronizace fyzického času

## 1.1 Cristianův algoritmus

- Byl navržen v roce 1989 _Cristianem Flaviem_, brazilským informatikem.
- Předpokládá, že existuje **jeden server**, jehož **hodiny jsou přesné** (např. synchronizované pomocí GPS nebo atomových hodin). Ostatní počítače si od něj _pravidelně zjišťují aktuální čas_ a _podle něj upravují své hodiny_.

### 1.1.1 Princip

1. Uzel **pošle žádost** o aktuální čas a **uloží so čas požadavku** $t_1$
2. Server obdrží žádost a odpoví zprávou obsahující **aktuální čas serveru** $t_s$
3. Uzel si zaznamená **čas přijetí** $t_2$
4. Uzel vypočítá jednostranné **zpoždění**: $\frac{t_2 - t_1}{2}$
  - Předpokládá, že _cesta tam a zpět, byla přibližně stejná_.
5. **Nastaví** své hodiny: $t_{new}=t_s+\text{delay}$

### 1.1.2 Vlastnosti

- Velmi jednoduchý
- Snadná implementace
- **Největší problém**: Předpokládá stejnou dobu přenosu tam, i zpět.
- Závislí na _jednom serveru_ (single point of failure)

## 1.2 NTP

- **NTP (Network Time Protocol)** je nejpoužívanější protokol pro synchronizaci hodin počítačů přes síť.

> [!info]
> V běžném Internetu dosahuje přesnosti v řádu **milisekund**, v lokální síti často i **desítek až stovek mikrosekund**.

### 1.2.1 Hierarchie serverů

- **NTP servery** jsou organizovány do **hierarchie označované jako stratum**, která určuje, jak daleko je daný server _od původního zdroje přesného času_.
- Čím **nižší číslo** stratum, tím _přesnější a spolehlivější_ je zdroj času.
- Hierarchie zajišťuje _škálovatelnost_ a _zabraňuje přetížení_ nejpřesnějších časových serverů.

- **Stratum 0** – referenční zdroje času (GPS, atomové hodiny), **nejsou to NTP servery**
- **Stratum 1** – servery přímo synchronizované se Stratum 0.
- **Stratum 2** – synchronizují se se Stratum 1.
- **Stratum 3** – synchronizují se se Stratum 2.
- Princip pokračuje i do dalších vrstev.

### 1.2.2 Princip

- Při jedné komunikaci se zaznamenají **čtyři časové značky**

1. Uzel _požádá server_ a **uloží čas požadavku** $t_1$
2. Server **přijme požadavek** v čase $t_2$ a **odpoví svým aktuálním časem** $t_3$
3. Klient obdrží odpověď a **uloží čas přijetí** $t_4$
4. Výpočty:
  - **Round-trip delay**. Doba, kterou zprávy _skutečně strávily v síti_ (bez času, kdy server požadavek zpracovával)
    - $\text{RTD}=(t_4-t_1)-(t_3-t_2)$
  - **Odchylka hodin**. Udává, _o kolik jsou hodiny klienta posunuté_ vůči serveru.
    - $\text{offset}=\frac{(t_2-t_1) + (t_3-t_4)}{2}$
      - $\text{offset}>0$— Hodiny jsou **pozadu** a musí je _posunout_
      - $\text{offset}<0$— Hodiny jsou **napřed** a musí je _zpomalit_

### 1.2.3 Vlastnosti

- **Standard** používaný prakticky na všech operačních systémech
- _Odolný vůči výpadku_ jednoho serveru
- Přesnost stále _závisí na kvalitě sítě_

## 1.3 Berkeley algoritmus

- Nepředpokládá _existenci přesného časového serveru_. Místo toho je jeden počítač zvolen jako **koordinátor (master)**, který _zajišťuje synchronizaci_ s ostatními uzly.

> [!danger]
> Důležité je, že **nikdo není považován za absolutně správný zdroj času**. Cílem je shoda všech uzlů.

### 1.3.1 Princip

1. Koordinátor **osloví všechny uzly** o jejich čas
2. Uzly **odešlou** svůj čas
3. Koordinátor vypočítá **průměrný čas**
4. Koordinátor **spočítá korekce** pro každý uzel
5. Uzly **upraví** své hodiny

> [!info]
> Berkeley algoritmus je vhodný například v **uzavřených lokálních distribuovaných systémech**, kde není dostupný externí zdroj přesného času, ale je důležité, aby všechny počítače měly mezi sebou shodný čas.

### 1.3.2 Vlastnosti

- Nevyžaduje GPS ani atomové hodiny
- Výsledný čas nemusí být skutečný (UTC), pouze společný pro všechny uzly
- Koordinátor představuje **single point of failure**
- Je potřeba komunikovat se všemi uzly, což zvyšuje režii

## 1.4 RBS

- **RBS (Reference Broadcast Synchronization)** je algoritmus pro synchronizaci fyzických hodin, který využívá **referenční broadcastovou zprávu**.
- Základní myšlenkou je, že **odesílatel do zprávy vůbec nevkládá svůj čas**. Důležitý je pouze _okamžik_, kdy jednotlivé _uzly_ tuto _zprávu přijmou_.

### 1.4.1 Princip

- Představme si _tři uzly_:
  - **m** – vysílač,
  - **p** a **q** – přijímači.

1. Uzel **m** vyšle _jednu broadcastovou zprávu_ sousedům **p** a **q**.
2. Po přijetí zprávy si každý uzel **uloží čas** _podle svých vlastních hodin_.
  - Uzel **p** uloží čas $T_{pm}$
  - Uzel **q** uloží čas $T_{qm}$
3. Uzly si **časy vymění**
4. **Spočítají** vzájemný offset

### 1.4.2 Vlastnosti

- Vhodný pro bezdrátové a senzorové sítě
- Eliminuje chybu při vysílání zprávy (Např. operační systém může zprávu chvíli zdržet, síťová karta ji nemusí ihned vyslat…)
- Funguje hlavně tam, kde je možné využít broadcast
- Neposkytuje absolutní čas (UTC), pouze synchronizuje hodiny mezi uzly

---

# 2. Synchronizace logického času

## 2.1 Lamportovy logické hodiny

- Při synchronizaci fyzických hodin _nikdy nedokážeme zajistit_, že všechny uzly budou **ukazovat úplně stejný čas**. V mnoha distribuovaných algoritmech ale ani **není důležité znát skutečný čas**. Důležitější je vědět, _která událost nastala dříve a která později_.
- Proto Leslie Lamport navrhl **logické hodiny**, které neurčují skutečný čas, ale **pořadí událostí v distribuovaném systému**.

### 2.1.1 Princip

- **Lokální hodiny**
  - Každý uzel si **udržuje čítač**, který je při _vykonání jakékoliv operace inkrementován o 1_.
  - Při _zaslání zprávy inkrementován_ a **poslán společně** se zprávou.
  - Když jiný _uzel zprávu přijme_ zprávu porovná svůj čítač s čítačem ve zprávě a **nastaví**: $L=max(L,L_{zpráva})+1$

> [!danger]
> **Co hodiny zaručují**: Pokud událost _A způsobila událost B_, pak vždy platí $L(A)<L(B)$
>
> **Co hodiny nezaručují**: Neumí určit _pořadí nezávislých událostí_ na různých procesech, jelikož **neexistuje** mezi nimi **žádný kauzální vztah**.
>
> ---
>
> - **Zaručují:** $a \to b \Rightarrow L(a) < L(b)$
> - **Nezaručují obráceně:** $L(a) < L(b) \not\Rightarrow a \to b$— nízké číslo neznamená kauzální předcházení

### 2.1.2 Vlastnosti

- Zachovává _kauzální pořadí událostí_
- Nevyžaduje _synchronizaci fyzických hodin_ (neurčuje skutečný čas)
- Neumí rozpoznat současně probíhající události

---

## 2.2 Vektorové hodiny

- Lamportovy hodiny mají zásadní slabinu:
  - z $L(a) < L(b)$ **nelze usoudit**, že $a \to b$
- **Vektorové hodiny** tento problém řeší
  - $\vec{V}(a) < \vec{V}(b) \Leftrightarrow a \to b$

### 2.2.1 Princip

- _Každý uzel_ $P_i$ **udržuje vektor** $\vec{V}_i = [v_1, v_2, \ldots, v_n]$ kde $n$ je _počet uzlů_.
  - $\vec{V}_i[i]$ je **lokální logický čas uzlu** $i$
  - $\vec{V}_i[j] = k$ znamená: _„Uzel i ví, že Uzel j provedl alespoň_ $k$ _operací"_

**Pravidla aktualizace:**

```
Inicializace:
  V_i = [0, 0, ..., 0]

Pravidlo 1 (lokální událost):
  V_i[i] = V_i[i] + 1

Pravidlo 2 (odeslání zprávy):
  V_i[i] = V_i[i] + 1
  Zpráva nese kopii celého vektoru V_i

Pravidlo 3 (přijetí zprávy):
  V_i[i] = V_i[i] + 1
  Pro všechna j ≠ i: V_i[j] = max(V_i[j], V_m[j])
```

### 2.2.2 Uspořádání vektorů

Pro vektory $\vec{V}_1$ a $\vec{V}_2$:

$$
\vec{V}_1 \leq \vec{V}_2 \iff \forall i: \vec{V}_1[i] \leq \vec{V}_2[i]
$$
$$
\vec{V}_1 < \vec{V}_2 \iff \vec{V}_1 \leq \vec{V}_2 \wedge \vec{V}_1 \neq \vec{V}_2
$$

> [!note]
> **Intuice**:
>
> 1. Každá složka vektoru $V_1$ musí být _menší nebo rovna_ odpovídající složce vektoru $V_2$
> 2. Zároveň nesmí být oba vektory stejné → **alespoň jedna složka je přísně menší**

**Srovnání dvou událostí** $a$ a $b$ na jiných uzlech:

- $a \to b \iff \vec{V}_i(a) < \vec{V}_j(b)$
- $b \to a \iff \vec{V}_j(b) < \vec{V}_i(a)$
- $a | b \iff$ vektory jsou **neporovnatelné = konkurenční** (ani jeden není $\leq$ druhému)

![[019f71a2-386f-7129-abcb-fc9832dc9861.png]]

### 2.2.3 Vlastnosti

- Zachovávají kauzální pořadí
- Umí rozpoznat nezávislé (konkurenční) události
- Každý proces musí uchovávat vektor o velikosti počtu procesů
- Při velkých distribuovaných systémech jsou náročnější na paměť i komunikaci