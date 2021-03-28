"""
The task is to convert the Dictionary into sublist and than allowing user to input the Countries
It will handle and capitalize the Value entered by user and if its found in the Sublist we will get the index of Sublist
and Show the Capital of the Country based on the index.
@Authors
    Swapnil Bandgar, id : 500186962
    Urmi Parekh, id : 500186977
    Karthik Thallam, id : 500188370
    Ashish Sharma, id : 500188494
"""


def getIndex(result_country, name_of_country):
    # We will extract the index of the elements of the Country entered by user
    is_found = False
    # iterating over the list
    for i in range(len(result_country)):
        # iterating over the sub list
        for j in range(len(result_country[i])):
            # checking for the element whether it is existing in Sublist
            if result_country[i][j] == name_of_country:
                # printing the sub list index that contains the element
                print(f'Index of the Country {name_of_country}: {i}')
                Indexvalue = i
                # changing the flag to True
                is_found = True
            # breaking the inner loop
            break
        # breaking the outer loop
        if is_found:
            break
        # checking whether the element is found or not
    return Indexvalue


def extract_CountryDetails():
    # initializing dictionary with 7 countries
    countryCapitals = {"India": "New Delhi", "Canada": "Toronto", "Australia": "Sydney", "Bangladesh": "Dhaka",
                       "Bhutan": "Thimpu", "Zambia": "Lusaka", "Zimbabwe": "Harare"}
    # Converting Country into sublist
    resultCountry = [[k, v] for k, v in countryCapitals.items()]
    # User will input the Country
    nameofCountry = str(input("Enter Country: ")).capitalize()
    # Validate whether country Exist in Sublist
    if any(nameofCountry in sublist for sublist in resultCountry):
        Indexvalue = getIndex(resultCountry, nameofCountry)
        print("Capital of the Country {} is {}.".format(nameofCountry, resultCountry[Indexvalue][1]))
    else:
        print("Country Not Present")


if __name__ == '__main__':
    extract_CountryDetails()
