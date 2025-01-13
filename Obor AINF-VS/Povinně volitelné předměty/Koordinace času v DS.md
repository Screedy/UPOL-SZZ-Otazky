- V mnoha případech je potřeba koordinace na základě času (typicky jsou to úlohy, kde potřebujeme časové razítko - timestamp)
- Koordinace času v DS je **náročný problém** kvůli **odlišným hodinám na různých uzlech** a možným **zpožděním při přenosu zpráv mezi uzly**.
- Různé důvody proč zařízení mají jiný čas - technologie, mimoběžnost, drift, ...
- Skutečný čas vs logický čas.
- Omezení: **čas nikdy nevracíme zpět**
	- Není dobré pro logiku počítače. Musíme se zpomalit a počkat až nás reálný čas doběhne.

>[!tip] Definice mimoběžnosti:
>**Mimoběžnost** říká, že mezi dvěma událostmi existuje vztah, který je buď **kauzální** (tj. jedna událost ovlivňuje druhou), nebo není možné, aby tyto události byly současné.
>Pokud dvě události nejsou mimoběžné, říkáme, že jsou **současné (concurrent)**.

## Cristianův algoritmus
- Cristianův algoritmus je *jedním z jednoduchých algoritmů pro synchronizaci času* v DS.
- Byl navržen v roce **1989 Cristianem Flaviem**, Brazilským informatikem.
- Algoritmus vychází z myšlenky, že **existuje referenční čas na centrálním serveru** a ostatní uzly mohou pomocí něj korigovat svůj lokální čas.

>[!Example] Princip Cristianova algoritmu:
>- Klient $K$ požaduje čas od serveru $S$ s UTC.
>1. $K$ požádá o čas $S$ a uloží čas požadavku $t_{1}$.
>2. $S$ odpoví svým aktuálním časem $t_{S}$.
>3. $K$ uloží čas přijetí $t_{2}$.
>4. Výsledný čas $K$: $t_{s}+\frac{t_{2}-t_{1}}{2}$.
>- Problém při různém trvání dotazu a odpovědi. (Vytváření, přenos, ...)
>- Lze poslat více dotazů a udělat průměr

## NTP
- *Network Time Protokol*
- Umožňuje synchronizaci času v distribuovaných počítačových sítích. 
- Jeho hlavním cílem je udržovat co nejpřesnější čas na všech uzlech sítě.

>[!text] Jak funguje NTP:
>- V hierarchii **NTP jsou uzly uspořádány do stromu** (tzv stratumů).
>- Uzel s *přímým přístupem k referenčním hodinám*, jako jsou atomové hodiny nebo GPS, má úroveň $1$.
>- Čím vyšší je úroveň, tím více vrstev uzlů se nachází mezi uzlem a referenčními hodinami.

>[!text] Získání času:
>- Každý uzel v NTP síti může sloužit jako server nebo klient, případně obojí.
>- Klienti posílají žádosti o aktuální čas serverům a server odpovídá s aktuálním časem.
>- NTP definuje speciální typy zpráv pro tento účel.
>- Funguje podobně jako Cristianův algoritmus.

>[!Example] Postup:
>- Klient $K$ požaduje čas od serveru $S$ s UTC.
>1. $K$ požádá o čas $S$ v čase $t_{1}$.
>2. $S$ přijme požadavek v čase $t_{2}$.
>3. $S$ pošle odpověď s aktuálním časem $t_{3}$.
>4. $K$ přijme odpověď v čase $t_{4}$.
>5. Odhad offsetu $K$ vůči $S$: $\Theta = t_{3}+\frac{(t_{2}-t_{1})+(t_{4}-t_{3})}{2}-t_{4}$.
>6. Odhad zpoždění zpráv: $\delta = \frac{(t_{4}-t_{1})-(t_{3}-t_{2})}{2}$.
>7. $K$ případně upraví rychlost času do srovnání.

## Navíc: Berkeley algoritmus
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

## Lamportovy logické hodiny
- Lamportovy logické hodiny jsou konceptem navrženým Leslie Lamportem.
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

## Vektorové hodiny
- Byly vyvinuty pro sledování a zachycení kauzálních vztahů mezi událostmi na různých uzlech systému.
- Oproti Lamportovým logickým hodinám, které zajišťují porovnání pořadí událostí, vektorové hodiny *uchovávají více informací o vzájemných vztazích mezi událostmi*.

>[!Example] Jak fungují:
>- Každý uzel v DS udržuje vlastní vektor hodin.
>- Vektor hodin obsahuje **pro každý uzel ze systému hodnotu**, která představuje *aktuální počet provedených událostí na daném uzlu*.
>- Porovnání vektorů hodin:
>	- Chování je analogické jako v případě logických hodin $$VC_{1} \leq VC_{2} \text{ pokud } VC_{1}[i]\leq VC_{2}[i] \text{ pro } \forall i$$ $$VC_{1} < VC_{2} \text{ pokud } VC_{1} \leq VC_{2} \text{ a } \exists j \text{ takové, že } VC_{1}[j] < VC_{2}[j]$$
>	- Neporovnatelné jsou považovány za konkurentní.

>[!Example] Příklad:
>![[MacBook-2025-01-04-002363.png]]

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