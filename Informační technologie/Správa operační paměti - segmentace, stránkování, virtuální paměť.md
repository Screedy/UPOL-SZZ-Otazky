## Operační paměť
- základní část PC
- slouží k uložení kódu a dat běžících procesů, operačního systému, přístupu k zařízením, přístup k souborovému systému
- může být realizována různými prostředky - DRAM, SRAM, HDD, SSD, flash

## Požadavky na správu operační paměti
- hw a OS počítače se podílí na:
	- evidenci volného a přiděleného prostoru procesům
	- přidělování a uvolňování paměti procesů
	- ochrana přiděleného prostoru
	- realizace virtuální paměti

## Správa paměti v jednoúlohových operačních systémech
- v jeden okamžik může běžet pouze jeden proces - žádné extra nároky
- časté řešení: OS a ovladače zařízení na začátku nebo na konci, program ve zbylé části
![[MacBook-2024-05-03-001158.png]]

## Stránkování
- alternativa k přidělování souvislých bloků paměti, kde místo operační paměti naopak "kouskujeme" programy
- řeší vnější fragmetace
- **adresní** (logický) **prostor** je rozdělen na úseky stejné délky $\rightarrow$ **stránky** (pages)
- fyzická paměť je rozdělena na úseky stejné délky $\rightarrow$ **rámce** (frames)
---
- provádí se **mapování** logických adres na fyzické
- CPU společně s OS udržuje stránkovací tabulku, díky které se adresy převádí
>[!Example]+ Ukázka stránkování
![[MacBook-2024-05-03-001160.png]]
- logická adresa: pd, kde p je číslo stránky a d je offset
- fyzická adresa: fd
- číslo stránky se vezme jako index do stárnkovací tabulky a nahradí se tam uložených číslem rámce f
---
- v praxi se používají víceúrovňové tabulky
	- část logické adresy udává tabulku, další část index v tabulce a další část offset

>[!Example]+ Ukázka i386 s Physical Address Extention
>![[MacBook-2024-05-03-001163.png]]
- **TLB: Translation Lookaside Buffer**
	- cache procesoru obsahující **hodně používané části** stránkovacích tabulek
	- pro danou stránku uchovává **adresu rámce**
	- pokud je v cache - **cache hit**, jinak **cache miss** a načtení stránky trvá déle

## Segmentace
- paměť je rozdělena do několika segmentů (alespoň na kód, data, zásobník)
- stránkování je obvykle pro programátora transparentní
	- oproti tomu segmentace umožňuje rozdělit program do logických celků
---
- při použití segmentace a stránkování programy nepracují přímo s lineární adresou
- používají logickou adresu ve tvaru segment + offset a ta je poté převádí na fyzickou adresu pomocí stránkování
>[!Example]+ Ukázka segmentace
![[MacBook-2024-05-03-001162.png]]

## Virtuální paměť
- primární paměť RAM je obvykle málo
- k primární paměti je připojen ještě velký soubor na disku
- za pomoci OS se počítač tváří, jako by primární paměti bylo více
- aktuálně používaná  data musí být v RAM
>[!Example] Pojmy
>- virtuální paměť: operační paměť zahrnující jak primární paměť, tak i vyhrazený prostor na pevním disku
>- swapování: je proces, kdy OS vyměňuje úsek operační paměti mezi primární pamětí a diskem
>- stránkovací/swapovací soubor: je soubor na disku obsahující data namapovaná systémem do operační paměti

##### Navigace
Předchozí: [[Problém uváznutí, jeho detekce a metody předcházení]]
Následující: [[Práce se vstupně výstupními zařízeními, ovladače]]
Celý okruh: [[2. Informační technologie]]