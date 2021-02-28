a = []
with open("input.txt") as k:
    a += k.read().split()
b = set(a)
c = {i : a.count(i) for i in b}
k = list(b)
abc = 'abcdefghijklmnopqrstuvwxyz'
cba = {abc[i] : abc[25-i] for i in range(26)}
mx = 0
for i in b:
    mx = max(len(i),mx)
def f(s):
    return [cba[i] for i in s]+['{' for i in range(mx-len(s))]
k.sort(reverse = True,key = lambda x: (c[x],f(x)))
for i in k:
    print(i)