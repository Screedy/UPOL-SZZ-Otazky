## ThreadPool
- Návrhový vzor
- **Úkoly** se ukládají **do fronty** a postupně jsou jim **přidělována** vlákna
- Odpadá režie znovuvytvoření vláken (zrychlení, menší režie)
- Běžné primitivum v řadě programovacích jazyků

>[!Example]- Příklad vytvoření threadpoolu v Pythonu
>```Python
>from multiprocessing.pool import ThreadPool
>
>pool = ThreadPool(num_threads)
>pool.map(add_in_thread, list(range(num_iterations)))
>pool.close()
>pool.join()
>```

## Klasické paralelní problémy
- Večeřící filozofové
- Producent-konzument
- Čtenáři a písaři
- Hodující divoši
- Holičství
- Santa Clause
- $H_{2}0$
- Sushi bar
- Jídelna
- ...

### Večeřící filozofové
- Simulace *současného přístupu k více zdrojům*
>[!tip] Problém:
>*$5$ filozofů přemýšlí, folozof jí*.
>Jíst může, pokud má dvě vidličky.
>Vidličku **nemůže** mít více filozofů
- Je potřeba synchronizace $\Rightarrow$ *lehce může dojít k deadlocku*
>[!success] Řešení:
>1. Jeden filozof je **levák** a zdvihá vidličky naopak (není efektivní a férové - u některých zdrojů určit prioritu)
>2. **Číšník** - Máme vlákno, které zajistí koordinace (velké plýtvání zdroji, může dojít k vyhladovění - filozofové se budou předbíhat)
>3. Zvedne vidličku, **nemůže** získat, tak **položí** (může vzniknout livelock)
>4. Budeme mít jen **4 židle** (nevznikne deadlock, ale musíme vyřešit filozofy sdílející vidličku)

### Producent-konzument
- Reálný, často používaný problém
>[!tip] Problém:
>Producenti produkují, konzumenti konzumují a sdílejí omezený prostor - nelze tedy **přepsat nezkonzumované** a nelze **opakovaně konzumovat**
- Typicky máme více producentů a konzumentů
>[!success] Řešení:
>- Dva semafory (`not_empty`, `not_full`) a zámek (zápis na místo v poli)
>- Zjednodušeně:
>```Python
># Producent
>	not_full.wait()
>	# produkce
>	not_empty.signal()
>
># Konzument
>	not_empty.wait()
>	# konzumace
>	not_full.signal()
>```

### Čtenáři a písaři
- Reálný, často používaný problém
- Dva typy procesů soutěží o přístup k datům:
	- písaři **mezi sebou**
	- čtenáři jako třída **s písaři**
- Písaři se vzájemně vylučují
- Čtenáři jako třída vylučuje písaře
>[!success] Řešení:
>- Obecně přímočaré, ale je třeba dávat pozor na **spravedlivost** (preference čtenářů nebo písařů)
>- Některé jazyky mají RWlock
>
>>[!text] Nespravedlivé řešení - *upřednostňuje čtenáře*:
>>![[MacBook-2025-01-03-002355@2x.png]]
>
>>[!text] Spravedlivé řešení
>>![[MacBook-2025-01-03-002356@2x.png]]

### Kuřáci
- **Agent** má zdroje - **papír, tabák** a **sirky**
- Existují tři typy kuřáků:
	1. Ti co mají papír
	2. Ti co mají tabák
	3. Ti co mají sirky
- Agent opakovaně dává k dispozici dva náhodné zdroje. Cílem je, aby kuřák, který může pokračovat, pokračoval.

>[!tip] Motivace v OS
>Existují tři verze:
>1. **Nemožná**: Nelze měnit kód agenta a není možné použít větvení a pole semaforů (neřešitelné)
>2. **Zajímavá**: Nelze měnit kód agenta
>3. **Triviální**: Lze měnit kód agenta

>[!success]- Řešení (Idea - pomocí dealerů):
>```Python
>agent = Semaphore(1)
>tobacco = Semaphore(0)
>paper = Semaphore(0)
>match = Semaphore(0)
>
>def agent_A():
>	while True:
>		agent.acquire()
>		tobacco.release()
>		paper.release()
>
>def agent_B():
>	while True:
>		agent.acquire()
>		paper.release()
>		match.release()
>
>def agent_C():
>	while True:
>		agent.acquire()
>		tobacco.release()
>		match.release()
>
>isTobacco = False
>isPaper = False
>isMatch = False
>tobaccoSem = Semaphore(0)
>paperSem = Semaphore(0)
>matchSem = Semaphore(0)
>lock = Lock()
>
>def pusher_A():
>	global isPaper
>	global isMatch
>	global isTobacco
>	
>	while True:
>		tobacco.acquire()
>		lock.acquire()
>		if isPaper:
>			isPaper = False
>			matchSem.release()
>		elif isMatch:
>			isMatch = False
>			paperSem.release()
>		else:
>			isTobacco = True
>		lock.release()
>
>def smoker_M():
>	while True:
>		matchSem.acquire()
>		print(f"smoker_M made a cigar.")
>		agent.release()
>```
>- Rozšíření: Agent nečeká na signalizaci

### Hodující divoši
- $n$ divochů jí $x$ porcí misionáře z hrnce. Pokud **dojdou**, **požádají kuchaře** o navaření dalších $n$ porcí.

>[!success]- Řešení:
>```Python
>NUM_SAVAGES = 5
>NUM_MISSIONARY = 10
>
>need_cook = Semaphore(1)
>taking_portions = Semaphore(0)
>PORTIONS = 0
>
>def savage(i: int):
>	global PORTIONS
>	global need_cook
>	global taking_portions
>	
>	while True:
>		time.sleep(1)
>		taking_portions.acquire()
>		PORTIONS -= 1
>		if PORTIONS == 0:
>			need_cook.release()
>			eat(i)
>		else:
>			taking_portions.release()
>			eat(i)
>
>def cooker(i: int):
>	global PORTIONS
>	global need_cook
>	global taking_portions
>	
>	while True:
>		need_cook.acquire()
>		PORTIONS = NUM_MISSIONARY
>		print(f"Bon Appétit.")
>		taking_portions.release()
>```

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FZ%C3%A1kladn%C3%AD%20synchroniza%C4%8Dn%C3%AD%20primitiva%20a%20jejich%20pou%C5%BEit%C3%AD" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FProst%C5%99edky%20pro%20synchronizaci%20proces%C5%AF" style="text-decoration: none;">
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