def join_list(lst1,lst2):
    list1.extend(list2)
    print(list1)

list1 = []
n1 = int(input("Enter the number of elements for the first list: "))
for i in range(n1):
    element = int(input(f"Enter element {i+1} for list 1: "))
    list1.append(element)


list2 = []
n2 = int(input("Enter the number of elements for the second list: "))
for i in range(n2):
    element = int(input(f"Enter element {i+1} for list 2: "))
    list2.append(element)

join_list(list1,list2)
print(list1)
print(list2)