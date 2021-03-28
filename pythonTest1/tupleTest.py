
tupletest = ("Swapnil",500186962,"AI&DS","Jan21",True)
fruitSet = {"apple", "banana", "cherry"}

print(tupletest(2))

set1 = {"abc", 34, True, 40, "male"}

thisdict = {
  "StudentName": "Swapnil",
  "Student_Id": 500186962,
  "Course": "AI&DS",
    "Intake": "Jan21",
    "Online": True

}
print(thisdict)


for i in tupletest:
    print(i)

for fruit in fruitSet:
    print(fruit)

for di in thisdict:
    print(di,": ",thisdict[di])