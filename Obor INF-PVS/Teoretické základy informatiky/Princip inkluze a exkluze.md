- **Princip inkluze a exkluze** je často používaný kombinatorický princip
- Udává počet prvků sjednocení několika množin **pomocí počtu prvků průniku** jednotlivých množin
- Pro množiny $A_{1}, ..., A_{n}$ platí $$| A_{1} \cup A_{2} \cup\ ...\ \cup A_{n}| = \sum_{\emptyset \neq I \subseteq \set{1,2,...,n}}(-1)^{|I| - 1} |\cap_{i \in I} A_{i}|$$
- Zastavme se nejdřív nad tím, co princip inkluze a exkluze říká.
	- Na levé straně rovnosti je počet prvků, které patří do sjednocení $A_{1} \cup ... \cup A_{n}$. tj. alespoň do jedné z $A_{1}, ... A_{n}$.
	- Na pravé straně je součet výrazů $(-1)^{|I| - 1} | \cap_{i \in I} A_{i}|$, kde $I$ probíhá přes všechny neprázdné podmnožiny množiny $set{1, ..., n}$. $|\cap_{i +in I} A_{i}|$ je počet prvků průniku množiny, jejichž index patří do $I$
		- např. pro $I = \set{2,3,5}$ je to $|A_{2} \cap A_{3} \cap A_{5}|$. Výraz $(-1)^{|I|+1}$ je roven $1$, pokud $I$ obsahuje lichý počet prvků, a je roven $-1$, pokud $I$ obsahuje sudý počet prvků.
- Tedy v součtu na pravé straně jsou počty prvků všech možných průniků (jednočlenných, dvoučlenných, ..., až po $n$-členné) utvořené z $A_{1}, ..., A_{n}$, přitom počet prvků daného průniku je se znaménkem $+$ pro průniky **lichého počtu** množin a se znaménkem $-$ pro průniky **sudého počtu množin**.

>[!tip]- Důkaz
>![[MacBook-2024-05-31-001428.png]]![[MacBook-2024-05-31-001429.png]]

>[!Example] Příklad
>- V jedné malé základní škole fungují tři kroužky. Florbalový kroužek navštěvuje 18 dětí, výtvarný 14 dětí a šachový je osmičlenný. Z florbalistů jsou dva šachisté a čtyři výtvarníci. Do výtvarného a zároveň do šachového kroužku chodí tři děti. Jedno dítě chodí na všechny tři kroužky. Kolik dětí navštěvuje alespoň jeden ze tří uvedených kroužků?
>- **Řešení**: $|F \cup V \cup Š| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|  = 18 + 14 + 8 - 2- 4- 3 + 1 = 32$


##### Navigace
Předchozí:  [[Binomická věta]]
Následující: [[Pravděpodobnost, Laplaceova definice pravděpodobnosti, pravděpodobnostní prostor, vlastnosti pravděpodobnosti]]
Celý okruh: [[1. Teoretické základy informačních technologií]]