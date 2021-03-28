"""

"""


from datetime import datetime


def read_file(my_file_new):
    # my_file1 = open("test.txt", "r+")
    print(my_file_new.__sizeof__())
    if my_file_new.__sizeof__() >= 0:
        for x in my_file_new:
            print(x)
    else:
        print("File is empty")


def write_to_file(user_name):
    date_write = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    my_file.writelines("\n")
    my_file.write("user with: " + user_name + " login time : " + date_write)
    # my_file.close()
    return my_file


if __name__ == '__main__':
    print("User log :")
    user = str(input("Enter user name : "))
    my_file = open("test.txt", "r+")
    my_file = write_to_file(user)
    read_file(my_file)
    my_file.close()


