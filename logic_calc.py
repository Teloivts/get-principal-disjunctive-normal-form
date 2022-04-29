import copy
def priority(x):
    if x == '(':
        return -2
    if x == ')':
        return -1
    if x == '!':
        return 5
    if x == '&':
        return 4
    if x == '|':
        return 3
    if x == '>':
        return 2
    if x == '-':
        return 1
    return 0
def op(x,y,z):
    if(x=='&'):
        return y&z
    if(x=='|'):
        return y|z
    if(x=='!'):
        return y^1
    if(x=='>'):
        if(y==1 and z==0):
            return 0
        return 1
    if(x=='-'):
        if(y==z):
            return 1
        return 0
def logic(x,y,z):
    if len(x)==len(y):
        z.append(copy.deepcopy(x))
    for a in x:
        if not(a in y):
            y.append(a)
            x[a]=0
            logic(x,y,z)
            x[a]=1
            logic(x,y,z)
            y.pop()
            return 
def show(x):
    ans = ''
    for a in x:
        if x[a]==1:
            ans += a+'∧ '
        else:
            ans += '┐'+a+'∧ '
    #print('('+ans[:-2]+')')
    return ('('+ans[:-2]+')')
def calc(x,y):
    op_stack =[]
    num_stack =[]
    for a in x:    
        if(priority(a)==0):
            num_stack.append(y[a])
        elif(priority(a)==-2):
            op_stack.append(a)
        elif(priority(a)==-1):
            while True:
                temp = op_stack.pop()
                if(temp=='('):
                    break
                else:
                    if temp == '!':
                        num1 = num_stack.pop()
                        num_stack.append(op(temp,num1,0))
                        continue
                    num1 = num_stack.pop()
                    num2 = num_stack.pop()
                    num_stack.append(op(temp,num1,num2))
        else:
            while True:
                if op_stack==[]:
                    op_stack.append(a)
                    break
                temp = op_stack.pop()
                if(priority(temp)<=priority(a)):
                    op_stack.append(temp)
                    op_stack.append(a)
                    break
                else:
                    if temp == '!':
                        num1 = num_stack.pop()
                        num_stack.append(op(temp,num1,0))
                        continue
                    num1 = num_stack.pop()
                    num2 = num_stack.pop()
                    num_stack.append(op(temp,num1,num2))
        #print(op_stack,end='')
        #print(num_stack)    
    #print(op_stack,end='')
    while(not op_stack==[]):
        temp = op_stack.pop()
        if temp == '(':
            pass
        if temp == '!':
            num1 = num_stack.pop()
            num_stack.append(op(temp,num1,0))
            continue
        num1 = num_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(op(temp,num1,num2))
    if num_stack[0]:
        return show(y)+'∨ '
    return ''     
def main():
    table = {}
    truth_table = []
    print('请输入你的命题公式,!为非，&为合取,|为析取,>为蕴涵,-为等价')
    #data = '('+input()+')'
    data = input()
    for a in data:
        if (ord(a)>=ord('A') and ord(a)<=ord('Z')):
            table[a]=0
    logic(table,[],truth_table)
    #print(truth_table)
    ans = ''
    for a in truth_table:
        ans += calc(data,a)
    if((len(ans)==0)):
        print('这是矛盾式，没有主析取范式')
    else:
        print('你的主析取范式:'+ans[:-2])
if __name__ == '__main__':
    main()