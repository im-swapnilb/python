"""
Create dict with different key- values and print it.
Adding error function as well as the error message in code, This program will give you error once ran.
@Author Swapnil_Bandgar, Student_id : 500186962
"""


# create dictionary from list
def list_to_dist(list_convert):
    it = iter(list_convert)
    # using zip function converting to dictionary
    result_dist = dict(zip(it, it))
    return result_dist


# create dictionary from tuple
def tuple_to_dist(tuple_convert):
    dict3 = dict(tuple_convert)
    return dict3


# creating dictionary using different methods
def create_dict():
    # empty dictionary
    empty_dict = {}

    # string key and value dictionary
    dict_string = {"Name": "Swapnil", "Course": "AI&DS", "Intake": "Jan21"}
    print(dict_string)

    # string as key and number as value dictionary
    dict_string_num = {"Born month": 5, "Born date": 13, "Born year": 1992}
    print(dict_string_num)

    # string as value and number as key dictionary
    dict_num_string = {1: "One", 2: "Two", 3: "Three", 4: "Four"}
    print(dict_num_string)

    # complex dictionary with tuple and string as Key and list as a values
    dict_laptop = {"Brand": ["Apple", "lenovo", "hp"], "Ram": ["8GB", "16GB"],
                   "chip": ["Intel", "M1"], "Graphics": ["Nvidia", "AMD"],
                   ("Screen_Size", "Resolution"): ["13", "14", "15", "1040x1080"]}

    print(dict_laptop)

    # Error in dictionary because we are using list as Key and list is mutable
    dict_laptop_err = {"Brand": ["Apple", "lenovo", "hp"], "Ram": ["8GB", "16GB"],
                       "chip": ["Intel", "M1"], "Graphics": ["Nvidia", "AMD"],
                       ["Screen_Size", "Resolution"]: ["13", "14", "15", "1040x1080"]}

    print(dict_laptop_err)
    # ["Screen_Size", "Resolution"]: ["13", "14", "15", "1040x1080"]}
    # TypeError: unhashable type: 'list' (As list is mutable object)


if __name__ == '__main__':
    print('here you go for creating dictionary ')
    list1 = ['County', 'India', 'dialCode', 91]
    tuple1 = ((1, "a"), (2, "b"))
    create_dict()
    print(list_to_dist(list1))
    print(tuple_to_dist(tuple1))
