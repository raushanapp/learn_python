li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cahr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
li2 = [1, 2, 3, "a", True]

#  Data Structure

amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
# print(amazon_cart[1])

# List slicing
# string="hellooo"
# string[0:5:2]
greet = "hello"
# greet[0] = "world"  # because string are immutable  --> can not chage the her
print(greet)
# print(amazon_cart)

amazon_cart[0] = "laptop"
new_cart = amazon_cart[0:3]
new_cart[0] = 'Gum'
# print(new_cart)
# print(amazon_cart)

#  here we are not copying the list
amazon_cart[0] = 'laptop1'
new_cart = amazon_cart
new_cart[0] = 'gum 1'

# print(new_cart)
# print(amazon_cart)

amazon_cart[0] = 'laptop 2'

new_cart = amazon_cart[:]  # : --> it's mean copying the amazon_cart not modifying here using : symbol inside the [:]
new_cart[0] = 'gum 2'

# print(new_cart)
# print(amazon_cart)

#  Matrix

matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]
# print(matrix[0][1])

basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(len(basket))

#  adding ---> what does do just he append into the list but not display the result to the append item list
new_list = basket.append(10)
#  above case we can not print to current item push to the list
#  if order to have new_list something when append to item to the basket list we
basket.append(11)
new_list = basket

# Insert method
#  Insert modify the list and he does not create a copy of list
basket.insert(5, 100)

#  Extend() --> which list we can iterators the list
new_list = basket.extend([1000])

#  removing
# pop with give to as parameter pass the index
basket.pop()
basket.pop(0)
#  we pass the value we removed
basket.remove(4)

#  Clear()  --> removed every thing in have in the list
new_list = basket.clear()
new_basket = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Index
# new_basket.index((2))

# print(new_basket.index("e", 0, 5))
# print(new_basket.index("e"))

# sort and sorted built in function

items = ["a", "c", "d", "b", "f"]
items.sort()
#  sorted create a new copy of items
# print(items)
# print(sorted(items))

# Common List Patterns
item1 = ["a", "c", "d", "b", "f", "x"]
item1.sort()
item1.reverse()
# print(len(item1))
# print(item1[::-1])
# print(item1[:])  # copy the list


# print(item1)
# items.remove()

# print(basket)
# print(new_list)

# Range to create the list
# print(list(range(1, 101)))

sentence = ' '
new_sentence = sentence.join(["hi", "my", "name", "is", "jojo"])
print(new_sentence)

#  List unpacking
list_unpack = [1, 2, 3]
a, b, c = [4, 5, 6]
d, e, f = 9, 0, 10

g, h, i, *other, m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, ]
#  None --> means -> special data that exist in the python
none = None
#  we creating a videos game when starting there is no weapon so we can put the value None
weapons = None
