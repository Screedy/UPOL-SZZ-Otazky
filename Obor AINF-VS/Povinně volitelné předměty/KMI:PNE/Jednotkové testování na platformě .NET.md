# **0. Testování**

- Testování slouží k ověření, že software odpovídá specifikaci a chová se správně. Může být:
  - **manuální** nebo **automatizované**,
  - **white-box (bílá skříňka)** – tester zná vnitřní implementaci,
  - **black-box (černá skříňka)** – tester testuje pouze vstupy a výstupy.

- _Typy automatických testů_:
  - **Unit testy (jednotkové testy)**
    - Testují nejmenší funkční celky: metody, třídy. Jsou rychlé, izolované, spouštějí se stovkykrát za den.
  - **Integrační testy**
    - Ověřují provázanost komponent navzájem, spolupráci s OS, databází nebo jinými systémy. Pomalejší, nákladnější.
  - **UI testy**
    - Simulují chování uživatele v grafickém rozhraní.
  - **Performance / load testy**
    - Měří výkon a odezvu pod zátěží.

**CI/CD pipeline** — testy jsou **automaticky spouštěny** při každém _commit/push_ do repozitáře. Okamžitá zpětná vazba, zda změna nic nerozbila.

**Regresní testování** — Při objevení chyby v produkci: **nejdříve napíšeme test, který chybu reprodukuje**, pak opravíme kód. Test zůstane v projektu — chyba se nikdy nevrátí bez povšimnutí.

---

# 1. Unit testy

> [!success]
> Unit test ověřuje **nejmenší testovatelnou jednotku kódu** (typicky jednu metodu nebo třídu) **izolovaně** od zbytku systému – bez _databáze, sítě, souborového systému či jiných externích závislostí_. Ověřuje, že pro **daný vstup** metoda **vrátí očekávaný výstup.**

- _Jak vybrat vstupní data?_
  - **Mezní hodnoty** — `null`, prázdné pole `[]`, prázdný řetězec `""`, první a poslední prvek kolekce, nula, `int.MaxValue`.
  - **Neplatné hodnoty** — záporné číslo tam, kde je očekáváno kladné, záporný věk, neexistující ID.
  - **Smysluplné hodnoty** — typické vstupy odpovídající reálnému použití.

## 1.1 Testovací frameworky v .NET

- V .NET se nejčastěji používají tři frameworky:
  - **MSTest**
  - **NUnit**
  - **xUnit**

### 1.1.1 MSTest

- **MSTest** je **oficiální testovací framework společnosti Microsoft**. Je součástí ekosystému Visual Studia.
- Testovací třídy a metody jsou označeny pomocí **atributů (anotací)**.

> [!info]
> _Například_:
>
> - `[TestClass]` – označuje testovací třídu,
> - `[TestMethod]` – označuje testovací metodu.

- Každá metoda označená atributem `TestMethod` představuje **jeden nezávislý test**, který framework automaticky spustí.

#### 1.1.1.1 Ověřování výsledků

- _Výsledek testu se kontroluje_ pomocí statické třídy **Assert**.
- Nejpoužívanější metody:
  - `Assert.AreEqual()` – očekávaná a skutečná hodnota jsou stejné,
  - `Assert.AreNotEqual()`
  - `Assert.IsTrue()`
  - `Assert.IsFalse()`
  - `Assert.IsNull()`
  - `Assert.IsNotNull()`
  - `Assert.ThrowsException<>()` – ověření vyhození výjimky.

> [!danger]
> Pokud podmínka není splněna, test skončí jako **Failed**.

#### 1.1.1.2 Životní cyklus testů

- MSTest umožňuje _spouštět kód před a po testech_.
- Nejdůležitější atributy:
  - `[TestInitialize]` – spustí se před každým testem.
  - `[TestCleanup]` – spustí se po každém testu.
  - `[ClassInitialize]` – jednou před všemi testy dané třídy.
  - `[ClassCleanup]` – jednou po dokončení všech testů.
- Používají se například pro:
  - **vytvoření testovacích dat**,
  - _otevření databázového spojení_,
  - **úklid po testech**.

#### 1.1.1.3 Spouštění testů

- Testy se standardně spouštějí **v abecedním pořadí**,
- Framework podporuje **paralelní spouštění testů**.

---

### 1.1.2 NUnit

