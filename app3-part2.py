"""
Problem statement :
1.	Create a function that prints your company name, your position and your gross income each in a new line
2.	Create a function that prints your company name, your position and your gross income each in a new line.
The function has three parameters. Now, in your program create three variables and assign values to them.
Call the function and pass the required arguments.
3.Create a function that multiplies two numbers then calculates the square root of the result, and then returns the
result to the caller. In your program, first, ask the user to enter two numbers. Then call the function.
The caller passes to the function the two numbers as arguments, then the program prints the returned result.
4.	Create a main function in which you call two functions: the first one calculates the power of a given number (a)
to 5, and then the function prints the result.
The second function calculates the modf of a given number( theModF = modf (b) , where b is the given number) and
then the function prints the result.
The main function contains all variables assignments.
In the main function, these variables are passed as arguments when calling the two functions.

@Authors
    Swapnil Bandgar, id : 500186962
    Urmi Parekh, id : 500186977
    Karthik Thallam, id : 500188370
    Ashish Sharma, id : 500188494
"""
import cmath
import math


# function will display the employee details
def employee_details_display():
    print(input("Enter your company name : ") + "\n" + input("Enter your position in your company : ") +
          "\n" + float(input("Enter your gross income : ")).__format__(","))


# function will store value in variable and display
def employee_details(company_name, position, gross_income):
    company = company_name
    position_held = position
    gross_income_final = gross_income
    print(company + "\n" + position_held + "\n" + f"{gross_income_final:,}")


# function will get square root and return to main function
def get_sqrt(num1, num2):
    num_multiplication = num1 * num2
    # complex and negative number case also handled output will be displayed as complex.
    square_root = cmath.sqrt(num_multiplication)
    return square_root


# This is mail function will handle power and mod function calling and input
def main():
    print("Power function started : ")
    num = int(input("Enter number for power calculation : "))
    calculate_power(num)
    print("Mod function started : ")
    calculate_mod(num)


# function will calculate the power for number
def calculate_power(num):
    power = pow(num, 5)
    print("The power is ", power)


# function will calculate the mod for number
def calculate_mod(num1):
    mod = math.modf(num1)
    print("The value of modf is : ", mod)


if __name__ == '__main__':
    print("Employee details display function started :")
    print("\n------------------------------------------------------------------ \n")
    employee_details_display()
    print("\n------------------------------------------------------------------\n")
    print("Employee details enter and display function started :")
    company_name = input("Enter your company name : ")
    position = input("Enter your position in your company : ")
    gross_income = float(input("Enter your gross income : "))
    employee_details(company_name, position, gross_income)
    print("\n------------------------------------------------------------------ \n")
    print("Number function started : ")
    a = int(input("Please, enter the first number: "))
    b = int(input("Please, enter the second number: "))
    print("The result of the square root is : ", get_sqrt(a, b))
    print("\n------------------------------------------------------------------ \n")
    print("main function started :")
    main()
    print("\n------------------------------------------------------------------ \n")
