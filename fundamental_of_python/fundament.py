# fundamental Data Types
# int and float
# print(type(6));
# print(type(2-4))
# print(type(2*4))
# print(type(2/4)) # division always return float and python automatically converts int to float if needed
from mimetypes import init

print(type(10.56))
print(type(9.9+1.1)) # addition of two floats results in a float
print(9.9+1.1)

#  double multiply 
print(2**2) # 2 raised to the power of 2
print(2**3) # 2 raised to the power of 3
print(2//4) # floor division returns the largest integer less than or equal to the division result

print(5//4) # floor division of 5 by 4
print(5%4) # modulus returns the remainder of the division

#  math functions

print(round(3.1)) # rounds to the nearest integer
print(abs(-3)) # returns the absolute value of the number

# Operator precedence
# In Python, the order of operations follows the standard mathematical rules:
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication and Division (from left to right) *, /, //, %
# 4. Addition and Subtraction (from left to right) +, -

print(20-3*4) # multiplication has higher precedence than subtraction
print((20-3)*4) # parentheses alter the precedence, subtraction happens first
print(20-(3*4)) # multiplication inside parentheses happens first
print(20-3**2) # exponentiation has higher precedence than subtraction
print((20-3)**2) # parentheses alter the precedence, subtraction happens first
print(20-3*2**2) # exponentiation has higher precedence than multiplication and subtraction
print((20-3*2)**2) # parentheses alter the precedence, multiplication happens first 
print(20-(3*2)**2) # exponentiation inside parentheses happens first
print((20-3)**2 + 4) # parentheses alter the precedence, subtraction happens first, then addition
print(20-3**2 + 4) # exponentiation has higher precedence than subtraction and addition
print((20-3**2) + 4) # parentheses alter the precedence, exponentiation happens first, then subtraction and addition    
print(20-3**2 * 2) # exponentiation has higher precedence than multiplication and subtraction
print((20-3**2) * 2) # parentheses alter the precedence, exponentiation happens first, then subtraction and multiplication
print(20-(3**2 * 2)) # exponentiation has higher precedence than multiplication, which has higher precedence than subtraction
print((20-3**2 * 2)) # parentheses alter the precedence, multiplication happens first, then exponentiation, then subtraction    
print(20-3**2 * 2 + 1) # exponentiation has higher precedence than multiplication, which has higher precedence than subtraction and addition
print((20-3**2 * 2) + 1) # parentheses alter the precedence, multiplication happens first, then exponentiation, then subtraction, then addition
print(20-3**2 * (2 + 1)) # parentheses alter the precedence, addition happens first, then exponentiation, then multiplication, then subtraction
print((20-3**2) * (2 + 1)) # parentheses alter the precedence, exponentiation happens first, then subtraction, then multiplication

#  Extra data
# complex
# int and float  # store in the memory in binaray version in the
print(bin(5))

print(int('0b101',2))