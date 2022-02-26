from math import log
from math import floor
from math import pow

def Binary_Representation_Without_MSB(x):
	binary = "{0:b}".format(int(x))
	binary_without_MSB = binary[1:]
	return binary_without_MSB

def EliasGammaEncode(k):
	if (k == 0):
		return '0'
	N = 1 + floor(log(k, 2))
	Unary = (N-1)*'0'+'1'
	return Unary + Binary_Representation_Without_MSB(k)

def EliasDeltaEncode(x):
	Gamma = EliasGammaEncode(1 + floor(log(x, 2)))
	binary_without_MSB = Binary_Representation_Without_MSB(x)
	return Gamma+binary_without_MSB

def Elias_Delta_Decoding(x):
	x = list(x)
	L=0
	while True:
		if not x[L] == '0':
			break
		L= L + 1
	
	# Reading L more bits and dropping ALL
	x = x[2 * L +1:]
	
	# Prepending with 1 in MSB
	x.insert(0,'1')
	x.reverse()
	n=0
	
	# Converting binary to integer
	for i in range(len(x)):
		if x[i]=='1':
			n = n + pow(2,i)
	return int(n)

for i in range(2,21,2):
    elias_delta_encoding = EliasDeltaEncode(i)
    print(f'Elias Delta encoding for {i} is ', elias_delta_encoding)
    elias_delta_decoding = Elias_Delta_Decoding(elias_delta_encoding)
    print(f'Elias Delta Decoding for {elias_delta_encoding} is ', elias_delta_decoding)

print("Pratyush Kumar 19BCE0506")