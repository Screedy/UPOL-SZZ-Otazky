# Generické třídy a metody v Javě

## Motivace – problém pevných typů

Při práci se seznamy jsme často nuceni používat obecný typ `Object`, což s sebou nese:
- Nutnost přetypovávání při čtení hodnot
- Riziko vložení hodnoty nesprávného typu

Cílem generik je tyto problémy **odstranit pomocí typové bezpečnosti**, bez nutnosti psát opakovaný kód pro různé typy.

---

## Generická třída

Generická třída je **šablona**, která se přizpůsobí konkrétnímu typu při vytvoření objektu.

```java
public class MyList<T> {
    private T[] items;
    private int size;

    public MyList(int capacity) {
        items = (T[]) new Object[capacity]; // přetypování nutné kvůli JVM
        size = 0;
    }

    public void add(T item) {
        if (size == items.length) {
            T[] newArray = (T[]) new Object[items.length * 2];
            for (int i = 0; i < items.length; i++)
                newArray[i] = items[i];
            items = newArray;
        }
        items[size++] = item;
    }

    public T get(int index) {
        return items[index];
    }

    public int size() {
        return size;
    }
}
```

Použití:
```java
MyList<Light> lights = new MyList<>(10);
lights.add(new Light("red"));
```

---

## Upřesnění typových parametrů (`extends`)

Omezení na konkrétní typ nebo jeho potomky:
```java
public class Point<T extends Number> {
    private final T x, y;
    public double distance(Point<T> that) {
        double dx = this.x.doubleValue() - that.x.doubleValue();
        double dy = this.y.doubleValue() - that.y.doubleValue();
        return Math.sqrt(dx * dx + dy * dy);
    }
}
```

Použití:
```java
Point<Integer> p1 = new Point<>(1, 2);
Point<Double> p2 = new Point<>(3.5, 4.2);
```

---

## Generické metody

Metody mohou mít vlastní typový parametr:
```java
public static <T> boolean areEquals(T a, T b) {
    return a.equals(b);
}
```

Lze i omezit typ:
```java
public static <T extends Number> T min(T a, T b) {
    return a.doubleValue() < b.doubleValue() ? a : b;
}
```

---

## Wildcards – žolíky v generikách

Pro větší flexibilitu lze použít tzv. **žolíky** (`?`) v metodách:

```java
public static void printOut(MyList<?> list) {
    for (int i = 0; i < list.size(); i++)
        System.out.println(list.get(i));
}
```

### Omezení typu s `extends`:
```java
public static double average(MyList<? extends Number> list) {
    double sum = 0;
    for (int i = 0; i < list.size(); i++)
        sum += list.get(i).doubleValue();
    return sum / list.size();
}
```

### Omezení s `super`:
```java
MyList<? super Double> numbers;
```

Používá se např. při zápisu (vkládání hodnot), kdy typ může být i nadřazený.

---

## Shrnutí

- Generické třídy a metody umožňují psát **znovupoužitelný a typově bezpečný kód**.
- Pomáhají předejít chybám při přetypování a poskytují vyšší sémantickou jistotu.
- Wildcards (`?`) umožňují psát obecné metody bez znalosti přesného typu.
- Omezení `extends` a `super` určují, jaké typy mohou být použity.

---

# Kolekce v Javě – seznamy, slovníky a množiny

## Co jsou kolekce?

Kolekce jsou obecné datové struktury pro ukládání a práci se skupinou objektů.  
Jsou součástí balíčku `java.util` a poskytují bohaté API pro:
- vkládání, mazání a vyhledávání objektů
- práci s duplikáty nebo bez nich
- udržení nebo ignorování pořadí

Kolekce používají rozhraní (`List`, `Set`, `Map`) a jejich konkrétní implementace (`ArrayList`, `HashSet`, `HashMap`).

---

## Seznam (`List`)

Udržuje **pořadí vložených prvků** a umožňuje přístup pomocí indexu.

### Implementace:
- `ArrayList<T>` – založený na poli (rychlý přístup, pomalejší změny uprostřed)
- `LinkedList<T>` – spojový seznam (rychlé vkládání/mazání na krajích)

### Příklad:
```java
List<String> names = new ArrayList<>();
names.add("alice");
names.add("bozena");
names.add("cyril");
names.remove("bozena");
names.add(1, "benedikt");

names.get(2); // "cyril"
names.size(); // 4
names.indexOf("david");
names.contains("david");
```

### For-each:
```java
for (String name : names) {
    System.out.println(name);
}
```

### Neměnný seznam:
```java
List<Integer> numbers = List.of(1, 2, 3);
```

---

## Slovník (`Map`)

Slovník (mapa) uchovává dvojice **klíč – hodnota**.

### Rozhraní:
- `Map<K, V>` – základ
- `HashMap<K, V>` – ukládá páry do hash tabulky
- `TreeMap<K, V>` – binární vyhledávací strom (seřazení podle klíče)
- `LinkedHashMap<K, V>` – zachovává pořadí vkládání

### Příklad s `HashMap`:
```java
Map<String, Double> g = new HashMap<>();
g.put("methan", 16.04);
g.put("ethan", 30.07);
g.get("ethan");        // 30.07
g.containsKey("butan"); // true
g.remove("methan");
```

### Hashovací funkce:
- Každý objekt má `hashCode()`
- Klíč by měl být neměnný a mít dobře definované `equals()` a `hashCode()`

---

## `TreeMap` – seřazené klíče

Klíče musí být `Comparable` nebo musíme dodat `Comparator`.

```java
public class Car implements Comparable<Car> {
    public int compareTo(Car o) {
        return Integer.compare(this.speed, o.speed);
    }
}
```

### Alternativně:
```java
Map<String, Integer> m = new TreeMap<>(new StringLengthComparator());
```

Klíče jsou pak seřazeny (např. podle délky řetězce).

---

## Množina (`Set`)

Množina je kolekce bez duplicit.

### Rozhraní:
- `Set<T>` – základ
- `HashSet<T>` – rychlé, ale neuspořádané
- `TreeSet<T>` – seřazené prvky
- `LinkedHashSet<T>` – zachová pořadí vložení

### Příklad:
```java
Set<Integer> nums = new HashSet<>();
for (int i = 0; i < 10; i++)
    nums.add(i * 10);

for (int i : nums)
    System.out.print(i + " ");
```

### Neměnná množina:
```java
Set<String> s = Set.of("a", "b", "c");
```

---

## Operace nad množinami

- `addAll(s)` – sjednocení
- `retainAll(s)` – průnik
- `removeAll(s)` – rozdíl

---

## Shrnutí

| Kolekce | Rozhraní | Umožňuje duplikáty | Zachovává pořadí |
|---------|----------|---------------------|-------------------|
| List    | `List`   | Ano                | Ano               |
| Set     | `Set`    | Ne                 | Ne / podle typu   |
| Map     | `Map`    | Klíče: Ne, Hodnoty: Ano | podle typu |

- **`ArrayList`** – rychlé čtení
- **`LinkedList`** – rychlé mazání/přidání
- **`HashMap`/`HashSet`** – rychlé, neuspořádané
- **`TreeMap`/`TreeSet`** – seřazené (nutnost `Comparable` nebo `Comparator`)

---