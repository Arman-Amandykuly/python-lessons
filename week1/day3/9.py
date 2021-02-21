n, m = map(int,input().split())
a = set()
for i in range(n):
  a.add(int(input()))
b = set()
for i in range(m):
    b.add(int(input()))
c = a.intersection(b)
print(len(c))
for i in sorted(list(c)):
    print(i, end = ' ')
print()
print(len(a)-len(c))
for i in sorted(list(a.difference(c))):
    print(i,end = ' ')
print()
print(len(b)-len(c))
for i in sorted(list(b.difference(c))):
    print(i,end = ' ')