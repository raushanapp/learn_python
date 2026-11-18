#  Set -->  Simple means unorder collection of unique object
#  set have only value
#  only return unique sets
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9}
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

my_set.add(10)
my_set.add(2)

# print(my_set)
# print(set(my_list))
# print(1 in my_set)
# print(list(my_set))

# .difference()
print(my_set1.difference(your_set))
# .discard()
print(my_set1.discard(5))  # here getting because not returning anything : --> None
print(my_set1)

# .difference_update()
my_set1.difference_update(your_set)
# print(my_set1)

# .intersection()
my_set1.intersection(your_set)
print(my_set1.intersection(your_set))
print(my_set1 & your_set)

# .isdisjoint()

print(my_set1.isdisjoint(your_set))
# .issueperset()
print(my_set2.issuperset(your_set))

# .issubaset()
print(my_set2.issubset(your_set))

# .union()
print(my_set1.union(your_set))
# short cut
print(my_set1 | your_set)
