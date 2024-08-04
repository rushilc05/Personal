print("Enter 'q' to quit")
while True:
    num1 = input("\nEnter a number: ")
    num2 = input("Enter another number: ")
    try:
        print(int(num1) + int(num2))
    except ValueError:
        if num1 == 'q' or num2 =='q':
            break
        else:
            print("One of your values is not a number.")
