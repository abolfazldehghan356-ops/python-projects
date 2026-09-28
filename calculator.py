number1 = float(input("Enter first number: "))
operation = input("Enter + or -: ")
number2 = float(input("Enter second number: "))

if operation == "+":
    print(number1 + number2)

elif operation == "-":
    print(number1 - number2)

else:
    print("Invalid operation!")
