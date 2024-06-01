>[!info] Definice třídy časové a prostorové složitosti
>- Pro funkci $f: \mathbb{N} \rightarrow \mathbb{N}$ rozumíme **třídou časové složitosti $T(f)$**, množinu těch probému, které jsou řešeny TS s **časovou složitostí v $O(f)$**.
>- **Třídou prostorové složitosti $S(f)$**, rozumíme třídu těch problémů, které jsou řešeny TS s **prostorovou složitostí v $O(f)$**

## PTIME
- Třída obsahující **všechny problémy řešitelné algoritmy s polynomiální časovou složitostí** $$PTIME = \cup^{\infty}_{k=0}T(n^{k})$$
- **Robustnost třídy PTIME** znamená **nezávislost** na zvoleném referenčním modelu počítačů. Když bychom totiž jako referenční model vzali např. stroje RAM, třída PTIME by se nezměnila.

## NPTIME
- Třída **všech $ANO/NE$ problémů**, které jsou rozhodovány **nedeterministickými algoritmy s polynomiální časovou složitostí.**
- **Robustnost třídy NPTIME** znamená **nezávislost** na zvoleném referenčním modelu počítačů. Když bychom totiž jako referenční model vzali např. stroje RAM, třída NPTIME by se nezměnila

>[!tip] Důvod zavedení tříd **PTIME** a **NPTIME**
>- Třídy časové složitosti PTIME a NPTIME byly vytvořené pro **popis** a **kategorizaci** problémů, které jsou řešitelné deterministickými a nedeterministickými algoritmy s polynomiální časovou složitostí.
>- **PSPACE**
>	- Třída obsahující **všechny problémy řešitelné algoritmy s polynomiální prostorovou složitostí.**
>- **NPSPACE**
>	- Třída obsahující **všechny problémy řešitelné nedeterministickými algoritmy s polynomiální prostorovou složitostí**

## Vzájemný vztah
$$PTIME \subseteq NPTIME \subseteq PSPACE = NPSPACE$$
1. $PTIME \subseteq NPTIME$
	- Přes velké úsilí vědecké komunity, zatím nebylo dokázáno, že $PTIME = NPTIME$, ani že $PTIME \neq NPTIME$. To znamená, že stále existuje možnost, že některé problémy, které jsou řešitelné nedeterministickými algoritmy v polynomiálním čase, mohou být řešitelné i deterministickými algoritmy v polynomiálním čase, nebo naopak.
	- Nicméně existuje mnoho problémů, u kterých se věří, že jsou řešitelné nedeterministickými algoritmy v polynomiálním čase, ale nebylo nalezeno žádné deterministické řešení v polynomiálním čase.
	- Tyto problémy jsou považovány za "typické" pro třídu $NPTIME$. Mezi takové problémy patří například problém nalezení Hamiltonovské kružnice v grafu.
	  
	  **Název:** HK (problém Hamiltonovské kružnice)
	  **Vstup**: Neorientovaný graf $G$
	  **Otázka**: Existuje v $G$ hamiltonovská kružnice (tj. uzavřená cesta, procházející každým vrcholem právě jednou?
	- Abychom dokázali, že $PTIME \subset NPTIME$, museli bychom najít problém, který **patří do $NPTIME$, ale zároveň nepatří do $PTIME$**
	- Abychom dokázali, že $PTIME = NPTIME$, tak bychom **museli dokázat $SAT \in PTIME$**
2. $NPTIME \subseteq PSPACE$
	- Pro libovolnou funkci $f$ je $T(f(n)) \subseteq S(f(n))$
		- např. Turingův stroj očividně navštíví při výpočtu nejvýše tolik políček, kolik udělá kroků
3. $PSPACE = NPSPACE$
	- Platí podle Savitchovi věty

##### Navigace
Předchozí:  [[Složitost algoritmu (časová a paměťová)]]
Následující: [[NP-úplné problémy]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]