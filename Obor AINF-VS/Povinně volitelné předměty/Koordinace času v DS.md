- V mnoha případech je potřeba koordinace na základě času (typicky jsou to úlohy, kde potřebujeme časové razítko)
- Koordinace času v DS je **náročný problém** kvůli **odlišným hodinám na různých uzlech** a možným **zpožděním při přenosu zpráv mezi uzly**.
- Přesné synchronizace času (= omezení rozdílu dvou hodin) mezi všemi uzly v DS může být obtížná nebo dokonce nemožná. Nicméně existují různé techniky a protokoly, které slouží k minimalizaci a správě nepřesností v časové koordinaci.

## Cristianův algoritmus
- Cristianův algoritmus je *jedním z jednoduchých algoritmů pro synchronizaci času* v DS.
- Byl navržen v roce **1989 Cristianem Flaviem**, Brazilským informatikem.
- Algoritmus vychází z myšlenky, že **existuje referenční čas na centrálním serveru** a ostatní uzly mohou pomocí něj korigovat svůj lokální čas.

>[!Example] Princip Cristianova algoritmu:
>- Uzel, který chce synchronizovat svůj čas, **pošle serveru žádost o aktuální čas a uloží si čas požadavku $t_{1}$**.
>- Centrální server obdrží žádost a **odpoví zprávou obsahující aktuální čas serveru $t_{s}$**.
>- Uzel **obdrží odpoveď** od serveru a **zaznamená si čas přijetí $t_{2}$**. Poté **vypočte zpoždění** jako polovinu rozdílu mezi časem obdržení $t_{2}$ odpovědi a časem odeslání žádosti $t_{1}$.
>- Uzel koriguje svůj lokální čas přidáním změřeného zpoždění k aktuálnímu času. Tím získává aproximaci času na centrálním serveru.$$t_{new}=t_{s}+(t_{2}-t_{1})/2$$

- Cristianův algoritmus má několik omezení a **nebere v úvahu možné změny v síti**, které mohou způsobit nepřesnosti v určení zpoždění. Algoritmus také **předpokládá, že čas dotazu a odpovědi je stejný**.
- Tento algoritmus může být vhodný pro prostředí, kde jsou síťové zpoždění relativně malá a kde je dostačující dosažení pouhé aproximace času.
- **POZOR:** Čas nikdy nelze vrátit zpět.

## NTP protokol
- Network Time Protokol
- Umožňuje synchronizaci času v distribuovaných počítačových sítích. Jeho hlavním cílem je udržovat co nejpřesnější čas na všech uzlech sítě.

>[!Example] Jak funguje NTP:
>- V hierarchii **NTP jsou uzly uspořádány do stromu** (tzv stratumů).
>- Uzel s *přímým přístupem k referenčním hodinám*, jako jsou atomové hodiny nebo GPS, má úroveň $1$.
>- Čím vyšší je úroveň, tím více vrstev uzlů se nachází mezi uzlem a referenčními hodinami.

>[!Example] Získání času:
>- Každý uzel v NTP síti může sloužit jako server nebo klient, případně obojí.
>- Klienti posílají žádosti o aktuální čas serverům a server odpovídá s aktuálním časem.
>- NTP definuje speciální typy zpráv pro tento účel.
>- Funguje podobně jako Cristianův algoritmus.

>[!warning] Zpoždění a přesnost:
>- Při synchronizaci měří NTP zpoždění zprávy od klienta k serveru a zpět.
>- *Na základě tohoto zpoždění a časového razítka vytváří odhad, jak dlouho trvala komunikace*.
>- NTP také měří přesnost zpětné synchronizace.

>[!Example] Postup:
>1. Klient požádá server a **uloží čas požadavku $t_{1}$**
>2. **Server přijme požadavek v čase $t_{2}$** a **odpoví svým aktuálním časem $t_{3}$**
>3. Klient obdrží odpověď a **uloží čas přijetí $t_{4}$**
>
>Výpočet zpoždění:
>- $\text{RTD} = (t_{4}-t_{1})-(t_{3}-t_{2})$
>- $t_{4} = t_{3} - \text{offset} + \text{RTD}/2$
>- $t_{2} = t_{1} + \text{offset} + \text{RTD}/2$
>- $\text{offset} = t_{3} + \text{RTD}/2-t_{4}=\frac{(t_{2}-t_{1})+(t_{3}-t_{4})}{2}$

## Berkeley algoritmus
- Berkeley algoritmus na synchronizaci času byl navržen pro DS a má za cíl synchronizovat lokální hodiny na různých uzlech sítě.
- Hlavním principem tohoto algoritmu je, že **existuje jeden "vůdce"** (leader), který slouží jako **základna pro synchronizaci s ostatními uzly**.

