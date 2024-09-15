def stringbreak(list, n):
    while len(list)%n != 0:
        list.append(0)
    listolists = []
    while bool(list) != False:
        minilist = []
        for i in range(n):
            minilist.append(list.pop(0))
        listolists.append(minilist)
    return(listolists)

# print(stringbreak([1,2,3,4,5,6]))


