# Další vlastnosti objektového modelu v Javě

## Řetězce (`String`)

- Třída `String` reprezentuje neměnné řetězce znaků.
- Nové řetězce se vytvářejí buď literálem (`"abc"`), nebo pomocí konstruktoru:
```java
String s = new String("abcdef");
```

### Důležité vlastnosti:
- `String` je **neměnný (immutable)** – všechny operace vytvářejí nový objekt.
- Porovnání pomocí `==` testuje identitu, ne obsah:
```java
String a = "abc";
String b = "abc";
a == b       // true (možná)
a.equals(b)  // vždy správně
```

### Časté metody:
- `length()` – délka
- `charAt(i)` – znak na pozici
- `indexOf("x")`, `substring(a,b)`

---

## Efektivní spojování řetězců: `StringBuilder`

```java
StringBuilder sb = new StringBuilder();
for (int i = 1; i <= 10; i++) {
    sb.append(i).append(" ");
}
String result = sb.toString();
```

Při spojování mnoha částí je `StringBuilder` výrazně výkonnější než `+`.

---

## Pole

Pole uchovává posloupnost prvků stejného typu.

### Deklarace a inicializace:
```java
int[] a = new int[10];
Car[] cars = new Car[5];
int[] b = {1, 2, 3};
```

### Přístup k prvkům:
```java
a[0] = 10;
int x = a[1];
```

### Procházení pole:

**Klasický cyklus:**
```java
for (int i = 0; i < a.length; i++) {
    System.out.println(a[i]);
}
```

**For-each:**
```java
for (int x : a) {
    System.out.println(x);
}
```

---

## Variabilní počet parametrů (`varargs`)

Metoda může přijmout libovolný počet argumentů (poslední parametr typu `...`):
```java
public double total(double discount, double... prices) {
    double sum = 0;
    for (double p : prices) sum += p;
    return sum * (1 - discount / 100);
}
```

Volání:
```java
total(10, 100, 200, 300);
```

---

## Statické atributy a metody

Přístupné bez vytváření objektu:
```java
public class MathFuncs {
    public static int fact(int n) {
        if (n == 0) return 1;
        return n * fact(n - 1);
    }
}
```

Volání:
```java
int f = MathFuncs.fact(5);
```

---

## Statické atributy – sdílená data

Užití např. pro počítání vytvořených instancí:
```java
public class Car {
    private static int unitsProduced;
    private final int serialNo;

    public Car(...) {
        serialNo = ++unitsProduced;
    }
}
```

---

## Konstanta – `static final`

```java
public class Physics {
    public static final int SPEED_OF_LIGHT = 299_792_458;
}
```

Použití:
```java
Physics.SPEED_OF_LIGHT;
```

---

## Singleton – návrhový vzor

Zajistí, že v programu existuje pouze **jedna instance** dané třídy:
```java
public class Logger {
    private static Logger logger;
    private long eventId;

    private Logger() { eventId = 1; }

    public static Logger getInstance() {
        if (logger == null)
            logger = new Logger();
        return logger;
    }

    public void log(String message) {
        System.out.println(eventId++ + ": " + message);
    }
}
```

Volání:
```java
Logger.getInstance().log("Zpráva");
```

---

## Shrnutí

- `String` je neměnný objekt; spojování přes `StringBuilder` je efektivní.
- Pole umožňuje uchovávat kolekce hodnot a pracovat s nimi pomocí indexů nebo `for-each`.
- `static` atributy/metody patří třídě, nikoliv objektu – užitečné pro konstanty, počítadla, nástroje.
- Vzor Singleton umožňuje bezpečné sdílení jediné instance v celém programu.

---

# Rozhraní a polymorfismus v Javě

## Rozhraní jako smlouva mezi objekty

Rozhraní definuje, jaké metody **musí** třída implementovat.  
Je to formální vyjádření **rozhraní objektu** – tedy způsobu, jakým lze s objektem komunikovat bez ohledu na jeho konkrétní implementaci.

Např. automobil ovládáme přes volant a pedály, aniž bychom museli znát vnitřní fungování motoru.

---

## Deklarace rozhraní

```java
public interface Shape {
    void printOut();       // výpis informací o objektu
    double getArea();      // výpočet plochy
}
```

- V rozhraní se definují pouze hlavičky metod (bez těla).
- Třída, která chce rozhraní implementovat, musí všechny metody definovat (`implements`).

---

## Implementace rozhraní

```java
public class Rectangle implements Shape {
    private double a, b;
    public Rectangle(double a, double b) { this.a = a; this.b = b; }

    public void printOut() {
        System.out.println("Obdélník o stranách " + a + ", " + b);
    }

    public double getArea() {
        return a * b;
    }
}

public class Circle implements Shape {
    private double r;
    public Circle(double r) { this.r = r; }

    public void printOut() {
        System.out.println("Kruh o poloměru " + r);
    }

    public double getArea() {
        return Math.PI * r * r;
    }
}
```

---

## Polymorfismus

Polymorfismus = schopnost zacházet s různými typy objektů jednotně na základě společného rozhraní.

```java
Shape x = new Rectangle(10, 20);
Shape y = new Circle(10);

Shape largest = x.getArea() > y.getArea() ? x : y;
largest.printOut();
```

- Pracujeme pouze s metodami, které definuje `Shape`.
- Není důležité, jestli je `x` obdélník nebo kruh – víme, že umí `getArea()` a `printOut()`.

---

## Předávání polí rozhraní

```java
public static void printShapes(Shape[] shapes) {
    for (Shape s : shapes) {
        s.printOut();
        System.out.println("Plocha: " + s.getArea());
    }
}
```

