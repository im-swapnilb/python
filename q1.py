"""
Create two lists; one contains 10 elements and the other one is empty.
Write a python program that iterates through the first one, pops the elements from the end of it,
then it pushes them one by one to the empty list. As your program iterates through the first list,
clean it before processing the data, meaning if any element is like a special character ( , . ; : )
it must be discarded and not gets pushed to the second list.
@Authors
    Urmi Parekh, id : 500186977
    Karthik Thallam, id : 500188370
    Ashish Sharma, id : 500188494
    Swapnil Bandgar, id : 500186962

"""


def listOperation():
    # Defining list 1
    list1 = [1, 'LoyalistAI', 'A', 6, 'Loyalist123', 'Urmi@2020', 'I', 8, ':', 10]

    # Defining empty list
    list2 = []

    print("List1 before operation:", list1)
    print("Empty list  before operation:", list2)

    # Iterating through all the elements from the list
    for i in range(len(list1)):

        # Removing the last element from the list
        poped_element = str(list1.pop())

        # Checking if list contains any special character
        if not poped_element.isnumeric() and not poped_element.isdigit() and not poped_element.isalpha() and not poped_element.isalnum():
            print("The special character", poped_element + " is removed.")

        else:
            # Adding elements from list1 to the empty list
            list2.append(poped_element)
            print("List 1:", list1)
            print("New List :", list2)


if __name__ == '__main__':
    print("The list operations begins now:")

    # Calling the function
    listOperation()
