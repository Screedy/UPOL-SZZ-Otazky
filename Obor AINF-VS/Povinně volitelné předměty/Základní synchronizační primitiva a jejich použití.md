## Zámek
- Nejjednodušší synchronizační primitivum.
- Pouze **dva stavy**: zamknuto nebo odemknuto.
- Jednoduché použití, ale pozor na přehnanou synchronizaci.

>[!Example] Příklad: chceme modifikovat pole, každé vlákno přičte k hodnotě pole $1$
>```Python
>data: T.List[int] = [0] * 10000000
>idx: int = 0
>mutex = Lock()
>
>def thread_code(i: int):
>	global data
>	global idx
>	global mutex
>
>	# kritická sekce
>	data[idx] += 1
>	idx += 1
>```

>[!Fail]- Možná špatná použití zámku
>```Python
># Žádná paralelizace, první vlákno udělá vše
># ostatní jen ověří, že nemají co dělat (=> čas navíc)
>mutex.acquire()
>while idx < len(data):
>	data[idx] += 1
>	idx += 1
>mutex.release()
>```
>
>```Python
># Error - testujeme proměnou mimo kritickou sekci
># budeme zapisovat mimo index pole
>while idx < len(data):
>	mutex.acquire()
>	data[idx] += 1
>	idx += 1
>	mutex.release()
>```
>
>```Python
># Deadlock, super :-) neodemkli jsme zámek
>while True:
>	mutex.acquire()
>	if idx >= len(data):
>		break
>	data[idx] += 1
>	idx += 1
>	mutex.release()
>```
>
>```Python
># Deadlock je pryč, ale nic pomalejšíjo jsme (snad) vymyslet nemohli
>while True:
>	mutex.acquire()
>	if idx >= len(data):
>		mutex.release()
>		break
>	data[idx] += 1
>	idx += 1
>	mutex.release()
>```

>[!success] Správné využití zámku
>```Python
># Nejlepší varianta, ale idx = len(data) + num_threads
>while True:
>	mutex.acquire()
>	idx_local = idx
>	idx += 1
>	mutex.release()
>	if idx_local >= len(data):
>		break
>	data[idx_local] += 1
>```

## Semafor
- Nazývá se také *chráněný čítač*.
- **Chráněná proměnná** obsahuje **počítadlo s nezápornými celými čísly**.
- *Chráněně* je možné **pouze zapisovat**, ne číst.
- *Nestrukturované primitivum, je náročnější jej použít při rozsáhlejších programech*.
- **Operace čekání** - pokud je hodnota čísla nenulová, **sníží hodnotu** o jedna, jinak **čeká**, až bude hodnota zvýšena.
- **Operace signalizace** - zvýší hodnotu o $1$.
- operace `P` a `V` se provádějí atomicky.

- **Binární semafor** - zámek
- **Obecný semafor** - slouží k řízení přístupu ke zdrojům, kterých je konečné množství

- Implementace je možná **pomocí aktivního čekání** (je potřeba **silné férovosti**), nebo **pasivního čekání** (na to je potřeba spolupráce OS)

- Odvozené vzory ze semaforu:
	- **Signalizace** - semafor nastavený na 0, čeká se na signalizační událost
	- **Rendezvous** \[randejvů\] - čeká se na setkání více vláken (podobné bariéře)

## Signalizace
```Python
from threading import Event

signal1 = Event()
signal2 = Event()

counter: int = 0

def thread_code_1(i: int):
	global counter

	print(f"thread #{i}")
	# do some work
	signal1.set()

def thread_code_2(i: int):
	global counter

	print(f"thread #{i}")
	# do some work
	signal2.set()

def thread_code_3(i: int):
	global counter

	signal1.wait()
	signal2.wait()

	print(f"thread #{i}")
	# do some work
```

- Např. Omezení přístupu ke zdroji. *Tři vlákna mohou současně tisknout do sdílené tiskárny.*

## Bariéra
- Mechanismus synchronizace, zajišťující, že více vláken nebo procesů čeká na určitém bodě programu, dokud všechny nedosáhnou tohoto bodu.

>[!Example] Jak bariéra funguje
>- Každé vlákno nebo proces pokračuje svou činnost, dokud nedosáhne bodu, kde je umístěna bariéra.
>- Jakmile vlákno dosáhne bariéry, zastaví se a čeká na ostatní vlákna.
>- Jakmile všechna vlákna dosáhnou bariéry, bariéra se “uvolní” a všechna vlákna mohou pokračovat dále ve své činnosti.


