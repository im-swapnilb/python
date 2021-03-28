import random

"""
@Author Karthik_Thallam(500188370) and Swapnil_Bandgar(500186962)
This program will work with different list operations with examples .
"""


def list_operations():
    list_new = ['Karthik', 'Swapnil', 0, 1, 2]
    apple1 = []
    for item in list_new:
        apple1.append(item)
    print("list after append:", apple1)
    apple1.pop()
    print("list after pop: ", apple1)
    apple1.remove(1)
    print("list after removing 1st element:", apple1)
    apple1.insert(2, 'Group')
    print("list after inserting new element: ", apple1)
    print('The length of the apple1 list is:', len(apple1))
    list2 = ['Python', 'As01']
    apple1.extend(list2)
    print("list after extending another list: ", apple1)
    subApp = ['winter', 'AI']
    apple1.append(subApp)
    print("list after appending the subApp list: ", apple1)
    print('The subApp list inside the apple1 list is:', apple1[6])
    nested_list = apple1[6]
    print("Nested list: ", nested_list)
    first_element = subApp[0]
    print('The first element in subApp is:', first_element)
    random_element = random.choice(apple1)
    print('The random element from the apple1 list is:', random_element)


if __name__ == '__main__':
    list_operations()
