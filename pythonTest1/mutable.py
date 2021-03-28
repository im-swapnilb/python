
comlab = ['hp','Dell','Apple','Asus']

print(comlab)
print('Address of comlab is: {}'.format(id(comlab)))
## ['hp', 'Dell', 'Apple', 'Asus']
## Address of comlab is: 2500368814600

comlab[0] = 'lenovo'
print(comlab)
print('Address of comlab is: {}'.format(id(comlab)))

## ['lenovo', 'Dell', 'Apple', 'Asus']
## Address of comlab is: 2500368814600



print(comlab)
#['lenovo', 'Dell', 'Apple', 'Asus']
print(id(comlab[0]))
#1836208447664
comlab[0] = 'MSI'
print(comlab)
#['MSI', 'Dell', 'Apple', 'Asus']
print(id(comlab[0]))
#1836208696240
