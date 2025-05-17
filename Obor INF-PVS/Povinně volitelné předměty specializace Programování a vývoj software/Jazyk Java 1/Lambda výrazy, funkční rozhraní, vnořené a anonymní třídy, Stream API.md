# Vnořené třídy a lambda výrazy v Javě

## Vnořené třídy

Vnořená třída je třída deklarovaná **uvnitř jiné třídy**. Používá se pro lepší zapouzdření a čitelnost, pokud daná třída slouží jen pro účely nadřazené třídy.

Typické využití: interní implementace iterátoru, pomocná struktura, definice stavů apod.

---

## Statické vnořené třídy (`static`)

- Nemají přístup k **nestatickým** členům vnější třídy.
- Chovají se jako běžné třídy – jen jsou definovány uvnitř jiné třídy.

Příklad:
```java
public class MyList<T> {
    private T[] items;
    private int size;

    public static final class MyIterator<E> implements Iterator<E> {
        private final MyList<E> list;
        private int index;

        public MyIterator(MyList<E> list) {
            this.list = list;
            this.index = 0;
        }

        public boolean hasNext() {
            return (index < list.size);
        }

        public E next() {
            return list.get(index++);
        }
    }

    public Iterator<T> iterator() {
        return new MyIterator<>(this);
    }
}
```

---

## Nestatické vnořené třídy

- Mají přístup ke všem členům nadřazené třídy (i privátním).
- Využívají implicitní odkaz na instanci vnější třídy.

Příklad:
```java
private final class MyIterator implements Iterator<T> {
    private int index = 0;

    public boolean hasNext() {
        return index < size;
    }

    public T next() {
        return items[index++];
    }
}
```

---

## Anonymní třídy

Používají se, pokud potřebujeme **jednorázově** implementovat třídu nebo rozhraní.

```java
Iterator<T> iterator = new Iterator<>() {
    private int index = 0;

    public boolean hasNext() {
        return index < size;
    }

    public T next() {
        return items[index++];
    }
};
```

- Deklarace a vytvoření instance probíhá zároveň.
- Má přístup k finálním/efektivně finálním proměnným z okolí.

---

## Lambda výrazy

Lambda výrazy jsou **zkrácený zápis anonymních funkcí**. Používají se tam, kde se očekává funkcionální rozhraní (tj. rozhraní s jednou metodou).

### Zápis:
```java
(arg1, arg2) -> výraz
x -> x * 2
(x, y) -> x + y
```

### Blokový zápis:
```java
(x, y) -> {
    System.out.println(x);
    return x + y;
};
```

---

## Použití s funkcionálními rozhraními

```java
Action<Integer> action = number -> System.out.println(number);
action.perform(20);
```

Nebo:
```java
numbers.forEach((Integer value) -> System.out.println(value));
```

---

## Reference na metody (`::`)

Zkrácený zápis místo lambda výrazu:
```java
System.out::println      // místo (x) -> System.out.println(x)
Integer::toBinaryString  // místo (n) -> Integer.toBinaryString(n)
```

---

## Shrnutí

- **Vnořené třídy** pomáhají zapouzdřit pomocné konstrukce do souvisejících tříd.
- **Anonymní třídy** slouží k jednorázové implementaci.
- **Lambda výrazy** a **method reference** umožňují zapisovat funkce elegantně a úsporně.
- V kombinaci s generikami (`filter`, `map`, `forEach`) umožňují elegantní zpracování kolekcí.

---