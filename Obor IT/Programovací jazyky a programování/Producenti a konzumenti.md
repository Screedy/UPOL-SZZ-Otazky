- Problém producentů a konzumentů je klasickým **problémem synchronizace vláken**, popisuje situaci, kdy máme **několik vláken produkujících data** (producenti) a **několik vláken zpracovávajících tato data** (konzumenti). 
- Producenti vytvářejí data a umísťují je do **sdílené fronty** (**bufferu**), zatímco konzumenti **odebírají data ze stejné fronty a zpracovávají je**.
- Tento **vzor** se často používá ke **zlepšení výkonu** a **efektivity zpracování dat**.
---
- Vzor producenta a konzumenta umožňuje lepší souběžný běh **cyklických procesů**, které **pracují různými rychlostmi**.
- Díky použití **fronty** může producent vytvářet data **nezávisle na rychlosti spotřebitele**. 
- Pokud je tvorba dat rychlá, může producent tyto data **vytvářet napřed** a spotřebitel je pak bude **zpracovávat ve svém vlastním tempu**. 
- Je to vhodné například při **komunikaci po síti**, kdy fungují dva procesy v různých rychlostech. 
- První proces může neustále přijímat pakety ze sítě, zatímco druhý přijaté pakety analyzuje. 
	- V tomto příkladě je první proces producentem a druhý konzumentem. 
	- S použitím fronty mohou být pakety přijaté rychleji, než jsou analyzovány. 

>[!Example] příklad implementace, v python
>```python
>import threading
>import queue
>import time
>import random
>
># Vytvoření sdílené fronty
>buffer = queue.Queue(maxsize=10)
>
>class Producer(threading.Thread):
> 	def run(self):
> 		while True:
> 			item = random.randint(1, 100)
> 			buffer.put(item)  # Vložení položky do fronty
> 			print(f'Producent vytvořil: {item}')
> 			time.sleep(random.uniform(0.1, 0.5))  # Simulace práce
>
>class Consumer(threading.Thread):
> 	def run(self):
> 		while True:
> 			item = buffer.get()  # Odebrání položky z fronty
> 			print(f'Konzument zpracoval: {item}')
> 			buffer.task_done()
> 			time.sleep(random.uniform(0.1, 0.5))  # Simulace práce
>
># Vytvoření producentů a konzumentů
>producers = [Producer() for _ in range(2)]
>consumers = [Consumer() for _ in range(2)]
>
># Spuštění všech vláken
>for p in producers:
> 	p.start()
>for c in consumers:
> 	c.start()
>
># Čekání na dokončení úkolů (nikdy nedojde, protože jsou vlákna v nekonečné smyčce)
>buffer.join()
>```

>[!Example] Řešení pomocí semaforu, příklad v C
>1. `signal()` – jeho zavoláním se celočíselná hodnota semaforu zvedne o 1
>2. `cekat()` – zavolani funkce `cekat()` sníží hodnotu semaforu o 1; 
>	- pokud je hodnota semaforu již před zavoláním 0, nahrazuje toto volání funkci `sleep()`, dokud někdo nezavolá `signal()` a nezvýší tím hodnotu semaforu o 1
>
>- Obě funkce `signal()` a `cekat()` jsou nedělitelné atomické operace. 
>
>``` C
>int volne = VEL_ZASOBNIKU;  	// semafor, počet volných slotů v zásobníku
>int obsazene = 0;		// semafor, počet obsazených slotů v zásobníku
>
>producent() {
> 	while (TRUE) {
> 		polozka = vytvoritPolozku();
> 		cekat(volne);
> 		vlozPolozkuDoZasobniku(polozka);
> 		signal(obsazene);
> 	}
>}
>
>spotrebitel() {
> 	while (TRUE) {
> 		cekat(obsazene);
> 		polozka = vyjmoutPolozkuZeZasobniku();
> 		signal(volne);
> 		spotrebujPolozku(polozka);
> 	}
>}
>```

##### Navigace
Předchozí:  [[Synchronizace vláken - problém kritické sekce, zámky, semafory]]
Následující: [[Večeřící filozofové]]
Celý okruh: [[3. Programovací jazyky a programování]]