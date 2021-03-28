"""
This program will used to identify user will get loan or not and his total payment.
@Author Swapnil_Bandgar, Student_id : 500186962

"""


def score(cust_score):
    approval = False
    if cust_score >= 750:
        approval = True
    return approval


def loanCalculator(cust_loan_type="personal", tenure=10, amount=0):
    total_payment = 0
    if cust_loan_type.lower() == "personal":
        interest = 11.25
        total_payment = float(tenure) * (interest/100) * amount
        print(float(total_payment))
        print("Total Payable amount for {} loan : {}".format(cust_loan_type, total_payment))
    elif cust_loan_type.lower() == "car":
        interest = 6.25
        total_payment = float(tenure) * (interest/100) * amount
        print("Total Payable amount for {} loan : {}".format(cust_loan_type, total_payment))
    elif cust_loan_type.lower() == "home":
        interest = 7.25
        total_payment = float(tenure) * (interest/100) * amount
        print("Total Payable amount for {} loan : {}".format(cust_loan_type, total_payment))
    else:
        print("invalid {%s} loan type, please enter correct loan type" % cust_loan_type)
    return total_payment


if __name__ == '__main__':
    print("Loan amount calculation ")
    score_number = float(input("Enter your cibil score: "))
    if score(score_number):
        loan_type = input("Enter loan type as car, home, personal as per your requirement: ")
        loan_duration = int(input("Enter tenure of your loan amount: "))
        loan_amount = float(input("Enter amount you need as loan: "))
        total_payable = loanCalculator(loan_type, loan_duration, loan_amount)
    else:
        print("Sorry your cibil {} is low, please try next time ".format(score_number))
