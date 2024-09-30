""" words_system = 'abcdefghijklmnopqrstuvwxyz'

words_input_user = str(input("Enter your name: "))

for letter in words_input_user:
    if letter.upper() in words_system.upper():
        print(letter)
"""

""" for i in range(0,277,1):
    print(chr(i))
"""

"""
for i in range(1,50,5):
    for j in range(1,10):
        print(f"{j} x {i} : {i}")
"""

options = input("Options: ")

while (options != 0):
    print(f"You chose: {options}")
    
    if options == '+':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Result: {num1 + num2}")
    elif options == '-':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Result: {num1 - num2}")
    elif options == '*':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Result: {num1 * num2}")
    elif options == '/':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
            




