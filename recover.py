from ecc import *
from helper import hash256

def recoverKey(z1, z2, s1, s2):

    alphaint = (z1 - z2) % N
    betaint = (s1 - s2) % N
    k = FieldElement(alphaint, N) / FieldElement(betaint, N)

    r = (k.num*G).x.num
    k_inv = pow(k.num, N-2, N)

    #print signature
    print("\nr value: ")
    print(hex(r))
    print("\ns1 value: ")
    print(hex(s1))
    print("\ns2 value: ")
    print(hex(s2))

    #work out the private key
    alphaint = ((z1 * s2 % N) - (z2 * s1 % N)) % N
    betaint = r * (s1 - s2) % N
    alpha = FieldElement(alphaint, N)
    beta = FieldElement(betaint, N)
    x = alpha / beta
    print("\nFound private key: ")
    print(hex(x.num))
    return hex(x.num)