- **NUnit** je _velmi podobný MSTestu_, ale nabízí více možností konfigurace a bohatší sadu atributů.

> [!info]
> **Původě port JUnit**, od verze 3 kompletně přepsán.

#### 1.1.2.1 Nejčastější atributy

- `[TestFixture]` – testovací třída.
- `[Test]` – testovací metoda.
- `[SetUp]` – před každým testem.
- `[TearDown]` – po každém testu.
- `[OneTimeSetUp]` – jednou před všemi testy.
- `[OneTimeTearDown]` – jednou po všech testech.

#### 1.1.2.2 Assert

- Stejně jako MSTest používá třídu **Assert**.

---

### 1.1.3 xUnit

- **xUnit** je _nejmodernější z těchto frameworků_ a dnes patří mezi **nejpoužívanější** _při vývoji nových .NET aplikací_.

#### 1.1.3.1 Označení testů

- xUnit **nepoužívá atribut pro označení testovací třídy**. _Každá veřejná třída obsahující testovací metody_ je **automaticky** _považována za testovací třídu_.
- Místo `[TestMethod]` používá:
  - `[Fact]` – běžný test.
  - `[Theory]` – parametrizovaný test.

#### 1.1.3.2 Inicializace

- Na rozdíl od MSTestu nebo NUnit nemá atributy typu `SetUp`.
- Místo nich používá:
  - **konstruktor třídy** – spouští se před každým testem,
  - rozhraní `IDisposable` – provede úklid po testu.

---

### 1.1.4 Srovnání syntaxe na stejném testu

```csharp
// MSTest
[TestClass]
public class CalculatorTests
{
    [TestMethod]
    public void Add_TwoNumbers_ReturnsSum()
    {
        var result = Calculator.Add(2, 3);
        Assert.AreEqual(5, result);
    }
}

// NUnit
[TestFixture]
public class CalculatorTests
{
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
        var result = Calculator.Add(2, 3);
        Assert.That(result, Is.EqualTo(5));
    }
}

// xUnit
public class CalculatorTests
{
    [Fact]
    public void Add_TwoNumbers_ReturnsSum()
    {
        var result = Calculator.Add(2, 3);
        Assert.Equal(5, result);
    }
}
```

## 1.2 Vzor AAA (Arrange, Act, Assert)

> [!warning]
> _Každý unit test_ by měl být strukturován do **tří jasně oddělených sekcí**:
>
> - **Arrange** — vytvoříme objekty, nastavíme mock objekty, připravíme data.
> - **Act** — zavoláme přesně jednu testovanou operaci.
> - **Assert** — ověříme výsledek pomocí asercí.
>   - Každý test by měl mít ideálně jednu logickou asserci (může to být i více řádků, ale ověřují jednu věc).

```
[Fact]
public void Divide_ByZero_ThrowsException()
{
    // Arrange – příprava dat a závislostí
    var calc = new Calculator();

    // Act – zavolání testované operace
    Action act = () => calc.Divide(10, 0);

    // Assert – ověření výsledku
    Assert.Throws<DivideByZeroException>(act);
}
```

> [!info]
> Pojmenování testovacích metod se doporučuje ve tvaru `Metoda_Scénář_OčekávanýVýsledek`.

## 1.3 Parametrizované testy

- Spouštění stejného testu s různými vstupy bez duplikace kódu:

```
// xUnit
[Theory]
[InlineData(2, 3, 5)]
[InlineData(-1, 1, 0)]
[InlineData(0, 0, 0)]
public void Add_VariousInputs_ReturnsSum(int a, int b, int expected)
{
    Assert.Equal(expected, Calculator.Add(a, b));
}

// NUnit
[TestCase(2, 3, 5)]
[TestCase(-1, 1, 0)]
public void Add_VariousInputs_ReturnsSum(int a, int b, int expected)
{
    Assert.That(Calculator.Add(a, b), Is.EqualTo(expected));
}
```

## 1.4 Test lifecycle

| Účel | MSTest | NUnit | xUnit |
| --- | --- | --- | --- |
| Před každým testem | `[TestInitialize]` | `[SetUp]` | konstruktor třídy |
| Po každém testu | `[TestCleanup]` | `[TearDown]` | `IDisposable.Dispose()` |
| Jednou před všemi testy třídy | `[ClassInitialize]` | `[OneTimeSetUp]` | `IClassFixture<T>` |
| Jednou po všech testech třídy | `[ClassCleanup]` | `[OneTimeTearDown]` | `IClassFixture<T>` |

