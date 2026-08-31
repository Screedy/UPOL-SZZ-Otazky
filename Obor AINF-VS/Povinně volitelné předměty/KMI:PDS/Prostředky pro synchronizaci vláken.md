# 1. Vlákno

> [!success]
> **Vlákno** je _nejmenší jednotka vykonávání programu_. Je _součástí procesu_ a sdílí s ostatními vlákny téhož procesu **stejnou adresovou paměť** a _většinu systémových prostředků_. Díky tomu mohou vlákna _efektivně spolupracovat_, ale je **nutné** jejich přístup ke sdíleným datům **synchronizovat**. (Jinak je velké riziko výskytu chyb souběhu)

## 1.1 Správa vláken — Thread Pool

> [!success]
> **Thread Pool** je **návrhový vzor pro efektivní správu vláken**. Místo neustálého vytváření a rušení vláken se při startu aplikace vytvoří **skupina vláken**, která opakovaně zpracovávají přidělené úkoly z fronty.

---

# 2. Základní prostředky synchronizace vláken

## 2.1 Atomické operace

> [!success]
> **Atomická operace** je operace, kterou _nelze přerušit jiným vláknem_ nebo procesem.

- Jsou **_základem_** _většiny synchronizačních prostředků_ (např. mutexů nebo semaforů).

### 2.1.1 Na úrovni programovacího jazyka

- Programátor používá hotové _atomické typy nebo funkce_ poskytované **jazykem** či **knihovnami**.

```cpp
std::atomic<int> counter;
counter++;
```

### **2.2.2 Na úrovni procesoru**

- _Atomičnost_ zajišťuje přímo **hardware** pomocí _speciálních instrukcí procesoru_.

#### 2.1.1.1 Test-and-Set (TAS)

```java
function test_and_set(boolean lock):
   boolean initial = lock;
   lock = true;
   return initial;
```

- `test_and_set` _atomicky přečte hodnotu a nastaví ji na_ `true`.
- Pokud vrátí `true`→ zámek byl volný, nyní uzamčen → vstup do KS.
- Pokud vrátí `false`→ zámek byl zamknutý → čekáme.
- **Nevýhoda:** Vyhladovění možné (není zaručeno pořadí).

#### 2.1.1.2 Compare-and-Swap (CAS)

```
atomic bool compare_and_swap(int *ptr, int expected, int newval):
    if *ptr = expected:
        *ptr ← newval
        return true
    return false
```

#### 2.1.1.3 Fetch-and-Add

```
atomic int fetch_and_add(int *ptr, int delta):
    old ← *ptr
    *ptr ← old + delta
    return old
```

- **Použití**: Implementace ticketového zámku.

## 2.2 Zámek (Mutex)

