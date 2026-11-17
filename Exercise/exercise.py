#  input("jayjay")
#  input("secret")

# print('{username}, your password {*******} is {6} letters long')

# print("*" * 10)


username = input('what is your name?')
password = input('what is your password?')
password_lenght = len(password)
hidden_password = "*" * password_lenght

print(f'{username}, your passowrd {hidden_password}  is {password_lenght} characters long')
