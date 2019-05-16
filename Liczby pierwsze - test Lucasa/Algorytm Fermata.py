import math

divisors = []


def step1(a):
    k = 0
    d = 0
    if a % 2 != 0:
        return a
    while d % 1 == 0 and a % 2 == 0:
        d = a / 2
        k += 1
        a = d

    for i in range(k):
        divisors.append(2)

    return d


def step23(d):
    x = math.ceil(math.sqrt(d))
    while True:
        y2 = x ** 2 - d
        y = math.floor(math.sqrt(y2))

        if (y2 == y ** 2):
            d1 = x + y
            d2 = x - y
            if (d2 == 1):
                divisors.append(d)
                break
            else:
                step23(d1)
                step23(d2)
                return divisors
        x += 1

        if (x + y > d):
            break

    return divisors


def removeDuplicates(listofElements):
    uniqueList = []

    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    return uniqueList


d = step1(int(input('a: ')))
step23(d)

divisors.sort()

help_list = []
for i in range(2, divisors[len(divisors) - 1] + 1):
    help_list.append(i)

multiplication = [0] * len(help_list)
for i in range(len(divisors)):
    for j in range(len(help_list)):
        if help_list[j] == divisors[i]:
            multiplication[j] += 1

while 0 in multiplication:
    multiplication.remove(0)

print(removeDuplicates(divisors), multiplication)



