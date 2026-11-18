# Sets in Python

A **set** is an **unordered collection of unique items**, written in curly braces `{}`. It holds only values (no keys), and duplicates are removed automatically.

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9}

print(my_set)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}  -> the extra 9 is gone
```

## Key properties

- **Unique:** each value appears only once.
- **Unordered:** no index, so `my_set[0]` is an error and order is not guaranteed.
- **Mutable:** you can add and remove items.
- **Items must be immutable** (numbers, strings, tuples). A list can't be inside a set.
- Very fast membership checks (`in`).

## Where to use sets

- **Removing duplicates** from a list.
- **Fast membership checks:** is this user/word/ID already seen?
- **Comparing groups:** common friends, missing items, items in either group (intersection, difference, union).
- Tracking unique visitors, tags or categories.

```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
unique_emails = list(set(emails))   # duplicates removed (order not kept)
```

## Creating sets

```python
s = {1, 2, 3}
from_list = set([1, 2, 2, 3])   # {1, 2, 3}
empty = set()                   # empty set

print(type({}))      # <class 'dict'>  <- {} is an empty DICTIONARY
print(type(set()))   # <class 'set'>
```

Always use `set()` for an empty set.

## Converting between list and set

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

print(set(my_list))          # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(list(set(my_list)))    # back to a list, which can be indexed
```

## Membership and length

```python
my_set = {1, 2, 3}
print(1 in my_set)   # True
print(len(my_set))   # 3
```

## Adding items

```python
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set.add(10)    # adds 10
my_set.add(2)     # already there, so nothing changes
my_set.update([11, 12])   # add many items at once
```

## Removing items

```python
my_set1 = {1, 2, 3, 4, 5}

print(my_set1.discard(5))   # None  (discard modifies the set and returns nothing)
print(my_set1)              # {1, 2, 3, 4}

my_set1.discard(99)         # item missing: no error
# my_set1.remove(99)        # KeyError: remove() raises if missing
```

| Method | Behaviour |
|--------|-----------|
| `discard(x)` | remove `x`; no error if missing |
| `remove(x)` | remove `x`; `KeyError` if missing |
| `pop()` | remove and return an arbitrary item |
| `clear()` | remove everything |

## Set operations

These mirror maths set operations.

```python
my_set1 = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
```

### `difference()` / `-`: in the first set only

```python
print(my_set1.difference(your_set))   # {1, 2, 3}
print(my_set1 - your_set)             # {1, 2, 3}
```

### `intersection()` / `&`: in both sets

```python
print(my_set1.intersection(your_set))   # {4, 5}
print(my_set1 & your_set)               # {4, 5}
```

### `union()` / `|`: everything from both sets

```python
print(my_set1.union(your_set))   # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set1 | your_set)        # same
```

### `symmetric_difference()` / `^`: in one set but not both

```python
print(my_set1 ^ your_set)   # {1, 2, 3, 6, 7, 8, 9, 10}
```

### `difference_update()`: changes the set in place

`difference()` returns a **new** set; `difference_update()` modifies the original and returns `None`.

```python
my_set1.difference_update(your_set)
print(my_set1)   # {1, 2, 3}
```

Likewise `intersection_update()` and `update()` (union) change the set in place.

## Comparing sets

| Method | Returns `True` when |
|--------|---------------------|
| `isdisjoint(other)` | the sets have **nothing in common** |
| `issubset(other)` | every item of this set is in `other` (`<=`) |
| `issuperset(other)` | this set contains every item of `other` (`>=`) |

```python
my_set2 = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print({1, 2, 3}.isdisjoint(your_set))   # True   (no common items)
print(my_set2.issubset(your_set))       # True   ({4, 5} is inside your_set)
print(my_set2.issuperset(your_set))     # False  (my_set2 doesn't contain all of your_set)
print(your_set.issuperset(my_set2))     # True
```

## Real example: common and missing friends

```python
alice = {"bob", "carol", "dave"}
bimal = {"carol", "dave", "eve"}

print(alice & bimal)   # {'carol', 'dave'}   mutual friends
print(alice - bimal)   # {'bob'}             only Alice's friends
print(alice | bimal)   # all friends combined
```

## Frozen set

`frozenset` is an immutable set. It can be used as a dictionary key or inside another set.

```python
fs = frozenset([1, 2, 3])
```

## Summary

- A set is an unordered collection of **unique** items.
- Use `set(list)` to remove duplicates; use `set()` (not `{}`) for an empty set.
- `add`, `update`, `discard`, `remove`, `pop`, `clear` change the set in place.
- Operations: `union` `|`, `intersection` `&`, `difference` `-`, `symmetric_difference` `^`.
- Checks: `isdisjoint`, `issubset`, `issuperset`, and `in`.
- No indexing; items must be immutable.