> [!info]
> Zásadní rozdíl u xUnit: **pro každý test se vytváří nová instance testovací třídy** (test isolation by default) – proto se setup dělá v konstruktoru, ne ve zvláštní metodě.

## 1.5 Odstínění závislostí (Mock objekty)

> [!danger]
> **Problém:** Unit test testuje jednu třídu, ale ta závisí na databázi, HTTP službě nebo souboru. Tyto závislosti jsou pomalé, nestabilní a nelze je v testu ovládat.
>
> **Řešení:** Nahradíme závislost _falešnou_ implementací, která se chová předvídatelně.

| Název | Co dělá | Kdy použít |
| --- | --- | --- |
| **Stub** | Vrací **pevně nastavené hodnoty**, nereaguje na volání | Potřebuji ovlivnit, co závislost vrátí |
| **Mock** | Stub + **ověřuje**, zda byly metody **volány správně** | Chci zkontrolovat chování (nejen výstup) |
| **Fake** | Funkční lehká náhrada (in-memory databáze) | Rychlé integrační testy |
| **Spy** | **Reálná implementace**, která zaznamenává volání | Zřídka, spíše pro legacy |

### 1.5.1 Knihovna `Moq`

> [!info]
> Nejpoužívanější mockovací knihovna v .NET ekosystému.
>
> Umožňuje **generovat testovací dvojníky** pro rozhraní/virtuální metody **bez psaní vlastní implementace**.

```csharp
public interface IRepository
{
    Customer GetById(int id);
}

[Fact]
public void GetCustomerName_ValidId_ReturnsName()
{
    // Arrange
    var mockRepo = new Mock<IRepository>();
    mockRepo.Setup(r => r.GetById(1))
            .Returns(new Customer { Id = 1, Name = "Petr" });

    var service = new CustomerService(mockRepo.Object);

    // Act
    var name = service.GetCustomerName(1);

    // Assert
    Assert.Equal("Petr", name);
    mockRepo.Verify(r => r.GetById(1), Times.Once);
}
```

- `Setup` – definuje chování mocku (co má vrátit při daném volání).
- `.Object` – vrací vygenerovanou instanci rozhraní, kterou lze _injectnout_ do testované třídy.
- `Verify` – ověří, že daná metoda byla (ne)zavolána, případně kolikrát (`Times.Once`, `Times.Never`, `Times.Exactly(n)`).

---

# 2. Code coverage

> [!success]
> Metrika udávající, kolik procent kódu (řádků, větví) je pokryto testy.

- V .NET se měří typicky přes **Coverlet** a vizualizuje přes **ReportGenerator** nebo přímo ve Visual Studiu.

> [!note]
> **Zlaté pravidlo:** 100 % coverage neznamená, že kód je správný.  
> Znamená pouze, že **každý řádek byl někdy vykonán** — ale nemuselo být ověřeno, zda se chová správně. Coverage je ukazatel, ne cíl.

**Druhy pokrytí:**

- **Line coverage** — kolik řádků bylo vykonáno.
- **Branch coverage** — kolik větví (`if/else`, `switch`) bylo otestováno.
- **Path coverage** — kolik kombinací cest bylo procházeno (exponenciálně složité).

---

# 3. Test-Driven Development

> [!success]
> **TDD** je technika vývoje softwaru, kdy jsou testy psány **_před_ implementací**. Vývoj probíhá v krátkých cyklech: **Red → Green → Refactor**.

- **Red** – napiš test, který popisuje požadované chování; spustí se a selže (funkcionalita ještě neexistuje).
- **Green** – napiš nejjednodušší možnou implementaci, aby test prošel.
- **Refactor** – vyčisti kód při zachování zeleného testu.

## 3.1 Výhody TDD

- Kód je od začátku navrhován s ohledem na testovatelnost.
- Testy slouží jako _živá dokumentace_.
- Refactoring je _bezpečný_.
- Vede k menším, lépe ohraničeným metodám.

## 3.2 Nevýhody / realistický pohled

- Zpočátku pomalejší psaní kódu.
- Špatně se aplikuje tam, kde nejsou jasné specifikace.
- Autorský bias nevymizí — stále píšeš testy sám.