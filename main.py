# AS01

mylist = [1, 5, 2, 7, 8, 3, 6, 9, 4]

for a in range(len(mylist) - 1):
    for i in range(len(mylist) - 1):
        if mylist[i] > mylist[i + 1]:
            hold = mylist[i + 1]
            mylist[i + 1] = mylist[i]
            mylist[i] = hold

print(mylist)
