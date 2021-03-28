"""
Write a python program that reads 3 grades of a student in a class.
Store the student names , their grades and average in a list
@Authors
    Swapnil Bandgar, id : 500186962
    Urmi Parekh, id : 500186977
    Karthik Thallam, id : 500188370
    Ashish Sharma, id : 500188494
"""
import statistics


def student_grades_calculation():
    grades = []
    # as per program requirement is of 3 we have made it dynamic, so we can enter multiple grades too
    student_subject_count = int(input("Enter number of grades of the student: "))
    # Taking initial ans as yes
    ans = 'y'
    while ans.lower() == 'y':
        student_grades = []
        # Name of the student for which we need grades.
        student_name = input("Enter student name: ")
        # adding student name to list
        grades.append(student_name)
        for x in range(student_subject_count):
            grade = int(input("Enter grade for subject : {} ".format(x)))
            if 0 <= grade <= 100:
                # if grades are between our range add in list
                student_grades.append(grade)
            else:
                print("Please enter grades between 0 to 100")
        # adding grade list to original list
        grades.append(student_grades)
        # checking if all values has entered are not in rage so avg will be 0
        if len(student_grades) > 0:
            # Calculating average and rounding it to 2
            avg = round(statistics.mean(student_grades), 2)
        else:
            avg = 0
        # appending the average to list
        grades.append(avg)
        # printing the grade list with student name
        del student_grades
        # need to check with user if he wants to continue
        ans = input("Do you want to add more students if yes please enter y else enter n : ")
    return grades


if __name__ == '__main__':
    print("student garde calculation program :")
    print("Student withs grades: ", student_grades_calculation())
