myStr2 = "yytorxontytoyinsrrbexazutizfulz"
# using string slicing yuor program should
#output (Toronto is Beautiful)
myStr3 = myStr2[2::]
mystr4=myStr2.replace('y',' ')

print(mystr4.replace('x',' '))

print(myStr3[::1])

myStr2 = "yytorxontytoyinsrrbexazutizfulz"
print(myStr2[2:5].capitalize()+ myStr2[6:9] + myStr2[11:12] + " "+ myStr2[13:14].capitalize() + myStr2[15:16] + " " + myStr2[18:20].capitalize() + myStr2[21:22] + myStr2[23:26] + myStr2[27:30])