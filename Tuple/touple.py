# TUPLE --> data structure

# What are tuple --> unlike as list but tuple is immutable, it's means  one define tuple you can not change or modify from the memory
# only difference  is immutable  and less flex than list
# faster than list
# user case --> UBER --> we can use tuple for the location
my_tuple = (1, 2, 3, 4)
# new_tuple = my_tuple[1:2]
new_tuple = my_tuple[2:4]
x = my_tuple[0]
y, z, w, *other = (6, 7, 8, 9, 0)
user = {
    "basket": [1, 2, 4, 5, 6],
    "name": "Alice",
    "age": 31
}

user1 = {
    (1, 2): [1, 2, 4, 5, 6],
    "name": "Alice",
    "age": 31
}

# my_tuple[1] = 'Z'
print(my_tuple[1])
print(5 in my_tuple)
print(user1[(1, 2)])

print(new_tuple)
print("X --> ", y, z, w, other)

print(my_tuple.count(5))
print(my_tuple.index(2))
print(len(my_tuple))
