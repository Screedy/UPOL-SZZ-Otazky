## Základní operace

### Sčítání a odčítání:

```Python
# Sčítání
a = 0b1101
b = 0b1011
c = a + b
print(bin(c))  # Vypíše: 0b11000

# Odčítání
d = a - b
print(bin(d))  # Vypíše: 0b1
```
### Binární posun:

```Python
# Posun doprava (dělení 2)
x = 0b1101
x_right_shifted = x >> 1
print(bin(x_right_shifted))  # Vypíše: 0b110

# Posun doleva (násobení 2)
y = 0b1101
y_left_shifted = y << 1
print(bin(y_left_shifted))  # Vypíše: 0b11010
```

### Bitové operace:

```Python
# Bitový AND
a = 0b1101
b = 0b1011
c = a & b
print(bin(c))  # Vypíše: 0b1001

# Bitový OR
d = a | b
print(bin(d))  # Vypíše: 0b1111

# Bitový XOR
e = a ^ b
print(bin(e))  # Vypíše: 0b110

# Bitová negace
f = ~a
print(bin(f))  # Vypíše: -0b1110 (jelikož výsledek závisí na délce bitového slova)
```
