## Problém kritické sekce:

Problém kritické sekce je situace v paralelním programování, kdy více vláken soutěží o přístup k sdíleným prostředkům nebo datům, což může vést k nekonzistentním stavům dat nebo chybám v aplikaci. Nekonzistence může vzniknout, pokud jedno vlákno čte data, která jsou zároveň změněna jiným vláknem.
### 1. Sdílené prostředky:

- **Sdílené prostředky** jsou data nebo zdroje, ke kterým více vláken má přístup. Může se jednat o sdílenou paměť, soubory, databáze nebo další zdroje, ke kterým mohou vlákna přistupovat paralelně.
### 2. Neatomické operace:

- **Neatomické operace** jsou operace, které nelze provést atomicky, tj. nelze je provést jedním instrukčním cyklem CPU. Typické příklady zahrnují čtení a zápis do paměti nebo manipulaci se sdílenými daty.
### 3. Riziko kritické sekce:

- **Soutěžení o zdroje**: Kritická sekce vzniká, když více vláken soutěží o přístup k sdílenému zdroji. Pokud jedno vlákno provádí operaci nad sdílenými daty a zároveň je tato data čte nebo mění jiné vlákno, může dojít k nekonzistenci dat.
    
- **Nekonzistence dat**: Nekonzistence dat může zahrnovat nekonzistentní stavy, poškozené struktury dat nebo jiné neočekávané chování aplikace.

### 4. Řešení problému kritické sekce:

- **Synchronizační mechanismy**: Problém kritické sekce lze řešit pomocí synchronizačních mechanismů, jako jsou zámky, semafory nebo podmínkové proměnné. Tyto mechanismy umožňují regulovat přístup k sdíleným prostředkům a minimalizovat soutěžení o ně.
    
- **Kritické sekce**: Kritické sekce jsou části kódu, ve kterých mohou vlákna získat exkluzivní přístup k sdíleným zdrojům pomocí synchronizačních mechanismů. Během této kritické sekce jsou prováděny operace nad sdílenými daty, což minimalizuje riziko nekonzistence dat.
    
- **Atomické operace**: Některé programovací jazyky a platformy poskytují podporu pro atomické operace, které zajistí, že operace bude provedena jako jedna nedělitelná jednotka, což eliminuje riziko kritické sekce.

## Zámky:

Zámky jsou synchronizační mechanismy, které umožňují exkluzivní přístup k určitému zdroji nebo části kódu. Používají se k minimalizaci problémů kritické sekce a zabraňují soutěžení mezi vlákny o sdílené zdroje. Zámky mohou být buď jednoduché (binární), které mají dvě stavy (otevřený/zavřený), nebo mohou být složitější (například zámky s podporou priorit).

```Python
import threading

shared_resource = 0
lock = threading.Lock()

def increment():
    global shared_resource
    for _ in range(100000):
        lock.acquire()  # Získání zámku
        shared_resource += 1
        lock.release()  # Uvolnění zámku

threads = []
for _ in range(10):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Výsledek:", shared_resource)
```

V tomto příkladu zámek `lock` zajišťuje, že pouze jedno vlákno může získat exkluzivní přístup k inkrementaci sdílené proměnné `shared_resource` v každém okamžiku. Tím se minimalizuje problém kritické sekce a zabraňuje se nekonzistentním stavům dat.

## Semafor:

Semafor je synchronizační abstrakce, která udržuje interní počítadlo a umožňuje omezit počet vláken, která mohou současně získat přístup k sdíleným prostředkům. Semafor může mít počáteční hodnotu větší nebo rovnu nule. Pokud je počet vláken, která žádají o zámek, větší než hodnota semaforu, vlákna jsou umístěna do fronty čekajících a jsou probuzena, jakmile je semafor uvolněn.

```Python
import threading
import time

semaphore = threading.Semaphore(5)  # Vytvoření semaforu s maximálním počtem 5 povolených vláken

def worker():
    with semaphore:
        print("Vlákno", threading.current_thread().name, "získalo povolení")
        # Simulace dlouhodobého úkolu
        time.sleep(2)
        print("Vlákno", threading.current_thread().name, "končí")

for i in range(10):
    t = threading.Thread(target=worker)  # Spuštění vlákna s funkcí worker
    t.start()
```

