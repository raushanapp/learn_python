# Truthy and Falsy in Python

In a condition (`if`, `while`, `and`, `or`, `not`), Python doesn't need an actual `True` or `False`. Every value can be treated as a boolean:

- **Falsy:** the value acts like `False`.
- **Truthy:** the value acts like `True`.

Rule of thumb: **empty or zero means falsy; everything else is truthy.**

## Falsy values

| Value | Description |
|-------|-------------|
| `False` | the boolean |
| `None` | no value |
| `0`, `0.0`, `0j` | numeric zero |
| `Decimal(0)`, `Fraction(0, 1)` | zero of other number types |
| `''` | empty string |
| `[]` | empty list |
| `{}` | empty dictionary |
| `()` | empty tuple |
| `set()` | empty set |
| `b''`, `bytearray(b'')` | empty bytes |
| `range(0)` | empty range |

Also falsy: an object whose `__bool__()` returns `False`, or (when `__bool__` isn't defined) whose `__len__()` returns `0`.

**Everything else is truthy**: non-zero numbers (including negatives), non-empty strings or collections, and most objects.

## Checking with `bool()`

`bool(value)` shows how Python sees a value.

```python
print(bool("hello"))   # True
print(bool(5))         # True

print(bool(''))        # False
print(bool(0))         # False
print(bool([]))        # False
```

### Surprising truthy values

```python
print(bool("0"))       # True   non-empty string
print(bool("False"))   # True   non-empty string
print(bool(" "))       # True   a space is a character
print(bool([0]))       # True   list is not empty
print(bool(-1))        # True   non-zero
print(bool(float("nan")))  # True
```

## Using it in conditions

```python
is_old = bool("hello")   # True
is_licenced = bool(5)    # True

if is_old and is_licenced:
    print("You are old enough to drive and you have a licence!")
else:
    print('you are not of age!')
```

You can skip `bool()` and test the value directly:

```python
password = "123"
username = "johnny"

if password and username:
    print("both fields are filled in")
else:
    print("Wrong password and username!")
```

Careful: this only checks that **both are non-empty**. It does not check that the password is **correct**. Compare values with `==` for that.

```python
if username == "johnny" and password == "123":
    print("logged in")
```

## Pythonic style: avoid `len()` and `== True`

```python
items = []

# Verbose
if len(items) > 0:
    print("has items")

# Pythonic
if items:
    print("has items")
else:
    print("cart is empty")      # runs

# Avoid
if is_old == True:   # redundant
    pass
if is_old:           # better
    pass
```

## `and` / `or` return a value, not just `True`/`False`

- `a or b` returns `a` if it is truthy, otherwise `b`.
- `a and b` returns `a` if it is falsy, otherwise `b`.

```python
print('' or 'guest')       # guest   (first is falsy, so use second)
print('Raushan' or 'guest')   # Raushan
print(0 and 5)             # 0
print(3 and 5)             # 5
print(None or [] or 'x')   # x       (first truthy value)
```

## `None` vs `0` vs empty: be careful

All of them are falsy, but they mean different things. When `0` or `''` is a valid value, test for `None` explicitly.

```python
score = 0

if not score:
    print("no score")           # runs, but 0 may be a real score!

if score is None:
    print("not played yet")     # correct check for "no value"
```

## Real-life use cases

### 1. Validating form input (signup, login)

```python
username = input("Username: ").strip()   # strip() removes spaces

if not username:
    print("Username is required")
else:
    print(f"Welcome, {username}")
```

### 2. Shopping cart / empty results

```python
cart = []

if cart:
    print("Proceed to checkout")
else:
    print("Your cart is empty")
```

Same for search: `if results:` show them, otherwise show "No results found".

### 3. Default values

```python
nickname = ""
display_name = nickname or "Guest"
print(display_name)   # Guest

config = {}
port = config.get("port") or 8080
print(port)   # 8080
```

### 4. Checking if a value was provided (API / optional data)

```python
user = {"name": "Alice", "bio": ""}

if user.get("bio"):
    print(user["bio"])
else:
    print("No bio yet")
```

### 5. Loops that run while data remains

```python
queue = ["task1", "task2"]

while queue:                 # stops when the list is empty
    print("doing", queue.pop(0))
```

### 6. Game logic

```python
weapons = None

if weapons:
    print("attack!")
else:
    print("you have no weapon")
```

## `==` vs `is`

Both give a boolean, but they ask different questions.

| Operator | Question | Compares |
|----------|----------|----------|
| `==` | Are the **values** equal? | value |
| `is` | Are they the **same object** in memory? | identity (`id()`) |

### `==` : equality of value

```python
print(True == 1)      # True
print('' == 1)        # False
print('1' == 1)       # False
print([] == 1)        # False
print(10 == 10.0)     # True
print([] == [])       # True
```

Why each result:

- `True == 1` is `True` because `bool` is a subclass of `int`: `True` **is** the number `1` and `False` is `0`. (It is not `bool(1)` conversion.)
- `'' == 1` and `'1' == 1` are `False`: Python does **not** convert a string to a number. Different types, so not equal (`'1'` is text, `1` is a number).
- `[] == 1` is `False`: a list and a number are never equal. Being falsy doesn't matter; `==` doesn't use truthiness.
- `10 == 10.0` is `True`: numbers are compared by numeric value.
- `[] == []` is `True`: two lists with the same contents are equal.

Note: truthiness is **not** equality.

```python
print(bool([]) == False)   # True   bool([]) is False
print([] == False)         # False  a list is not equal to False
print(0 == False)          # True   0 equals False
print('' == False)         # False
```

### `is` : same object in memory

```python
print(True is 1)      # False
print(True is True)   # True
print('' is 1)        # False
print('1' is 1)       # False
print([] is 1)        # False
print(10 is 10.0)     # False
print([] is [])       # False
```

Why:

- `True is True` is `True`: `True` is a single object (a singleton). `None` is too.
- `True is 1` is `False`: they are equal in value but are **different objects** (a `bool` and an `int`).
- `10 is 10.0` is `False`: an `int` and a `float` are different objects. (No conversion happens; they are just different.)
- `[] is []` is `False`: every `[]` you write creates a **new list** in memory, so two lists are always different objects even with the same contents. Lists, dicts and sets are like this.

```python
a = [1, 2]
b = a          # b points to the same list
c = [1, 2]     # a new list with the same contents

print(a is b)    # True
print(a is c)    # False
print(a == c)    # True
```

Python warns about `True is 1` and `'1' is 1` with `SyntaxWarning: "is" with a literal`. Don't use `is` with literals.

### When to use which

| Use | For |
|-----|-----|
| `==` | comparing values: numbers, strings, lists, dicts |
| `is` / `is not` | `None`, `True`, `False` singletons |

```python
x = None
if x is None:        # recommended
    print("no value")

if x == None:        # works but not recommended (a class can override ==)
    pass

if x is not None:
    print("has a value")
```

Never use `is` to compare numbers or strings; the result can depend on how Python stores them.

## Summary

- Falsy: `None`, `False`, zero, and empty sequences/collections (`''`, `[]`, `{}`, `()`, `set()`, `range(0)`).
- Everything else is truthy, including `"0"`, `"False"` and `" "`.
- `bool(value)` shows how Python treats a value.
- Write `if items:` instead of `if len(items) > 0:`.
- `or` is handy for defaults; `and`/`or` return one of their operands.
- Use `is None` when `0` or `''` are valid values.
- A truthy check tests presence, not correctness.
- `==` compares values; `is` compares memory identity.
- `True == 1` is `True` (`bool` is a kind of `int`), but `True is 1` is `False`.
- `[] == []` is `True`, `[] is []` is `False`.
- Use `==` for values and `is` only for `None`, `True` and `False`.
