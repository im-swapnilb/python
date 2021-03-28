
# shuffle a tuple
import random

tup = (1, 2, 3, 4, 5)
test_list = [1, 4, 5, 6, 3]
print("The original tuple is : " , tup)
print("The original list is : " , test_list)




# Printing shuffled tuple and list
random.sample(tup, len(tup))
random.shuffle(test_list)

print("New shuffled tuple :", tup)
print ("The shuffled list is : " ,  test_list)
