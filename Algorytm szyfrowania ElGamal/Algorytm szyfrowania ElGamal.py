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


def new_list(p):
    S = []
    for i in range(2, p + 1):
        S.append(i)
    return S


def get_prime_numbers(list_S):
    i = 0
    j = len(list_S) - 1

    while list_S[i] < math.sqrt(list_S[j]):

        for k in range(j, i + 1, - 1):
            if list_S[k] % list_S[i] == 0:
                del list_S[k]
                j -= 1
        i += 1

    return list_S


while True:

    S = new_list(100000)
    S2 = get_prime_numbers(S)
    n = int(input('n: '))  # getting prime

    if n <= 0:
        print('Error: value must be positive.')
        break

    if n not in S2:
        print('Error: value not prime number.')
        break

    # start of searching the divisors

    d = step1(n - 1)
    step23(d)

    divisors.sort()

    help_list = []
    for i in range(2, int(divisors[len(divisors) - 1] + 1)):
        help_list.append(i)

    multiplication = [0] * len(help_list)
    for i in range(len(divisors)):
        for j in range(len(help_list)):
            if help_list[j] == divisors[i]:
                multiplication[j] += 1

    while 0 in multiplication:
        multiplication.remove(0)

    divisors2 = removeDuplicates(divisors)
    if len(divisors2) != len(multiplication):
        del divisors2[0]

    # end od searching the divisors

    r = int(input('r: '))

    if r <= 1 or r >= n - 1:
        print('Error: r not in appropriate interval')
        break

    cond = 0
    for i in range(len(divisors2)):
        if pow(r, int((n - 1) / divisors2[i]), n) == 1:
            cond = 1
            break

    if cond == 1:
        print('Error: r mod n = 1')
        break

    k = int(input('k: '))

    if k <= 1 or k >= n - 1:
        print('Error: k not in appropriate interval')
        break

    a = pow(r, k, n)
    print(f'public key: {n, r, a}')

    j = int(input('j: '))

    if j <= 1 or j >= n - 1:
        print('Error: j not in appropriate interval')

    t = int(input('t: '))

    if t <= 0:
        print('Error: t must be positive')
        break

    c1 = pow(r, j, n)
    c2 = (t * pow(a, j)) % n
    print(f'cypher: {c1, c2}')

    t_od = (c2 * pow(c1, n - 1 - k)) % n
    print(f't_decrypted: {t_od}')

    print('\t#######################################\t')
