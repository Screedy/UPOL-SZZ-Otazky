> [!success]
> **Tabulka symbolů** je _datová struktura používaná překladačem_ pro ukládání informací o **deklaracích, definicích** a _dalších údajích odvozených během fází překladu_ (hlavně sémantické analýzy)_._

- _Co se do tabulek ukládá:_
  - **jména a datové typy** proměnných, jejich počáteční hodnoty uvedené v deklaraci
  - u **polí** navíc počet dimenzí a rozsahy jednotlivých dimenzí
  - u **strukturovaných typů** (`struct`, `union`) jejich členy
  - **hlavičky funkcí** — počet parametrů, jejich datové typy, případné implicitní hodnoty, typ funkční hodnoty
  - odvozené datové typy (`typedef`)
  - a další údaje _odvozené během sémantické analýzy a dalších fází překladu_ (adresa, offset, příznak „byla přiřazena hodnota", příznak „proměnná se používá", registr…)
- Počet tabulek závisí na implementaci překladače. Může existovat:
  - **globální tabulka**, která obsahuje globální deklarace,
  - **lokální tabulky**, vytvářené například pro jednotlivé funkce nebo procedury.

- Tabulky symbolů jsou během překladu využívány _velmi intenzivně_
  - **Při zpracování deklarací a definic** se do nich ukládají informace o nově deklarovaných identifikátorech.
  - **Při překladu výrazů a příkazů** se tabulka prohledává, aby překladač zjistil:
    - zda je použitá proměnná deklarována,
    - jaký má datový typ,
    - případně další vlastnosti potřebné pro sémantickou kontrolu.
- Efektivita vyhledávání proto přímo určuje rychlost překladu, **a proto se pro uložení symbolů používají výlučně hashovací tabulky**.

| Implementace | `insert` | `lookup` | Poznámka |
| --- | --- | --- | --- |
| Neuspořádaný lineární seznam | $O(1)$ | $O(n)$ | jednoduché, jen pro akademické překladače |
| Uspořádané pole (binární vyhledávání) | $O(n)$ | $O(\log n)$ | drahé vkládání |
| Vyvážený binární vyhledávací strom | $O(\log n)$ | $O(\log n)$ | historicky používané (Pascal) |
| **Hashovací tabulka** | $O(1)$ | $O(1)$ | **standard** |

# 1. Hashovací tabulka s řetězením kolizí

> [!success]
> **_Hashovací tabulka_** _je tvořena polem, do kterého se symboly ukládají podle hodnoty_ vypočítané **hashovací funkcí**. Ta **z názvu identifikátoru** (např. proměnné nebo funkce) **vypočítá index**, na _který se symbol uloží_. Při dalším použití identifikátoru překladač znovu spočítá jeho hash, přejde přímo na odpovídající pozici a získá potřebné informace.
>
> **Kolize** nastává tehdy, když _dva různé identifikátory získají stejný index v hashovací tabulce_. Nejčastěji se řeší pomocí **zřetězení**, kdy se na jednom indexu _uchovává seznam všech symbolů se stejným hashem_. Při vyhledávání se pak prochází pouze tento seznam, nikoliv celá tabulka.

```
H[0] ─→ x ─→ NULL
H[1] ─→ y ─→ i ─→ i ─→ NULL      (kolize: 'y' a 'i' padnou do stejné přihrádky)
H[2] ─→ j ─→ j ─→ b ─→ j ─→ NULL
H[3] ─→ k ─→ c ─→ c ─→ NULL
...
```

> [!warning]
> **Zásadní implementační trik:**  
> Nový symbol se vkládá **na začátek řetězce**.  
> Tím při hledání narazíme nejdřív na _nejnověji deklarovaný_ symbol daného jména — a to je přesně ten s nejbližší deklarací.

## 1.1 Minimální perfektní hashování klíčových slov

- _Klíčová slova_ mají v běžných jazycích _stejnou syntaxi jako identifikátory_, takže lexikální analyzátor nejprve **rozpozná identifikátor** a pak se v **oddělené** _hashovací tabulce ptá, zda jde o klíčové slovo_.
- Protože je **množina** **klíčových slov pevná** a **předem známá**, lze _zvolit funkci bez jediné kolize_ a s tabulkou přesně velikosti počtu klíčových slov — **minimální perfektní hashování**.

> [!info]
> **Rozdíl proti tabulce symbolů:** tabulka klíčových slov je statická, jen pro čtení, bez rozsahů platnosti. Tabulka symbolů je dynamická a musí řešit viditelnost.

---

# 2. Rozsah platnosti (scope) a viditelnost

> [!success]
> **Rozsah platnosti** identifikátoru je _část programu, ve které je daná deklarace viditelná_.
>
> Při vyhledávání musí být vždy nalezena **proměnná s nejbližší deklarací.**

### Příklad — úrovně viditelnosti

```c
int i;              // 0 (globální)
float x;            // 0
void foo() {
    unsigned i;     // 1 (lokální)

    { double x, y; char c; }   // 2.1
    { int i; float w;      }   // 2.2
    int j;                     // 1
}
```

| Úroveň viditelnosti | Proměnné |
| --- | --- |
| 0   | `i`, `x` |
| 1   | `i`, `j` |
| 2.1 | `x`, `y`, `c` |
| 2.2 | `i`, `w` |

---

# 3. Vyhledávání proměnných

## 3.1 Samostatná tabulka pro každý rozsah platnosti (strom tabulek)

