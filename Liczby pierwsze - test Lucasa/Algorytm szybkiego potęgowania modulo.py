def my_bin(x):
    bin_v1 = bin(x)
    bin_v2 = bin_v1[2:]

    bin_l1 = []
    for i in range(len(bin_v2)):
        bin_l1.append(int(bin_v2[i]))

    bin_l2 = []
    for i in range(len(bin_l1) - 1, -1, -1):
        bin_l2.append(bin_l1[i])

    return bin_l2


def pow_hf(v, x, mod_v):
    pow_hl = [v % mod_v]
    for i in range(len(x) - 1):
        pow_hl.append((pow_hl[i] ** 2) % mod_v)

    for i in range(len(x)):
        if x[i] == 0:
            pow_hl[i] = 1

    val = 1
    for i in range(len(x)):
        val *= pow_hl[i]

    return val % mod_v


print('= ', pow_hf(int(input('a: ')), my_bin(int(input('b: '))), int(input('c: '))))
