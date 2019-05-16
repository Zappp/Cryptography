#kp = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0]
f = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
m = [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
r = [1, 0, 0, 1, 1]

def string_to_int_list(bin_string):
    output_list = []
    for i in range(len(bin_string)):
        output_list.append(int(bin_string[i]))
    return output_list


def hex_to_bin(hex):
    scale = 16  ## equals to hexadecimal
    num_of_bits = 16
    my_bin = (bin(int(hex, scale))[2:].zfill(num_of_bits))
    return string_to_int_list(my_bin)


def bin_to_hex(bin_data):
    return '%0*X' % ((len(bin_data) + 3) // 4, int(bin_data, 2))

###########################################################################

def text_key_check(text, key):
    while len(key)%16 != 0:
        key.append(0)
    while len(text)%16 != 0:
        text.append(0)

    return text, key



def into4split(list):  # dzieli liste 16 liczb bin na 4 podlisty
    splitted_list = []
    for i in range(4):
        splitted_list.append(list[(4 * i):(4 * i + 4)])
    return splitted_list


def xor(a, b):  # xor 2 wartosci, zwraca jedną po xorze
    if (a == b):
        return 0
    else:
        return 1


def sum16(list1, list2):  # suma (z xorem) 16 liczb w liscie
    sum16_list = []
    for i in range(4):
        for j in range(4):
            sum16_list.append(xor(list1[i][j], list2[i][j]))
    return sum16_list


def SBoxE(x):
    if (x == [0, 0, 0, 0]):
        return [1, 1, 1, 0]
    elif (x == [0, 0, 0, 1]):
        return [0, 1, 0, 0]
    elif (x == [0, 0, 1, 0]):
        return [1, 1, 0, 1]
    elif (x == [0, 0, 1, 1]):
        return [0, 0, 0, 1]
    elif (x == [0, 1, 0, 0]):
        return [0, 0, 1, 0]
    elif (x == [0, 1, 0, 1]):
        return [1, 1, 1, 1]
    elif (x == [0, 1, 1, 0]):
        return [1, 0, 1, 1]
    elif (x == [0, 1, 1, 1]):
        return [1, 0, 0, 0]
    elif (x == [1, 0, 0, 0]):
        return [0, 0, 1, 1]
    elif (x == [1, 0, 0, 1]):
        return [1, 0, 1, 0]
    elif (x == [1, 0, 1, 0]):
        return [0, 1, 1, 0]
    elif (x == [1, 0, 1, 1]):
        return [1, 1, 0, 0]
    elif (x == [1, 1, 0, 0]):
        return [0, 1, 0, 1]
    elif (x == [1, 1, 0, 1]):
        return [1, 0, 0, 1]
    elif (x == [1, 1, 1, 0]):
        return [0, 0, 0, 0]
    elif (x == [1, 1, 1, 1]):
        return [0, 1, 1, 1]


def SBoxD(x):
    if (x == [0, 0, 0, 0]):
        return [1, 1, 1, 0]
    elif (x == [0, 0, 0, 1]):
        return [0, 0, 1, 1]
    elif (x == [0, 0, 1, 0]):
        return [0, 1, 0, 0]
    elif (x == [0, 0, 1, 1]):
        return [1, 0, 0, 0]
    elif (x == [0, 1, 0, 0]):
        return [0, 0, 0, 1]
    elif (x == [0, 1, 0, 1]):
        return [1, 1, 0, 0]
    elif (x == [0, 1, 1, 0]):
        return [1, 0, 1, 0]
    elif (x == [0, 1, 1, 1]):
        return [1, 1, 1, 1]
    elif (x == [1, 0, 0, 0]):
        return [0, 1, 1, 1]
    elif (x == [1, 0, 0, 1]):
        return [1, 1, 0, 1]
    elif (x == [1, 0, 1, 0]):
        return [1, 0, 0, 1]
    elif (x == [1, 0, 1, 1]):
        return [0, 1, 1, 0]
    elif (x == [1, 1, 0, 0]):
        return [1, 0, 1, 1]
    elif (x == [1, 1, 0, 1]):
        return [0, 0, 1, 0]
    elif (x == [1, 1, 1, 0]):
        return [0, 0, 0, 0]
    elif (x == [1, 1, 1, 1]):
        return [0, 1, 0, 1]


def ZK(list):
    list[2], list[3] = list[3], list[2]
    return list


def multi_poly(list1, list2):
    output_list = [0] * 7
    for i in range(4):
        for j in range(4):
            output_list[i + j] += list1[i] * list2[j]
    return output_list


def xor_division(list1, list2):
    while (len(list1) != len(list2)):
        del list1[0]
    else:
        pass

    output_list = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            output_list.append(0)
        else:
            output_list.append(1)
    return output_list


def xor_list(list1, list2):
    output_list = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            output_list.append(0)
        else:
            output_list.append(1)
    return output_list


def devision(list1, list2):
    reminder = []
    while len(list2) <= len(list1) and len(list1) > 0:
        if list1[0] == 1:
            del list1[0]
            for i in range(len(list2) - 1):
                list1[i] = xor(list1[i], list2[i + 1])
            if len(list1) > 0:
                reminder.append(1)
        else:
            del list1[0]
            reminder.append(0)
    # list1 is now output list
    return list1


def multiplication(list1, list2):
    multiplied_list = format(multi_poly(list1, list2))
    output_list = devision(multiplied_list, r)
    return format_reminder(output_list)


def format(list):
    for i in range(len(list)):
        if (list[i] % 2 == 1):
            list[i] = 1
        elif (list[i] % 2 == 0):
            list[i] = 0
    return list


def format_reminder(list):
    format(list)
    r_list = reversed(list)
    while (len(r_list) < 4):
        r_list.append(0)
    return reversed(r_list)


def reversed(list):  # bezuzyteczne, potem wywalic
    reversed_list = []
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list


#############################################################
#############################################################

#  1
print('------------------------')
text = input('hex text: ')
t = hex_to_bin(f'{text}')
print(t)

key = input('hex key: ')
kp = hex_to_bin(f'{key}')

t, kp = text_key_check(t, kp)
print(f'text: {t}')
print(f'key; {kp}')

kp_ = into4split(kp)
t_ = into4split(t)
t1_1 = sum16(kp_, t_)
t1 = into4split(t1_1)
print(t1)

#  2
print('------------------------')
t2 = []
for i in range(4):
    t2.append(SBoxE(t1[i]))
print(t2)

#  3
print('------------------------')
t3 = ZK(t2)
print(t3)

#  4
print('------------------------')
m_ = into4split(m)
t4 = []

t4.append(xor_list(multiplication(m_[0], t3[0]), multiplication(m_[1], t3[2])))
t4.append(xor_list(multiplication(m_[0], t3[1]), multiplication(m_[1], t3[3])))
t4.append(xor_list(multiplication(m_[2], t3[0]), multiplication(m_[3], t3[2])))
t4.append(xor_list(multiplication(m_[2], t3[1]), multiplication(m_[3], t3[3])))
print(t4)

# 5
print('------------------------')
k1 = []
k1_00 = xor_list(kp_[0], SBoxE(kp_[3]))
k1.append(xor_list(k1_00, [0, 0, 0, 1]))
pocket = []
k1.append((xor_list(kp_[2], k1[0])))
k1.append(xor_list(kp_[1], k1[1]))
k1.append(xor_list(kp_[3], k1[2]))
pocket = k1[2]
k1[2] = k1[1]
k1[1] = pocket
print(f'k1: {k1}')
t5_ = sum16(t4, k1)
t5 = into4split(t5_)
print(t5)

# 6
print('------------------------')
t6 = []
for i in range(4):
    t6.append(SBoxE(t5[i]))
print(t6)

# 7
print('------------------------')
t7 = ZK(t6)
print(t7)

# 8
print('------------------------')
k2 = []
k2_00 = xor_list(k1[0], SBoxE(k1[3]))
k2.append(xor_list(k2_00, [0, 0, 1, 0]))
pocket = []
k2.append((xor_list(k1[2], k2[0])))
k2.append(xor_list(k1[1], k2[1]))
k2.append(xor_list(k1[3], k2[2]))
pocket = k2[2]
k2[2] = k2[1]
k2[1] = pocket
print(f'k2: {k2}')
t8_ = sum16(t7, k2)
t8 = into4split(t8_)
print(t8)

# cypher
print('------------------------')
print(t8_)
bin_string = int(''.join(map(str, t8_)))
hex = bin_to_hex(str(bin_string))
print(hex)


print('\n#################################################################\n')
