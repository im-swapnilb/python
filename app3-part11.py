"""
Problem statement :
Ask the user how many floating point numbers with 5 integer digits and two decimal digits the program should accept.
That means you need to check if the number entered by the user has 5 digits and two decimal digits to be accepted.
Your program should accept five of them. Add the numbers and display a subtotal.

@Authors
    Urmi Parekh, id : 500186977
    Ashish Sharma, id : 500188494
    Swapnil Bandgar, id : 500186962
    Karthik Thallam, id : 500188370
"""

import re

# Defining the regular expression to check for float value
regex = '[+-]?[0-9]+\.[0-9]+'


# Function for asking user for how many numbers he want to consider
def total_numbers_accept():
    total_numbers = int(input("Please enter how many floating point numbers would you like to consider : "))

    # Calling function to enter numbers
    enter_numbers(total_numbers)


# Function for accepting numbers for user
def enter_numbers(total_number):
    floating_numbers_list = []  # Defining list to store floating numbers from user
    i = 1

    while i <= total_number:
        val = input("Please enter floating point number " + str(i) + ": ")

        # Calling check function to check whether the entered value is of type float
        check_response = check_float(val)
        if check_response == 1:
            splitting_number = val.split(".")  # Splitting the integer digits and decimal digits
            integer_part = splitting_number[0]
            decimal_part = splitting_number[1]
            if len(integer_part) == 5 and len(
                    decimal_part) == 2:  # Checking if integer part has 5 digits and decimal part has 2 digits
                floating_numbers_list.append(val)  # Appending number into the list
                i += 1
            else:
                print("Please enter a floating point number which has 5 integer digits and 2 decimal places")
    # Calling this function to perform summation of all these values
    addition_operation(floating_numbers_list)


# A function for checking if values entered by user are of type float
def check_float(float_num):
    if re.search(regex, float_num):
        return 1

    else:
        print("Not a Floating point number. Please enter valid floating point number.")
        return 0


# Function for Addition operation
def addition_operation(floating_numbers_list):
    total = 0.0
    i = 0

    # We only need to accept 5 numbers as per the problem statement so the value of total_elements should be 5 or
    # less than that
    if (len(floating_numbers_list)) < 6:
        total_elements = len(floating_numbers_list)
    else:
        total_elements = 5

    while i < total_elements:
        total = total + float(floating_numbers_list[i])
        i = i + 1
    print("Total for floating point numbers is:", total)


if __name__ == '__main__':
    print("The floating operation begins now")

    # Calling the function for accepting numbers
    total_numbers_accept()
