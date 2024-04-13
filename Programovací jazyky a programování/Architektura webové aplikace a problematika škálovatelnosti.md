Většina webových aplikací se skládá ze tří částí: uživatelského rozhraní, logiky aplikace a datového rozhraní. Význam uživatelského rozhraní je jasný. Logika aplikace reprezentuje implementovanou funkcionalitu. Datové rozhraní představuje rozhraní pro připojení k databázi, kde jsou uložena data, se kterými aplikace pracuje.

## Monolitická architektura

Vše v jednom souboru.

## MVC architektura

Rozděluje aplikaci na 3 základní celky:

Model - Odpovídá za práci s daty a přístup k databázi. Také určuje formát dat.
View - Vytváří vizualizaci (UI). Typicky taková šablona jak bude vypadat webová stránka při poskytnutí určitých dat.
Controller - Implementuje části funkcionality aplikace. Většinou metody, kterým lze předávat parametry.

![[MVC.png]]

## Microservices architektura

Microservices architektura je v určitém smyslu protikladem monolitické architektury, ve které je aplikace realizována jako jeden celek. V případě microservices architektury jsou jednotlivé části aplikace rozděleny na malé nezávislé služby, jejímž pospojováním (vzájemnou komunikací) získáme výslednou aplikaci. Porovnání monolitické a microservices architektury znázorňuje nadcházející obrázek.

![[Microservices vs Monolit.png]]

Pro komunikaci mezi službami nebo UI a službou se většinou využívá webové API.