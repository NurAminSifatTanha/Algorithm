open_brackets = ['[','{','(']
close_brackets = [']','}',')']

def Balance_check(CheckString):
    stack =[]
    for i in CheckString:dc
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = CheckString.index(i)
            if len(stack)>0 and (open_brackets[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return 'Unbalance'
    if len(stack)==0:
        return "Balance"
    else:
        return 'Not balance'
if __name__=="__main__":
    print(Balance_check("()()("))