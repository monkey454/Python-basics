def FizzBuzz(number):
    for i in range(1,number+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz") 
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz") 
        else:
            print(i)

user_input = int(input("Enter a limit for FizBuzz\n"))
FizzBuzz(user_input)