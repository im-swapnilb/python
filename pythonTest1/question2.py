"""
@Author Karthik_Thallam(500188370) and Swapnil_Bandgar(500186962)
This program will calculate total bill according to your minutes used with using tax and your credit.
"""


def bill_calculation():
    minutes_included = 200
    cost_per_minute_first = 0.25
    cost_per_minute_second = 0.35
    taxes = 13
    extra_cost = 0
    tabs = '\t'
    customer_account_number = int(input("Please enter customer account number : "))
    minutes_used = int(input("Please enter minutes used : "))
    credit = int(input("Please enter credit if you have : "))

    if minutes_used <= minutes_included:
        bill_first = minutes_used * 0.25
        taxes = cost_per_minute_first * 13 / 100
        monthly_bill = bill_first + taxes - credit
    else:
        difference = minutes_used - minutes_included
        bill_first = minutes_included * 0.25
        extra_cost = difference * cost_per_minute_second
        taxes = (bill_first + extra_cost) * 13 / 100
        monthly_bill = bill_first + extra_cost + taxes - credit

    print("customer account number: ", tabs*5, customer_account_number)
    print("Minutes used: ", tabs*8, minutes_used)
    print("Charge for the first 200 minutes@ 0.25: ", tabs, bill_first)
    print("Charge for the remaining minutes@ 0.35: ", tabs, extra_cost)
    print("Taxes: ", tabs*9, taxes)
    print("Credits: ", tabs*9, credit)
    print("Total bill: ", tabs*8, monthly_bill)


if __name__ == '__main__':
    bill_calculation()
