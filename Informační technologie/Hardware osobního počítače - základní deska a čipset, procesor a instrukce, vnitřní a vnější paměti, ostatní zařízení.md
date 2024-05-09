## Vnitřní komponenty
- umístěny ve skříni počítače
- základní deska, procesor s chladičem, operační paměť, přídavné karty (grafická, zvuková, síťová atd.), pevné disky, mechaniky výměnných diskových médií, zdroj napájení/baterie, ventilátory

## Vnější komponenty
- umístěny mimo skříň počítače
- displej, klávesnice, myš, touchpad

## Základní deska a chipset
- slouží jako centrální platforma, na kterou jsou připojeny všechny ostatní komponenty počítače
- na základní desce se nachází **čipset**, který řídí datový tok mezi procesorem, pamětí, grafickou kartou a dalšími periferiemi
- **Sběrnice (BUS):**
	- soustava vodičů pro komunikaci a přenos dat
	- u sběrnice je důležitá **šířka přenosu** (kolik b můžeme najednou přenést), **frekvence** (v Hz), **propustnost** (množství přenesených dat za sekundu)
	- Typy sběrnic:
		- **Procesorová sběrnice (FSB)**: 
			- Spojuje procesor (CPU) s hlavním paměťovým řadičem.
			- **Účel**: Hlavním úkolem procesorové sběrnice je poskytovat rychlý přenos dat mezi CPU a pamětí, což je zásadní pro celkový výkon systému.
		- **Paměťová sběrnice**:
			- Zajišťuje komunikaci mezi CPU a fyzickou pamětí (RAM).
			- Speciální sběrnice, která se používá pro přenos dat, adres a kontrolních signálů mezi procesorem a pamětí.
			- **Účel**: Umožnit rychlý přístup k datům uloženým v RAM, což je klíčové pro rychlé vykonávání programů a operací.
		- **Rozšiřující sběrnice**:
			- Umožňuje připojení rozšiřujících karet nebo periférií.
			- grafické karty, síťové karty, zvukové karty, ...
			- ISA, PCI a AGP, PCIe
			- **Účel**: Poskytovat modulární rozšiřitelnost počítačů, umožňující uživatelům přidávat nové funkce a vylepšovat existující vlastnosti bez nutnosti nahrazovat celý počítač.
- **Chipset**:
	- koordinuje přenos dat mezi procesorem, pamětí, grafickými kartami, pevnými disky a dalšími periferiemi
	- Skládá z jednoho nebo více integrovaných obvodů, které fungují jako most mezi různými komponentami počítače.
	- V moderních počítačích může chipset rovněž řídit některé dodatečné funkce, jako je správa energie a interakce s externími zařízeními.
	1. **Severní můstek** (Northbridge)
	    - **Úloha**: Severní můstek byl zodpovědný za řízení vysokorychlostní komunikace mezi CPU, GPU a RAM. 
	    - V moderních počítačových architekturách jsou funkce severního můstku často integrovány přímo do CPU.
	2. **Jižní můstek** (Southbridge)
	    - **Úloha**: Jižní můstek se zabývá řízením většiny vstupně-výstupních (I/O) úloh, včetně komunikace s pevnými disky, USB porty, zvukovými zařízeními, a dalšími periferními zařízeními.
	    - **Rozhraní**: Zahrnuje řadiče pro rozhraní jako SATA pro disky, PCI pro rozšiřující karty a USB pro externí zařízení.

## Procesor a instrukce
- **Procesor (CPU)** je mozek počítače a zpracovává všechny instrukce z operačního systému a běžících aplikací.
- Procesor vykonává instrukce zapsané v programovém kódu, které mu říkají, co má dělat
- **Výrobci:** Intel, AMD, Apple, Qualcomm, Texas Instruments, ...
- **Mikroprocesor** = integrovaný obvod/čip nejvyššího stupně integrace

- Skládá se z:
	- **ALU** - realizuje výpočetní (aritmetické a logické) operace, celočíselná a v plovoucí řádové čárce (FPU)
	- **CU (řadič)** - zpracovává instrukce programu nad daty čtenými a zapisovanými z/do registrů
	- **cache paměť** - různé úrovně L1, L2, L3, **radič cache**
	- **Registry** - paměťové buňky pro instrukcemi zpracovávaná data
	- **řadič operační paměti** - pro práci s (virtuální) operační pamětí programů

- Instrukční sady:
	- **CISC** - complete instruction set computer
		- úplná instrukční sada, více instrukcí i pro déletrvající operace
	- **RISC** - reduced instruction set computer
		- redukovaná instrukční sada, instrukce pouze pro základní jednodušší operace, složitější překladačem programu
- Rigistry mají u CISC různý význam, u RISC jsou obecně univerzální
	- univerzální (datové) – pro operandy, mezivýsledky a výsledky instrukcí: EAX (RAX), EBX (RBX), ECX (RCX), EDX (RDX)
	- se stanoveným významem – pro řízení vykonávání programu, např. EIP (RIP), EBP (RBP), ESP (RSP), EFlags, pro implicitní operandy a výsledky, např. ESI (RSI), EDI (RDI), pro řízení procesoru, např. CRx, TRx, a další
## Vnitřní a vnější paměti
- umožňují ukládání, načítání a správu dat a programů
- důležité parametry u paměti jsou **kapacita, přenosová rychlost, přístupová doba**, spolehlivost a cena

### Vnitřní paměti
- slouží pro krátkodobé ukládání
- menší kapacity (řádově do GB), vyšší rychlosti, nízká přístupová doba
- **RAM**, **Registry**, **Cache**

### Vnější paměti
- poskytují trvalé ukládání dat a programů a jsou důležité pro dlouhodobé uchování informací
- větší kapacita, nižší rychlosti a vyšší přístupová doba
- jsou energeticky nezávislé
- CD/DVD, HDD, SSD, Cloud storage, ...

## Ostatní zařízení
- Různé přídavné karty jako je GPU, Síťové karty, zvukové, RAID karty, ...

##### Navigace
Předchozí:  [[Detekční a samoopravné kódy]]
Následující: [[Počítačové sítě, jejich služby a architektury]]
Celý okruh: [[2. Informační technologie]]