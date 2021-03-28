
student_name = input("Please enter your name:")
# degree_name = input("Please enter your degree name:")
# credit_taken = int(input("Please enter how many credits you have earned:"))
# total_credits = int(input("Please enter how many total credits are required:"))
# required_credits = int(total_credits - credit_taken)
tabs = '\t'*7
print("name ", tabs,  student_name)


print("Student name:\t " + '%s'.expandtabs(10) % student_name )

# print("Student name: {:>30} ".format(student_name) + "\nDegree name: {:>30} ".format(degree_name) +
#       "\nCredit taken so far: {:>22} ".format(credit_taken) +
#       "\nTotal number of credits required: {:>9} ".format(
#     total_credits) + "\nNumber of credits needed to graduate: {:>5} ".format(required_credits))
#
# print("Student name:\t\t\t\t\t\t\t " + '%s' % student_name + "\nDegree name:\t\t\t\t\t\t\t " +
#       '%s' % degree_name +
#       "\nCredit taken so far:\t\t\t\t\t " + '%d' % credit_taken + "\nTotal number of credits required:\t\t " +
#       '%d' % total_credits
#       + "\nNumber of credits needed to graduate:\t " + '%d' % required_credits)
