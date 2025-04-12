def factorial (num):
    fact = 1
    for i in range(1,num):
        fact = fact*num
        num = num - 1
    return fact

number = int(input("Enter the number to find it's factorial: "))
result = factorial(number)
print(result)