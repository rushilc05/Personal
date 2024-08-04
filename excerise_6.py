num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
try:
    print(int(num1) + int(num2))
except ValueError:
    print("One of your values is not a number.")