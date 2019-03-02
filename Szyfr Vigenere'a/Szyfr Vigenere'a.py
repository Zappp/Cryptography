import itertools


def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()


def alphabet_position(text):
    nums = [str(ord(x) - 97) for x in text.lower() if x >= 'a' and x <= 'z']
    return " ".join(nums)


def times_letter(new_n):  # amount of each letter in a cipher
    each_letter = [0] * len(alphabet)
    for i in range(len(alphabet)):
        for j in range(len(new_n)):
            if alphabet[i] == new_n[j]:
                each_letter[i] += 1
    return each_letter


def column(n, x):  # splitting text into columnes
    new_n = []
    y = int(len(n))
    j = 0

    for i in range(0, y, x):
        new_n.append(n[i])
        n[i] = None

    while j < y:
        if n[j] == None:
            n.remove(n[j])
            y -= 1
        j += 1
    return n, new_n


def Ic(each_letter, new_n):
    N = len(new_n)
    x = 0
    for i in range(len(each_letter)):
        x += (each_letter[i] ** 2 - each_letter[i])
    I = x / (N ** 2 - N)
    return I


def col_size(a, i):
    x = 0
    for j in range(len(a[i])):
        x += a[i][j]
    return x


def combination(d):
    comb = [0] * d
    for i in range(d):
        comb[i] = i
    comb_output = list(itertools.permutations(comb, 2))
    return comb_output


def IMc(a, k, i):
    N0 = col_size(a, k)
    N1 = col_size(a, i)

    x = 0
    for j in range(len(alphabet)):
        x += a[k][j] * a[i][j]

    return x / (N0 * N1)


#################################################################################

text = open('tekst.txt').read()
klucz = input('Podaj klucz: ')

listaT = alphabet_position(text)
listaT = listaT.split(' ')
listaT = [int(i) for i in listaT]

listaK1 = alphabet_position(klucz)
listaK1 = listaK1.split(' ')
listaK1 = [int(i) for i in listaK1]

N = len(listaT)  # lenght of a text list
d = len(listaK1)  # lenght of key list
w = int(N / d)  # amount of whole parts of text
z = N % d  # amount of parts left after division

listaK2 = []  # list of parts left after devision
for i in range(z):
    listaK2.append(listaK1[i])
listaK3 = listaK1 * w + listaK2  # finall lenght of a key

listaSz1 = [None] * N
n = [None] * N
for i in range(N):
    listaSz1[i] = chr((listaT[i] + listaK3[i] + 26) % 26 + 97)
    n[i] = ((listaT[i] + listaK3[i] + 26) % 26)  # same list but filled with ints

listaSz2 = ''.join(listaSz1)
save('NEIotwierajToTAJNE_KODY!!!!!!', listaSz2)

#################################################################################

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet_position(alphabet)
alphabet = alphabet.split(' ')
alphabet = [int(i) for i in alphabet]  # gives alphabet in list of ints

c = d = int(input('Podaj ilość kolumn: '))
i = 0
a = []  # how many times each letter occured in every column (list of c lists)
b = [0] * c  # text in column in ints
h = []  # help list to store data from while loop

while c > 0:
    n, new_n = column(n, c)
    each_letter = times_letter(new_n)
    a.append(each_letter)
    b[i] = new_n
    print(f'Ic(column {i}) = {Ic(each_letter, new_n)}')
    c -= 1
    i += 1

#################################################################################

for i in range(len(combination(d))):
    x = combination(d)[i]
    y1, y2 = x[0], x[1]
    print(f'IMc(column [{x[0]} and {x[1]}]) = {IMc(a, y1, y2)}')
