import math


def nwd(a, b, x1=1, x2=0, y1=0, y2=1):
    if b == 0:
        return x1

    q = int(a / b)
    r = a - q * b
    return nwd(b, r, x2, x1 - x2 * q, y2, y1 - y2 * q)


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



S = new_list(100000)
S2 = get_prime_numbers(S)

i = int(input('i: ')) - 1
j = int(input('j: ')) - 1
e = int(input('e: '))
t = int(input('t: '))

p, q = S2[i], S2[j]
n = p * q
m = (p - 1) * (q - 1)
x = nwd(e, m)
while x < 0:
    x += m
d = x
s = pow(t, e, n)
t_ = pow(s, d, n)
print(f'public key: {n, e}')
print(f'private key: {n, d}')