Funguje pro libovolné objekty, které implementují `Shape`:
```java
Shape[] shapes = {
    new Rectangle(4, 8),
    new Circle(10),
    new Rectangle(15, 20)
};

printShapes(shapes);
```

---

## Hledání největšího útvaru

```java
public static int largest(Shape[] shapes) {
    int index = -1;
    double max = Double.NEGATIVE_INFINITY;

    for (int i = 0; i < shapes.length; i++) {
        if (shapes[i].getArea() > max) {
            index = i;
            max = shapes[i].getArea();
        }
    }

    return index;
}
```

---

## Shrnutí

- Rozhraní definuje, co objekt umí, ne jak to dělá.
- `implements` znamená, že třída dodává konkrétní implementaci.
- Polymorfismus umožňuje zjednodušit logiku a pracovat se skupinami objektů bez ohledu na jejich konkrétní typ.
- Metody přijímající parametry typu rozhraní (`Shape[]`) umožňují zpracovávat různé typy dat jednotným způsobem.

---

# Dědičnost, přepisování metod a porovnávání objektů v Javě

## Dědičnost v Javě

Dědičnost umožňuje vytvořit **specializovanou třídu (potomek)** z obecné třídy (rodič). Potomek:
- Dědí veřejné (`public`) a chráněné (`protected`) metody a atributy.
- Může přidávat nové vlastnosti a metody.
- Může přepsat (override) chování zděděných metod.

Příklad hierarchie:

```
Osoba
├── Žák
├── Zaměstnanec
│   ├── Učitel
│   └── Technický pracovník
```

---

## Základní příklad dědičnosti

```java
public class Vehicle {
    protected double x, y;
    protected int direction;

    public void turn(int angle) { direction += angle; }
    public void driveForward(double distance) {
        double rad = Math.toRadians(direction);
        x += Math.cos(rad) * distance;
        y += Math.sin(rad) * distance;
    }
    public String toString() {
        return "Vehicle at " + x + ", " + y;
    }
}
```

```java
public class Car extends Vehicle {
    private int passengers;

    public Car(double x, double y, int p) {
        super.x = x;
        super.y = y;
        this.passengers = p;
    }

    @Override
    public String toString() {
        return "Car at " + x + ", " + y + " with " + passengers + " passengers";
    }
}
```

---

## Klíčové slovo `super`

- Volání konstruktoru rodiče: `super(...)`
- Přístup k metodě rodiče: `super.metoda()`

Používá se pro převzetí původní logiky při přepsání metody.

---

## Přepisování metod (method overriding)

Potomek může změnit chování metody rodiče:
```java
@Override
public void driveForward(double distance) {
    revenue += distance * FARE;
    super.driveForward(distance);
}
```

- Příklad: třída `Taxi` přidá výpočet tržby.

---

## Dědičnost vs. skládání objektů

- **Dědičnost** použijeme, když `A is a B` (např. `Car is a Vehicle`)
- **Skládání** použijeme, když `A has a B` (např. `Car has an Engine`)

Případ s třídou `Square extends Rectangle` může být problematický, pokud `Rectangle` umožňuje měnit strany nezávisle.

---

## Porovnávání objektů

### Porovnání pomocí `==`
Testuje **identitu** – zda proměnné odkazují na **stejný objekt**.

```java
Car c1 = new Car(...);
Car c2 = new Car(...);
c1 == c2; // false, i když mají stejná data
```

### Metoda `equals()`

Každý objekt má metodu `equals(Object other)` zděděnou z `Object`. Můžeme ji přepsat:

```java
@Override
public boolean equals(Object other) {
    if (other instanceof Car otherCar) {
        return this.plateNo.equals(otherCar.plateNo)
            && this.color.equals(otherCar.color)
            && this.speed == otherCar.speed;
    }
    return false;
}
```

- Kontrola typu pomocí `instanceof`
- Přetypování probíhá bezpečně – `Car otherCar = (Car) other;`
- `equals` by měla být reflexivní, symetrická a tranzitivní

---

## Rozhraní vs. dědičnost

| Vlastnost             | Rozhraní (`interface`)              | Dědičnost (`extends`)         |
|----------------------|--------------------------------------|-------------------------------|
| Definuje             | **Co objekt umí** (metody)           | **Z čeho objekt vychází**     |
| Více typů?           | Ano – může implementovat více       | Ne – pouze jeden předek       |
| Sdílení implementace | Ne (až na `default` metody)          | Ano – kód se dědí             |
| Typová flexibilita   | Vysoká (lepší pro polymorfismus)     | Méně flexibilní               |

---

## Výchozí (default) metody v rozhraní

Od Javy 8 mohou mít rozhraní i **default implementace** metod.

```java
public interface Shape {
    double getArea();

    default void printOut() {
        System.out.println("Tvar s plochou: " + getArea());
    }
}
```

- Pokud třída metodu `printOut()` nepřepíše, použije se výchozí verze.

---

## Shrnutí

- Dědičnost umožňuje sdílet vlastnosti a metody mezi třídami.
- Polymorfismus funguje i přes dědičnost – potomek lze použít místo předka.
- `super` odkazuje na rodičovskou třídu a její konstruktor nebo metody.
- Přepisování metod (`@Override`) umožňuje měnit nebo rozšiřovat chování.
- `equals()` umožňuje porovnávat obsah objektů, nikoliv jen odkazy.
- Výchozí metody v rozhraní rozšiřují možnosti bez porušení stávajícího kódu.

---