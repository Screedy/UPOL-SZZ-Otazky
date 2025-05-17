## Úvod do jazyka Java

Java je jedním z nejpoužívanějších programovacích jazyků současnosti. Mezi hlavní výhody patří:

- **Srozumitelná a explicitní syntaxe**
- **Široká dostupnost knihoven a nástrojů**
- **Multiplatformnost** – jednou zkompilovaný kód lze spouštět na libovolném systému s JVM
- **Dlouhodobá udržitelnost** – vhodná pro rozsáhlé aplikace (bankovnictví, podnikové systémy)

Java je objektově orientovaný jazyk, ale pro jednodušší úlohy se často používá procedurální styl programování.

---

## Proměnné v Javě

Každá proměnná má:
- **Název**
- **Datový typ**
- **Paměťovou adresu**, kde je uložena její hodnota

### Deklarace:
```java
int a;                 // proměnná bez počáteční hodnoty
int b = 1;             // proměnná s hodnotou
final int c = 42;      // konstanta
```

Od Javy 10 lze použít:
```java
var b = 1;
final var c = 42;
```
(překladač typ odvodí automaticky – nebudeme používat kvůli přehlednosti)

---

## Primitivní datové typy

Java nabízí následující typy (Tabulka níže):

| Typ      | Popis                                |
|----------|----------------------------------------|
| `byte`   | Celá čísla (−128 až 127)              |
| `short`  | Celá čísla (−32 768 až 32 767)        |
| `int`    | Celá čísla (±2,1 miliardy)            |
| `long`   | Celá čísla (velký rozsah)             |
| `float`  | Desetinná čísla                       |
| `double` | Desetinná čísla (vyšší přesnost)      |
| `boolean`| Pravdivostní hodnota (`true`, `false`)|
| `char`   | Jeden znak                            |

---

## Výrazy a operátory

Výrazy kombinují proměnné a operátory. Java používá běžné operátory jako:

### Aritmetické operace:
```java
+, -, *, /, %, +=, -=, *=, ++, --
```

### Porovnávací operace:
```java
==, !=, <, >, <=, >=
```

### Logické operace:
```java
&&, ||, !
```

Příklad:
```java
int x = 10;
int y = 20;
int obvod = (x + y) * 2;
```

---

## Řízení toku – Podmínky

Konstrukce pro větvení kódu:

### `if` / `else`
```java
if (x < 0) {
    abs = -x;
} else {
    abs = x;
}
```

### `switch`
```java
switch (number) {
    case 1 -> "jedna";
    case 2 -> "dva";
    default -> "jiné";
}
```

---

## Cykly

### `while` cyklus
```java
int i = 1;
while (i <= 10) {
    System.out.println(i);
    i++;
}
```

### `for` cyklus
```java
for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}
```

### `do-while` cyklus
```java
int i = 1;
do {
    System.out.println(i);
    i++;
} while (i <= 10);
```

---

## První program

```java
public class MyFirstJavaProgram {
    public static void main(String[] args) {
        System.out.println("Prvni program!");
    }
}
```

---

## Shrnutí

- Java kombinuje procedurální a objektový přístup.
- Primitivní datové typy jsou základem výpočtů.
- K řízení toku slouží podmínky a cykly (`if`, `switch`, `for`, `while`).
- Syntaxe je podobná jazykům jako C nebo C#.

---

# Objektově orientované programování v Javě – třídy, objekty, metody

## Objekt jako model reálného světa

Objekty v paměti počítače reprezentují reálné entity (auta, žáky...). Každý objekt má:
- **Atributy** – vlastnosti (např. barva, rychlost, jméno)
- **Metody** – chování (např. zrychli, vytiskni se)

Objekt je **instance třídy** – šablony, která určuje, jaké vlastnosti a chování má mít.

---

## Třída a instance

Třída definuje:
- atributy – data objektu
- metody – funkce objektu

Např. třída `Car` popisuje auta:
```java
public class Car {
    private final String plateNo;
    private final String color;
    private int speed;

    public Car(String plateNo, String color) {
        this.plateNo = plateNo;
        this.color = color;
        this.speed = 0;
    }

    public void accelerate(int s) {
        speed += s;
    }

    public void brake(int s) {
        speed -= s;
        if (speed < 0) speed = 0;
    }

    public int getSpeed() {
        return speed;
    }

    public void printOut() {
        System.out.println(color + " car no. " + plateNo + " is running " + speed + "km/h");
    }
}
```

---

## Konstruktor

- Metoda, která nastavuje počáteční stav objektu.
- Má stejný název jako třída.
- Volá se při použití `new`:
```java
Car blueCar = new Car("1A2 4816", "blue");
```

---

## Zapouzdření (Encapsulation)

- Atributy jsou `private`, přístup je přes veřejné metody (`public`).
- Chrání objekt před nekonzistencí.
- Snadnější údržba a rozšiřitelnost kódu.

Např. metoda `brake()` zajistí, že rychlost nebude záporná.

---

## Identita objektů

Proměnná neobsahuje objekt, ale **odkaz** na něj:
```java
Car a = new Car(...);
Car b = a;
```

Obě proměnné odkazují na stejný objekt – změna přes `b` ovlivní i `a`.

Testování identity:
```java
a == b      // true, pokud odkazují na stejný objekt
```

Pozor: dva různé objekty se stejným obsahem jsou stále různé:
```java
new Car("1A2", "blue") == new Car("1A2", "blue") // false
```

---

## Null reference

Proměnná může neodkazovat na žádný objekt:
```java
Car car = null;
car.printOut(); // vyhodí výjimku NullPointerException
```

---

## Skládání objektů

Objekt může obsahovat jiné objekty jako atributy:
```java
public class TrafficLight {
    private Light red;
    private Light yellow;
    private Light green;

    public TrafficLight() {
        red = new Light("red");
        yellow = new Light("yellow");
        green = new Light("green");
    }

    public void setStop() {
        turnAllOff();
        red.turnOn();
    }

    private void turnAllOff() {
        red.turnOff();
        yellow.turnOff();
        green.turnOff();
    }

    public void printOut() {
        red.printOut();
        yellow.printOut();
        green.printOut();
    }
}
```

---

## Konvence pojmenování

- Třída: `Car`, `TrafficLight` – velké písmeno na začátku
- Proměnná/metoda: `speed`, `printOut` – malé písmeno na začátku, camelCase
- `private` metody a atributy začínají malým písmenem, `public` třídy a metody podle konvence

---

## Shrnutí

- Třídy popisují objekty – jejich vlastnosti (atributy) a chování (metody).
- Objekty se vytvářejí pomocí `new` a inicializují konstruktorem.
- Zapouzdření chrání stav objektu.
- Identita objektu je určena referencí.
- Objekty lze skládat z jiných objektů.
- Dodržování konvencí zlepšuje čitelnost a správnost kódu.

---