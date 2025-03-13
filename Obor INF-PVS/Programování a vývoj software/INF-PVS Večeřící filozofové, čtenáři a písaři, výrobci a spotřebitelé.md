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
- 