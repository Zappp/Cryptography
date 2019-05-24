r_list = []
x_list = []
y_list = []

def nwd(a, b, x1=1, x2=0, y1=0, y2=1):

    if b == 0:
        return r_list[len(r_list) - 2], x1, y1

    q = int(a / b)
    r = a - q * b
    r_list.append(r)
    x_list.append(x2)
    y_list.append(y2)


    return nwd(b, r, x2, x1 - x2 * q, y2, y1 - y2 * q)


a = int(input('a: '))
b = int(input('b: '))

r, x, y = nwd(a, b)
del r_list[len(r_list) - 1]
del x_list[0]
del y_list[0]

for i in range(len(r_list)):
    print(f'r{i + 1} = {r_list[i]} | x{i + 1} = {x_list[i]} | y{i + 1} = {y_list[i]}')


print(f'NWD({a},{b}) = {r}')
