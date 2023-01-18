from recover import recoverKey
from ecc import *

e = 123456789
z1 = int.from_bytes(b'0x4b2cdf712dc7d3fac8e7ed63b3a2e806556ca7d5c30ed5f4b34dbb2a12b0c18f', 'big') #message 1
z2 = int.from_bytes(b'0x1cd506860c52d7e042f56b33a856b94fdefa3bcc808a06dd3b82619db2c01969', 'big') #message 2 
k = 255
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s1 = (z1+r*e) * k_inv % N
s2 = (z2+r*e) * k_inv % N
key = recoverKey(z1, z2, s1, s2)

if hex(e) != key:
    print("TEST FAILED")
else:
    print("TEST SUCCESSFUL")
