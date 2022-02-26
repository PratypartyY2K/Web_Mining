# Python3 implementation
import math

log2 = lambda x: math.log(x, 2)

def Unary(x):
	return (x-1)*'0'+'1'

def Binary(x, l = 1):
	s = '{0:0%db}' % l
	return s.format(x)
	
def Elias_Gamma(x):
	if(x == 0):
		return '0'

	n = 1 + int(log2(x))
	b = x - 2**(int(log2(x)))

	l = int(log2(x))

	return Unary(n) + Binary(b, l)

def Elias_Gamma_Decoding(x):
    x = list(x)
    K = 0
    while True:
        if not x[K] == '0':
            break
        K = K + 1
      
    # Reading K more bits from '1'
    x = x[K:2*K+1]
  
    n = 0
    x.reverse()
      
    # Converting binary to integer
    for i in range(len(x)):
        if x[i] == '1':
            n = n+math.pow(2, i)
    return int(n)

for i in range(2,21,2):
    encoded = Elias_Gamma(i)
    print(f'Elias Gamma Encoding for {i} is ', encoded)
    print(f'Elias Gamma Decoding for f{encoded} is ', Elias_Gamma_Decoding(encoded))

print("Pratyush Kumar 19BCE0506")