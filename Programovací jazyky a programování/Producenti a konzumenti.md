Problém producentů a konzumentů je klasickým problémem synchronizace vláken, který popisuje situaci, kdy máme několik vláken produkujících data (producenti) a několik vláken zpracovávajících tato data (konzumenti). Producenti vytvářejí data a umísťují je do sdílené fronty (bufferu), zatímco konzumenti odebírají data ze stejné fronty a zpracovávají je.

Vzor producenta a spotřebitele umožňuje lépe souběžně běžet cyklickým procesům, které pracují v různých rychlostech. Díky použití zásobníku jako úložného prostoru může producent vytvářet data nezávisle na rychlosti spotřebitele. Pokud je možnost tvorby dat rychlá, může producent tyto data vytvářet napřed a spotřebitel je pak bude zpracovávat ve svém vlastním tempu. Je to obzvláště vhodné například při komunikaci po síti, kdy fungují dva procesy v různých rychlostech. První proces může neustále přijímat pakety ze sítě, zatímco druhý přijaté pakety analyzuje. V tomto příkladě je první proces producentem a druhý spotřebitelem. S použitím zásobníku mohou být pakety přijaté rychleji, než jsou analyzovány. Komunikace je tak velmi efektivní a minimalizuje ztrátu dat.

Zde je ukázka kódu, ve kterém může dojít k deadlocku:

``` C
int pocetPolozek = 0;

producent() {
    while (true) {
        polozka = vytvoritPolozku();
        if (pocetPolozek == VEL_ZASOBNIKU) {
            spat();
        }
        vlozPolozkuDoZasobniku(polozka);
        pocetPolozek = pocetPolozek + 1;
        if (pocetPolozek == 1) {
            vzbudit(spotrebitel);
        }
    }
}

spotrebitel() {
    while (true) {
       if (pocetPolozek == 0) {
           spat();
       }
       
       polozka = vyjmoutPolozkuZeZasobniku();
       pocetPolozek = pocetPolozek – 1;
       
       if (pocetPolozek == VEL_ZASOBNIKU - 1) {
           vzbudit(producent);
       }
       spotrebujPolozku(polozka);
    }
}
```

Za běžných okolností nedojde k žádnému problému. Rozběhnou se oba procesy, spotřebitel, pokud je počet položek nulový, usne. Když běží producent a zásobník není plný, vloží do něj položku, a probudí spotřebitele. A tak vše běží dál. Problém nastává v této situaci: spotřebitel zjistí, že v zásobníku nejsou žádné položky. Chystá se usnout. Pokud se v tu chvíli ale dostane na řadu producent, který přidá položku a zavolá signál probuzení spotřebitele, spotřebitel ji nepřijme, protože ještě nespí. Pak usne, po krátké době producent naplní zásobník a usne také. Nikdy se však už ani jeden neprobudí. Problém se dá vyřešit pomocí Semaforů. Semafor je speciální celočíselný datový typ, asociovaný se dvěma funkcemi:

1. signal() – jeho zavoláním se celočíselná hodnota semaforu zvedne o 1, nahrazuje volání funkce vzbudit()
2. cekat() – zavolani funkce cekat() sníží hodnotu semaforu o 1; pokud je hodnota semaforu již před zavoláním 0, nahrazuje toto volání funkci spát(), dokud někdo nezavolá signal() a nezvýší tím hodnotu semaforu o 1

Obě funkce signal() a cekat() jsou nedělitelné atomické operace. Použitím semaforu nahradíme proměnnou pocetPolozek. Zde je kód, který problém řeší vhodným způsobem:

``` C
int volne = VEL_ZASOBNIKU;  	// semafor, počet volných slotů v zásobníku
int obsazene = 0;		// semafor, počet obsazených slotů v zásobníku

producent() {
       while (TRUE) {
               polozka = vytvoritPolozku();
               cekat(volne);
               vlozPolozkuDoZasobniku(polozka);
               signal(obsazene);
       }
}

spotrebitel() {
        while (TRUE) {
                cekat(obsazene);
                polozka = vyjmoutPolozkuZeZasobniku();
                signal(volne);
                spotrebujPolozku(polozka);
        }
}
```