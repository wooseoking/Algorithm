import string
mod = 1234567891
lower = string.ascii_lowercase
alpha = dict()
for i,v in enumerate(lower):
    alpha[v] = i+1
n = int(input())
query = input().strip()
h = 0
for i,v in enumerate(query):
    h+=pow(31,i)*alpha[v]
h %=mod
print(h)