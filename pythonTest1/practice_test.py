'''
1- Create your own list in python (of 5 elements) and perform the following:
a. Print a complete list and its length
b. Print starting from a specific element
c. Append a new list to the existing list and access the elements of the inner list
d. Create a sub list (a new list) in the original list
e. Extend your original list to add more elements
f. Use count function in your python
g. Use pop to remove an item (not the last one)
'''

my_List = ['Swapnil','Jan21',500186962,'AI&DS','Online']
print("List is : ",my_List)
print("length is : ", len(my_List))
print("Starting from 3 elemet : ",my_List[3:])
new_List = ['ML','Python','AI']
my_List.append(new_List)
print("Appended list : ",my_List)
print("Appended list items: ",my_List[5][:])
my_List.append([3,5,6])
print("New list got added: ",my_List)
ex_list = [7,8,9]
my_List.extend(ex_list)
print("New list with exteded items : ",my_List)
print("count of items in list are : ",my_List.count('Jan21'))
print("Poping the 3rd value in a list: ",my_List.pop(3))
print("Final list :",my_List)


