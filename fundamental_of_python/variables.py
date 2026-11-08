# variables --> store information to hold the data to use in our programs
#  variable rule
# snake_case
# Start with lower case or underscore
# Letters, numbers, underscores
# Case sensitive
# Don't overwrite the keywords
iq = 109

_user_id = 190
user41 = "180"
user_IQ = 200
# print(user_iq)  we can not case like this is because Case sensitive

#  two small gotcha
# constants
PI = 3.14  # this value never gone change this
# __hi="hi" we should not create with double underscore
e, b, c = 1, 2, 3

print(iq)
# print(a)
print(e, b, c)

#  Expression and statement
user_age = iq / 4  # this is expression and this case what action performing

# augmented assignment operator
#
some_value = 5
some_value = some_value * 2  # in memory point to value 10
#  cleaner way doing like this and also keep it mind this variable has some previous value
some_value += 2
some_value *= 3
some_value -= 4
#  operator comes to the left to the equal sign
print(some_value)
