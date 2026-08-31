- **Chord** je _protokol založený na distribuované hashovací tabulce_ (Distributed Hash Table – DHT). **Definuje pravidla** (proto je to protokol), podle kterých _uzly ukládají data_, _vyhledávají je_ a _reagují na připojování či odpojování dalších uzlů_. Patří mezi **strukturované peer-to-peer (P2P) systémy**.

> [!warning]
> **Peer-to-peer síť** je _decentralizovaná architektura_, ve které každý uzel může _současně vystupovat jako_ **klient i server**. Neexistuje zde _žádný centrální server,_ takže odpadá _problém jediného bodu selhání_ (single point of failure).
>
> **Nestrukturovaná P2P** — Uzly nemají _žádnou předem danou topologii_. _Vyhledání klíče_ může vyžadovat $O(n)$ **zpráv**, není zaručeno nalezení.
>
> **Strukturovaná P2P** — Topologie a umístění dat se _řídí deterministickým pravidlem_. **Vyhledání klíče v** $O(\log n)$.

---

# 1. Konzistentní hashování

> [!info]
> _Jak systém pozná, na kterém uzlu mají být konkrétní data uložena?_
>
> K tomu Chord využívá **konzistentní hashování**. Jeho úkolem je přiřadit každému uzlu i každému klíči (identifikátor dat) jednoznačný identifikátor a podle něj rozhodnout, **který uzel bude za daná data zodpovědný**.

## 1.1 Princip

- Použije se **hashovací funkce** (například SHA-1), s $m$ **-bitovým výstupem**, tedy prostor _identifikátorů je od_ $0$ _do_ $2^m - 1$
- Tento prostor identifikátorů si představujeme jako **logický kruh (ring)**.
- **Do stejného kruhu** se mapují:
  - **uzly** — Jejich identifikátor vznikne například jako hash IP adresy/jména,
  - **klíče** — Jejich identifikátor vznikne jako hash daného klíče.
- Díky tomu se uzly i data nacházejí ve stejném adresním prostoru.

> [!info]
> **Klíč je identifikátor dat**, podle _kterého Chord určuje, na kterém uzlu budou tato data uložena_. Může jím být například _název souboru, ID uživatele nebo jiný jednoznačný identifikátor_.

## 1.2 Přiřazení klíčů uzlům

- Každý klíč je uložen na **prvním uzlu, na který narazíme při pohybu po kruhu ve směru hodinových ručiček**.
- Tento uzel se nazývá **následník** **(successor)** **klíče** a značí se **succ(k)**.

### 1.2.1 Příklad

- $m=4$
- **Uzly: 1, 4, 9, 11, 14**
  - Klíč $k = 6$: klíč 6 je uložen na uzlu 9
  - Klíč $k = 10$: klíč 10 je na uzlu 11
  - Klíč $k = 15$: klíč 15 je na uzlu 1

![[019f9f49-2bce-77ef-abd5-75afcdb5bc23.png]]

## 1.3 Vlastnosti konzistentního hashování

- Při přidání/odebrání uzlu se přesouvá pouze $O(K/n)$ klíčů (kde $K$= počet klíčů, $n$= počet uzlů).
- Srovnej s klasickým hashováním ($k \mod n$), kde změna $n$ vyžaduje přemapování téměř všech klíčů.
- Rozložení klíčů je rovnoměrné

> [!danger]
> Teoreticky mohou _nastat hashovací koliz_e, kdy dva různé klíče vytvoří stejný hash. Chord ale **používá kvalitní hashovací funkce** _s velmi velkým adresním prostorem_, takže pravděpodobnost kolize je v praxi zanedbatelná a **protokol ji běžně neřeší**.

---

# 2. Vyhledávání klíče (lookup)

## 2.1 Naivní přístup

- Nejjednodušší způsob vyhledávání předpokládá, že **každý uzel zná pouze svého přímého následníka** v kruhu.

1. Uzel _přijme požadavek_ na vyhledání klíče **k**.
2. Zkontroluje, zda klíč _patří jeho následníkovi_.
  1. $k$ leží v intervalu $(\text{id}, \text{succ}.\text{id}]$
3. Pokud **ano**, _vrátí tohoto následníka_.
4. Pokud **ne**, _předá požadavek svému následníkovi_.
5. Stejný postup se **opakuje**, dokud není nalezen uzel _odpovědný za daný klíč_.

![[019f9f60-d66f-72e8-8ba3-522fdfc137d5.png]]

> [!warning]
> **Složitost:** $O(n)$ **hopů** v nejhorším případě — musíme projít celý kruh.

## 2.2 Finger Table

- Místo toho, aby každý uzel znal _pouze svého přímého následníka_, uchovává si také **Finger Table** – směrovací tabulku **obsahující odkazy na vzdálenější uzly**.
- To umožňuje v každém kroku _přeskočit přibližně polovinu zbývající vzdálenosti ke klíči_ → $O(\log n)$ **hopů**.

### 2.2.1 Struktura Finger Table

- Každý uzel obsahuje **m záznamů**, kde **m** je počet bitů identifikátoru.
- Pro **i-tý** záznam platí:

$$
FT_{\text{id}}[i] = \text{succ}(\text{id} + 2^{i-1}) \mod 2^m
$$

kde:

$id$ je _identifikátor uzlu_,

$succ()$ označuje _následníka dané pozice na kruhu_.

### 2.2.2 Příklad

**Finger table uzlu 1:**

