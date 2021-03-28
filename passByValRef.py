"""
an exercise: create an application that contains two funs: withdraw and deposit
to allow user to take money or deposit a pau cheque. Demo the pass by vlaue vs. pass by ref.
"""


def withdraw(withdraw_amount, account_amount):
    original_amount = account_amount - withdraw_amount
    return original_amount


def deposit(deposit_amount, account_amount):
    original_amount = account_amount + deposit_amount
    return original_amount


if __name__ == '__main__':
    original_amount = 1000;
    money_deposit = float(input("Enter value to deposit :"))
    money_withdraw = float(input("Enter value to withdraw: "))
    print(withdraw(money_withdraw, original_amount))
    print(deposit(money_deposit,original_amount))
    print(original_amount)


