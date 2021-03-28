"""
Create dictionary with different key-values and print it
@Author Swapnil_Bandgar, Student_id : 500186962
"""


# creating dictionary with different approach and datatype
def create_dict():
    # creating empty dictionary
    dict4 = {}

    # dictionary with multiple data types
    dict1 = {"Name": "Swapnil", "Course": "AI & DS", "Intake": "Jan21", "SId": 123,
             "Subjects": ["Python", "Optimization", "Stats", "AI", "ML"]}
    print("Student dictionary: ", dict1)
    key_search = "Subjects"
    print("All subjects: ", dict1.get(key_search, "Check key once"))
    tuple1 = ((1, "Swapnil"), (2, "Bandgar"))
    print("dictionary created from tuple ", dict(tuple1))

    # dictionary with tuple, list and string, number
    dict2 = {"Movies": ["Toy Story 1", "Toy Story 2", "Toy Story 3"], "Rating": [4.0, 5.0, 4.7],
             "Released year": (2009, 2011, 2015)}
    print("Movie dictionary: ", dict2)


if __name__ == '__main__':
    print("lets create dictionary with different data types and methods :")
    create_dict()
