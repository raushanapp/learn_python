# Lists in Python

A **list** is an ordered, changeable (mutable) collection of items written in square brackets `[]`. It is one of Python's main **data structures**: a way to store and organise many values under one name.

```python
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chars = ["a", "b", "c", "d", "e"]
li2 = [1, 2, 3, "a", True]      # a list can mix different types
```

## Where to use lists

- Storing many related items: a shopping cart, usernames, scores, to-do tasks.
- When order matters and you access items by position.
- When the collection must change: add, remove or update items.
- Grid or table data (a list of lists, called a matrix).

```python
amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
```

## Indexing and slicing

Lists work like strings: indexes start at `0`, negatives count from the end, and slicing is `[start:stop:step]`.

```python
amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]

print(amazon_cart[1])      # sunglasses
print(amazon_cart[-1])     # grapes
print(amazon_cart[0:3])    # ['notebooks', 'sunglasses', 'toys']
print(amazon_cart[::-1])   # reversed copy
```

## Lists are mutable

Unlike strings (immutable), list items can be changed in place.

```python
greet = "hello"
# greet[0] = "world"        # TypeError: strings are immutable

amazon_cart[0] = "laptop"   # works
print(amazon_cart)          # ['laptop', 'sunglasses', 'toys', 'grapes']
```

## Copying a list

A slice creates a **new** list. Plain assignment does **not** copy; both names point to the same list.

```python
amazon_cart = ["laptop", "sunglasses", "toys", "grapes"]

# Slice: a new list
new_cart = amazon_cart[0:3]
new_cart[0] = "Gum"
print(amazon_cart[0])   # laptop  (unchanged)

# Assignment: the SAME list
new_cart = amazon_cart
new_cart[0] = "gum 1"
print(amazon_cart[0])   # gum 1   (changed!)

# [:] copies the whole list
new_cart = amazon_cart[:]
new_cart[0] = "gum 2"
print(amazon_cart[0])   # gum 1   (unchanged)
```

`amazon_cart.copy()` does the same as `[:]`. These are shallow copies: nested lists are still shared.

## Matrix (nested lists)

A list can hold other lists. Use two indexes: `matrix[row][column]`.

```python
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]
print(matrix[0][1])   # 2
```

Use it for grids, game boards, tables.

## Length

```python
basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(basket))   # 9
```

## Adding items

These methods **modify the list in place and return `None`**, so do not assign their result.

| Method | Purpose |
|--------|---------|
| `append(x)` | add one item to the end |
| `insert(i, x)` | add an item at index `i` |
| `extend(iterable)` | add every item of another list/iterable |

```python
basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = basket.append(10)
print(new_list)        # None  <- append returns nothing
print(basket)          # [1, ..., 9, 10]

basket.insert(5, 100)  # [1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10]
basket.extend([1000])  # [..., 10, 1000]
```

`append([1, 2])` adds the list as one item; `extend([1, 2])` adds `1` and `2` separately.

## Removing items

| Method | Purpose |
|--------|---------|
| `pop()` | remove and return the last item |
| `pop(i)` | remove and return the item at index `i` |
| `remove(x)` | remove the first item equal to value `x` |
| `clear()` | remove everything |

```python
basket = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10, 1000]

print(basket.pop())    # 1000  (last)
print(basket.pop(0))   # 1     (first)
basket.remove(4)       # removes the value 4
basket.clear()         # []
```

`remove()` raises `ValueError` if the value isn't in the list.

## Finding an index

`index(value, start, stop)` returns the first position of `value`; it raises `ValueError` if not found. `stop` is exclusive.

```python
new_basket = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(new_basket.index("e"))        # 4
print(new_basket.index("e", 0, 5))  # 4  (searches indexes 0-4)
# new_basket.index("e", 0, 4)       # ValueError
```

Use `"e" in new_basket` for a simple True/False check.

## Sorting: `sort()` vs `sorted()`

```python
items = ["a", "c", "d", "b", "f"]

print(sorted(items))   # ['a', 'b', 'c', 'd', 'f']  -> new list, original unchanged
print(items)           # ['a', 'c', 'd', 'b', 'f']

items.sort()           # sorts in place, returns None
print(items)           # ['a', 'b', 'c', 'd', 'f']
```

Use `sorted()` when you need to keep the original; `sort()` when you don't.

## Reversing

```python
item1 = ["a", "b", "c", "d", "f", "x"]

item1.reverse()        # reverses in place
print(item1)           # ['x', 'f', 'd', 'c', 'b', 'a']
print(item1[::-1])     # reversed copy, original unchanged
print(item1[:])        # copy of the list
```

## Creating a list with `range()`

```python
print(list(range(1, 101)))   # [1, 2, ..., 100]
```

## `join()`: list to string

`join()` is a string method that glues list items together using the string as a separator. Items must be strings.

```python
sentence = ' '
new_sentence = sentence.join(["hi", "my", "name", "is", "jojo"])
print(new_sentence)   # hi my name is jojo

print(", ".join(["a", "b", "c"]))   # a, b, c
```

## List unpacking

Assign list items to separate variables in one line.

```python
a, b, c = [4, 5, 6]        # a=4, b=5, c=6
d, e, f = 9, 0, 10         # works with plain values too

# * collects the "rest" into a list
g, h, i, *other, m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(other)   # [4, 5, 6, 7, 8, 9]
print(m)       # 11
```

The number of variables must match the number of items, unless you use `*`.

## `None`

`None` is Python's special value meaning "nothing / no value yet".

```python
# A game starts and the player has no weapon yet
weapons = None
```

Use it as a placeholder until a real value exists. Check with `if weapons is None:`.

## Summary

- Lists are ordered, mutable and can hold mixed types.
- Slice with `[start:stop:step]`; copy with `[:]` or `.copy()`, never with `=`.
- Add: `append`, `insert`, `extend`. Remove: `pop`, `remove`, `clear`.
- `sort()` changes the list; `sorted()` returns a new one.
- Methods that modify a list return `None`.
- `join()` turns a list of strings into one string.
- Unpack with `a, b, *rest = items`.
