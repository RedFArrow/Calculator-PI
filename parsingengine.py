numbers = ['1','2','3','4','5','6','7','8','9','0','.']
import sliceprocessor

def sepbyint(strlist):
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
    firstnum  = join(strlist[0:defin])
    secondnum = join(strlist[defin:len(strlist)])

    ##okay so now i need to combine all the first numbers into one value, all the second numbers into another value. easy right?
    return('hi')

def pairbrackets(f,s):
    brackets = {}
    for i in range(0,len(f)):
        brackets[f[i]] = s[i]
    return brackets

def bracketparcing(string):
    firstbrackets = []
    secondbrackets = []
    for i in range(0,(len(string))):
        if string[i] == '(':
            firstbrackets.append(i)
        elif string[i] == ')':
            secondbrackets.append(i)
    if len(firstbrackets) != len(secondbrackets):
        print('SYNTAX ERROR. MISSING BRACKETS.')
    else:
        brackets = pairbrackets(firstbrackets,secondbrackets)
    #okay so at this point, we have a dictionary which gives the location of all the brackets. Now we just need to seperate those brackets, while still keeping the seperate operators.
            
    return(brackets,string)

            

def space_removal(strlist):
    templist = []
    len(strlist)
    for i in range(len(strlist)):
        if strlist[i] == ' ':
            templist.append(i)
    for i in reversed(templist):
        del strlist[i]
    return(strlist)

def parsingengine(string):
    string = list(string) #Converts the input to a list
    string = space_removal(string) #removes any spaces from the list
    ##----------------#before this next part, it program needs to automatically add brackets in the correct locations.
    s1,s2 = bracketparcing(string) #Finds brackets in string
    bracketstring = sliceprocessor.mainpro(s1,s2) #Returns the bracketed sections in seperate dictionary values. [In]
    pprint(bracketstring)
    return('end')