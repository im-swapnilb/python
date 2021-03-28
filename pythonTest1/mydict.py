
dict1 = {"Name": "Swapnil","Course":"AI & DS","Intake": "Jan21"}
dict2 = {"Laptop": "Mac","Ram":["8GB","16GB"],"chip":["Intel","M1"]}

print(dict1)
print(dict2)
dict1.popitem()
print(dict1)

for i in dict1:
    print("name of key :", i)
    print("value :", dict1.get(i))
