# 1. Proces

> [!success]
> **Proces** je spuštěná instance programu s _vlastním adresním prostorem a systémovými prostředky_. Na rozdíl od vláken procesy (standardně) **nesdílejí adresní prostor ani data**.

- **Synchronizace** procesů slouží ke **koordinaci více procesů**, _které spolupracují_.
- Protože procesy _standardně nesdílejí adresní prostor_, je pro jejich spolupráci nutné _využít vhodný mechanismus pro výměnu dat_ a _synchronizaci_.

---

# 2. Prostředky synchronizace procesů

## 2.1 Remote Procedure Call

> [!success]
> **Remote Procedure Call (RPC)** je mechanismus, který umožňuje **volat funkci běžící v jiném procesu nebo na jiném počítači**, jako _by byla součástí vlastního programu_.

> [!info]
> Je to _abstrakce nad IPC_ – obvykle využívá sockety.

### **2.1.1 Jak funguje?**

1. Proces zavolá vzdálenou funkci.
2. Parametry se **serializují** (převedou do přenositelné podoby = marshaling).
3. _Odešlou_ se druhému procesu.
4. Druhý proces převedě serializovaná data do **interní podoby** (= unmarshaling)
5. _Vykoná_ funkci.
6. Výsledek se opět _serializuje_.
7. _Odešle_ se zpět.
8. První proces **obdrží návratovou hodnotu**.

### 2.1.2 Typy RPC

#### Synchronní RPC

- Ve synchronním RPC čeká **volající proces na odpověď** ze vzdáleného procesu _po dobu trvání RPC_. **Proces je blokován**, dokud _druhý proces nevrátí výsledek_ volané procedury.

#### Asynchronní RPC

- Asynchronní RPC umožňuje procesu **pokračovat v práci bez čekání** na _dokončení vzdáleného volání._

#### Jednosměrné RPC

- Proces **pouze odešle požadavek**, nečeká na odpověď.

#### Multicast RPC

- Stejný požadavek se odešle **více procesům současně**.

## 2.2 Roury (Pipes)

> [!success]
> **Roura (Pipe)** je _prostředek IPC_ (Inter Process Communication), který umožňuje **předávání dat mezi dvěma procesy**.
>
> Data se zapisují na jeden konec roury a čtou z druhého.
>
> Přenášejí se jako **proud bajtů** v pořadí **FIFO**

> [!info]
> _Nejjednodušší forma_ IPC.

### 2.2.1 Typy rour

#### 2.2.1.1 Nepojmenovaná roura

- Vytváří ji operační systém
- Existuje pouze po dobu životnosti procesu, který ji vytvořil
- Dědí se přes `fork()` — proto ji mohou sdílet rodič a potomek

```
int fd[2];
pipe(fd);

pid_t pid = fork();

if (pid == 0) {
    // potomek
    close(fd[1]);      // nebude zapisovat
    read(fd[0], ...);
}
else {
    // rodič
    close(fd[0]);      // nebude číst
    write(fd[1], ...);
}
```

#### 2.2.1.2 Pojmenovaná roura

- Vytvoří se jako soubor v souborovém systému
- Existuje i po skončení procesů (ale data se nezachovají — je to stále buffer v jádře)
- Mohou ji použít **libovolné nesouvisející** (nemusí být potomek a rodič) **procesy**, znají-li cestu

## 2.3. Fronty zpráv

> [!success]
> **Fronta zpráv** je prostředek **IPC** (Inter Process Communication), který umožňuje _asynchronní komunikaci mezi procesy_.
>
> Jedná se o **pojmenovaný, perzistentní kanál** pro výměnu **strukturovaných zpráv**.

> [!info]
> Je možná **obousměrná** _komunikace_.

### **2.3.1 Jak funguje?**

1. Odesílající proces _vytvoří zprávu_.
2. Zprávu _vloží do fronty_.
3. Operační systém ji ve frontě **uchová**.
4. Přijímající proces _si zprávu z fronty přečte_.

> [!danger]
> Procesy **nemusí běžet současně** – zpráva může ve frontě čekat, dokud si ji příjemce nevyzvedne.

## 2.4 Socket

> [!success]
> **Socket** je _komunikační rozhraní_ (koncový bod komunikace), které umožňuje procesům _vzájemně si vyměňovat data_.
>
> Pomocí socketů mohou komunikovat:
>
> - procesy na **stejném** _počítači_,
> - procesy na **různých** _počítačích_.

> [!info]
> Je to _nejuniverzálnější IPC mechanismus_.

### **2.4.1 Jak funguje?**

1. _Vytvoření_ socketu.
2. _Navázání_ spojení.
3. _Přenos_ dat.
4. _Ukončení_ spojení.

### 2.4.2 Typy socketů

#### 2.4.2.1 Síťové sockety

- Komunikace _mezi různými počítači_ (ale mohou být i na stejném)
- Používají síťové protokoly **TCP/IP** nebo **UDP/IP**,
- Identifikují se pomocí **IP adresy a portu**.

#### 2.4.2.2 Unix Domain Sockets

- Komunikace pouze mezi procesy na stejném počítači.
- Identifikuje se cestou k souboru v souborovém systému.

## 2.5 Sdílená paměť

> [!success]
> **Sdílená paměť** je _mechanismus IPC_, který umožňuje více procesům přistupovat ke **stejné oblasti operační paměti**.
>
> Na rozdíl od ostatních IPC mechanismů se data **nekopírují**, ale všechny procesy **pracují přímo se stejnými daty**.

> [!info]
> Je to _nejrychlejší způsob komunikace_ mezi procesy (nic se nekopíruje)

> [!danger]
> Je nutné použít _synchronizační prostředky_! Může dojít k **race condition**

---

# 3. Večeřící filozofové (distribuovaná varianta)

- V klasické variantě mají filozofové přístup ke **sdíleným vidličkám**. Ale co, když nemáme sdílenou paměť? Koordinace **probíhá zasíláním zpráv**.

## 3.1 Varianta 1 – Vidličky jsou samostatné procesy

- Každá vidlička je vlastní proces. Filozof pošle vidličce zprávu “Mohu si tě vzít?”. Vidlačka odpoví “Ano” / “Ne”.

## 3.2 Varianta 2 – Filozofové komunikují mezi sebou

- Každý filozof dostane jednu špinavou vidličku
- Když chce jíst potřebuje další vidličku od souseda, pošle mu zprávu s žádostí o vidličku
- Pokud filozof obdrží žádost, vidličku si nechá pokud je čistá, jinak ji vyčistí a pošle (žádost si pamatuje)
- Když se filozof nají, vidličky jsou špinavé (pošle ji jedné zapamatované žádosti)