| $i$ | Start = $(1 + 2^{i-1}) \mod 16$ | $FT_1[i] = \text{succ}(\text{start})$ |
| --- | --- | --- |
| 1   | $(1+1) = 2$ | $\text{succ}(2) = 4$ |
| 2   | $(1+2) = 3$ | $\text{succ}(3) = 4$ |
| 3   | $(1+4) = 5$ | $\text{succ}(5) = 9$ |
| 4   | $(1+8) = 9$ | $\text{succ}(9) = 9$ |

**Finger table uzlu 9:**

| $i$ | Start = $(9 + 2^{i-1}) \mod 16$ | $FT_9[i] = \text{succ}(\text{start})$ |
| --- | --- | --- |
| 1   | $(9+1) = 10$ | $\text{succ}(10) = 11$ |
| 2   | $(9+2) = 11$ | $\text{succ}(11) = 11$ |
| 3   | $(9+4) = 13$ | $\text{succ}(13) = 14$ |
| 4   | $(9+8) = 1$ | $\text{succ}(1) = 1$ |

## 2.3 Vyhledávání pomocí Finger Table

- _Při vyhledávání klíče uzel_ využívá svou **Finger Table**, ve které hledá záznam s **identifikátorem co nejblíže hledanému klíči**, aniž **by jej překročil**. Dotaz poté _přepošle na odpovídající uzel_ a stejný _postup se opakuje_, dokud není nalezen uzel odpovědný za daný klíč.
- **Krajní případy**:
  - Klíč je **menší než první položka** Finger Table → Pošlu _na první položku FT_
  - Klíč je **větší než všechny položky** Finger Table → Pošlu na _poslední položku_ FT

### 2.3.1 Příklad průběhu

Hledáme klíč $k = 12$ a začínáme na uzlu **1**:

1. **Uzel 1:** Je $12 \in (1, 4]$? Ne. Hledám `closest_preceding_finger(12)`:
  - $FT_1[4] = 9$: je $9 \in (1, 12)$? Ano → přepošli na uzel **9**.
2. **Uzel 9:** Je $12 \in (9, 11]$? Ne. Hledám `closest_preceding_finger(12)`:
  - $FT_9[3] = 14$: je $14 \in (9, 12)$? Ne.
  - $FT_9[2] = 11$: je $11 \in (9, 12)$? Ano → přepošli na uzel **11**.
3. **Uzel 11:** Je $12 \in (11, 14]$? Ano → vrať uzel **14** .

> [!warning]
> **Složitost**:$O(\log n)$ **hopů**

![[019f9f9a-8284-75bf-bf8e-5d900d6a2808.png]]

---

# 3. Operace s uzly

## 3.1 Připojení nového uzlu

Když se do sítě připojí nový uzel $n$:

1. **Nový uzel vytvoří svůj identifikátor** pomocí hashovací funkce.
2. **Nalezení následníka:** $n$ se zeptá $n'$: „Kdo je $\text{succ}(n)$?" → pomocí standardního lookup.
3. **Zařadí se do kruhu** mezi svého předchůdce a následníka.
4. **Přesun klíčů:** Klíče z intervalu $(\text{pred}(n), n]$, které dosud držel $\text{succ}(n)$, se přesunou na $n$.
5. **Aktualizace finger tables:** Ostatní uzly musí aktualizovat své finger tables, pokud $n$ ovlivňuje jejich záznamy.

## 3.2 Odpojení uzlu

Když uzel $n$ odchází:

1. **Přesun klíčů:** Všechny klíče uzlu $n$ se přesunou na $\text{succ}(n)$.
2. **Aktualizace ukazatelů:** Předchůdce uzlu $n$ aktualizuje svůj ukazatel na následníka $n$
3. **Aktualizace finger tables** ostatních uzlů.

---

# 4. Stabilizační protokol

- Po připojení nebo odpojení uzlu nejsou všechny informace v síti okamžitě správné. Některé uzly mohou mít zastaralé ukazatele na svého předchůdce, následníka nebo zastaralé záznamy ve Finger Table. Chord proto využívá **stabilizační protokol**, který tyto _informace průběžně opravuje a zajišťuje, že se síť postupně vrátí do konzistentního stavu_.

- Každý uzel periodicky provádí několik kontrol:
  - ověřuje, zda je jeho **následník (successor)** stále správný,
  - ověřuje, zda je jeho **předchůdce (predecessor)** stále dostupný,
  - postupně aktualizuje záznamy ve své **Finger Table**

---

# 5. Odolnost vůči chybám

- V distribuovaném systému _může kdykoliv dojít k výpadku uzlu_. Pokud by každý uzel znal **_pouze svého přímého následníka_**, mohl by výpadek způsobit **přerušení kruhové struktury** a **znemožnit vyhledávání některých klíčů**.

- Proto Chord obsahuje mechanismy, které umožňují pokračovat v činnosti i při selhání uzlů.

## 5.1 Successor list

- Každý uzel si neuchovává pouze jednoho následníka, ale **seznam několika po sobě jdoucích následníků (Successor List)**.
- Pokud _přímý následník přestane reagovat_, uzel **využije dalšího** následníka ze seznamu. Díky tomu zůstává kruh propojen i při výpadku jednoho nebo několika uzlů.

## 5.2 Replikace klíčů (dat)

- Pro **zvýšení dostupnosti se klíče** často _neukládají pouze na jeden uzel_, ale také na _několik jeho následníků_.
- Pokud odpovědný uzel selže, lze data získat z některé z replik.

## 5.3 Omezení Chordu

- Chord předpokládá **crash failures**, tedy situaci, kdy uzel jednoduše přestane komunikovat.
- **Neřeší byzantské chyby**, kdy uzel záměrně poskytuje nesprávné informace nebo se chová škodlivě. Pro takové prostředí jsou potřeba jiné mechanismy nebo nadstavby.