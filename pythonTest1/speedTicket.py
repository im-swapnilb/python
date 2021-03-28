
# Identify if person is getting ticket for speeding

speed = int(input("Enter speed at you were driving"))
zone = input("Enter zone which you were driving")

if (speed > 80) & (zone.lower() == "red"):
    print("Ticket")

elif (speed > 60) & (zone.lower() == "green"):
    print("Ticket")

else:
    print("No ticket")


