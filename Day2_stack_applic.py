from Day1_stack import Stack


#表达式括号匹配
parleft = '('
parright = ')'
operation = {}

def parCheck(s) -> bool:
    s1 = Stack()
    s2 = Stack()
    for par in s:
        if par == parleft:
            s1.push(par)
        elif par == parright:
            s2.push(par)

    return s1.size() == s2.size()

def expressionTrans(s) -> str:
    operation['+'] = operation['-'] = 1
    operation['*'] = operation['/'] = 2
    s1 = Stack()
    s = list(s)
    ls = []
    for par in s:
        if par in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or par in "0123456789":
            ls.append(par)
        elif par == parleft:
            s1.push(par)
        elif par == parright:
            t = s1.pop()
            while par != parleft:
                ls.append(t)
                t = s1.pop()
        else:
            while (not s1.isEmpty()) and \
                    (operation[s1.peek()] >= operation[par]):
                ls.append(s1.pop())
            s1.push(par)
    while not s1.isEmpty():
        ls.append(s1.pop())
    return "".join(ls)

s2 = input()
print(expressionTrans(s2))

# s = "(1(34(56)7)abc)"
# print(parCheck(s))