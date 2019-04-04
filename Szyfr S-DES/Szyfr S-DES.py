my_hexdata = input("INPUT (in hex): ")

per1 = [0, 1, 2, 3, 4, 5, 6, 7]
per2 = [1, 5, 2, 0, 3, 7, 4, 6]

kp1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
kp2 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
kp = 1100000011

sl = [0, 1, 2, 3, 4]
sl1 = [1, 2, 3, 4, 0]
sl2 = [2, 3, 4, 0, 1]

per3 = [5, 2, 6, 3, 7, 4, 9, 8]
per4 = [3, 0, 1, 2, 1, 2, 3, 0]

SB1list = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
SB2list = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

per5 = [0, 1, 2, 3]
per6 = [1, 3, 2, 0]

per7 = [3, 0, 2, 4, 6, 1, 7, 5]


def hex_to_bin(hex):
    scale = 16  ## equals to hexadecimal
    num_of_bits = 8
    my_bin = (bin(int(hex, scale))[2:].zfill(num_of_bits))
    my_bin = my_bin + '0' * (((len(my_bin) + 8) - ((len(my_bin) + 8) % 8)) - len(my_bin))
    return my_bin


def bin_to_hex(bin_data):
    return '%0*X' % ((len(bin_data) + 3) // 4, int(bin_data, 2))


def permutation(bit_list, l1, l2):
    l_o = []
    for i in range(len(l2)):
        x = l1[i]
        l_o.append(bit_list[l2[x]])

    return l_o


def slice_(step, text):
    amount_of_slices = int((len(text) / step))
    slices = []
    for i in range(amount_of_slices):
        x = i * step
        slices.append(text[x:x + step])
    return slices


def good_shit(my_bin, l1, l2):
    slices = slice_(8, my_bin)
    perm_list = []
    perm_list_ = []
    perm_list_1 = []
    for i in range(int(len(my_bin) / 8)):
        perm_list.append(permutation(slices[i], l1, l2))
        perm_list_.append(''.join(perm_list[i]))
    perm_list_1.append(''.join(perm_list_))  # na razie nei uzywam bo chce na 8 botach operowac
    return perm_list_


def szyfrowanie_kluczami(t, klucz, runda):
    t1 = t[0:4]
    t2 = t[4:8]

    P4w8_t2_1 = permutation(t2, per1, per4)
    k1 = list(klucz)

    Xor_1 = []
    for i in range(len(k1)):
        if (P4w8_t2_1[i] == k1[i]):
            Xor_1.append(0)
        else:
            Xor_1.append(1)

    Xor_1_1 = Xor_1[0:4]
    Xor_1_2 = Xor_1[4:8]
    SB_ret = f'{sbox(Xor_1_1, SB1list)}{sbox(Xor_1_2, SB2list)}'
    print(f'SBox1: {sbox(Xor_1_1, SB1list)}')
    print(f'SBox2: {sbox(Xor_1_2, SB2list)}')
    P41_ = permutation(SB_ret, per5, per6)
    P41 = ''.join(P41_)

    Xor_2 = []
    for i in range(len(P41)):
        if (P41[i] == t1[i]):
            Xor_2.append('0')
        else:
            Xor_2.append('1')
    Xor_2_ = "".join(Xor_2)

    print(f'klucz rundy {runda}: {bin_to_hex(Xor_2_ + t2)}')

    return Xor_2_ + t2


def sbox(xor, SBl):
    a = xor[0]
    b = xor[1]
    c = xor[2]
    d = xor[3]

    xb1 = int(f'{a}{d}', 2)
    xb2 = int(f'{b}{c}', 2)
    if (SBl[xb1][xb2] == 0):
        return '00'
    elif ((SBl[xb1][xb2]) == 1):
        return '01'
    elif ((SBl[xb1][xb2]) == 2):
        return '10'
    elif ((SBl[xb1][xb2]) == 3):
        return '11'


################################################################


## klucz shit
P_kp = permutation(f'{kp}', kp1, kp2)
P_kp_ = ''.join(P_kp)
kp_sliced = slice_(5, P_kp_)

P_ks = []
P_ks_ = []
for i in range(2):
    P_ks.append(permutation(kp_sliced[i], sl, sl1))
    P_ks_.append(''.join(P_ks[i]))
Pks = P_ks_[0] + P_ks_[1]
print(f'druga permutacja po podzieleniu klucza: {Pks}')
P_4 = permutation(Pks, per1, per3)
Klucz1 = "".join(P_4)
print(f'klucz1 = {Klucz1}')

### k2

SL2_1 = permutation(P_ks_[0], sl, sl2)
SL2_2 = permutation(P_ks_[1], sl, sl2)

SL2_ = SL2_1 + SL2_2
SL2 = ''.join(SL2_)
klucz2_ = permutation(SL2, per1, per3)
klucz2 = ''.join(klucz2_)
print(f'klucz2 = {klucz2}')

################################################################

my_bin = hex_to_bin(my_hexdata)
print(f'tekst w bin : {my_bin}')
perm_list1 = good_shit(my_bin, per1, per2)
print(f'po permutacji wstępnej: {perm_list1}')

print("###########################################################################")

for i in range(int(len(my_bin) / 8)):
    print(f'BAJT : {i + 1}')
    print('\nRUNDA 1:')
    bin_po_klucz1 = szyfrowanie_kluczami(perm_list1[i], Klucz1, 1)  # szyfrowanie kluczem rundy 1
    bin_po_zamianie = bin_po_klucz1[4:] + bin_po_klucz1[:4]
    print('\nRUNDA 2:')
    bin_po_klucz2 = szyfrowanie_kluczami(bin_po_zamianie, klucz2, 2)  # szyfrowanie kluczem rundy 2
    reverse_perm_ = permutation(bin_po_klucz2, per1, per7)
    reverse_perm = ''.join(reverse_perm_)
    print(f'\nszyfrogram : {bin_to_hex(reverse_perm)}')

    print("###########################################################################")
