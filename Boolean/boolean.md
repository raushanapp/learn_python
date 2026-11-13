# Booleans in Python

A **boolean** (`bool`) has only two possible values: `True` and `False`. Both are written with a capital first letter.

```python
name = "Raushan"
is_cool = False

is_cool = True          # variables can be reassigned
print(type(is_cool))    # <class 'bool'>
```

Booleans are used for logical operations and decisions, such as checking a condition.

## The `bool()` function

`bool()` converts any value to `True` or `False`.

```python
print(bool(1))   # True
print(bool(0))   # False
```

### Truthy and falsy values

- **Falsy** (become `False`): `0`, `0.0`, `""` (empty string), `[]`, `{}`, `()`, `None`, `False`
- **Truthy** (become `True`): almost everything else, such as non-zero numbers and non-empty strings or collections

```python
print(bool(-5))      # True
print(bool("a"))     # True
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False
```

## Comparison operators return booleans

```python
print(5 > 3)        # True
print(5 == 3)       # False
print(5 != 3)       # True
print("a" in "abc") # True
```

## Logical operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | `True` only if both are `True` | `True and False` -> `False` |
| `or`  | `True` if at least one is `True` | `True or False` -> `True` |
| `not` | reverses the value | `not True` -> `False` |

```python
age = 20
has_id = True

print(age >= 18 and has_id)   # True
print(age < 18 or has_id)     # True
print(not has_id)             # False
```

## Using booleans in conditions

```python
is_cool = True

if is_cool:
    print("You are cool")
else:
    print("Not cool")
```

## Good to know

- `True` and `False` behave like `1` and `0` in arithmetic: `True + True` is `2`.
- `=` assigns a value; `==` compares two values.

## Summary

- A boolean is either `True` or `False`.
- `bool(value)` converts a value; `0`, empty values and `None` are `False`.
- Comparisons produce booleans; combine them with `and`, `or`, `not`.
