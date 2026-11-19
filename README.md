# Learn Python

My personal Python learning journey, based on the ZTM (Zero To Mastery) course. Each topic has its own folder with a practice `.py` file and a `.md` file containing my notes and code examples for later reference.

## Topics learned

### Python fundamentals
| Topic | Folder | Notes | What I learned |
|-------|--------|-------|----------------|
| Numbers, operators and variables | [`fundamental_of_python`](fundamental_of_python) | [fundamental.md](fundamental_of_python/fundamental.md) | `int` and `float`, arithmetic operators, math functions, operator precedence, binary representation, variable naming rules, constants, expressions vs statements, augmented assignment (`+=`) |
| Type conversion | [`Type_Conversion`](Type_Conversion) | [type_conversion.md](Type_Conversion/type_conversion.md) | `type()`, `input()` returns a string, `int()` / `float()` / `str()` / `bool()`, `ValueError`, `try`/`except` |
| Strings | [`Strings`](Strings) | [string.md](Strings/string.md) | quotes, concatenation, escape sequences, f-strings and `.format()`, indexing, slicing, immutability |
| Booleans | [`Boolean`](Boolean) | [boolean.md](Boolean/boolean.md) | `True` / `False`, `bool()`, truthy and falsy values, comparison and logical operators |
| Built-in functions | [`Built_in_functions`](Built_in_functions) | [README.md](Built_in_functions/README.md) | `len()`, `str()`, `int()`, string methods (`upper`, `lower`, `capitalize`, `find`, `replace`) |

### Data structures
| Topic | Folder | Notes | What I learned |
|-------|--------|-------|----------------|
| Lists | [`List`](List) | [list.md](List/list.md) | indexing and slicing, copying, matrix, `append` / `insert` / `extend`, `pop` / `remove` / `clear`, `sort` vs `sorted`, `join`, unpacking, `None` |
| Dictionaries | [`Dictionaries`](Dictionaries) | [dictionaries.md](Dictionaries/dictionaries.md) | key-value pairs, unique and immutable keys, `get()`, `in`, `keys` / `values` / `items`, `update`, `pop`, `copy` |
| Tuples | [`Tuple`](Tuple) | [touple.md](Tuple/touple.md) | immutable sequences, unpacking, tuples as dictionary keys, `count`, `index` |
| Sets | [`Sets`](Sets) | [sets.md](Sets/sets.md) | unique items, removing duplicates, union, intersection, difference, subset and superset checks |

### Python level 2
| Topic | Folder | Notes | What I learned |
|-------|--------|-------|----------------|
| Conditional logic and indentation | [`Python_level_2/Conditional_logic`](Python_level_2/Conditional_logic) | [conditional_logic.md](Python_level_2/Conditional_logic/conditional_logic.md) | `if` / `elif` / `else`, `and` / `or` / `not`, truthy values, nested conditions, indentation rules |
| Truthy and falsy | [`Python_level_2/Truthy_Falsy`](Python_level_2/Truthy_Falsy) | [truthy_falsy.md](Python_level_2/Truthy_Falsy/truthy_falsy.md) | falsy values, `bool()`, `if items:` style, `or` defaults, `is None`, real-life validation use cases |

## Practice and exercises

- [`Exercise/exercise.py`](Exercise/exercise.py): mini program using `input()`, `len()` and string multiplication to hide a password.
- [`fundamental_of_python/execise.py`](fundamental_of_python/execise.py): operator precedence practice.

## Project structure

```
learn_python/
├── fundamental_of_python/   # numbers, operators, variables
├── Type_Conversion/
├── Strings/
├── Boolean/
├── Built_in_functions/
├── List/
├── Dictionaries/
├── Tuple/
├── Sets/
├── Python_level_2/
│   ├── Conditional_logic/
│   └── Truthy_Falsy/
├── Exercise/
└── README.md
```

## How to run

```bash
python3 Strings/strings.py
```

Replace the path with any practice file.

## Up next

Loops (`for`, `while`), functions, and more of Python level 2.
