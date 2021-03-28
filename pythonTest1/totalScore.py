# indentify total score scored


print("Enter three scores")
total_Score = 0;

print("------------------------------------------------")

total_Score += int(input("Enter total score: "))
total_Score += int(input("Enter total score: "))
total_Score += int(input("Enter total score: "))

# calculation
avg_score = round(total_Score/3,1)

print("------------------------------------------------")

print("Total score: ", total_Score, "\n Avg score: ",avg_score)

print("Bye")