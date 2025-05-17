# Abstraktní třídy, výčtové typy, záznamy a omezení dědičnosti

## Abstraktní třídy a metody

Abstraktní třída slouží jako základ pro **obecné chování**, které není samostatně použitelné – má sloužit jako **šablona pro potomky**.

- Nelze z ní vytvářet instance.
- Může obsahovat jak abstraktní (bez těla), tak i konkrétní metody.

```java
public abstract class Expression {
    public abstract int evaluate();
}
```

Třída `ConstantExpression` pak implementuje chování:

```java
public class ConstantExpression extends Expression {
    private final int value;
    public ConstantExpression(int value) {
        this.value = value;
    }
    public int evaluate() {
        return value;
    }
}
```

---

## Dědičnost a přepisování metod

Kombinací abstraktních tříd lze efektivně modelovat např. aritmetické výrazy:
```java
public abstract class AbstractOperationExpression extends Expression {
    protected final Expression lhs;
    protected final Expression rhs;

    public AbstractOperationExpression(Expression lhs, Expression rhs) {
        this.lhs = lhs;
        this.rhs = rhs;
    }

    protected abstract String getOperationSymbol();

    public String toString() {
        return "(" + lhs + " " + getOperationSymbol() + " " + rhs + ")";
    }
}
```

---

## Výčtové typy (`enum`)

`enum` definuje **konečnou množinu předem známých hodnot** – např. typ operace.

```java
public enum ArithmeticOperation {
    ADDITION("+"),
    SUBTRACTION("-"),
    MULTIPLICATION("*"),
    DIVISION("/");

    private final String symbol;

    ArithmeticOperation(String symbol) {
        this.symbol = symbol;
    }

    public String getSymbol() {
        return symbol;
    }
}
```

Hodnoty typu `ArithmeticOperation` lze použít v `switch`:
```java
switch (operation) {
    case ADDITION -> ...
}
```

---

## Třída `BinaryExpression` s výčtovým typem

```java
public class BinaryExpression extends Expression {
    private final Expression lhs;
    private final Expression rhs;
    private final ArithmeticOperation operation;

    public BinaryExpression(ArithmeticOperation operation, Expression lhs, Expression rhs) {
        this.lhs = lhs;
        this.rhs = rhs;
        this.operation = operation;
    }

    public int evaluate() {
        int left = lhs.evaluate();
        int right = rhs.evaluate();
        return switch (operation) {
            case ADDITION -> left + right;
            case SUBTRACTION -> left - right;
            case MULTIPLICATION -> left * right;
            case DIVISION -> left / right;
        };
    }

    public String toString() {
        return "(" + lhs + " " + operation.getSymbol() + " " + rhs + ")";
    }
}
```

---

## Záznamy (`record`)

`record` je datový typ určený pro **neměnné datové třídy** – typicky DTO, hodnotové typy.

- Automaticky generuje konstruktor, `toString()`, `equals()`, `hashCode()`
- Nelze měnit hodnoty atributů
- Nelze dědit z `record`, ale může implementovat rozhraní

```java
public record Point(double x, double y) {
    public double distance(Point that) {
        return Math.sqrt(Math.pow(this.x - that.x, 2) + Math.pow(this.y - that.y, 2));
    }
}
```

---

## Sealed typy (omezení dědičnosti)

`sealed` určuje **přesně, kdo smí dědit** z dané třídy nebo rozhraní:

```java
public sealed interface Expression permits ConstantExpression, BinaryExpression { }
```

- Zajišťuje typovou uzavřenost
- Umožňuje bezpečně využít `switch` bez `default` větve

---

## Pattern matching `switch` pro `record`

Java umožňuje v `switch` konstrukci rozbalit záznam:
```java
public static String toString(Expression expr) {
    return switch (expr) {
        case ConstantExpression(int value) -> Integer.toString(value);
        case BinaryExpression(ArithmeticOperation op, Expression l, Expression r) ->
            "(" + toString(l) + " " + op.getSymbol() + " " + toString(r) + ")";
    };
}
```

