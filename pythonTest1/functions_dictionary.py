"""
Explore all dictionary built in functions
@Author Swapnil_Bandgar, Student_id : 500186962
"""


def func_dist():
    # dictionary with tuple, list and string, number
    dict2 = {"Movies": ["Toy Story 1", "Toy Story 2", "Toy Story 3"], "Rating": [4.0, 5.0, 4.7],
             "Released year": (2009, 2011, 2015)}
    print("Length of dictionary: ", len(dict2))
    print("dictionary in string :", str(dict2))
    print("Type of dictionary: ", type(dict2))
    # coping dictionary from one to another
    dict_copy = dict2.copy()
    print("Copy of dictionary: ", dict_copy)
    dict_new = {"Director": "Swapnil"}
    # updating dictionary
    dict2.update(dict_new)
    print("Updated dictionary :", dict2)
    print("Sorted keys in dict_copy : ", list(sorted(dict_copy.keys())))


if __name__ == '__main__':
    print("Here we go some dictionary functions:")
    func_dist()
