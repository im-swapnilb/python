import random
import copy

def list_kwldge_check():
    list_check = ['Swapnil', 13, 5, 1992, 'Loyalist']
    list_append = ['Canada', 'Toronto']

    list_check.append(list_append)
    print("Append list :", list_check)
    list_check[1] = 'March'
    print("inserted list :", list_check)
    print("Index of list :", list_check.index(['Canada', 'Toronto']))
    list_check.remove(5)
    print("Element removed list: ", list_check)
    list_check.pop(2)
    print("list after pop: ", list_check)
    return list_check


def list_operations(list_get):
    print("received list :", list_get)
    print("Count of loyalist", list_get.count('Loyalist'))
    print("reverse of list", list_get.reverse())
    print("reverse of list", list_get)
    list_get.pop(0)
    list_get.sort()
    print("sorted of list", list_get)
    print("max of list", max(list_get))
    print("min of list", min(list_get))
    print("choice of list", random.choice(list_get))
    print("shuffle of list", random.shuffle(list_get))
    print("deepcopy of list", copy.deepcopy(list_get))


if __name__ == '__main__':
    print('here you go for assignment')
    list_new = list_kwldge_check()
    print("Final list is: ", list_new)
    list_operations(list_new)
