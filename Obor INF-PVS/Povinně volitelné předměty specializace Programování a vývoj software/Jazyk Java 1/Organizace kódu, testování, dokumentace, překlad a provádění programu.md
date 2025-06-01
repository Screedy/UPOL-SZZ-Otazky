# Streamy v Javě – práce s daty, transformace, terminální operace a Optional

## Co jsou streamy

Streamy jsou deklarativní rozhraní pro zpracování kolekcí. Představují **posloupnost hodnot**, kterou můžeme různě filtrovat, transformovat a agregovat.

### Vlastnosti streamů:
- Pracují deklarativně – říkáme **co**, ne **jak**
- Operace jsou **líné** – neprovedou se, dokud nejsou potřeba
- **Není změněn** původní obsah kolekce
- Podporují **nekonečné** a **paralelní** zpracování

---

## Vytvoření streamu

```java
Stream<String> stream = Stream.of("alfa", "beta", "gama");

List<String> words = List.of("alfa", "beta", "gama", "delta");
Stream<String> stream2 = words.stream();

Stream<Integer> oddNumbers = Stream.iterate(1, n -> n + 2); // nekonečný stream
```

Výpis hodnot:
```java
stream.forEach(System.out::println);
```

> Stream lze projít pouze jednou – pro opakované použití je nutné vytvořit nový.

---

## Transformace streamu

Nejčastější operace:

| Metoda        | Význam                                       |
|---------------|-----------------------------------------------|
| `filter()`    | výběr prvků podle podmínky (`Predicate<T>`) |
| `map()`       | transformace hodnot                          |
| `skip(n)`     | přeskočí prvních `n` prvků                   |
| `limit(n)`    | omezí na `n` prvků                           |
| `sorted()`    | seřazení (vyžaduje `Comparable`)             |
| `distinct()`  | odstranění duplicit                          |

Příklad:
```java
stream.filter(s -> s.contains("e"))
      .map(String::toUpperCase)
      .limit(3)
      .sorted()
      .forEach(System.out::println);
```

---

## Koncové operace

### Převod na seznam/pole
```java
List<String> list = stream.toList();
String[] arr = stream.toArray(String[]::new);
```

### Obecné sběry pomocí `collect`
```java
Set<String> set = stream.collect(Collectors.toSet());
String joined = stream.collect(Collectors.joining(", "));
Map<Integer, List<String>> grouped = stream.collect(Collectors.groupingBy(String::length));
long count = stream.collect(Collectors.counting());
Double avg = stream.collect(Collectors.averagingInt(String::length));
```

---

## Testování podmínek

```java
stream.anyMatch(s -> s.contains("x"));  // existuje prvek?
stream.allMatch(s -> s.length() > 1);   // všechny prvky?
stream.noneMatch(s -> s.equals(""));    // žádný prvek?
```

---

## Vyhledávání

```java
Optional<String> value = stream.findAny();     // libovolný prvek
Optional<String> first = stream.findFirst();   // první prvek
```

---

## Optional

Objekt `Optional<T>`:
- může/nebo nemusí obsahovat hodnotu
- zabraňuje `NullPointerException`

### Práce s Optional:
```java
if (value.isPresent()) System.out.println(value.get());
value.ifPresent(System.out::println);
System.out.println(value.orElse("N/A"));
```

### Vytvoření Optional:
```java
Optional.of("text")
Optional.empty()
```

---

## Streamy čísel

Pro primitivní typy: `IntStream`, `LongStream`, `DoubleStream`.

```java
IntStream.range(0, 10).sum();
IntStream.range(0, 10).map(x -> x * 2).average();
```

### Převod:
```java
stream.mapToInt(String::length).average();
IntStream.of(1, 2, 3).mapToObj(Integer::toHexString).collect(Collectors.joining(", "));
```

---

## Paralelní streamy

Paralelní zpracování pomocí `parallel()`:

```java
stream.parallel()
      .filter(s -> s.contains("e"))
      .map(String::toUpperCase)
      .toList();
```

> Výhodné u větších datových objemů nebo náročných operací.

---

## Shrnutí

- Streamy přinášejí **deklarativní a efektivní** způsob práce s daty.
- Pracují s libovolnými kolekcemi a lze je snadno transformovat a agregovat.
- Operace jsou **líné** a spustí se až při koncové operaci (`forEach`, `collect`, `find...`).
- Třída `Optional<T>` umožňuje bezpečně zachytit „chybějící“ hodnoty.
- Pro číselné operace slouží `IntStream` apod.
- Streamy lze zpracovávat **paralelně**, pokud je to výhodné.

---

## Organizace kódu v Javě

Java programy se skládají z tříd, každá ve vlastním souboru s příponou `.java`. Třídy jsou členěny do balíčků (packages), které odpovídají adresářové struktuře. Balíček se definuje direktivou `package` na začátku souboru.

Hlavní třída má statickou metodu `main`, která slouží jako vstupní bod programu.

## Testování

Testování se provádí pomocí knihovny JUnit. Testy se zapisují jako metody označené anotací `@Test` a ověřují očekávané chování pomocí asercí.

Testy se zpravidla organizují do zrcadlové struktury vůči produkčnímu kódu a spouštějí se pomocí nástrojů jako Maven nebo Gradle.

## Dokumentace

Java používá komentáře ve formátu JavaDoc, které jsou umístěné nad třídami a metodami. Obsahují popis funkce, parametrů a návratových hodnot.

Z komentářů lze vygenerovat HTML dokumentaci.

Příklad komentáře:

```java
/**
 * Vrátí součet dvou čísel.
 * @param a první číslo
 * @param b druhé číslo
 * @return součet
 */
```

## Překlad a provádění programu

Program se nejprve překládá pomocí kompilátoru `javac`, který ze zdrojového kódu vytvoří soubor `.class` s bajtkódem.

Při spouštění programů se bajtkód vykonává na virtuálním stroji JVM, který jej překládá do strojového kódu pomocí tzv. just-in-time kompilace.

Tento přístup umožňuje nezávislost kódu na platformě a jednotné spouštění na různých operačních systémech.
