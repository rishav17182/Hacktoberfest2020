t=input()
g=int(input())
d=""
c=26
r=97
r1=int(g)-97
for i in range(len(t)):
     g1=ord(t[i])+r1
     d+=chr((g1)%c+r)
print(d)
