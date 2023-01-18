# recover-ecc-keys
A tool to calculate the private key when the nonce has been reused. Based on Jimmy Song's library from Programming Bitcoin.

# How to use

To use this tool, you must have:
- The signature s values s1 & s2
- The message hashes z1 & z2

``` python
from recover import *

s1 = 0x92b0522fabec7154a73c992617a35e9e82e46f0e1811f4f15e1e52169a9f6ed2
s2 = 0x50fad87fd9a390460676798f5148ac7630c88a217992c2bd7c9674f24f8e19a7
z1 = int.from_bytes(b'0x4b2cdf712dc7d3fac8e7ed63b3a2e806556ca7d5c30ed5f4b34dbb2a12b0c18f', 'big')
z2 = int.from_bytes(b'0x1cd506860c52d7e042f56b33a856b94fdefa3bcc808a06dd3b82619db2c01969', 'big')

recoverKey(z1, z2, s1, s2)
```
Output:
```
r value: 
0x1b38903a43f7f114ed4500b4eac7083fdefece1cf29c63528d563446f972c180

s1 value: 
0x92b0522fabec7154a73c992617a35e9e82e46f0e1811f4f15e1e52169a9f6ed2

s2 value: 
0x50fad87fd9a390460676798f5148ac7630c88a217992c2bd7c9674f24f8e19a7

Found private key: 
0x75bcd15
```
