#
# tupletest = ("Swapnil",500186962,"AI&DS","Jan21",True)
# fruitSet = {"apple", "banana", "cherry"}
#
#
#
# tupletest[2] = 'Cyber'
# print(tupletest[2])


# t1=("happy\t ")
# t2=("monday")
# print(t1+t2)
# my_str = "Swapnil is mad boy"
#
# print("Updated String:",my_str[:6]+'String')

x = [1, 2, 3]
x.append([4, 5])
print(x) # [1, 2, 3, [4, 5]]
print(type(x))
x.extend([4, 5])
print (x) # [1, 2, 3, 4, 5]
print(type(x))
