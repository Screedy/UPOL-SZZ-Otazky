>[!warning]
>Nově vytvořené instance by rovnou měly být v **konzistentním stavu**.

## Zapouzdření
- hodnoty slotů objektu smí **přímo** číst a měnit pouze metody daného objektu
- ostatní přistupují pouze pomocí zasílání zpráv
- tento přístup umožňuje jednodušší změnu vnitřní reprezentace dat a zabrání uvést objekt do nekonzistentního stavu
- ![[zapouzdreni-OOP.png]]
>[!info]
>Datům objektů, kterou můžeme pomocí zaslání zprávy nastavit říkáme **vlastnosti objektu** (properties).
## Polymorfismus
- různé třídy mohou definovat pro tutéž zprávu různé metody (liší se implementací)
```java
interface Flight {
    public void fly();
}

class Bat implements Flight {
    public void fly() {
        System.out.println("Bap bap");
    }
}

class Bird implements Flight {
    public void fly() {
        System.out.println("Flap flap");
    }
}
```
## Dědičnost
- společné rysy objektů "přesuneme" do obecnější třídy, od které pak specifičtější dědí
- šetří kód, snižuje potenciální množství chyb
- může dojít k tzv. **přepisování metod** (pro každou třídu definujeme jinou obsluhu zprávy)
	- pokud má objekt na výběr více metodami stejného názvu, vykoná vždy tu **nejvíce specifickou**
	- jiný náhled: hledá ji ve stromu třídu od spodu nahoru dokud ji nenajde (případně skončí chybou)c
	- i v tomto případě můžeme vynutit zavolání předchozí metody (v Lispu `(call-next-method`)
- typ *datové abstrakce*
>[!info] Princip dědičnosti
>Možnost vytvářet ke třídám potomky (eventuálně předky). Vzniká tím stromová hierarchie (**strom dědičnosti**). Pokud je vztah přímý (není na cestě obsažena třída) nazýváme **přímý předek/potomek**.
- ![[strom-trid.png]]
#### Vícenásobná dědičnost
- třída dědí o více než 1 rodiče (není podporováno ve všech jazycích)
- může přinášet tzv. *problém diamantu*
- ![[problem-diamantu.png]]
	- tento problém má různá řešení (podle jazyku)
	- `C++` - bere třídu A jako rozdílného předka podle B a C, z A udělá virtuální
	- `Python` - používá tzv. MRO (method resolution order) a linearizačního algoritmu, který vytvoří seznam předků jako seznam a podle něj hledá, metoda `__mro__` pro zjištění
- Jazyky nepodporující tuto funkcionalitu to řeší různě - pomocí rozhraní či abstraktních tříd (C#, Java)
- 
