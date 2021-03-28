
print("The miles per gallon program")

miles_Driven = float(input("Enter miles driven"))
gallon_Used = float(input("Enter gallon used"))


# calculation and round miles per gallon

mpg = miles_Driven/gallon_Used
mpg = round(mpg,2)

print("Miles per gallon ",(mpg),"\n Bye")

