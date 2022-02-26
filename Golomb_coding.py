import math

def unary(x):
	return (x-1)*'0'+'1'

def decimalToBinary(n):
    return "{0:b}".format(int(n))

def code(num, x):
    num = str(num)
    num_bin = decimalToBinary(num)
    num_bin = (x-len(num_bin))*'0' + num_bin
    return num_bin

def encoding(x, b = 10):
    q = math.floor(x/b)

    un = unary(q+1)

    i = math.floor(math.log(b,2))
    d = math.pow(2,i+1) - b

    r = x - q*b

    if r<d:
        # code r using i bits
        r_new = code(r,i)
        ans = un + r_new

    if r>=d:
        #code r+(2^i+1)-b using i+1 bits
        r_new = code(r + int(math.pow(2,i+1)) - b, i+1)
        ans = un + r_new
    
    return ans

def decoding(x, b=10):
    x = list(x)
    for pos in range(len(x)):
        if x[pos] == '1':
            q = pos
            break

    i = math.floor(math.log(b,2))
    d = math.pow(2,i+1) - b

    r_extract = []
    for ex in range(q+1, q+i+1):
        r_extract.append(x[ex])
    case_2 = r_extract.copy()

    r_extract = ''.join(r_extract)
    r = int(r_extract,2)

    if r>=d:
        case_2.append(x[ex+1])
        case_2 = ''.join(case_2)
        r = int(case_2,2) - d
    x = q*b + r
    return int(x)

for i in range(2,21,2):
    golomb_encoding = encoding(i)
    print(f'Golomb encoding of {i} is ', golomb_encoding)
    print(f'Golomb decoding of {golomb_encoding} is ', decoding(golomb_encoding))

print("Pratyush Kumar 19BCE0506")