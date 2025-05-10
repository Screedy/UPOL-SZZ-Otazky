- jedná se o klasické synchronizační úlohy v paralelním programování
	- takže ilustrují klasické problém, které mohou nastat - *uváznutí, vyhledaovění, vzájmené vyloučení*
## Výrobci a spotřebitelé
- **zadání**: ![[Pasted image 20250310213925.png]]
- **požadavky**: každá zpráva se musí zpracovat právě jednou
- vzejde invariant `pocet_vyzvednuti_zpravy ≤ pocet_ulozeni_zpravy`
- tento "systém" ukládání do bufferu se používá pro zvýšení efektivity (např. komunikace po síti)
- **řešení 1**: ![[Pasted image 20250310214445.png]]
- **řešení 2 (semafory)**: ![[Pasted image 20250310214511.png]]
- **řešení 3 (obecný počet)**: ![[Pasted image 20250310214721.png]]
## Večeřící filozofové
- ilustruje synchronizační problém při správě sdílených zdrojů pro více procesů
- popis algoritmu problému: ![[Pasted image 20250313204929.png]]
- nutné doplňující podmínky:
	- filozof potřebuje k jídlu 2 vidličky
	- 2 filozofové nemůžou držet současně 1 vidličku
	- absence uváznutí
	- absence vyhladovění
	- absence zbytečného čekání
#### Řešení 1 (levák):
- filozofové se snaží získat vidličku dominantní rukou (všichni praváci, jen jeden levák)
- tím pádem jeden vždy dostane obě vidličky a může s najíst, poté je položí a nají se zbytek
- neřeší vyhladovění zdrojů
#### Řešení 2 (hierarchie zdrojů)
- zdroje musí být v určitém pořadí získané a v opačném zase uvolněné
- V našem případě budou zdroje (hůlky) očíslované od 1 po 5 v nějakém pořadí a každý filozof si vždy vezme nejdříve hůlku s menším číslem a až potom hůlku s větším číslem. 
- Pak vždy položí nejdříve hůlku s vyšším číslem, následně hůlku s menším číslem. 
- Pokud tedy 5 filozofů najednou zvedne hůlku s menším číslem, tak zůstane na stole hůlka s největším číslem, takže 5. filozof bude bez hůlky. 
- Navíc pouze jeden z filozofů bude mít přístup k oběma hůlkám. Když dojí, pustí obě hůlky, přičemž tu hůlku s nižším číslem pustí dříve, což umožní, aby se najedl filozof sedící vedle něj.
#### Řešení 2 (číšník)
- Jednoduché řešení lze dosáhnout zavedením číšníka u stolu. 
- Číšník určí, kdo si hůlky vezme, co v podstatě vyřeší problém rozhodování. Protože si uvědomuje, které hůlky jsou použity, je schopen rozhodnout a zabránit tak deadlocku. 
- Protože na stole zůstala v případě 5 filozofů ještě jedna hůlka, je zřejmé, že následovat v jezení bude ten filozof, který se stal jejím dočasným majitelem. Tomu pak číšník přisoudil hůlku, kterou zrovna obsluhuje vedle sedící filozof.
- Nevýhodou je přidání 1 centrálního bodu (číšníka)
## Čtenáři a písaři
- Popisuje problém např. přístupu ke sdílené databázi/souboru
- **Čtenáři** mohou data pouze **číst**, ale nesmí je měnit. **Může jich být více současně**.
- **Písaři** mohou data **měnit**, ale **musí mít výhradní přístup** (tj. žádný jiný čtenář ani písař nesmí mít přístup současně).
- Řešení se může zdát přímočaré, ale je nutné dávat pozor na spravedlivost
- Některé jazyky přímo poskytují *RW lock*
#### Řešení 1
- Preferujeme čtenáře a písař může vstoupit až když žádný čtenář nečte
- Písaři mohou hladovět
#### Řešení 2
- Použití prioritní fronty, která zajistí střídání (spravedlivé)