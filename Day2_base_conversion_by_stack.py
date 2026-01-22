from Day1_stack import Stack


def baseConversion(num, base):
    """
    Converse decimal number into binary number or vice versa.
    :param num: The number you input.
    :param base: The base you want to converse
    :return: Number after conversing
    """

    s = Stack()
    ans = []
    if base == 2 :
        c = 0
        while num > 0:
            s.push(num % 2)
            num = num // 2
            ans.append(s.pop())
            c += 1


    if base == 10 :
        i = 0
        while num > 0:
            s.push(num % 10)
            num = num // 10
            ans.append(s.pop())
            i += 1

    elif base != 2 and base != 10:
        ans = []

    ans.reverse()
    return ans


if __name__ == '__main__':

    num = int(input())
    base = int(input())
    if baseConversion(num, base):
        print(f"Number after conversing: {baseConversion(num, base)}")

    else:
        print("Something's wrong, please retry.")
