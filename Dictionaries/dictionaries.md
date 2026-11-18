# Dictionaries in Python

A **dictionary** (`dict`) is a data structure that stores data as **key: value** pairs inside curly braces `{}`. You look up a value by its key instead of by a position number (as in a list).

```python
user = {
    "basket": [1, 2, 3],
    "greet": "hello",
    "age": 20
}

print(user["greet"])   # hello
print(type(user))      # <class 'dict'>
```

## Where to use dictionaries

- Describing one thing with named properties: a user, product, or settings (`name`, `age`, `isMarried`).
- Fast lookup by a label: phone book, word counts, ID -> record.
- Representing JSON or API data.
- A list of dictionaries represents many records (like database rows).

## Keys and values

- **Keys** must be **immutable** (string, number, boolean, tuple). Strings are the most common.
- **Values** can be anything: number, string, bool, list, or another dictionary.

```python
dictionary = {
    "a": [1, 2, 3, 4],
    "b": "hello",
    "x": True
}
```

### Keys must be immutable

```python
dicti = {
    123: [12, 2, 4],
    "rul_age": 30,
    True: "Hello",
    "[100]": True       # OK: this is a string
    # [100]: True       # TypeError: unhashable type: 'list'
}
```

### Keys must be unique

If you repeat a key, the later value **overrides** the earlier one.

```python
d = {"a": 1, "a": 2}
print(d)   # {'a': 2}
```

Watch out: `True` equals `1`, so `{1: "a", True: "b"}` becomes `{1: "b"}`.

## Ordered or unordered?

Dictionaries are conceptually "unordered" key-value stores, and in many languages they are. Since **Python 3.7** a dictionary **remembers insertion order**. You still access items by key, not by index, so don't rely on position.

## Nested data: list of dictionaries

```python
my_list = [
    {"age": 29, "name": "Andrei",  "isMarried": True},
    {"age": 30, "name": "Alice",   "isMarried": False},
    {"age": 31, "name": "Raushan", "isMarried": False},
]

print(my_list[2]["name"])   # Raushan
```

Use the list index first, then the dictionary key.

## Accessing values

```python
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

print(user["age"])       # 20
# print(user["size"])    # KeyError: 'size'  (key doesn't exist)
```

### `get()`: safe access

`get(key, default)` returns `None` (or your default) instead of raising an error when the key is missing.

```python
print(user.get("age", 55))    # 20  (key exists)
print(user.get("size"))       # None
print(user.get("size", 55))   # 55  (default used)
```

## Adding and changing items

```python
user["name"] = "Raushan"   # adds a new key
user["age"] = 21           # updates an existing key
```

## Creating a dictionary

```python
user = {"name": "johnJhon"}
user2 = dict(name="johnJhon")      # keyword style (keys become strings)
print(user2)                       # {'name': 'johnJhon'}
```

## Checking membership

`in` checks **keys** by default.

```python
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

print("basket" in user)           # True
print("size" in user)             # False
print("greet" in user.keys())     # True
print("hello" in user.values())   # True  (checks values)
```

## Dictionary methods

| Method | What it does |
|--------|--------------|
| `keys()` | all keys |
| `values()` | all values |
| `items()` | all `(key, value)` pairs |
| `get(key, default)` | safe lookup |
| `copy()` | shallow copy |
| `pop(key)` | remove key, return its value |
| `popitem()` | remove and return the last inserted pair |
| `update({...})` | add/overwrite keys from another dictionary |
| `clear()` | remove everything |

```python
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

print(user.keys())     # dict_keys(['basket', 'greet', 'age'])
print(user.values())   # dict_values([[1, 2, 3], 'hello', 20])
print(user.items())    # dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])

user3 = user.copy()    # independent copy (top level)

print(user.pop("age"))   # 20
print(user.popitem())    # ('greet', 'hello')  <- last inserted pair

user.clear()             # {}
```

`pop(key)` raises `KeyError` if the key is missing; `pop(key, default)` does not.

### `update()` modifies in place and returns `None`

```python
user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

print(user.update({"age": 31}))   # None  <- don't assign the result
print(user)                       # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 31}
```

## Looping

```python
user = {"greet": "hello", "age": 20}

for key in user:
    print(key, user[key])

for key, value in user.items():
    print(f"{key} -> {value}")
```

## Summary

- A dictionary stores **key: value** pairs and is accessed by key.
- Keys are **immutable and unique**; values can be anything.
- Ordered by insertion since Python 3.7, but not accessed by index.
- Use `get()` to avoid `KeyError`; `in` checks keys.
- `update()`, `pop()`, `popitem()` and `clear()` change the dictionary in place.
- Use a list of dictionaries for multiple records.