Podmínky lze doplnit o `when`:
```java
case BinaryExpression(ArithmeticOperation op, Expression l, Expression r)
    when op == ArithmeticOperation.DIVISION && r instanceof ConstantExpression c && c.value() == 0
    -> "DELENI NULOU";
```

---

## Shrnutí

- **Abstraktní třídy** umožňují definovat strukturu pro své potomky.
- **Výčtové typy (`enum`)** bezpečně nahrazují magické konstanty.
- **Záznamy (`record`)** jsou efektivní a imutabilní datové objekty.
- **Sealed typy** umožňují přesně omezit dědičnost – užitečné pro bezpečnost a predikovatelnost.

---

# Výjimky, balíčky a práce se soubory v Javě

## Výjimky – ošetření chybových stavů

Při běhu programu může dojít k neočekávané situaci – např. dělení nulou, neplatný vstup, chyba při čtení ze souboru.

Java poskytuje mechanismus **výjimek (exceptions)**, který tyto stavy zachytí a umožní na ně reagovat.

### Vlastní výjimky
```java
public class InvalidDigitException extends Exception {
    private final char invalidDigit;
    public InvalidDigitException(char c) { invalidDigit = c; }
    public char getInvalidDigit() { return invalidDigit; }
}
```

### Vyvolání výjimky
```java
if (number.length() > 31) throw new IntegerOverflowException();
if (digit != '0' && digit != '1') throw new InvalidDigitException(digit);
```

### Deklarace výjimky
```java
public static int binaryToInt(String number) throws InvalidDigitException, IntegerOverflowException
```

---

## Ošetření výjimek

### Konstrukce `try-catch`
```java
try {
    int result = binaryToInt("10201");
} catch (InvalidDigitException e) {
    System.out.println("Neplatná číslice: " + e.getInvalidDigit());
} catch (IntegerOverflowException e) {
    System.out.println("Příliš velké číslo");
}
```

### Více typů výjimek:
```java
catch (InvalidDigitException | IntegerOverflowException e) { ... }
```

### Blok `finally` – provede se vždy:
```java
try { ... } catch (...) { ... } finally { /* uvolnění zdrojů */ }
```

---

## Balíčky (packages)

Balíčky slouží k organizaci tříd a zabránění konfliktům jmen.

### Deklarace balíčku:
```java
package cz.upol.jj1.lecture07;
```

### Použití třídy z jiného balíčku:
```java
import cz.upol.jj1.lecture07.Foo;
```

- Třídy ve stejném balíčku se vidí bez `import`.
- `java.lang` je importováno automaticky.

---

## Práce s textovými soubory

### Zápis (s `PrintWriter` a `FileWriter`)
```java
try (PrintWriter pwr = new PrintWriter(new FileWriter("/tmp/employees.csv"))) {
    for (Employee e : employees) {
        pwr.printf("%s,%d,%.2f%n", e.name(), e.age(), e.salary());
    }
} catch (IOException e) {
    System.out.println("Chyba při zápisu do souboru");
}
```

### Čtení (s `BufferedReader`)
```java
try (BufferedReader br = new BufferedReader(new FileReader("/tmp/employees.csv"))) {
    String line;
    while ((line = br.readLine()) != null) {
        String[] parts = line.split(",");
        Employee e = new Employee(parts[0], Integer.parseInt(parts[1]), Double.parseDouble(parts[2]));
        System.out.println(e);
    }
} catch (IOException e) {
    System.out.println("Chyba při čtení ze souboru");
}
```

---

## Try-with-resources

Zjednodušuje správu zdrojů – automaticky zavře soubory:
```java
try (FileWriter writer = new FileWriter("...")) {
    // automaticky zavře writer
}
```

---

## Práce s binárními soubory

### Zápis (`DataOutputStream`)
```java
try (DataOutputStream dos = new DataOutputStream(new FileOutputStream("..."))) {
    dos.writeUTF(e.name());
    dos.writeInt(e.age());
    dos.writeDouble(e.salary());
}
```

