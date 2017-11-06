import sys

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
def encode_binary_string(s):
    return ''.join([bin(ord(c))[2:].rjust(8,'0') for c in st])
def invertir(s):
        return a[::-1]

f = open("texto.txt", "rb")
st=f.read()

x=encode_binary_string(st)
f= open("text.txt", "a")
f.write(x)
f.close()
print ("El texto encriptado es:")

print x

print ("El texto des encriptado es :")
a=decode_binary_string(x)
print a
b=invertir(a)
print b
