"""
This program will cover different parameters function and loops  for different datatypes and calculate
cost of apartment depending on requirement.
@Author Swapnil_Bandgar, Student_id : 500186962

"""


def costCalculation(bed_required, area_required, facing_required):
    sqrt_price_gardan = 500
    sqrt_price = 400
    if facing_required.lower() == 'yes':
        price = sqrt_price_gardan * area_required * bed_required
        print("{} bedroom apartment with garden facing will cost you : {} $".format(bed_required, price))
    elif facing_required.lower() == 'no':
        price = sqrt_price_gardan * area_required * bed_required
        print("{} bedroom apartment without garden facing will cost you : {} $".format(bed_required, price))
    else:
        print("I am not looking for apartment or I have not entered apartment facing requirement")


if __name__ == '__main__':
    print("here you go for calculating your apartment price")
    bed = int(input("Enter number of bedrooms required : "))
    area = float(input("Enter area required for apartment : "))
    facing = input("Do you need garden facing apartment : ")
    costCalculation(bed, area, facing)
