def fibonnaci(num):
   a=0
   b=1
   while num>=a:
      print(a,end= " ")
      next_num = a+b
      a=b
      b=next_num
      
number = int(input("Enter the limit of fibonnaci series"))
fibonnaci(number)
