"""
Create dict with different key- values and print it
@Author Swapnil_Bandgar, id : 500186962
"""


def bill_calculation(list_months):
    from statistics import mean
    month = "Month"
    past_year = "2019"
    current_year = "2020"
    star = "*"
    saving = "Saving"
    save_bill_list = []
    max_saving = "Max.Saving"
    min_saving = "Min.Saving"
    avg_saving = "Avg.Saving"
    tab = "\t"

    # bill_2019 = [805, 899, 863, 844, 850, 866, 779, 790, 701, 780, 870, 875]
    # bill_2020 = [739, 809, 788, 790, 777, 759, 690, 710, 639, 718, 800, 790]
    #
    # month_bills = {'January': [805, 739], 'February': [899, 809], 'March': [863, 788],
    #                'April': [844, 790], 'May': [850, 777], 'June': [866, 759], 'July': [779, 690],
    #                'August': [790, 710], 'September': [701, 639], 'October': [780, 718],
    #                'November': [870, 800], 'December': [875, 790]}

    print(month, tab*2, past_year, tab*2, current_year, tab*2, saving, tab*2, max_saving, tab*2,
          min_saving, tab*2, avg_saving)
    print(len(month) * star, tab*2, len(past_year) * star, tab*2, len(current_year) * star,
          tab*2, len(saving) * star, tab*2, len(max_saving) * star, tab*2, len(min_saving) * star,
          tab*2, len(avg_saving) * star)

    for key in list_months.keys():
        saved_bill_amount = list_months[key][0] - list_months[key][1]
        list_months[key].append(saved_bill_amount)
        save_bill_list.append(saved_bill_amount)

    avg_save = round(mean(save_bill_list), 2)
    for key in list_months.keys():
        if len(key) > 6:
            space = tab
        else:
            space = tab*2
        if key == 'January':
            print(key, space, list_months[key][0], tab*2, list_months[key][1], tab*2, list_months[key][2],
                  tab*3, max(save_bill_list), tab*4, min(save_bill_list), tab*4, avg_save)
        else:
            print(key, space, list_months[key][0], tab*2, list_months[key][1], tab*2, list_months[key][2])


def bill_data():
    month_list_data = {'January': [], 'February': [], 'March': [], 'April': [], 'May': [],
                       'June': [], 'July': [], 'August': [], 'September': [], 'October': [],
                       'November': [], 'December': []}
    # bill_list = []
    # Taking bill amount as input from user for every month.
    for key in month_list_data:
        print("Enter bill value for the month of :", key)
        bill2019 = int(input("Enter bill amount before go green for year 2019 :"))
        bill2020 = int(input("Enter bill amount after go green for year 2020 :"))
        month_list_data[key].append(bill2019)
        month_list_data[key].append(bill2020)

    print(month_list_data)
    return month_list_data


if __name__ == '__main__':
    print("Bill data collection :")
    month_list = bill_data()
    print("Bill calculation :")
    bill_calculation(month_list)
