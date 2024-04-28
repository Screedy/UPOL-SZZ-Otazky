- Technologie AJAX (Asynchronous JavaScript and XML) je způsobem komunikace mezi webovým prohlížečem a serverem bez nutnosti obnovení celé stránky. 
- Tento přístup umožňuje **dynamicky aktualizovat obsah** stránky a interagovat s uživatelem, **aniž by došlo k kompletnímu načtení nové stránky**.
## Použití:
Použití AJAXu může zahrnovat:
1. **Dynamické načítání obsahu**: Místo načtení celé nové stránky můžete pomocí AJAXu načíst pouze část stránky, což může zlepšit rychlost a výkon webové aplikace.
2. **Asynchronní odesílání dat na server**: Uživatelské akce, jako je vyplnění formuláře, mohou být odeslány na server pomocí AJAXu bez nutnosti obnovení celé stránky. To umožňuje rychlejší a plynulejší interakci s uživatelem.
3. **Dynamické aktualizace obsahu**: Webová stránka může pomocí AJAXu periodicky aktualizovat obsah nebo přijímat aktualizace z serveru bez nutnosti obnovení celé stránky. To je užitečné například pro zobrazení živých dat.
4. **Získávání dat z různých zdrojů**: AJAX umožňuje získávat data z různých zdrojů, jako jsou REST API nebo XML soubory, a integrovat je do webové stránky.

K použití AJAXu se obvykle používají technologie jako JavaScript pro manipulaci s DOM (Document Object Model) a HTTP žádosti pro komunikaci se serverem. Moderní webové frameworky a knihovny, jako je například jQuery nebo frameworky založené na Reactu nebo Angularu, poskytují abstrakce a nástroje pro snadnější práci s AJAXem.

Příklad užití AJAXu:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AJAX Example</title>
</head>
<body>

<div id="content">
    <p>Obsah se načte pomocí AJAXu.</p>
</div>

<button id="loadData">Načíst data</button>

<script>
    document.getElementById('loadData').addEventListener('click', function() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'example.txt', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                document.getElementById('content').innerHTML = xhr.responseText;
            } else if (xhr.readyState === 4 && xhr.status !== 200) {
                console.error('Chyba při načítání dat: ' + xhr.status);
            }
        };
        xhr.send();
    });
</script>

</body>
</html>
```