#  Dictionaries
# dict type of python and also have data structure in the python
#  Key is string
#  Value is number ,dictionary or string bool list
#  unorder dictionary --> they all over the place of memory
# a dictionary is unorder key - value pair
# Heads up! As of Python 3.7, they have updated this data structure to now have order maintained now. You can read about it here.
# However, keep in mind that dictionaries from a programming perspective have usually been unordered (and most other languages have dictionaries that are unordered).


dictionary = {
    "a": [1, 2, 3, 4],
    "b": "hello",
    'x': True
}
my_list = [
    {
        'age': 29,
        "name": "Andrei",
        "isMarried": True

    },

    {
        'age': 30,
        "name": "Alice",
        "isMarried": False

    },
    {
        'age': 31,
        "name": "Raushan",
        "isMarried": False

    },

]

dicti = {
    123: [12, 2, 4],
    'rul_age': 30,
    True: "Hellp",
    # [100]: True ==> this wrong
    '[100]': True
}
#  dictionary key always has to be immutable
# key has to be unique  in the dictionary , something only used to once other wise we override the keys

# print(dictionary['b'])
# print(dictionary)

#  Dictionary to have to have unique key

user = {
    "basket": [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

# print(user.get("age",
#                55))  # default value add like this ,what we are doing here if age is does exist add the default value

user2 = dict(name="johnJhon")
# print(user2)
# print('basket' in user2)
# print('size' in user2)
# Dictionary Method in Python

print('greet' in user.keys())
print('hello' in user.values())

# print(user.clear())
# print(user.items())

user3 = user.copy()
# print(user3)

# print(user.pop('age'))
# print(user.popitem())

print(user.update({"age": 31}))
print(user)
