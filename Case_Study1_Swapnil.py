"""
Problem statement :
Last year, a local college implemented rooftop gardens as a way to promote energy efficiency and
save money. Write a program that will allow the user to enter the energy bills from January to December
for the year prior to going green. Next, allow the user to enter the energy bills from January to
December of the past year after going green.
@Authors
    Swapnil Bandgar, id : 500186962
    Urmi Parekh, id : 500186977
    Karthik Thallam, id : 500188370
    Ashish Sharma, id : 500188494
"""
from statistics import mean


def bill_calculation(list_months):
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

    # Defining heading of the table and printing it
    print(month, tab * 2, past_year, tab * 2, current_year, tab * 2, saving, tab * 2, max_saving, tab * 2,
          min_saving, tab * 2, avg_saving)

    # Printing stars
    print(len(month) * star, tab * 2, len(past_year) * star, tab * 2, len(current_year) * star,
          tab * 2, len(saving) * star, tab * 2, len(max_saving) * star, tab * 2, len(min_saving) * star,
          tab * 2, len(avg_saving) * star)

    # Creating list for containing difference between two years bills
    for key in list_months.keys():
        # Calculating difference between 2020 and 2019
        saved_bill_amount = list_months[key][0] - list_months[key][1]

        # Appending difference amount to dictionary as a 3rd value of a key
        list_months[key].append(saved_bill_amount)

        # Storing difference amount in the list
        save_bill_list.append(saved_bill_amount)

    # Calculating average amount of saving
    avg_save = round(mean(save_bill_list), 2)

    # Displaying the data month wise
    for key in list_months.keys():
        if len(key) > 6:
            space = tab
        else:
            space = tab * 2
        if key == 'January':
            print("%s" % key, space, "%d" % list_months[key][0], tab * 2, "%d" % list_months[key][1], tab * 2,
                  "%d" % list_months[key][2],
                  tab * 3, "%d" % max(save_bill_list), tab * 4, "%d" % min(save_bill_list), tab * 4, "%d" % avg_save)
        else:
            print("%s" % key, space, "%d" % list_months[key][0], tab * 2, "%d" % list_months[key][1], tab * 2,
                  "%d" % list_months[key][2])


def bill_data():
    # Declaring the dictionary for containing the information of cost month wise
    month_list_data = {'January': [], 'February': [], 'March': [], 'April': [], 'May': [],
                       'June': [], 'July': [], 'August': [], 'September': [], 'October': [],
                       'November': [], 'December': []}

    #  Taking inputs from users for energy bills of prior and after years of going green
    for key in month_list_data:
        print("Enter bill value for the month of : ", key)
        bill2019 = int(input("Enter bill amount before go green for year 2019 : "))
        bill2020 = int(input("Enter bill amount after go green for year 2020 : "))
        month_list_data[key].append(bill2019)
        month_list_data[key].append(bill2020)

    print("\n\n\n\n")
    return month_list_data


if __name__ == '__main__':
    print("Bill data collection :")
    month_list = bill_data()
    print("Bill calculation :\n")
    bill_calculation(month_list)
