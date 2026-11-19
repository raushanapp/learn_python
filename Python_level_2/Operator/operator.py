#  Ternary Operator
#  These ternary operator also called the conditional expressions
#  condition_if_true if condition else condition_if_false

is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

#  Short Circuiting

is_Friends = False
is_User = True

if is_Friends and is_User:
    print("Best friends")

# we can do this here short circuiting

if is_Friends or is_User:
    print("Best friends forever")

#  Logical Operators

# print(4=5) --> syntaxError --> keyword can't be an expression

print(4 == 5)
print("hello" == "hello")
print('a' > 'b')  # here check unicode not a character --> False a -> 97 b-> 98 A -> 65
print('a' > 'A')  # True
print(1 > 2)
print(1 < 2 > 3 < 4)
print(1 >= 0)  # True
print(1 <= 0)  # False
print(0 <= 0)
print(0 != 0)
print(not (True))  # not just does opisite of the result of give value