### Čtení (`DataInputStream`)
```java
try (DataInputStream dis = new DataInputStream(new FileInputStream("..."))) {
    while (dis.available() > 0) {
        Employee e = new Employee(dis.readUTF(), dis.readInt(), dis.readDouble());
        System.out.println(e);
    }
}
```

---

## Práce se soubory s objekty

### Serializace (`ObjectOutputStream`)
```java
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("..."))) {
    oos.writeObject(employees); // pole Employee[]
}
```

### Deserializace (`ObjectInputStream`)
```java
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("..."))) {
    Employee[] es = (Employee[]) ois.readObject();
}
```

Třída musí implementovat `Serializable`:
```java
public record Employee(...) implements Serializable { }
```

---

## Shrnutí

- Výjimky zajišťují bezpečnou reakci na chyby.
- Bloky `try-catch-finally` slouží k jejich záchytu a ošetření.
- Práce se soubory je možná jak s textovými, tak binárními daty.
- Serializace umožňuje ukládat celé objekty a jejich pozdější načtení.
- Try-with-resources výrazně zjednodušuje správu otevřených zdrojů.

---

# Komentáře a jednotkové testování v Javě (JUnit)

## Komentáře v kódu

Komentáře pomáhají pochopit, **co program dělá a proč**, nikoliv jak. Program by měl být čitelný sám o sobě – komentáře doplňují složitější nebo právně či technicky důležité informace.

### Typy komentářů:
- **Jednořádkový:** `// komentář`
- **Víceřádkový:** `/* více řádků komentáře */`
- **JavaDoc komentář:** `/** ... */` – slouží pro generování dokumentace

```java
/**
 * Metoda převede řetězec v binární soustavě na int.
 * @param number řetězec např. "110011"
 * @return odpovídající hodnota typu int
 * @throws IntegerOverflowException při přetečení rozsahu
 * @throws InvalidDigitException při neplatném znaku
 */
```

JavaDoc tagy:
- `@param`, `@return`, `@throws`, `@see`, `@author`, `@since`

---

## Zásady psaní komentářů

- Komentuj **záměr**, ne implementaci.
- Komentář by měl doplňovat informace, které nejsou zjevné z kódu.
- Dlouhý komentář často značí složitý kód – zjednodušit!
- **Špatný nebo neaktuální komentář je horší než žádný.**

---

## Jednotkové testy

Testy ověřují, že metody/třídy fungují podle očekávání. Provádí se automaticky a opakovaně.

---

## Framework JUnit

```java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class BinaryTest {
    @Test
    void binaryToIntTest() throws Exception {
        assertEquals(5, Binary.binaryToInt("101"));
    }
}
```

### Výjimky:
```java
assertThrows(InvalidDigitException.class,
    () -> Binary.binaryToInt("1102"));
```

### Pole:
```java
assertArrayEquals(new int[] {1, 2}, new int[] {1, 2});
```

---

## Komplexnější testy

```java
class CarTest {
    private Car car;

    @BeforeEach
    void setUp() {
        car = new Car("AAA 1234", "blue");
        car.accelarate(10);
    }

    @Test
    void accelerateTest() {
        car.accelarate(15);
        assertEquals(25, car.getSpeed());
    }
}
```

---

## Testování výstupu přes StringWriter

```java
StringWriter buf = new StringWriter();
writeEmployees(buf, new Employee[] {
    new Employee("Alice", 20, 1234.56),
    new Employee("Bob", 42, 7890.23)
});
assertEquals(""" 
Alice,20,1234.56
Bob,42,7890.23
""".trim(), buf.toString().trim());
```

---

## Shrnutí

- Komentáře zvyšují srozumitelnost a údržbu kódu.
- JavaDoc je základ pro automatickou dokumentaci.
- Jednotkové testy zajišťují spolehlivost a stabilitu aplikace.

---