> [!success]
> _Pro každý rozsah_ (program, procedura, funkce) se **vytvoří vlastní tabulka**.  
> Tabulky _tvoří strom kopírující vnoření deklarací_.  
> Každá tabulka má **ukazatel** na tabulku **nadřazenou**.

- Tento přístup je přirozený u jazyků typu **Pascal**, kde jsou všechny lokální proměnné uvedeny hned na začátku procedury/funkce a lze je uložit do jedné tabulky.

### 3.1.1 Příklad

```pascal
program p
  var x,y of real;
  procedure f()
    var i of integer;
    begin  end
  procedure g()
    var c of char, x of real;
    procedure r()
      var b of boolean;
      begin  end
    procedure s()
      var y,z of real;
      begin  end
    begin  end
  procedure h()
    var i,j of integer;
    begin  end
```

Strom tabulek:

![[019f9952-a675-733a-913b-6784f2c4c105.png]]

### 3.1.2 Algoritmus vyhledávání

- Vyhledávání probíhá **odspodu nahoru**:
  1. Nejprve se prohledá tabulka aktuální procedury
  2. Pokud se symbol nenajde, pokračuje se v nadřazené tabulce
  3. Nakonec lze dojít až ke globální tabulce
  4. Pokud se symbol nenajde → chyba

### **3.1.3 Vlastnosti**

- Struktura _přesně odpovídá struktuře programu_. Tabulku funkce lze po dokončení funkce _jen odložit_ nebo _zrušit_.
- Snadná kontrola redeklarace → stačí prohledat jednu tabulku.
- **Vyhledávání** je $O(\text{hloubka vnoření})$ hashovací dotazů, ne jeden (**neefektivní**)
- Pro jazyky, kde smí být blok deklarován kdekoli, by vzniklo obrovské množství tabulek (**neefektivní**)

## 3.2 Jedna hashovací tabulka + zásobník bloků

> [!success]
> Pro jazyky jako C a C++, kde mohou být v každém bloku deklarovány nové lokální proměnné, je výhodnější mít **jednu společnou tabulku pro všechny úrovně viditelnosti** (globální i lokální) a k ní **prostředek pro odstranění symbolů deklarovaných v bloku na konci tohoto bloku**.

- Datová struktura má tři složky:
  1. **Hashovací tabulka** — všechny symboly všech aktuálně otevřených bloků. Kolize se řeší řetězením, nové symboly se vkládají **na začátek** řetězce.
  2. **Řetězec symbolů bloku** — každá proměnná deklarovaná v bloku (kromě poslední) má ukazatel na další proměnnou deklarovanou v témže bloku.
  3. **Zásobník bloků** — pro každý otevřený blok obsahuje ukazatel na **první proměnnou deklarovanou v tomto bloku**.

### 3.2.1 Příklad

```c
int i, j;              // G
char c;                // G
bool b;                // G
void f(){
  int j;               // B1
  float x, w;
  {
    int i;             // B2
    float y;
    {         
      int j;           // B3
      bool c;          
      { 
        char a, b;             // B4.1
      }
      {                        // B4.2
        { 
          int k;               // B5.1
        }
        { 
          double x, y;         // B5.2
        }
      }
    }
  }
}
```

![[019fce77-9e97-726c-93d4-f90e9a71f427.png]]

- **Zásobník** pro každý blok obsahuje **ukazatel na první proměnnou** _deklarovanou v bloku_.
- Každá proměnná deklarovaná v bloku vyjma poslední **má ukazatel na další proměnnou**  
  _deklarovanou v bloku_.
- Při opuštění bloku je **odebrán ukazatel** z vrcholu zásobníku a _s použitím_  
  _uvedených ukazatelů_ jsou všechny proměnné deklarované v bloku **odstraněny** z hashovací  
  tabulky.

---

# 4. Kdo s tabulkou symbolů pracuje

- **Lexikální analýza** — rozpozná identifikátor a hashováním ověří, zda nejde o klíčové slovo. Do tabulky symbolů zpravidla ještě nezapisuje typy, ale může do ní vkládat samotné jméno / řetězec.
- **Syntaktická analýza** — sama tabulku typicky nepotřebuje; výjimkou je C, kde `A * b;` je buď deklarace ukazatele (je-li `A` typedef), nebo výraz. Parser se proto musí tabulky ptát (známý _lexer hack_).
- **Sémantická analýza** — hlavní uživatel. Při zpracování pravidla `DEKL → TYP IDENT IDENT1 ;` se dědičným atributem `typ` šíří datový typ ke všem identifikátorům v seznamu a ty se zapisují do tabulky. Při analýze výrazu `(i & j) * r` se naopak typy z tabulky **čtou** a syntetizovaným atributem `E.typ` se skládají zdola nahoru.
- **Generování interní formy** — atribut `E.ref` odkazuje na proměnnou ze zdrojového programu, na literál, nebo na **dočasnou proměnnou** vytvořenou funkcí `newtemp()`. I dočasné proměnné a návěští (`newlabel()`) se evidují v tabulce, protože pro ně je nutné vyhradit místo.
- **Optimalizace** — analýza toku dat (živé proměnné, dosažitelné definice) pracuje nad množinami proměnných, které jsou identifikovány záznamem v tabulce.
- **Generování kódu a přidělování registrů** — z tabulky se berou velikosti a offsety. Do tabulky se zapisuje přidělený registr.