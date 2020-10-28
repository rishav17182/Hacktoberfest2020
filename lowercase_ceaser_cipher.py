
m=input()#input string contain only lowercase alphabets [a-z]
n=int(input())#key

def F(m,n):
  l=len(m)
  c=''# ciphertext
  for k in range(l):
    ch=m[k]
    num=(ord(ch) + n - 97)
    c_h=chr(num%26 +97)
    c+=c_h
  return c
print(F(m,n))
