def alphanum(string):
    finallist = []
    for char in string:
        finallist.append(ord(char))
    return(finallist)

def numalpha(listslist):
    numlist = []
    alphlist = []
    for minilist in listslist:
        for char in minilist:
            numlist.append(char)
    for char in numlist:
        char = int(char)
        char = chr(char)
        alphlist.append(char)
    alphlist = "".join(alphlist)
    return(alphlist)