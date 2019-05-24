import math


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


def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]


S = new_list(100000)
i = int(input('i: ')) - 1
j = int(input('j: ')) - 1

S2 = get_prime_numbers(S)
print(S2[i], S2[j])
