# Strings in Python

A **string** (`str`) is a piece of text: a sequence of characters wrapped in quotes.

```python
print(type('hello world'))  # <class 'str'>

username = "supercoder"
password = 'supersecret'
```

Single `'...'` and double `"..."` quotes work the same way.

## Multi-line strings

Use triple quotes (`'''` or `"""`) to span several lines.

```python
long_string = '''
wow
o o
----
'''
print(long_string)
```

## Concatenation

Concatenation means adding strings together with `+`.

```python
first_name = "Raushan"
last_name = "Kumar"

full_name = first_name + " " + last_name
print(full_name)               # Raushan Kumar
print("hello " + "Raushan")    # hello Raushan
```

> You can only `+` a string with another string. `"age " + 5` raises a `TypeError`; use `str(5)`.

## Type conversion

```python
a = str(100)    # '100'  -> string
b = int(a)      # 100    -> integer
print(type(b))  # <class 'int'>
print(type(int(str(100))))  # <class 'int'>
```

## Escape sequences

A backslash `\` lets you put special characters inside a string.

| Sequence | Meaning      |
|----------|--------------|
| `\n`     | new line     |
| `\t`     | tab          |
| `\'`     | single quote |
| `\"`     | double quote |
| `\\`     | backslash    |

```python
weather = "\t It\'s \"kind of\" sunny \n  hope you have a good day!"
print(weather)
```

## Formatted strings

```python
name = "Johnny"
age = 55

# 1. Concatenation (clumsy, needs str())
print("hi " + name + ". you are " + str(age) + " years old")

# 2. f-string (recommended, Python 3.6+)
print(f"hi {name}. you are {age} years old")

# 3. .format() with empty placeholders (filled in order)
print("hi {}. you are {} years old".format("johnny", "55"))

# 4. .format() with index numbers
print("hi {1}. you are {0} years old".format(name, age))
# -> hi 55. you are Johnny years old   (index 1 = age, index 0 = name)

# 5. .format() with named placeholders
print("hi {new_name}. you are {age} years old".format(new_name="sally", age=100))
```

Mixing index placeholders with keyword arguments raises an error:

```python
# "hi {0}. you are {1} years old".format(new_name="sally", age=100)  # IndexError
```

## String indexes

Strings are stored in memory in order, and each character has an index starting at `0`. Negative indexes count from the end.

```python
selfish = 'me me me'
# index: 01234567
print(selfish[7])   # e
print(selfish[6])   # m
```

## Slicing

Syntax: `[start:stop:step]`. `start` is included, `stop` is excluded.

```python
step = "123456789"
#       012345678

print(step[0:8:2])  # 1357   -> step over two
print(step[1:])     # 23456789
print(step[:5])     # 12345
print(step[::1])    # 123456789
print(step[-1])     # 9      -> last character
print(step[::-1])   # 987654321 -> reversed
print(step[::-2])   # 97531  -> reversed, every second character
```

## Immutability

Strings are **immutable**: once created, their characters cannot be changed in place. You can reassign the variable to a new value, but you can't modify the existing string.

```python
selfish = "123238923"
selfish = 100         # OK: the name now points to a new value

s = "hello"
s[0] = "j"            # TypeError: 'str' object does not support item assignment

# Build a new string instead
s = "j" + s[1:]       # jello
```

## Quick summary

- `str` is text; use `'...'`, `"..."`, or `'''...'''` for multi-line.
- `+` concatenates; convert other types with `str()`.
- Use `\` escape sequences for special characters.
- Prefer f-strings for formatting.
- Slice with `[start:stop:step]`; `[::-1]` reverses.
- Strings are immutable.

