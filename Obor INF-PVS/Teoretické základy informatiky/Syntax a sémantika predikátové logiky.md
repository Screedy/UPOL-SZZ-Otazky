## Syntax predikátové logiky
- Predikátová logika oproti výrokové pracuje s tvrzeními na jemnější úrovni
- Obecně umožňuje používat *proměnné, relační symboly, funkční symboly kvantifikátory a predikáty*

> [!info] Definice
> **Jazyk PL** obsahuje:
>> - **proměnné** $x, y, z, ..., x_1, ...$
>> - **relační symboly** $p, q, r, ..., p_1, ...$ (ke každému relačnímu symbolu $r$ je dáno nezáporné číslo $\sigma(r)$ nazývané *arita symbolu* $r$)
>> - **funkční symboly** $f, g, h, ..., f_1, ...$ (ke každému relačnímu symbolu $r$ je dáno nezáporné číslo $\sigma(r)$ nazývané *arita symbolu* $f$)
>> - **symboly pro logické spojky**: $\neg$ a $\Rightarrow$
>> - **symbol pro univerzální kvantifikátor** $\forall$
>> - **pomocné symboly** jako závorky a čárka
- Množina všech **relačních** symbolů jazyka se značí $R$
- Množina všech **funkčních** symbolů jazyka se značí $F$
- Je-li $r \in R$ a $\sigma(r) = n$, pak řekneme že $r$ je **n-ární** (ekvivalentně pro $f$ a $F$)
- Trojici $\lt R, F, \sigma \gt$ nazýváme jako **typ jazyka** (jednoznačně to určí jazyk)
	- Množiny $R$ a $F$ musí být disjunktní
- Základní jednotky jazyka jsou **termy a formule**

> [!info] Definice
> **Term** jazyka typu $\lt R, F, \sigma \gt$ je definován takto
>> - každá proměnná $x$ je term
>> - pokud $f \in F$ je n-ární a jsou $t_1, ..., t_n$ termy, pak $f(t_1, ..., t_n)$ je term
- Pro zápis používáme **infixovou notaci**
	- $x f y$ místo $f(x, y)$ ... $2 + 3$ místo $+(2, 3)$
>[!info] Definice
>**Formule** jazyka typu $\lt R, F, \sigma \gt$ je definován takto
>> - je-li $r \in R$ je n-ární a jsou $t_1, ..., t_n$ termy, pak $r(t_1, ..., t_n)$ je (atomická) formule
>> - jsou-li $\varphi$ a $\psi$ formule, pak $\neq \varphi, (\varphi \Rightarrow \psi)$ jsou také formule
>> - je-li $\varphi$ formule a $x$ proměnná, pak $(\forall x)\varphi$ je formule

- I v PL můžeme provádět důkazy strukturální indukcí jako ve VL

## Sémantika predikátové logiky
- Přiřazuje význam (nemá smysl uvažovat $x + 0$)
>[!info] Definice
>**Struktura pro jazyk** typu $\lt R, F, \sigma \gt$ je trojice $M = \lt M, R^M, F^M \gt$, která sestává z:
>> - neprázdné množiny $M$
>> - $R^M = \{ r^M \subseteq  M^n \mid r \in R, \sigma(r) = n \}$
>> - $F^M = \{f^M: M^n \rightarrow M \mid f \in F, \sigma(f) = n\}$
 > 
 > Pokud $\approx \in R$, pak $\approx$ interpretujeme jako relaci identity ($\approx^M = \omega_M = \{ \lt u, u \gt \mid u \in M \}$)
- Jedná se tedy o systém relací a funkcí pro daný jazyk
#### M-ohodnocení
- Zobrazení přiřazující každé proměnné $x$ prvek $v(x) \in M$

>[!info] Definice
>Nechť $v$ je M-ohodnocení. Hodnota $\mid\mid t \mid|mid_{M, v}$ termu $t$ v $M$ při $v$ je definována takto
>> 1. $v(x)$ - je-li $t$ proměnná $x$
>> 2. $f^M(\mid\mid t_1 \mid\mid_{M, v}, ..., \mid\mid t_k \mid\mid_{M, v})$ - je-li tvaru $f(t_1, ..., t_k)$

> [!info] Definice
> Pravdivostní hodnota $\|\varphi \|_{M,v}$ formule $\varphi$ při M-ohodncení $v$ je definována takto:
>> 1) pro atomické forumule: $$\| r(t_1, \dots, t_n) \|_{M,v} = \begin{cases} 1, & \text{je-li } \langle \| t_1 \|_{M,v}, \dots, \| t_n \|_{M,v} \rangle \in r^M \\ 0, & \text{jinak} \end{cases}$$
>> 2) pro formule $( \varphi )$ ve tvaru $( \neg \alpha )$ a $(\alpha \Rightarrow \beta)$: $$ \neg \alpha \|_{M,v} = \begin{cases} 1, & \text{pokud } \| \alpha \|_{M,v} = 0 \\  0, & \text{pokud } \| \alpha \|_{M,v} = 1 \end{cases} $$ 
>>$$ \alpha \Rightarrow \beta \|_{M,v} = \begin{cases}  1, & \text{pokud } \| \alpha \|_{M,v} = 0 \text{ nebo } \| \beta \|_{M,v} = 1 \\ 0, & \text{jinak} \end{cases} $$
>> 3) pro kvantifikovanou formuli $\varphi$: $$ | (\forall x) \varphi \|_{M,v} = \begin{cases} 1, & \text{pokud pro každé } v' \text{ takové, že } v' =_x v \text{ je } \| \varphi \|_{M,v'} = 1 \\ 0, & \text{jinak} \end{cases} $$
>
> Je-li $\| \varphi \|_{M,v} = 1 \space\space ( \| \varphi \|_{M,v} = 0 )$, říkáme, že formule $\varphi$ je pravdivá (nepravdivá) ve struktuře $M$ při ohodnocení $v$.
- **tautologie ve struktuře** jestliže $\| \varphi \|_{M,v} = 1$ platí pro každé M-ohodnocení
- **tautologie** pokud je $\varphi$ tautologií v každé struktuře $M$
	- Prostě pro libovolnou strukturu a libovolné ohodnocení musí být pravdivá

>[!info] Definice
> **Teorie** v jazyku PL typu $\lt R, F, \sigma \gt$  je libovolná množina $T$ formulí jazyka tohoto typu. Struktura $M$ jazyka typu $\lt R, F, \sigma \gt$ se nazývá **model teorie** $T$ (zápis: $M \vDash T$ či $\| T \|_M = 1$), jestliže **každá formule z $T$ je pravdivá v $M$**.
- Teorie má stejný význam jako v přirozeném jazyce ("Nesouhlasím s tvojí teorií"). Přičemž teorií myslíme soubor tvrzení (v PL je to množina formulí)

>[!info] Definice
> Množina $S$ formulí **sémanticky plyne** z množiny $T$ formulí  (píšeme $T \models S$; píšeme také $T \models \varphi$), jestliže $S = \{\varphi\}$, podobně když $T = \{\psi\}$, jestliže každý model $T$ je modelem $S$).
> 
> *Slovy: Tedy $S$ sémanticky plyne z $T$ právě když v každé struktuře, ve které jsou pravdivé všechny formule z $T$, jsou také pravdivé všechny z $S$.*

>[!tip] Věta
> Platí, že $\varphi$ je **tautologie**, právě když $\vDash \varphi$.

>[!Example]- Příklady
>![[Pasted image 20250320091207.png]]
>![[Pasted image 20250320091223.png]]
>![[Pasted image 20250320091252.png]]
>![[Pasted image 20250320091312.png]]


