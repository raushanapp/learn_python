#  input("jayjay")
#  input("secret")

# print('{username}, your password {*******} is {6} letters long')

# print("*" * 10)


# username = input('what is your name?')
# password = input('what is your password?')
# password_lenght = len(password)
# hidden_password = "*" * password_lenght
#
# print(f'{username}, your passowrd {hidden_password}  is {password_lenght} characters long')

#  Gaming company
is_magician = True
is_expert = False

#  check if magician and expert : "you are a master magician"
#  chek if magician but not expert : "At least you're getting there"
#  if you're not a magician : "You need magic powers

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('At least you are getting there')
elif not is_magician:
    print('You need magic powers')
