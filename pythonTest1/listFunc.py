#
# mylist = ['Swapnil',500186962,'Loyalist','Jan21']
#
# for i in mylist:
#     print(i)
#     if mylist.__contains__('Jan21'):
#         print("he is %s student".format(mylist[3]))


comlab = ['hp','Dell','Apple','Asus']


server = 'lenovo'

if server in comlab:
    print("Its already there")
    print(comlab)
else:

    comlab.append(server)
    print("Server added")
    print(comlab)

## Server added
##['hp', 'Dell', 'Apple', 'Asus', 'lenovo']