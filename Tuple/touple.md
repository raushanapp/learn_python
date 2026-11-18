# Tuples in Python

A **tuple** is an ordered collection of items written in round brackets `()`. It is like a list, but **immutable**: once created, you cannot add, remove or change its items.

```python
my_tuple = (1, 2, 3, 4)
print(type(my_tuple))   # <class 'tuple'>
```

## Tuple vs list

| | List `[]` | Tuple `()` |
|---|-----------|------------|
| Mutable | Yes | **No** |
| Flexibility | More methods | Less flexible |
| Speed | Slower | Slightly faster, less memory |
| Can be a dictionary key | No | Yes (if items are immutable) |

## Where to use tuples

- Data that should **never change**: coordinates (e.g. an Uber pickup location `(lat, lng)`), RGB colours, dates, days of the week.
- **Dictionary keys**, because keys must be immutable.
- Returning **multiple values** from a function.
- Protecting data from accidental modification.

```python
location = (28.6139, 77.2090)    # latitude, longitude
colour = (255, 0, 0)             # RGB red
```

## Indexing and slicing

Works exactly like lists and strings.

```python
my_tuple = (1, 2, 3, 4)

print(my_tuple[0])     # 1
print(my_tuple[1])     # 2
print(my_tuple[-1])    # 4
print(my_tuple[2:4])   # (3, 4)   slicing returns a new tuple
```

## Immutability

```python
my_tuple = (1, 2, 3, 4)
my_tuple[1] = "Z"      # TypeError: 'tuple' object does not support item assignment
```

To "change" a tuple, build a new one:

```python
my_tuple = my_tuple + (5,)   # (1, 2, 3, 4, 5)
```

Note: if a tuple holds a mutable item such as a list, that inner list can still change.

```python
t = ([1], 2)
t[0].append(5)
print(t)   # ([1, 5], 2)
```

## Creating tuples

```python
a = (1, 2, 3)
b = 1, 2, 3              # brackets are optional
c = tuple([1, 2, 3])     # from a list
d = ()                   # empty tuple

single = (5,)            # a single item needs a trailing comma
not_tuple = (5)          # this is just the int 5
print(type(single), type(not_tuple))   # <class 'tuple'> <class 'int'>
```

## Tuple unpacking

Assign items to separate variables. `*` collects the rest into a **list**.

```python
y, z, w, *other = (6, 7, 8, 9, 0)
print(y, z, w)   # 6 7 8
print(other)     # [9, 0]
```

Swapping variables uses tuple packing and unpacking:

```python
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1
```

## Tuples as dictionary keys

A list can't be a key, but a tuple can.

```python
user = {
    "basket": [1, 2, 4, 5, 6],
    "name": "Alice",
    "age": 31
}

user1 = {
    (1, 2): [1, 2, 4, 5, 6],   # tuple key
    "name": "Alice",
    "age": 31
}

print(user1[(1, 2)])   # [1, 2, 4, 5, 6]
```

Handy for grid positions, e.g. `board[(row, col)]`.

## Returning multiple values from a function

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([3, 1, 9])
print(low, high)   # 1 9
```

## Tuple methods and functions

Because tuples are immutable, they have only two methods.

```python
my_tuple = (1, 2, 3, 4)

print(5 in my_tuple)        # False  (membership)
print(my_tuple.count(5))    # 0      (how many times 5 appears)
print(my_tuple.index(2))    # 1      (position of first 2; ValueError if missing)
print(len(my_tuple))        # 4
```

Also: `+` joins tuples, `*` repeats them, and `for item in my_tuple:` loops over them.

## Summary

- Tuple = ordered, **immutable** collection in `()`.
- Faster and safer than lists when data shouldn't change.
- Supports indexing, slicing, unpacking, `in`, `len()`, `count()` and `index()`.
- Can be used as a dictionary key.
- A one-item tuple needs a comma: `(5,)`.
- Typical uses: coordinates, fixed records, multiple return values.
