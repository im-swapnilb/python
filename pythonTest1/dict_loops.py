"""
Explore all loops in dictionary and accessing key values using same.
@Author Swapnil_Bandgar, Student_id : 500186962
"""


def dict_for_loop():
    # created dictionary using string, number and list
    dict1 = {"Name": "Swapnil", "Course": "AI & DS", "Intake": "Jan21", "SId": 123,
             "Subjects": ["Python", "Optimization", "Stats", "AI", "ML"]}

    # for loop for accessing keys using key as input
    for key in dict1.keys():
        print("Keys to our dictionary: ", key)

    # for loop for accessing values using value as input
    for values in dict1.values():
        print("Values to our dictionary: ", values)

    # for loop for accessing key and values using key-value as input
    for key, value in dict1.items():
        print(key, " : ", value)


def dict_if_loop():
    # created dictionary using list and string
    dict2 = {"Laptop": "Mac", "Ram": ["8GB", "16GB"], "chip": ["Intel", "M1"]}
    # search key present in dictionary
    search_key = "Ram"
    if search_key in dict2:
        print("Yes we have", search_key, "with values :", dict2[search_key])
    else:
        print("No searchkey available")


def dict_while_loop():
    # created dictionary using string and list
    dict2 = {"Laptop": "Mac", "Ram": ["8GB", "16GB"], "chip": ["Intel", "M1"]}
    search_key = "chip"
    # search key which is not present in dictionary
    search_chip = "M2"
    # accessing key values using while loop
    while search_key in dict2:
        # this will give you number of chips available
        print(dict2[search_key])
        if search_chip in dict2[search_key]:
            print("Yes We have ", search_chip, "Chip")
            break
        else:
            print("No, We don't have ", search_chip)
            break


if __name__ == '__main__':
    print("Will be calling multiple loops to get values and keys in dictionary ")
    dict_for_loop()
    dict_if_loop()
    dict_while_loop()
