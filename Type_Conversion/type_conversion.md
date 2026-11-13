# Type Conversion in Python

**Type conversion** (type casting) means changing a value from one data type to another, for example a string to an integer.

## Check a type with `type()`

```python
name = "Raushan Kumar"
age = 30

print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
```

## `input()` always returns a string

Whatever the user types, `input()` gives back a `str`, even if it looks like a number.

```python
birth_year = input('what year were you born?')   # user types 1995
print(type(birth_year))   # <class 'str'>
print(birth_year)         # 1995
```

Because of this, calculations fail unless you convert first:

```python
# 2026 - birth_year   -> TypeError: unsupported operand type(s) for -: 'int' and 'str'

age = 2026 - int(birth_year)     # convert to int first
print(f'your age is : {age}')    # your age is : 31
```

## Common conversion functions

| Function | Converts to | Example | Result |
|----------|-------------|---------|--------|
| `int()`   | integer | `int("100")` | `100` |
| `float()` | decimal | `float("3.5")` | `3.5` |
| `str()`   | string  | `str(10)` | `'10'` |
| `bool()`  | boolean | `bool("")` | `False` |
| `list()`  | list    | `list("abc")` | `['a', 'b', 'c']` |

```python
print(int("100"))    # 100
print(float("3.5"))  # 3.5
print(str(10))       # '10'
print(bool(""))      # False
print(list("abc"))   # ['a', 'b', 'c']
```

### Things to remember

- `int()` on a float **truncates** (does not round): `int(3.9)` is `3`.
- `int(True)` is `1` and `int(False)` is `0`.
- `bool()` is `False` for `0`, `""`, `[]`, `None`; otherwise `True`.

## Conversion errors

A value must look like the target type, otherwise Python raises a `ValueError`.

```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError: use float("3.5") first, then int()
```

Handle bad input safely with `try`/`except`:

```python
birth_year = input('what year were you born?')

try:
    age = 2026 - int(birth_year)
    print(f'your age is : {age}')
except ValueError:
    print("Please enter a valid year, e.g. 1995")
```

## Implicit vs explicit conversion

- **Explicit:** you convert it yourself, e.g. `int("5")`.
- **Implicit:** Python does it automatically in safe cases, e.g. `1 + 2.5` gives `3.5` (int becomes float).
- Python will **not** mix strings and numbers: `"5" + 5` raises a `TypeError`. Use `"5" + str(5)` or `int("5") + 5`.

## Summary

- `type()` shows the type of a value.
- `input()` returns a string, so convert it with `int()` or `float()` for maths.
- Use `int()`, `float()`, `str()`, `bool()` to convert explicitly.
- Invalid conversions raise `ValueError`; wrap them in `try`/`except`.
