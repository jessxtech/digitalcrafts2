firstNumber = int(input("What is the first number?"))
secondNumber = int(input("What is the second number?"))

operator = input("What is the operator? (*,/,+,-)")

print(firstNumber, secondNumber, operator)

if operator == "+":
    print(firstNumber + secondNumber)

if operator == "*":
    print(firstNumber * secondNumber)

if operator == "/":
    print(firstNumber / secondNumber)

if operator == "-":
    print(firstNumber - secondNumber)