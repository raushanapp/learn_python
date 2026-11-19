# Conditional Logic and Indentation in Python

**Conditional logic** lets a program make decisions: run some code only when a condition is `True`. Python uses `if`, `elif` and `else`.

## `if` / `elif` / `else`

```python
is_old = True
is_licenced = True

if is_old:
    print('you are old enough to drive!')
elif is_licenced:
    print('you can drive now!')
else:
    print('check')
```

How it works:

1. Python evaluates conditions **top to bottom**.
2. The first condition that is `True` runs, and the rest are **skipped**.
3. `else` runs only if **none** of the conditions were `True`.

In the example above, `is_old` is `True`, so only the first message prints. The `elif` is never checked, even though `is_licenced` is also `True`.

| Keyword | Purpose | How many allowed |
|---------|---------|------------------|
| `if` | first condition | exactly one |
| `elif` | extra conditions | zero or more |
| `else` | fallback when nothing matched | zero or one (last) |

### `if` vs several separate `if`s

`elif` stops after the first match. Separate `if`s are each checked independently.

```python
a, b = True, True

if a:
    print("first")
elif b:
    print("second")   # skipped, because a was True

if a:
    print("first")
if b:
    print("second")   # also runs
```

## Combining conditions

Use the logical operators `and`, `or`, `not`.

```python
is_old = True
is_licenced = True

if is_old and is_licenced:
    print("you are old enough to drive, and you have a licence")
else:
    print("you are not of age!")
```

| Operator | `True` when |
|----------|-------------|
| `a and b` | both are `True` |
| `a or b` | at least one is `True` |
| `not a` | `a` is `False` |

## Comparison operators

```python
age = 20

print(age == 20)   # True   equal
print(age != 18)   # True   not equal
print(age > 18)    # True
print(age >= 20)   # True
print(age < 18)    # False
print(18 <= age < 65)   # True   chained comparison
```

`=` assigns a value; `==` compares.

## Truthy and falsy values

Conditions don't need to be booleans. Empty or zero values count as `False`.

```python
name = ""
if name:
    print("hello", name)
else:
    print("no name given")   # runs: empty string is falsy

items = [1, 2]
if items:                    # same as: if len(items) > 0
    print("cart has items")
```

Falsy: `False`, `None`, `0`, `""`, `[]`, `{}`, `()`, `set()`. Almost everything else is truthy.

## Checking membership

```python
user = {"name": "Alice", "age": 31}

if "age" in user:
    print(user["age"])

if "x" not in "hello":
    print("no x here")
```

## Nested conditions

```python
age = 20
has_licence = True

if age >= 18:
    if has_licence:
        print("you can drive")
    else:
        print("get a licence first")
else:
    print("too young")
```

Often `and` is cleaner: `if age >= 18 and has_licence:`.

## One-line conditional (ternary)

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

Use it only for simple choices.

## Indentation

Python uses **indentation** (leading spaces) to define which lines belong to a block. Other languages use `{ }`; Python does not.

- A line ending with `:` (`if`, `elif`, `else`, `for`, `while`, `def`) starts a block.
- The indented lines below it form the body of that block.
- A line back at the left level is outside the block.

```python
is_old = True

if is_old:
    print("inside the if")      # indented: runs only when is_old is True
    print("still inside")
print("outside the if")         # not indented: always runs
```

### Rules

- Use **4 spaces** per level (the standard, from PEP 8).
- Be **consistent**: don't mix tabs and spaces.
- All lines in one block must have the same indentation.

### Common errors

```python
if True:
print("hello")
# IndentationError: expected an indented block after 'if' statement

if True:
    print("a")
      print("b")
# IndentationError: unexpected indent
```

Indentation changes meaning, not just looks:

```python
is_old = False

if is_old:
    print("old")
    print("this also needs is_old")   # inside
print("runs always")                  # outside
```

## Common mistakes

- Missing `:` after `if`, `elif`, or `else`.
- Using `=` instead of `==` in a condition.
- Wrong indentation.
- Writing `else if`; Python's keyword is `elif`.
- Putting a condition on `else` (`else` never takes one).

## Where to use it

- Validating input (age, password, empty fields).
- Permissions and access (is logged in, is admin).
- Game logic and rules (has weapon, health is 0).
- Choosing different outputs or actions based on data.

## Summary

- `if` / `elif` / `else` run only the **first** matching branch.
- Combine conditions with `and`, `or`, `not`; compare with `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Empty and zero values are falsy.
- Indentation (4 spaces) defines blocks; a `:` starts one.
- Wrong indentation causes `IndentationError`.
