"""
This will cover different operations for dictionary
@Author Swapnil_Bandgar, Student_id : 500186962

"""


# Dictionary functions with different operations
def dict_functions():
    # created dictionary with String
    dict1 = {"Name": "Swapnil", "Course": "AI & DS", "Intake": "Jan21"}
    # copied dictionary one to another
    dict2 = dict1.copy()
    print("New copied dictionary : ", dict2)
    dict1.pop("Course")
    # removing the Course from the dictionary
    print("Dictionary after pop: ", dict1)
    # removing the last element from the dictionary
    dict2.popitem()
    print("Dictionary after pop last item: ", dict2)
    dict1.update({"year": "2021"})
    # updating dictionary with new
    print("Dictionary after update: ", dict1)
    # deleting all items in dictionary
    dict2.clear()
    print("Dictionary after clear: ", dict2)
    # checking dictionary has element or not
    admission = "Intake"
    if admission in dict1:
        print(admission, "For", dict1[admission])
        # Deleting the element is dictionary
        del dict1[admission]
        print(admission, "got deleted")
        print("Dictionary after deleting ", admission, dict1)
    else:
        # To avoid the key error
        print("Sorry ", dict1.get(admission, "No key found"))


if __name__ == '__main__':
    print('here you go for for some dictionary functions ')
    dict_functions()
