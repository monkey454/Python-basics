def is_prime(num):
        if num < 2:
            return "neither prime nor composite" 
        
        divisor_count = 0
        for i in range(1,num+1):
            if num%i == 0:
                divisor_count +=1 
        if divisor_count == 2:
            return "prime number"
        else:
            return "not prime number"
number = int(input("Enter a number\n"))
result = is_prime(number)
print(f"{number} is",result)    