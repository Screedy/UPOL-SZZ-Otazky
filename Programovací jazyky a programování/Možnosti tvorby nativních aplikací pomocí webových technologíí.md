- Jako alternativa k nativnímu vývoji se nabízí vyvinout multiplatformní (někdy také hybridní) aplikaci.

- Ty jsou založeny na poměrně jednoduchém principu. Aplikace je tvořena nativní skořápkou (pouze minimální nativní aplikace) obsahující komponentu webview, která zpřístupňuje jádro webového prohlížeče.

- Skutečná aplikace je webová aplikace, která běží právě v této komponentě. Tento vývoj je poměrně populární jelikož umožňuje vyvinout snadno multiplatformní aplikaci, přičemž je sdílen kód na různých platformách. Nevýhodou je horší UI a UX (byť je v těchto oblastech v poslední době značný pokrok).

- Aby se mohla webová aplikace běžící uvnitř webview komponenty chovat jako nativní aplikace, musí mít možnost ovládat hardware daného zařízení. Například zpřístupnit fotoaparát čí datové uložiště.

- K tomu účelu se využívají frameworky pro vývoj multiplatformních aplikací jako například Apache Cordova nebo PhoneGap.

- Tento přístup je postupně je postupně utlačován technologiemi typu React native. Ty poskytují API pro přístup k systémovým službám a usnadňují distribuci nativní skořápky.


## Progresivní webová aplikace

- Díky neustále se rozrůstajícím možnostem webových prohlížečů a webových technologí je možné na místo výše uvedených frameworků použít jako interface mezi hardware právě webový prohlížeč. Díky tomu je možné z běžné webové stránky/aplikace vytvořit mobilní nebo desktopovou aplikaci. Aplikace tohoto typu se označují jako progresivní webové aplikace (PWA).

- PWA aplikace jsou nezávislé na OS, responzivní, umožňují práci offline, instalovatelné, bezpečné (lze je provozovat pouze na HTTPS) a dostupné skrze URL (není je možné distribuovat skrze aplikační obchody).

- Každá progresivní webová aplikace obsahuje manifest soubor, který udržuje základní informace o aplikaci. Offline modu je zajištěno pomocí JavaScriptu, přesněji řečeno servis workera, který slouží jako proxy middleware.

## HTML API

- Zpřístupnění hardware je možné skrze HTML API.

- Například IndexedDB API umožňuje v prohlížeči provozovat relační databázi a ukládat perzistentně data.

- Analogicky je možné využit Storage API, které jsme již představili. Fotoaparát je možné zpřístupnit pomocí MediaDevices rozhraní.
## **React Native**:

-  **Charakteristika**: React Native je framework vyvinutý společností Facebook, který umožňuje vývoj mobilních aplikací pomocí JavaScriptu a Reactu. Jedná se o open-source projekt, který umožňuje sdílení kódu mezi platformami iOS a Android.
- **Použití**: React Native umožňuje vývoj nativních mobilních aplikací, které mají výkon a vzhled podobný aplikacím vyvinutým přímo pro danou platformu. React Native využívá nativního UI, což zajišťuje, že aplikace vypadají a chovají se jako klasické nativní aplikace.
- **Výhody**: Jedním z hlavních benefitů React Native je možnost sdílení kódu mezi iOS a android aplikacemi, což snižuje náklady a zjednodušuje vývoj. Také umožňuje vývojářům s webovými dovednostmi využít své znalosti při vývoji mobilních aplikací.
## **Electron**:

- Elektron je technologie umožňující vytvářet multiplatformní desktopové aplikace. Princip je analogický jako v případě multiplatformních mobilních aplikací.
- Elektron poskytuje API, které zpřístupňuje částí operačního systému webové aplikaci, které běží v node.js. Renderování UI je zajištěno pomocí webview komponenty.

- **Charakteristika**: Electron je open-source framework vyvinutý společností GitHub, který umožňuje vytvářet multiplatformní desktopové aplikace pomocí webových technologií, jako jsou HTML, CSS a JavaScript. S Electronem můžete vytvářet aplikace pro Windows, macOS a Linux.
- **Použití**: Electron je často používán pro vývoj desktopových aplikací, jako jsou textové editory, komunikační aplikace nebo vývojová prostředí. Jednou z nejznámějších aplikací postavených na Electronu je například Visual Studio Code.
- **Výhody**: Jednou z hlavních výhod Electronu je možnost využití webových technologií pro vývoj desktopových aplikací, což může být pro vývojáře pohodlné a efektivní. Electron také poskytuje přístup k nativním funkcím operačního systému, což umožňuje vytvářet plnohodnotné desktopové aplikace.