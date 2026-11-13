# Built-in Functions and String Methods in Python

## Built-in functions

Built-in functions are always available; no import is needed. They are called as `function(value)`.

| Function | Purpose | Example |
|----------|---------|---------|
| `str()`  | convert a value to a string  | `str(100)` -> `'100'` |
| `int()`  | convert a value to an integer | `int("100")` -> `100` |
| `len()`  | number of items/characters    | `len("hello")` -> `5` |
| `type()` | type of a value               | `type("hi")` -> `<class 'str'>` |
| `print()`| show output                   | `print("hi")` |

```python
str()          # empty string ''
int()          # 0

greet = "helllooo"
print(len(greet))              # 8
print(greet[0:len(greet)])     # helllooo  -> slice from start to the end
```

`len(greet)` is the length of the string, so `greet[0:len(greet)]` returns the whole string.

## String methods

Methods belong to a type and are called on a value with a dot: `value.method()`. They are not general built-in functions, but they are used the same way you explore strings.

```python
quote = "to be or not to be"

print(quote.upper())            # TO BE OR NOT TO BE
print(quote.capitalize())       # To be or not to be   (first letter only)
print(quote.lower())            # to be or not to be
print(quote.find("be"))         # 3   -> index of the first match (-1 if not found)
print(quote.replace("be", "me"))  # to me or not to me
```

| Method | What it does |
|--------|--------------|
| `upper()` | all characters to uppercase |
| `lower()` | all characters to lowercase |
| `capitalize()` | first character uppercase, the rest lowercase |
| `find(sub)` | index of the first occurrence of `sub`, or `-1` |
| `replace(old, new)` | returns a new string with `old` replaced by `new` |

## Strings are immutable

Methods never change the original string; they return a **new** one.

```python
print(quote.replace("be", "me"))  # to me or not to me   (new string)
print(quote)                      # to be or not to be   (unchanged)

quote = quote.replace("be", "me")  # reassign to keep the result
```

## Tip

Use `help()` or `dir()` to explore what is available:

```python
print(dir(str))        # list all string methods
help(str.upper)        # documentation for one method
```

