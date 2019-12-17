numbers = ['1','2','3','4','5','6','7','8','9','0','.','^']
reals = ['1','2','3','4','5','6','7','8','9','0','.']



def contpower(list): #Checks if there are powers. If so, works them out.
    power = False
    for i in range(len(list)):
        num = False
        for x in reals:
            if list[i] == x:
                num = True
        if num == False:
            power = True
            defin = i
    if power == True:
        FA = ''.join(list[0:defin])
        FB = ''.join(list[(defin+1):len(list)])
        return(float(FA)**float(FB))
    else:
        returnval = ''.join(list[0:len(list)])
        return(returnval)

def findparts(strlist): # Seperates a very simple formula into three parts, first number, second number and operator.
    seperators = {}
    operator = '0'
    for i in range(len(strlist)):
        num = False
        for x in numbers:
            if strlist[i] == x:
                num = True
        if num == False:
            operator = strlist[i]
            defin = i
    firstnum = strlist[0:defin]    
    secondnum = strlist[(defin+1):len(strlist)] 
    firstnum = contpower(firstnum) #Checks if there are powers. If so, works them out.
    secondnum = contpower(secondnum) #Checks if there are powers. If so, works them out.
    firstnum = float(firstnum)
    secondnum = float(secondnum)
    return(operator,firstnum,secondnum)


    

def calculate(strlist):
    op,first,second = findparts(strlist)
    if op == '*':
        return(first * second)
    elif op == '/':
        return(first / second)
    elif op == '+':
        return(first + second)
    elif op == '-':
        return(first - second)
    else:
        return('No valid operator')



