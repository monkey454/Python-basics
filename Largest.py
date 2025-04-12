num = int(input("Enter first number\n"))
num1 = int(input("Enter second number\n"))
num2 = int(input("Enter third number\n"))

if num>num1 and num>2:
    print(f"{num} is the greater number")
elif num1>num and num1>num2:
    print(f"{num1} is the greater number")
else:
    print(f"{num2} is the greater number")

