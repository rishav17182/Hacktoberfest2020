import gmpy2
#from final1 import p1
from gmpy2 import mpz
import random
#rand_state = gmpy2.random_state()
c=int(input("Enter c:"))
d=int(input("Enter d:"))
n=int(input("Enter n:"))
#k1=int(input())
#k1=q-1
#n2=p-1
#l=[]

#w=1
#rand_state=gmpy2.random_state(42)



m2=gmpy2.powmod(c,d,n)

print(m2)