>[!Example] Kroky pro dosažení synchronizace času:
>1. Je vybrán jeden uzel jako vůdce.
>2. Každý uzel měří svůj lokální čas a **vytváří tak lokální hodinovou značku**.
>3. Uzly posílají své lokální hodinové značky **vůdci**.
>4. Vůdce přijímá hodinové značky od uzlů a **vypočítává průměrný čas** nebo medián z těchto hodinových značek.
>5. **Vůdce vypočítá korekce pro každý uzel** na základě průměrného času a odesílá tyto korekce zpět na uzly.
>6. Každý uzel přijímá korekce od vůdce a **aplikuje je na své lokální hodiny**.

- Je důležité poznamenat, že algoritmus **nemusí** dosáhnout absolutní přesnosti v čase, ale **zajistí koordinaci mezi uzly** na úrovni, která může být dostačující pro daný systém.

## Plně distribuované řešení
- U bezdrátových a senzorových sítí obvykle *není možné komunikace každého uzlu s každým*.
- Využití **Reference Broadcast Synchronization** (RBS)
	- Uzel pošle **zprávu $m$ sousedům $p$ a $q$**.
	- Uzly $p$ a $q$ zprávu zaznamenají a **uloží si čas přijetí $T_{p_{m}}$ a $T_{q_{m}}$**
	- Uzly $p$ a $q$ si pošlou časy $T_{p_{m}}$ a $T_{q_{m}}$ a určí vzájemný offset (průměrem, lineární regrese)

## Lamportovi logické hodiny
- Lamportovi logické hodiny jsou konceptem navrženým Leslie Lamportem.
- Slouží k uspořádání událostí v DS.
- Tyto logické hodiny **nezajišťují přesný čas**, ale **umožňují porovnávání pořadí událostí** na různých uzlech systému.

>[!Example] Jak fungují:
>- Časová razítka:
>	- Každý proces v DS **udržuje lokální hodiny (čitač)**.
>	- Při vykonání operace/zaslání zprávy je inkrementován a poslán společně se zprávou. 
>	- Příjemce nastaví svůj čitač na `max(citac, citac_ve_zprave)`.
>- Udržování uspořádání událostí:
>	- Lamportovy logické hodiny zajistí, že *pokud událost $A$ nastane před událostí $B$ na jednom procesu,* pak i *časové razítko $A$ bude menší než časové razítko $B$*.
>	- Může nastat, že dvě operace budou prováděny současně. Poté je to řešeno podle `ID` procesu.

- Lamportovy logické hodiny mají **omezení**!
	- V situacích, kdy jsou **dvě události na různých procesech vzájemně nezávislé** a **neexistuje mezi nimi žádný kauzální vztah**.
	- V takových případech nemusí časová razítka vždy zachytit reálné pořadí událostí.

>[!info]
>Pro komplexnější situace mohou být použity rozšířené koncepty, například vektorové hodiny (vector clocks)m které umožňují více informací o vzájemných vztazách mezi událostmi v DS.

## Vektorové hodiny
- Byly vyvinuty pro sledování a zachycení kauzálních vztahů mezi událostmi na různých uzlech systému.
- Oproti Lamportovým logickým hodinám, které zajišťují porovnání pořadí událostí, vektorové hodiny *uchovávají více informací o vzájemných vztazích mezi událostmi*.

>[!Example] Jak fungují:
>- Vektor hodin:
>	- Každý uzel v DS udržuje vlastní vektor hodin.
>	- Vektor hodin obsahuje **pro každý uzel ze systému hodnotu**, která představuje *aktuální počet provedených událostí na daném uzlu*.
>- Porovnání vektorů hodin:
>	- Chování je analogické jako v případě logických hodin $$VC_{1} \leq VC_{2} \text{ pokud } VC_{1}[i]\leq VC_{2}[i] \text{ pro } \forall i$$ $$VC_{1} < VC_{2} \text{ pokud } VC_{1} \leq VC_{2} \text{a} \exists j \text{ takové, že } VC_{1}[j] < VC_{2}[j]$$
>	- Neporovnatelné jsou považovány za konkurentní.

>[!Example] Příklad:
>![[MacBook-2025-01-04-002363@2x.png]]

## Odbočka: Čas v počítačových hrách
- Řešeno:
	- *Klient-server* model:
		- Klient pošle date, server zpracuje a pošle odpověď
		- Problém: zpoždění $\rightarrow$ omezuje se hra
	- *Lock-step*:
		- Klient pokračuje až dostane data od serveru (jede se rychlostí nejpomalejšího hráče)
		- Triviální, vhodné pro pomalé hry
	- *Predikce*:
		- Predikuje se na klientovi (simulace vývoje hry)
		- Typicky $200$ms

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FProst%C5%99edky%20pro%20synchronizaci%20proces%C5%AF" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FVz%C3%A1jemn%C3%A9%20vylou%C4%8Den%C3%AD%20v%20DS" style="text-decoration: none;">
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