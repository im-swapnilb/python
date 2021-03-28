"""
This will cover different operations for dictionary
@Author Swapnil_Bandgar, Student_id : 500186962

"""


def dict_operations():
    list1 = []
    # created dictionary with list, tuple and String
    dict_laptop = {"Brand": ["Apple", "lenovo", "hp"], "Ram": ["8GB", "16GB"],
                   "chip": ["Intel", "M1"], "Graphics": ["Nvidia", "AMD"],
                   ("Screen_Size", "Resolution"): ["13", "14", "15", "1040x1080"]}

    # accessing dictionary keys using key as iterator
    for key in dict_laptop.keys():
        print("Features to consider while buying a laptop: ", key)

    # accessing dictionary values using value as iterator
    for values in dict_laptop.values():
        print("Best optionsS to consider while buying a laptop: ", values)

    # accessing dictionary key and values using key-value as iterator
    for key, value in dict_laptop.items():
        print(key, " : ", value)


if __name__ == '__main__':
    print('here you go for calling dictionary using key, value, and item')
    dict_operations()
