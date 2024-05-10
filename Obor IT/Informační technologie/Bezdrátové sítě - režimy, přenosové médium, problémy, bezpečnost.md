
## Režimy
- **Base station** - infrastrukturní režim
	- řídí komunikaci **připojených** (asociovaných) **uzlů**
	- obvykle **stanice** komunikují **pouze** s **base station**
	- přepínač + most: typicky připojený do jiné drátové sítě
	- např. **AP** (Wi-Fi), **BTS** (mobilní sítě)
- **Ad-hoc** režim
	- komunikace stanic **přímo mezi sebou**
	- typicky **bez base station**
- **Mesh**
- **Opakovač**
- **Mostový režim**

### Příklady
- **Wi-Fi** (IEEE 802.11), WiMax (802.16)
	- (W)LAN/MAN
	- jednotky Mb/s až Gb/s
	- desítky m až jednotky km
- **Mobilní sítě**
	- WAN
	- jednotky kb/s až stovky Mb/s
	- stovky m až desítky km
- **Bluetooth** (IEEE 802.15.1)
	- PAN
	- stovky kb/s až jednotky Mb/s
	- jednotky až desítky metrů
- **Satelitní sítě**
	- WAN
	- až stovky Mb/s
	- stovky až tisíce km

## Přenosové médium
- Pomocí **elektromagnetické záření.** (**rádiové** a **mikro** **vlny**)
- Přenos dat pomocí šíření signálu na dané frekvenci

- **SNR** (Signal-to-Noise Ratio)
	- **poměr** úrovně **přijímaného** **signálu** a **šumu** prostředí
	- měření v **dB**
	- **absolutní minimum -100 dBm**, pak **nelze rozpoznat** od šumu

- Šíření signálu ve frekvenčním pásmu (band)
	- pásmo se uvažuje jako okruh (vyhrazená část spektra)
	- **FHSS** (Frequency Hopping Spread Spectrum)
		- pseudo-náhodné přeskakování v čase mezi více frekvencemi
		- podle klíče který by měl znát pouze příjemce a odesílatel
		- starší metoda
	- **DSSS** (Direct Sequence Spread Spectrum)
		- současné využití více frekvencí v rámci spektra
		- dnes používáme skoro všude

- **Modulace bitů**
	- vysílání/přijímání **pořád analogovým způsobem**
	- musíme tedy **převést bity** (digitální signál) **na analogový signál**
	- Způsoby:
		- změna amplitudy
		- změna frekvence
		- změna fáze
		- kombinace amplitudy s fází (nejčastější)

- **Multiplex**
	- **frekvenční** (FDM) - **rozděluje pásmo** na **nepřekrývající se podpásma** dané šířky pro přenos
	- **časový multiplex** (TDM) - rozdělení času na časové rámce, každý rámec má konstantní počet slotů, každý slot asociovaný s daným přenosem
	- **ortogonální frekvenční** (OFDM(A)) - využívá **současně více nosných frekvencí** pro přenosy s podpásmy. **nyní se využívá nejvíce**
	- **Kódový** (CPM(A)) - kódování přenosu v celém pásmu (využívá chipping)

## Problémy
1. **Path fading** - klesající úroveň signálu se vzdáleností a průchodů materiály
2. **Interference signálu** **a šumu** na stejném frekvenčním pásmu
3. **Multipath propagation** - více cest s modifikovaným signálem k příjemci
4. **Více chyb s vyšší frekvencí** a nebo **nižší úrovní signálu**

- **Řešení**:
	- **Více frekvencí** (spread, multiplex)
	- více vyšílačů/přijímačů
	- různé metody modulace bitů do signálu
	- **opakování přenosu**
	- **opravné kódy**

## Bezpečnost
### Wi-Fi zabezpečení
- Původní specifikace **WEP** (**problém**)
- dočasné **WPA**, pak **WPA2** a nejnovější **WPA3**
- Autentizace:
	- **Stanice vůči AP** (AP se vždy důvěřuje)
	1. Pomocí **sdíleného hesla** (**personal**)
	2. **autentizační protokol** (**enterprise**) - až od **WPA2**
- **Šifrování**
	- Šifrují se rámce, data a kontrolní součet rámce
	- u WPA2/3 se šifrují i některé hlavičky
- **WPS** (Wi-Fi Protected Setup)
	- generování a distribuce SSID a nastavení zabezpečení z AP na stanice

##### Navigace
Předchozí:  [[Bezpečnost počítačových sítích]]
Následující: [[Wi-Fi - standardy, access point, použití média, linkový rámec, zabezpečení]]
Celý okruh: [[2. Informační technologie]]