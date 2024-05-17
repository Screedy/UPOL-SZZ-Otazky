- Synchronizace vláken je klíčový aspekt programování v prostředí, kde **více vláken přistupuje** ke sdíleným **zdrojům**. 
- Bez správné synchronizace mohou nastat problémy, jako je **nekonzistence dat** a **chyba souběhu** (race conditions). 
- Pro řešení těchto problémů se používají různé **synchronizační mechanismy**, jako jsou **kritické sekce**, **zámky** (locks) a **semafory**.

## Problém kritické sekce
- Kritická sekce je část kódu, kde **přístup** k **sdílenému** zdroji musí být **omezen** tak, aby k němu v **daném čase** mohlo **přistupovat pouze jedno vlákno**. 
- Pokud více vláken vstoupí do kritické sekce současně, může dojít k **nekonzistenci dat**.
 
### Požadavky na kritickou sekci
- **vzájemné vyloučení** - nejvýše jeden proces v kritické sekci
- **absence zbytečného čekání** - není-li žádný proces v kritické sekci a proces do ní chce vstoupit, není mu bráněno
- **zaručený vstup** - pokud se proces snaží vstoupit do kritické sekce, jednou musí uspět

### Řešení problému kritické sekce
- Řešení problému kritické sekce spočívá v zajištění toho, že pouze jedno vlákno má přístup ke sdílenému zdroji nebo kritické sekci v daném čase.
- V Pythonu lze tento problém řešit pomocí synchronizačních mechanismů, jako jsou zámky (locks) a semafory.
- Správným použitím těchto synchronizačních mechanismů lze zajistit, že kritická sekce bude bezpečně chráněna před souběžným přístupem více vláken, čímž se předejde nekonzistenci dat a dalším problémům spojeným s paralelním zpracováním.

## Zámky
- Zámky jsou synchronizační mechanismy, které umožňují exkluzivní přístup k určitému zdroji nebo části kódu. 
- Používají se k minimalizaci problémů kritické sekce a zabraňují soutěžení mezi vlákny o sdílené zdroje. 
- Zámky mohou být buď jednoduché (binární), které mají dvě stavy (otevřený/zavřený), nebo mohou být složitější (například zámky s podporou priorit).
- Python poskytuje zámky prostřednictvím modulu `threading`.

>[!Example] příklad použití zámku
>```Python
>import threading
>
>shared_resource = 0
>lock = threading.Lock()
>
>def increment():
> 	global shared_resource
> 	for _ in range(100000):
> 		lock.acquire()  # Získání zámku
> 		shared_resource += 1
> 		lock.release()  # Uvolnění zámku
>
>thread1 = threading.Thread(target=increment)
>thread2 = threading.Thread(target=increment)
>
>thread1.start()
>thread2.start()
>
>thread1.join()
>thread2.join()
>
>print(shared_resource)
>```
>- V tomto příkladu zámek `lock` zajišťuje, že pouze jedno vlákno může získat exkluzivní přístup k inkrementaci sdílené proměnné `shared_resource` v každém okamžiku. 

>[!Example] alternativní použití zámku
>```python
>def increment():
>	global shared_resource
>	for _ in range(100000):
>		with lock:               # získání zámku, kritická sekce v 
>			shared_resource += 1 # indentaci a automatické uvolnění
>```

## Semafor
- Semafor je synchronizační abstrakce, která udržuje interní počítadlo a umožňuje omezit počet vláken, která mohou současně získat přístup k sdíleným prostředkům. 
- Semafor může mít počáteční hodnotu větší nebo rovnu nule. 
- Pokud je počet vláken, která žádají o zámek, větší než hodnota semaforu, vlákna jsou umístěna do fronty čekajících a jsou probuzena, jakmile je semafor uvolněn.

>[!Example] příklad použití zámku
>```Python
>import threading
>import time
>
>semaphore = threading.Semaphore(5)  # Vytvoření semaforu s maximálním 
>								    # počtem 5 povolených vláken
>def worker():
> 	with semaphore:
> 		print("Vlákno", threading.current_thread().name, "získalo povolení")
> 		# Simulace dlouhodobého úkolu
> 		time.sleep(2)
> 		print("Vlákno", threading.current_thread().name, "končí")
>
>for i in range(10):
> 	t = threading.Thread(target=worker)  # Spuštění vlákna s funkcí worker
> 	t.start()
>```
>- opět místo `with semaphore` můžeme použít funkce `semaphore.acquire()` a `semaphore.release()`

##### Navigace
Předchozí:  [[Iterátory a generátory]]
Následující: [[Producenti a konzumenti]]
Celý okruh: [[3. Programovací jazyky a programování]]