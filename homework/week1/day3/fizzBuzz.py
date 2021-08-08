print("Enter 3 for Fizz, Enter  5 for Buzz, Enter 0 for Fizz Buzz")
num = int(input("Enter a number:"))


if  num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")

elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")

print("Thanks for your response!")