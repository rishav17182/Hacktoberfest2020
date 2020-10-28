import gmpy2
from gmpy2 import mpz
import random
#bit_count = 64
#rand_state = gmpy2.random_state()
c1=int(input("Enter c1:"))
c2=int(input("Enter c2:"))
e1=int(input("Enter e:"))
d1=int(input("Enter d:"))
n1=int(input("Enter n:"))
k2=gmpy2.powmod(c1,d1,n1)
jk=k2-1
k3=gmpy2.c_div(c2,gmpy2.powmod(jk,e1,n1)) 
print(int(k3))   
print(jk)  