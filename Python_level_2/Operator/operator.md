# Operators in Python: Ternary, Short Circuiting and Logical/Comparison

## 1. Ternary operator (conditional expression)

A one-line `if / else` that **produces a value**.

```
value_if_true if condition else value_if_false
```

```python
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)   # not allowed to message
```

It is the same as:

```python
if is_friend:
    can_message = "message allowed"
else:
    can_message = "not allowed to message"
```

Note the order: the **result comes first**, then the condition.

### Chained ternary (use sparingly)

```python
age = 20
group = "minor" if age < 18 else "teen" if age < 21 else "adult"
print(group)   # teen
```

If it gets hard to read, use a normal `if` / `elif` / `else`.

### Where to use it

- Choosing a label or message: `"Online" if user.is_active else "Offline"`.
- Default values: `discount = 10 if is_member else 0`.
- Inline text: `print(f"{n} item{'s' if n != 1 else ''}")`.

## 2. Short circuiting

Python evaluates `and` / `or` **left to right** and **stops as soon as the result is known**. The remaining part is never evaluated.

| Expression | Stops when |
|------------|------------|
| `a and b` | `a` is falsy (the result must be falsy) |
| `a or b` | `a` is truthy (the result must be truthy) |

```python
is_Friends = False
is_User = True

if is_Friends and is_User:        # is_Friends is False, so is_User isn't needed
    print("Best friends")

if is_Friends or is_User:         # is_Friends is False, so is_User decides: True
    print("Best friends forever")
```

You can see it with a function that prints when called:

```python
def check(n):
    print("called", n)
    return n

print(check(0) and check(1))   # called 0   -> 0        (second call skipped)
print(check(1) or check(2))    # called 1   -> 1        (second call skipped)
```

Both `and` and `or` return **one of their operands**, not always `True`/`False` (see the truthy/falsy notes).

### Where to use it

**Guard against errors:** put the safe check first.

```python
user = None

if user and user["name"] == "Alice":   # user["name"] never runs when user is None
    print("Hi Alice")
```

**Default values:**

```python
name = ""
print(name or "Guest")   # Guest
```

**Avoid expensive work:** put the cheap check first.

```python
if is_logged_in and has_permission(user):   # skip the slow call if not logged in
    ...
```

## 3. Comparison operators

They compare two values and return a boolean.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal | `4 == 5` | `False` |
| `!=` | not equal | `0 != 0` | `False` |
| `>` | greater than | `1 > 2` | `False` |
| `<` | less than | `1 < 2` | `True` |
| `>=` | greater or equal | `1 >= 0` | `True` |
| `<=` | less or equal | `1 <= 0` | `False` |

```python
print(4 == 5)               # False
print("hello" == "hello")   # True
print(1 > 2)                # False
print(1 >= 0)               # True
print(1 <= 0)               # False
print(0 <= 0)               # True
print(0 != 0)               # False
```

### `=` vs `==`

`=` assigns; `==` compares. Using `=` in a comparison is an error.

```python
# print(4 = 5)   # SyntaxError: a literal can't be assigned to, so it isn't an expression
```

### Comparing strings: Unicode values, not alphabet position

Python compares characters by their Unicode code point (`ord()`).

```python
print(ord('a'), ord('b'), ord('A'))   # 97 98 65

print('a' > 'b')   # False   (97 > 98 is False)
print('a' > 'A')   # True    (97 > 65): lowercase is greater than uppercase
```

Strings are compared character by character from the left:

```python
print('apple' < 'apricot')   # True   ('p' < 'r' at index 2)
```

For case-insensitive comparison, use `.lower()`:

```python
print("Apple".lower() == "apple".lower())   # True
```

### Chained comparisons

```python
age = 20
print(18 <= age < 65)       # True   same as 18 <= age and age < 65

print(1 < 2 > 3 < 4)        # False
# means: (1 < 2) and (2 > 3) and (3 < 4)  ->  True and False and True
```

### `==` vs `is`

- `==` compares **values**.
- `is` compares **identity** (the same object in memory). Use it for `None`.

```python
print([1] == [1])    # True
print([1] is [1])    # False  (two different lists)

x = None
print(x is None)     # True
```

### Float warning

```python
print(0.1 + 0.2 == 0.3)               # False (floating point rounding)
print(abs(0.1 + 0.2 - 0.3) < 1e-9)    # True  (compare with a tolerance)
```

## 4. Logical operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | both must be truthy | `True and False` -> `False` |
| `or` | at least one truthy | `True or False` -> `True` |
| `not` | reverses the result | `not True` -> `False` |

```python
print(not (True))    # False
print(not 0)         # True
print(not [])        # True
```

`not` returns the **opposite** of the given value's truthiness.

## 5. Real-life use cases

### Login check

```python
username = "johnny"
password = "123"
is_active = True

if username == "johnny" and password == "123" and is_active:
    print("Login successful")
else:
    print("Invalid login")
```

### Age and price rules

```python
age = 70
ticket = "free" if age < 5 or age >= 65 else "paid"
print(ticket)   # free
```

### Range validation

```python
score = 85
if 0 <= score <= 100:
    print("valid score")
```

### Permission check with a safe default

```python
settings = {}
theme = settings.get("theme") or "light"
print(theme)   # light
```

## Summary

- Ternary: `a if condition else b` gives a value in one line.
- `and` / `or` short circuit: they stop once the result is known and return an operand.
- Put the safe or cheap check first when using short circuiting.
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`; they return booleans and can be chained.
- Strings compare by Unicode code point: `'a' > 'A'` is `True`.
- `=` assigns, `==` compares, `is` checks identity (use for `None`).
- Don't compare floats with `==`.
