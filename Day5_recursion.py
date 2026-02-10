def listsum(num):
    if len(num) == 1:
        return num[0]
    return num[0] + listsum(num[1:])


def toStr(num, base):
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]

    else:
        return toStr(num // base, base) + convertString[num % base]


def MoveDisk(disk, fromPole, toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")


def Hanoi(n,fromPole, withPole, toPole):
    if n > 0:
        Hanoi(n-1, fromPole, toPole, withPole)
        MoveDisk(n, fromPole, toPole)
        Hanoi(n-1, withPole, fromPole, toPole)




