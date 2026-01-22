from Day1_stack import Stack


#表达式括号匹配
parleft = '('
parright = ')'

def parCheck(s) -> bool:
    s1 = Stack()
    s2 = Stack()
    for par in s:
        if par == parleft:
            s1.push(par)
        elif par == parright:
            s2.push(par)

    return s1.size() == s2.size()

s = "(1(34(56)7)abc)"
print(parCheck(s))