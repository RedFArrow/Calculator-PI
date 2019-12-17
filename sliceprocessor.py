def mainpro(brackets,l):
    x = {}
    y = 0
    for i in brackets:
        first = ((int(i))+1)
        second = int(brackets[i])
        x[y] = (l[first:second])
        y += 1
    return(x)