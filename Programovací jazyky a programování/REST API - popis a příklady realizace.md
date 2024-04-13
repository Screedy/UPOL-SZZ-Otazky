  
REST API (Representational State Transfer Application Programming Interface) je architektonický styl pro komunikaci mezi klientem a serverem pomocí standardních HTTP metod (GET, POST, PUT, DELETE) a formátů dat (například JSON, XML). Tento styl klade důraz na jednoduchost, rozšiřitelnost a nezávislost na stavech mezi klientem a serverem.

Ilustrace architektury REST API:

![[REST API.png]]

## Popis:

1. **Zdroje (Resources)**: Každý zdroj má jedinečný identifikátor (URI), kterým je možné k němu přistupovat. Například, pokud máme databázi uživatelů, každý uživatel by mohl mít svůj unikátní URI jako `/users/{id}`.

2. **Operace (Operations)**: Klient může provádět operace nad zdroji pomocí standardních HTTP metod. GET pro čtení, POST pro vytvoření, PUT pro aktualizaci a DELETE pro smazání zdroje.

3. **Reprezentace (Representation)**: Data, která jsou posílána mezi klientem a serverem, jsou reprezentována v určitém formátu, jako je JSON, XML, HTML atd.

4. **Stav aplikace (Statelessness)**: Každá požadavek od klienta na server musí obsahovat všechny informace potřebné pro porozumění a zpracování tohoto požadavku. Server neuchovává žádný kontext o klientovi mezi jednotlivými požadavky.

5. **Jednotné rozhraní (Uniform Interface)**: Rozhraní mezi klientem a serverem by mělo být jednotné, aby bylo snadné pro klienty porozumět a používat. To zahrnuje standardní HTTP metody a formáty dat.


## Příklady:

1. **Webová aplikace s REST API**: Webová aplikace může mít REST API pro komunikaci s backendem. Například, aplikace pro sociální sítě může mít REST API pro získávání informací o uživatelích, jejich příspěvcích a dalších dat.
    
2. **Mobilní aplikace s REST API**: Mobilní aplikace může komunikovat se vzdáleným serverem pomocí REST API. Mobilní aplikace může posílat požadavky na server pro získání dat nebo aktualizaci informací.
    
3. **IoT zařízení s REST API**: IoT zařízení může poskytovat REST API pro vzdálený přístup a správu. Například, chytrá domácnost může mít REST API pro ovládání osvětlení, termostatu a dalších zařízení.
    
4. **Cloudová služba s REST API**: Cloudová služba může poskytovat REST API pro manipulaci s daty v cloudu. Například, cloudové úložiště může mít REST API pro nahrávání, stahování a správu souborů.
    
5. **E-commerce platforma s REST API**: E-commerce platforma může poskytovat REST API pro správu produktů, objednávek a plateb. To umožňuje vývojářům integrovat platformu s různými aplikacemi a službami.

## Příklad dotazu:

``` JSON
POST /users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer your_access_token

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "country": "USA"
  }
}
```