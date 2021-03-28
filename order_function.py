"""
Order food
"""


def order_bill():
    menu = {'Sandwich': '2$', 'Burger': '4$'}
    order = input("Enter your oder from given menu: ")


if __name__ == '__main__':
    print("Bill data collection :")
    bill_payment = order_bill()