```Python
def thread_code(i: int):
	inter_local: int = iter

	while True:
		time.sleep(random.randint(1, 10) / 1000)
		print(f"thread #{i} is before barrier")
		idx = barrier1.wait()
		print(f"thread #{i} pass barrier")
		iter_local -= 1

		if iter_local == 0:
			barrier1.wait()
			break
```

## Monitor
- **Strukturovaný** synchronizační nástroj.
- **Vyšší** synchronizační primitivum.
- Rozdílné chování v různých programovacích jazycích, mnoho jej nemá, najdeme však obvykle něco podobného
	- Jeden pohled:
		- Zobecnění jádra OS ve smyslu, že se KS řeší v privilegovaném režimu (tj. v monitoru).
		- Místo jednoho "jádra" má každý objekt/modul/... svůj monitor.
		- V jednom okamžiku s monitorem pracuje nejvýše jeden proces.
	- Druhý pohled:
		- Zobecnění objektu z OOP $\rightarrow$ každý monitor je instance nějaké třídy.
		- Navíc ale s každou instancí může v jednom okamžiku pracovat nejvýše jeden proces.
		- Všechna data monitoru musí být zapouzdřená. (stav lze měnit pouze definovanými operacemi)

- Není určeno pořadí uvolňování čekajících procesů $\Rightarrow$ **může dojít k vyhladovění procesu**
![[MacBook-2025-01-02-002349.png|300]]

>[!Text] Podmíněná proměnná
>- Občas je potřeba, aby **proces**, který je právě v monitoru, **počkal na nějakou událost**. Monitor poskytuje tuto funkcionalitu pomocí tzv. *podmíněných proměnných*.
>
>- Když funkce monitoru potřebuje počkat na splnění podmínky, vyvolá operaci `wait` na podmíněné proměnné, která je s touto podmínkou svázána. Tato operace proces zablokuje, zámek držený tímto procesem je uvolněn (odejde z monitoru, aby mohl někdo jiný vejít) a proces je odstraněn ze seznamu běžících procesů a čeká, dokud není podmínka splněna. **Jiné procesy zatím mohou vstoupit do monitoru** (zámek byl uvolněn). Pokud je jiným procesem podmínka splněna, může funkce monitoru "*signalizovat*", tj. probudit čekající proces pomocí operace `signal`.
>- Kdyby proces při čekání monitor neopustil, vznikl by **deadlock**
>- Implementace je například pomocí fronty blokovaných procesů.
>- Funguje na třech metodách:
>	- `wait` - čekání **VŽDY BLOKUJE** 
>	  ![[MacBook-2025-01-02-002350.png|200]]
>	- `signal` - pouští čekající proces, když žádný není nic nedělá 
>	  ![[MacBook-2025-01-02-002351.png|200]]
>	- `empty` - vrací `true` nebo `false`, podle toho, zda někdo čeká 
>	  ![[MacBook-2025-01-02-002352.png|200]]
>
>**Problém**:
>- Při **uvolnění** čekající proces pokračuje a "**vstupuje**" do monitoru, **signalizující** proces ale také **pokračuje "do"** monitoru. **Dostáváme se do neplatného stavu!**
>- Jeden z procesů **musí počkat na opuštění monitoru**, který ale vybrat?
>	- Uvolněný čekající (W), Signalizující (S), Ostatní čekající (E)
>	- Klasické řešení: **E < S < W**

![[MacBook-2025-01-02-002353.png]]

>[!Text] Chráněné objekty
>- Klasický monitor podmíněnými proměnnými vyžaduje explicitní implementaci `waitC()`, `signalC()` a `emptyC()`
>- **Implicitní řešení:**
>	- **Před** zahájením operace **ověření podmínky** zda může být vykonána
>	- **Po** skončení operace **ověření podmínky** a **uvolnění** čekajícího procesu
>- Dává nám výrazně jednodušší řešení problému

<div style="text-align: center; margin-top: 20px;">
    <!-- Horní tlačítka -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 10px;">
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FAlgoritmy%20pro%20kritickou%20sekci" style="text-decoration: none;">
            <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Předchozí otázka
            </button>
        </a>
        <a href="obsidian://open?vault=SZZ-Otazky2024&file=Obor%20AINF-VS%2FPovinn%C4%9B%20voliteln%C3%A9%20p%C5%99edm%C4%9Bty%2FProst%C5%99edky%20pro%20synchronizaci%20vl%C3%A1ken" style="text-decoration: none;">
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