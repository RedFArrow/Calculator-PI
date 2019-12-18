def main(ans,operators): #ans is a list of numbers. [1,4,6,7,8] of any length, operators is a list of operators ['+','-','*']
    total = 0
    print(ans)
    for i in range(0,(len(operators))):
        if i == 0:
            if operators[i] == '+':
                print(ans[i])
                total = (ans[i]) + (ans[i+1])
            elif operators[i] == '-':
                total = (ans[i]-ans[i+1])
            elif operators[i] == '*':
                total = (ans[i]*ans[i+1])
            elif operators[i] == '/':
                total = (ans[i]/ans[i+1])
            else:
                print('no')
        else:
            if operators[i] == '+':
                total = total + ans[i]
            elif operators[i] == '-':
                total = total - ans[i]
            elif operators[i] == '*':
                total = total * ans[i]
            elif operators[i] == '/':
                total = total / ans[i]
            else:
                print('no')
    return(total)