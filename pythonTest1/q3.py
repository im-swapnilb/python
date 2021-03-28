"""
The task is to Enter the passwords entered by admin and store it in tuple.
Once passwords are stored we need to find out the passwords in tuple and if its found.
we need to print with an index of the input password entered during our search.
@Authors
    Karthik Thallam, id : 500188370
    Ashish Sharma, id : 500188494
    Urmi Parekh, id : 500186977
    Swapnil Bandgar, id : 500186962
"""


def inputPassword():
    # Create a passwordStored Tuple to store the Passwords entered by admin

    passwordStored = ()
    # Enter the count of total Number of passwords to be entered by user
    passwordCount = input("Enter the number of the Passwords you want to enter: ")
    # Looping through the range of inputs entered by Admin
    for i in range(1, int(passwordCount) + 1):
        password = input("Enter the password you want to Add: ").strip()
        passwordStored = passwordStored + (password,)
        # Adding the current password into tuple
    else:
        print("Passwords are entered by user and Stored in our backend.")

    print("Validate Password entered by User")
    passwordSearched = input("Please enter the Password to be searched: ").strip()
    # Validate if password is found in tuple stored
    if passwordSearched in passwordStored:
        print("Password  is found at index value : ", passwordStored.index(passwordSearched))
    else:
        print("Password is not found")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputPassword()

