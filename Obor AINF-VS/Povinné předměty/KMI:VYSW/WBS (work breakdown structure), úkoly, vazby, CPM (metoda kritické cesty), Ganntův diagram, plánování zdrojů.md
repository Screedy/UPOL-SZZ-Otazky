# 1. WBS (Work Breakdown Structure)

> [!success]
> **Work Breakdown Structure** je hierarchický rozklad projektu na menší a lépe řiditelné části.

- Usnadňuje _odhad pracnosti, času a nákladů_.
- _Vytvoří základ pro harmonogram_ projektu.

> [!danger]
> WBS nepopisuje pořadí prací ani jejich časové rozložení. Ukazuje pouze **co je potřeba udělat**.

## 1.1 Princip tvorby

- Každý _prvek WBS má jednoznačný identifikátor_ (číslování: 1.0, 1.1, 1.1.1…)
- Projekt se rozděluje shora dolů:

```
1.0 Projekt
│
├── 1.1 Analýza
│   ├── 1.1.1 Sběr požadavků
│   ├── 1.1.2 Analýza procesů
│   └── 1.1.3 Specifikace
│
├── 1.2 Návrh
│   ├── 1.2.1 Architektura
│   ├── 1.2.2 Databáze
│   └── 1.2.3 UI
│
├── 1.3 Implementace
│   ├── 1.3.1 Backend
│   ├── 1.3.2 Frontend
│   └── 1.3.3 API
│
├── 1.4 Testování
│
└── 1.5 Nasazení
```

- Nejnižší úroveň se nazývá _pracovní balík_ (Work Package)
- **Pracovní balík**:
  - Je jednoznačně definovaný
  - Lze odhadnout jeho pracnost
  - Lze za něj určit odpovědnou osobu
  - Lze jej naplánovat
