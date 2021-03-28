'''

Write a python program that will take in basic information from a student, including student name, degree name, number of credits taken so far, and the total number of credits required in the degree program. The program will then calculate how many credits are needed to graduate. Display should include the student name, the degree name, and credits left to graduate.
Write two print statements in this program. In the first one, use .format method with pre-specified order of the displayed outputs.
'''

def student_Info():
    print("Please enter below details :")
    student_Name = input("Please enter your name : ")
    degree_Name = input("Please enter your degree : ")
    credit_Taken = int(input("Please enter credit taken so far: "))
    total_Credit = int(input("Please enter total number of credits required: "))
    credit_required = int(input("Please enter number of credits needed to graduate: "))
    print('Student name: {0}\ndegree_Name: {1}\ncredit_Taken : {2}\ntotal_Credit: {3}\ncredit_required: {4}'.format(
        student_Name, degree_Name, credit_Taken, total_Credit, credit_required))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('here you go for assignment')
    student_Info()
