print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

symbol = input("Enter the symbol of the operation you want to perform: ")


num = int(input("Enter the first number: "))
num1 = int(input("Enter the second number: "))



if symbol == '+':
    print(f"{num}{symbol}{num1}=",num+num1)
elif symbol == '-':
    print(f"{num}{symbol}{num1}=",num-num1)
elif symbol == '*':
    print(f"{num}{symbol}{num1}=",num*num1)
elif symbol == '/':
    print(f"{num}{symbol}{num1}=",num/num1)
elif symbol == '%':
    print(f"{num}{symbol}{num1}=",num%num1)
else:
    print("Invalid input")
