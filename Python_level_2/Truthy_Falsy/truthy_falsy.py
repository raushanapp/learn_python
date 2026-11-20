#  Truthy and Falsy
# considered "truthy" except for the following, which are "falsy":
# None
# False
# Numbers that are numerically equal to zero, including:
#     0
#     0.0
#     0j
#     decimal.Decimal(0)
#     fraction.Fraction(0, 1)
# Empty sequences and collections, including:
#     [] - an empty list
#     {} - an empty dict
#     () - an empty tuple
#     set() - an empty set
#     '' - an empty str
#     b'' - an empty bytes
#     bytearray(b'') - an empty bytearray
#     memoryview(b'') - an empty memoryview
#     an empty range, like range(0)
# objects for which
#     obj.__bool__() returns False
#     obj.__len__() returns 0, given that obj.__bool__ is undefined


is_old = bool("hello")
is_licenced = bool(5)

print(bool("hello"))  # These are truthy and value in python
print(bool(5))  # These are truthy and value in python

#  But if you use the zero and empty string these are  falsy
print(bool(''))
print(bool(0))
print(bool([]))

if is_old and is_licenced:
    print("You are old enough to drive and you have a licence!")
else:
    print('you are not of age!')

print("okokok!")

password = "123"
username = "johnny"

if password and username:
    print("password and username are the same!")
else:
    print("Wrong password and username!")

#  Expression
#  == check equality of value
print(True == 1)  # True  this will convert to True == bool(1) --> here type conversion do internally by the python
print('' == 1)  # False
print('1' == 1)  # False  here  not because check directly type not converting to the one type
print([] == 1)  # False  Empty array are falsy
print(10 == 10.0)  # True  10.0 convert to 10 so that why true
print([] == [])  # True

#  is :  checks there is value in memory location is same or not
print(True is 1)  # false  this will convert to True == bool(1) --> here type conversion do internally by the python
print(True is True)  # True
print('' is 1)  # False
print('1' is 1)  # False  here  not because check directly type not converting to the one type
print([] is 1)  # False  Empty array are falsy
print(10 is 10.0)  # false  10.0 convert to 10 so that why true
#   two list different  location in the memory
#  [1,3,4,5] or [2,6,8,10] each time created it creating new location not a same location because this data structure
print([] is [])  # false
