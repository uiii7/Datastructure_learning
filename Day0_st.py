char1 = input()
char2 = input()
ls = []
# test

def ifchange() -> bool:
    """
    变位词判断
    假设两词长度相等

    :return: 判断结果（True or False）
    """
    for i in range(len(char1)):
        s1 = char1[i]
        for j in range(len(char2)):
            s2 = char2[j]
            if s1 == s2:
                s1 = None
                ls.append(1)

    if len(ls) == len(char1):
        return True
    return False


def ifchange_sort() -> bool:
    """
    变位词判断
    假设两词长度相等

    :return: 判断结果（True or False）
    """
    ls1 = list(char1)
    ls2 = list(char2)
    ls1.sort()
    ls2.sort()
    return ls1 == ls2


print(ifchange())
print(ifchange_sort())