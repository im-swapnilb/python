
age = int(input("Enter your age: "))     # enter your age in Int format
name = input("Enter your name: ")      # enter your first name
status = input("Are you single: ")     # Enter your status

def knowYourProf():
    instructor = input("Enter the prof's name: ")
    subject = input("Enter the subject name: ")
    term = input("Enter the term: ")
    # print(instructor, "will teach", subject, "in", term)
    # print(instructor, "will teach", subject, "in", term, sep='')
    print('{1} will be taught by {0} in {2}'.format(instructor, subject, term))


def whoami():
    if status.lower() == 'y':
        print("Hey, my name is {}, and age {}".format(name, age))
        print("Hey, my name is {n1}, and age {n2}".format(n1=name, n2=age))
        print("Hey, my name is {0}, and age {1}".format(name, age))
    else:
        print("Sorry only stag allowed")


whoami()
knowYourProf()