def decimalToBinary(n):
    return "{0:b}".format(int(n))

def Elias_Gamma_Encoding(x):
    bin_x = decimalToBinary(x)
    l = len(bin_x) - 1
    bin_x = l*'0' + bin_x

    return bin_x

def Elias_Gamma_Decoding(x):
    x = list(str(x))
    K = 0
    for i in range(len(x)):
        if x[i] == '1':
            break
        K += 1
    x = x[K:2*K+1]
    x = ''.join(x)
    ans = int(x,2)

    return ans

for i in range(2,21,2):
    encoded = Elias_Gamma_Encoding(i)
    print(f'Elias Gamma Encoding for {i} is ', encoded)
    print(f'Elias Gamma Decoding for {encoded} is ', Elias_Gamma_Decoding(encoded))

print("Pratyush Kumar 19BCE0506")