> [!success]
> **Mutex** je základní synchronizační primitivum se dvěma stavy (`zamknuto` / `odemknuto)`.

- **Operace:**
- `lock()` — pokud _je volný_, _zamkne a pokračuje_; jinak **blokuje** (čeká)
- `unlock()` — _uvolní zámek_ _(může jenom vlastník!)_; **probudí** čekající vlákno (pokud existuje)

### 2.2.1 Nesprávné použití

> [!danger]
> Silný nástroj **zabraňující paralelizaci** (třeba používat uvážlivě)

```
# Sdílená paměť
lock ← unlocked

# Úkol zvýšení hodnoty na každém indexu pole

# Žádná paralelizace
lock.lock()
while idx < len(data):
  data[idx] += 1
  idx += 1
lock.unlock()

# Testujeme proměnnou mimo kritickou sekci 
while idx < len(data):
  lock.lock()
  data[idx] += 1
  idx += 1
  lock.unlock()

# Deadlock -> neodemknutý zámek
while true:
  lock.lock()
  if idx >= len(data):
    break
  data[idx] += 1
  idx += 1
  lock.unlock()

# Pomalé
while true:
  lock.lock()
  if idx >= len(data):
    lock.unlock()
    break
  data[idx] += 1
  idx += 1
  lock.unlock()
```

### 2.2.2 Celkem dobré použití

```
while true:
  lock.lock()
  idx_local = idx
  idx += 1
  lock.unlock()

  if idx_local >= len(data):
    break
  data[idx_local] += 1
```

### 2.2.3 Čekání na zámek

- Existují _dva základní způsoby čekání_ na uvolnění zámku.

#### 2.2.3.1 Pasivní čekání

- Pokud je _zámek obsazen_, vlákno je **uspáno (zablokováno)** operačním systémem.
- Nezabírá procesorový čas.
- Po uvolnění zámku je vlákno probuzeno a pokračuje.

#### 2.2.3.2 Aktivní čekání (Spinlock)

- Pokud je _zámek obsazen_, vlákno **neustále opakuje test**, zda už není volný (tzv. _busy waiting_).
- Vlákno se **neuspí** a spotřebovává procesorový čas (zatěžuje CPU při delším čekání)

### 2.2.4 Vlastnosti

- Jednoduchý, bezpečný, velmi rozšířený
- **Nezaručuje pořadí** čekajících (bez férové implementace může dojít k vyhladovění)

## 2.3 Semafor

> [!success]
> **Semafor** je _chráněná proměná_ obsahující **počítadlo s nezápornými celými čísly**.

> [!info]
> Nazývaný také chráněný čítač

- Na rozdíl od mutex dovoluje **pustit více** procesů/vláken současně
- **Operace**:
  - `wait()` **(P)** — pokud je hodnota čísla **nenulová**, _sníží hodnotu_ o jedna_, jinak čeká_, až bude hodnota zvýšena
  - `signal()` **(V)** — **zvýší hodnotu** o 1

> [!info]
> Zmíněné operace jsou **atomické**. (Např. klasické čtení není atomické, zápis ano)

- **Druhy**:
  - **Binární semafo**r = chová se jako _mutex_
  - **Obecný semafor**. Slouží k řízení _přístupu ke zdrojům_, kterých je _konečné množství_ (např. tiskárny)
- _Odvozené vzory_ ze semaforu:
  - **Signalizace**. Semafor je nastavený na 0 a čeká se na signalizační událost.
  - **Rendezvous** [randejvů]**.** Čeká se na setkání více vláken, podobně jak u bariéry.

> [!danger]
> Na rozdíl od mutex _nevyžaduje vlastnictví._ `signal()` může volat **jiné vlákno** než to, které volalo `wait()`

### 2.3.1 Kritická sekce semaforem

```
# Sdílená paměť
semaphore = 1  # binární semafor

# Proces i
while true:
    # nekritická sekce
    semaphore.wait()
    # kritická sekce
    semaphore.signal()
```

### 2.3.2 Signalizace

- Semafor inicializovaný na **0** použijeme k synchronizaci: „B musí proběhnout až po A."

```python
# Sdílená paměť
semaphore = 0

# Vlákno A                    
# kód A                      
semaphore.signal()                  

# Vlákno B
semaphore.wait() 
# kód B
```

### 2.3.3 **Rendezvous**

```python
global count = 0      
mutex = Semaphore(1)  
barrier = Semaphore(0)
N = 3 

def thread_code(i):
  # kód procesů/vláken 
  mutex.lock()
  count += 1

  if count == N:
  # Poslední vlákno otevře bariéru
    for _ in range(N):
      barrier.signal()

  mutex.unlock()          # opuštění kritické sekce
  barrier.wait()          # čekání na ostatní
  print(f"Thread {i} prošel bariérou")
```

## 2.4 Monitor

> [!success]
> **Monitor** je _synchronizační konstrukce vyšší úrovně_, která sdružuje **sdílená data**, **operace nad nimi** a **synchronizační mechanismy** _do jednoho celku_.
>
> Zajišťuje, že v jednom okamžiku může _uvnitř monitoru_ vykonávat _kód pouze jedno proces/vlákno_.

- Operace na monitoru jsou _prováděny se vzájemným vyloučením_

> [!danger]
> _Není určeno pořadí_ uvolňování čekajících procesů ⇒ **může dojít k vyhladovění procesu**

### 2.4.1 Příklad — Bankovní účet

```
Monitor BankAccount
  int balance

  operation deposit(int amount)
    balance += amount   
  
  operation withdraw(int amount)
    balance -= amount

  operation getBalance()
    return balance
```

### 2.4.2 Podmínění proměnná

- Ve skutečnosti jsou **podmíněné proměnné (Condition Variables)** jednou z nejdůležitějších součástí monitoru. Samotný monitor totiž řeší jen to, že **do něj vstoupí vždy pouze jeden proces/vlákno**. Co ale když proces/vlákno sice vstoupí, ale **nemůže pokračovat**, protože není splněna nějaká podmínka?

> [!success]
> **Podmíněná proměnná** slouží k tomu, aby proces/vlákno _mohlo čekat na splnění určité podmínky_, **aniž by blokovalo** ostatní vlákna. (Jinak by vznikl deadlock)

- Operace:
  - `waitC()` — _čekání_ na splnění podmínky **(VŽDY BLOKUJE)**
  - `signalC()` — _pouští čekající proces_, když žádný není _nic nedělá_

```
waitC(cond):
    cond.enqueue(current_process)
    current_process.state = blocked
    monitor.lock.unlock()     

signalC(cond):
    if not cond.isEmpty():
        process ← cond.dequeue()
        process.state = ready
```

> [!danger]
> **Problém**: Při uvolnění _čekající proces pokračuje_ a „vstupuje” do monitoru, _signalizující proces_ ale také _pokračuje_ „do” monitoru 
>
> Dostáváme se **do neplatného stavu**!

| Priorita | Název | Chování |
| --- | --- | --- |
| W > S > E | **Signal and urgent wait (Hoare)** | W pokračuje ihned, S čeká ve „urgent" frontě, E čeká v entry frontě. |
| S > W = E | **Signal and continue (Mesa)** | S pokračuje, W se vrátí do entry fronty a musí znovu ověřit podmínku |

#### 2.4.2.1 Příklad: Semafor implementovaný pomocí monitoru

```
monitor Sem:
    s = n                    # počáteční hodnota semaforu
    notZero = Queue()        # podmínková proměnná

    operation Wait():
        while (s = 0)
            waitC(notZero)
        s ← s - 1

    operation Signal():
        s = s + 1
        signalC(notZero)
```

#### 2.4.2.2 Příklad: Bankovní účet s podmíněnými proměnými

```
Monitor BankAccount
    int balance = 100;
    condition enoughMoney;

    void withdraw(int amount) {
        while(balance < amount)
            waitC(enoughMoney);
        balance -= amount;
    }

    void deposit(int amount) {
        balance += amount;
        signalC(enoughMoney);
    }
```

> [!danger]
> `waitC()` dávat vždy do `while` cyklu, aby pro probuzení **proběhla znovu kontrola**!

#### 2.4.2.3 Srovnání: Monitor vs. Semafor

![[019f5bc4-5008-730f-92cc-6c4f4f55cec7.png]]

### 2.4.3 Chráněný objekt

> [!success]
> **Klasický monitor** používá _podmíněné proměnné_, se kterými programátor **pracuje explicitně** pomocí operací `waitC()` a `signalC()`. U **chráněného objektu** je tento _mechanismus skrytý_ – programátor **pouze definuje podmínku**, za které může být operace vykonána. Systém _automaticky ověří podmínku před vstupem do operace_ a _po jejím dokončení zkontroluje, zda nejsou splněny podmínky pro probuzení_ čekajících procesů.

## 2.5 Bariéra

> [!success]
> **Bariéra** je synchronizační bod, kde **všechna vlákna čekají**, dokud nepřijde poslední. Pak jsou všechna najednou propuštěna.

- **Operace**:
  - `wait()`

### 2.5.1 Použití bariéry

```python
# Sdílená paměť
n = 3
barrier = Barrier(n)

# Každé vlákno
def thread_code(i):
  # kód procesů/vláken 
  barrier.wait()          # čekání na ostatní
  print(f"Thread {i} prošel bariérou")
```

> [!info]
> Používá se například pro _paralelní výpočet násobení matic_. Každý proces/vlákno si _spočítá svoje_ a pomocí **bariéry se udělá finální výsledek**. (Na výsledek musíme počkat, až všichni dopočítají)