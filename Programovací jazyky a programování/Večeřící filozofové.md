Problém večeřících filozofů je klasický synchronizační problém, který ilustruje problém sdílených zdrojů a hrozbu deadlocku. Jedná se o myšlenkový experiment, který popisuje situaci, kdy několik filozofů sedí u kruhového stolu s talíři jídla mezi sebou a vidlicemi na stůl procházející přes každého filozofa. Filozof může buď jíst, nebo myslet. Chce-li jíst, musí uchopit obě vidlice, které leží po obou stranách něj. Problém spočívá v tom, aby filozofové mohli jíst bez zablokování (deadlocku) a současně minimalizovali zákmity (starvace).

![[Filozofové.png]]
## Řešení za pomocí přidání číšníka

Jednoduché řešení lze dosáhnout zavedením číšníka u stolu. Číšník určí, kdo si hůlky vezme, co v podstatě vyřeší problém rozhodování. Protože si uvědomuje, které hůlky jsou použity, je schopen rozhodnout a zabránit tak deadlocku. Protože na stole zůstala v případě 5 filozofů ještě jedna hůlka, je zřejmé, že následovat v jezení bude ten filozof, který se stal jejím dočasným majitelem. Tomu pak číšník přisoudil hůlku, kterou zrovna obsluhuje vedle sedící filozof.

## Řešení s hierarchií zdrojů

Další jednoduché řešení dostaneme vyhrazením částečného pořadí, nebo hierarchie pro zdroje (v tomto případě hůlky), a zřízením konvence, že všechny zdroje budou dosahované v určitém pořadí a v opačném pořadí uvolněné. V našem případě budou zdroje (hůlky) očíslované od 1 po 5 v nějakém pořadí a každý filozof si vždy vezme nejdříve hůlku s menším číslem a až potom hůlku s větším číslem. Pak vždy položí nejdříve hůlku s vyšším číslem, následně hůlku s menším číslem. Pokud tedy 5 filozofů simultánní zvedne hůlku s menším číslem, tak zůstane na stole hůlka s největším číslem, takže 5. filozof bude bez hůlky. Navíc pouze jeden z filozofů bude mít přístup k oběma hůlkám. Když dojí, pustí obě hůlky, přičemž tu hůlku s nižším číslem pustí dříve, což umožní, aby se najedl filozof sedící vedle něj.

Toto řešení i navzdory vyhýbání se deadlokům není příliš praktické, speciálně v případě, pokud neznáme předem používanou množinu zdrojů. Například pokud program drží zdroje 3 a 5 a potřebuje ještě zdroj 2, musí vypustit zdroj 5, pak 3, aby mohl požádat o 2 a opět požádat o zdroje 3 a 5 v tomto pořadí. Právě proto je tento způsob velmi neefektivní.

## Řešení Chandel-Misra

V roce 1984 K. Mani Chandel a J. Misra navrhli jiné řešení problému obědvajících filozofů, aby povolili libovolnému počtu programů (číslovaných P1, ..., Pn) soutěžit o libovolný počet zdrojů (číslovaných R1, ..., Rm). Na rozdíl od Dijkstrova řešení tato označení mohou být libovolná. Uvědomme si, že toto není skutečný problém obědvajících filozofů, protože _vyžaduje_ jejich vzájemnou komunikaci.

1. Pro každý pár filozofů válčících o zdroj vytvoří hůlku a dají ji filozofovi s nižším ID. Každá hůlka může být buď špinavá, nebo čistá. Na začátku je každá hůlka špinavá.
2. V případě, že chce filozof použít množinu zdrojů, musí dostat hůlky od svých soupeřících sousedů. Pro všechny takové hůlky zašle žádanku.
3. Filozof, který obdrží požadavek, si hůlku nechá, pokud je čistá, v opačném případě ji přenechá žádajícímu filozofovi. Předtím, než tuto hůlku zašle filozofovi, ji nejdříve očistí.
4. Potom, co filozof dojí, všechny jeho hůlky jsou špinavé. Pokud nějaký filozof dříve požádal o hůlku, filozof, který ji momentálně vlastní, ji očistí a pošle.

Toto řešení umožňuje velké množství paralelních programů a řeší libovolně velký problém s předpokladem, že každé vlákno potřebuje právě jeden zdroj v čase.

## Jeden filozof je levák
Je to podobné řešení jako při hiearchii zdrojů. Všichni se snaží získat vždy prvně vidličku pro svou dominantní ruku. Pokud je však jeden z filozofů levák, dostane jeden filozof vždy obě vidličky a poté co dojí je položí. Od této chvíle se můžou najíst další filozofové.