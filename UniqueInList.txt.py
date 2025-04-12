def unique_list(list):
    unique = []
    for num in list:
        if list.count(num) == 1:
            unique.append(num)
    return unique
# numbers = [1,2,3,3,4,5,6,6,7]
# print(unique_list(numbers))

limit = int(input("Enter the limit of the elements in the list\n"))

number = []

for i in range(limit):
    elements = int(input("Enter the elements of the"))
    number.append(elements)

print("The list is",number)
print("The unique numbers are",unique_list(number))