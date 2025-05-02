- Zásobníkové programování je zvláštní paradigma
- Nízkoúrovňové
- **zásobník** ... datová struktura LIFO
	- čili máme jen 2 operace - `push` a `pop`
	- ![[Pasted image 20250422210404.png]]
- Můžeme simulovat *zásobníkový stroj*, který vše řeší přes pouze zásobníky (může jich být více)
	- `rslt` ... zásobník na data
	- `exec` ... zásobník na kód programu, který se vykonává
	- stroj pracuje iterativně po jednotlivých krocích
	- obvykle používá **postfixovou notaci**
- Bytecody některých programovací hjazyků používají zásobníkový stroj (Python, Java, .NET)
- Zásobník má omezenou velikost $\longrightarrow$ může dojít $\longrightarrow$ problém stack overflow
#### Popis práce zásobníkového paradigmatu
1) Datový zásobník je prádzný, vše je na programovém
2) V každém kroku se odebere prvek z programového zásobníku a podle jeho typu se vykoná akce
3) Je-li to hodnota, ulož ho na vrchol datového zásobníku
4) Je-li to slovo, znamená to instrukci pro stroj co má dělat (provádění akce s oběma zásobníky)
5) Program končí po vyprázdnění programového zásobníku a výsledek je na vrcholu datového
- Konkrétní příklad programu
	- program: `5 3 :- 4 :*` (`5`je na vrcholu)
	1) 5 se přesune na datový zásobník
	2) 3 se přesune na datový zásobník
	3) :- je slovo, vypustí z datové zásobníku dvě čísla a uloží tam jejich rozdíl (tedy 2)
	4) 4 se přesune na datový zásobník
	5) :* je slovo, vypustí z datové ho zásobníku dvě čísla a uloží tam jejich součin (tedy 8)
- Vhodné jsou obrázky pro znázornění a krokování