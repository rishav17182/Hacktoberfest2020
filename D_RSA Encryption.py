import gmpy2
from gmpy2 import mpz
import random
#bit_count = 64
#rand_state = gmpy2.random_state()
p=int(input("Enter p:"))
q=int(input("Enter q:"))
m=int(input("Enter m:"))
k1=q-1
n2=p-1
l=[]
w=1
rand_state=gmpy2.random_state()
n1=gmpy2.mul(p, q)#number
p1=gmpy2.mul(k1,n2) #numberphi
k=gmpy2.mpz_random(rand_state, n1)

e=gmpy2.next_prime(q)#value of e
#print("e:",e)
if gmpy2.gcd(e, p1)==1:
  d=gmpy2.invert(e, p1)# value of d
  #print("d:",d)
  if gmpy2.t_mod(e*d, p1)==w:
    c1=gmpy2.powmod(k+1,e,n1) #value of c1
    print(c1)
    c2=gmpy2.powmod(k,e,n1)
    f1=gmpy2.mul(c2,m)
    # value of c2
    print(f1)
    print(k)
    print(e)
    print(d)
    print(n1)

  else:
      print("cannot be generated")
else:
  print("cannot be generated")