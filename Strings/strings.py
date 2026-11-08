# string
# str
# piece of text
# 'hi hello there ' it just piece of text
print(type('hello world'))

username = "supercoder"
password = "supersecret"

long_string = '''
wow
o o
----
'''
print(long_string)

first_name = "Raushan"
last_name = "Kumar"

full_name = first_name + " " + last_name
print(full_name)

#  string concatenation --> adding string together
print("hello " + "Raushan")

#  Type Conversion
a = str(100)
b = int(a)
c = type(b)
print(c)
print(type(int(str(100))))  # string type

#  Escape Sequence
weather = "\t It\'s \"kind of\" sunny \n  hope you have a good day!"

print(weather)

#  formatted strings
name = "Johnny"
age = 55
print("hi " + name + ". you are " + str(age) + " years old")
#  do like this
print(f"hi {name}. you are {age} years old")
print("hi {}. you are {} years old".format("johnny", "55"))
print("hi {1}. you are {0} years old".format(name, age))

# print("hi {0}. you are {1} years old".format(new_name="sally", age=100))  # in this case gett error

print("hi {new_name}. you are {age} years old".format(new_name="sally", age=100))

#  String indexes --> string store in memory order of sequence
selfish = 'me me me'
step = "123456789"
# 012345678

# [start:stop:stepover] we called string slicing
print(selfish[7], "-->>", selfish[6])
print(selfish[0:3])
print(step[0:8:2])  # --> this step over two
print(step[1:])
print(step[:5])
print(step[::1])
print(step[-1])
print(step[::-1])
print(step[::-2])

# Immutability
#  strings in python are immutable --> what do we mean by --> it's mean once decleare as variable  to the sting
selfish = "123238923"  # --> we not modify  the string but we can reassign the value of selfish
selfish = 100
#  but we can change the value when it created
selfish[0]="2" # this not modify

