def reverse_number(num):
    in_string = str(num)

    rever_text = in_string[::-1]
    print(rever_text)

user_input = int(input("Enter a number\n)"))
result = reverse_number(user_input)
print(f"{result} is the reverse of the entered number")