- **Struktura WBS**:
  - **Úroveň 0:** celý projekt (např. „Nový e-shop")
  - **Úroveň 1:** hlavní fáze nebo komponenty (analýza, vývoj, testování, nasazení)
  - **Úroveň 2:** podčásti fází (vývoj → back-end, front-end, databáze)
  - **Úroveň N:** pracovní balíky — konkrétní úkoly přiřaditelné osobě

## 1.2 Pravidlo 100%

- WBS by měla obsahovat **100 % práce potřebné k dokončení projektu**.
- To znamená, že **nic nesmí chybět**, a _nic by se nemělo překrývat_.

## 1.3 Výhody

- Lepší přehled o projektu
- Snadnější plánování
- Odhad nákladů
- Přiřazení odpovědností
- Základ harmonogramu

---

# 2. Úkoly (aktivity)

> [!success]
> Po vytvoření WBS se pracovní balíky převádějí na **konkrétní úkoly (aktivity)**.

- _Každý úkol má obvykle_:
  - **Název**
  - **Identifikátor**
  - **Dobu trvání**
  - **Začátek a konec**
  - **Odpovědnou osobu**
  - **Potřebné zdroje**
  - **Návaznosti na ostatní úkoly**

---

# 3. Vazby mezi úkoly (závislosti)

> [!success]
> _Úkoly na sebe často navazují_.
>
> Vazby **určují pořadí** a **podmínky provádění** úkolů.

**4 typy vazeb:**

| Typ | Zkratka | Popis | Příklad |
| --- | --- | --- | --- |
| Finish-to-Start | FS  | B začne až A skončí | Testování začne až po vývoji |
| Start-to-Start | SS  | A i B začínají současně | Dokumentace začne spolu s vývojem |
| Finish-to-Finish | FF  | B nesmí skončit dříve než A | Testování skončí současně s opravami chyb |
| Start-to-Finish | SF  | B nemůže skončit dokud A nezačne | Střídání směn |

**Prodleva (lag) a předstih (lead):**

- **Lag (+):** B začne 2 dny PO skončení A (např. čekání na vyschnutí betonu)
- **Lead (−):** B začne 2 dny PŘED skončením A (překrývání)

---

# 4. CPM (Critical Path Method)

> [!success]
> **CPM** je _metoda používaná pro plánování projektů_. Jejím cílem je najít **kritickou cestu**, tedy _nejdelší posloupnost vzájemně závislých úkolů_, která určuje **nejkratší možnou dobu trvání projektu**.
>
> Úkoly na kritické cestě **nemají žádnou časovou rezervu**. Pokud se některý _z nich zpozdí, zpozdí se celý projekt_.

## 4.1 Klíčové pojmy

- **ES (Early Start)** — _nejdříve možný začátek_ úkolu.
- **EF (Early Finish)** — _nejdříve možné dokončení_ úkolu.
  - $\text{EF}=\text{ES}+\text{trvání}$
- **LS (Late Start)** — _nejpozdější možný začátek úkolu_, aniž by se zpozdil projekt.
- **LF (Late Finish)** — _nejpozdější možné dokončení úkolu_.
  - $\text{LF} = \text{LS} + \text{trvání}$
- **Float (Slack, časová rezerva)** — doba, _o kterou lze úkol posunout_, aniž _by ovlivnil termín dokončení projektu_.
  - $\text{Float} = \text{LS} − \text{ES} = \text{LF} − \text{EF}$
  - _U úkolů na kritické cestě_ platí **Float = 0**.

## **4.2 Postup výpočtu CPM**

1. **Dopředný průchod** **(Forward pass)**
  - Vypočítávají se _nejdřívější možné termíny_ (**ES** a **EF**) **od začátku projektu**.
    - ES prvního úkolu = 0 (nebo datum zahájení)
    - ES každého dalšího úkolu = nejvyšší hodnota EF jeho předchůdců.
    - $\text{EF}=\text{ES}+\text{trvání}$
2. **Zpětný průchod** **(Backward pass)**
  - Vypočítávají se _nejpozdější přípustné termíny_ (**LS** a **LF**) **od konce projektu**.
    - LF posledního úkolu = EF posledního úkolu (nebo pevně stanovený termín dokončení).
    - LF předchozího úkolu = nejnižší hodnota LS jeho následníků.
    - $\text{LS} = \text{LF} - \text{trvání}$
3. **Určení kritické cesty**
  - Po výpočtu časových rezerv se _určí kritická cesta_.
    - Úkoly s **Float = 0** tvoří **kritickou cestu**.
    - Zpoždění kteréhokoli z těchto úkolů způsobí zpoždění celého projektu.

**Příklad:**

```
        A (3)
       /     \
    B (5)   C (4)
       \     /
        E (2)
```

- Úkoly A, B, E jsou součástí kritické cesty
- Úkol C má Float = 1 den

---

## 5. Ganttův diagram

> [!success]
> Ganttův diagram je **grafické znázornění harmonogramu projektu**.
>
> Na _vodorovné ose je čas_.
>
> Na _svislé ose jsou úkoly_.
>
> _Každý úko_l je zobrazen jako _vodorovný pruh_.

**Příklad**

![](/api/files/019f14dd-8499-73bd-82b2-d1374197ab88/obrazek.png)

## **5.1 Prvky Ganttova diagramu**

- **Pruhy úkolů** — Délka odpovídá trvání
- **Milníky** — Klíčové události s nulovým trváním (diamond/kosočtverec)
- **Vazby** — Šipky mezi pruhy zobrazující závislosti
- **Procento dokončení** — Pruhy mohou být přebarveny dle postupu
- **Kritická cesta** — Úkoly na kritické cestě bývají zvýrazněny (červeně)
- **Základní plán (baseline)** — Původní plán pro srovnání s aktuálním stavem

---

# 6. Plánování zdrojů

> [!success]
> Zdroje představují vše, co _je potřeba pro realizaci projektu_.

- **Jaké jsou zdroje**
  - **Lidské zdroje** — vývojáři, testeři, PM, analytici
  - **Materiální zdroje** — servery, hardware, kancelář
  - **Finanční zdroje** — rozpočet (náklady na lidi + materiál + režii)

## **6.1 Resource allocation (Přidělení zdrojů)**

- Každému úkolu se přiřadí:
  - pracovník,
  - tým,
  - vybavení,
  - rozpočet.
- Zdroj může mít různou **dostupnost** (100 %, 50 % — práce na více projektech)
- **Náklady** = trvání × hodinová sazba × dostupnost

## **6.2 Konflikty zdrojů (přetížení)**

- Pokud je _jeden člověk naplánovaný na více úkolů současně_, je potřeba harmonogram upravit.
- Řeší se **resource leveling** **(vyrovnání zdrojů)**:
  - **Posunutí úkolu** s rezervou — nezpůsobí zpoždění
  - Přidání **nového zdroje**
  - **Změna** rozsahu nebo **harmonogramu**

> [!info]
> **Přidání lidí na zpožděný projekt ho nezrychlí** (Brooksův zákon). Noví lidé potřebují čas na zaškolení, což situaci krátkodobě zhorší.