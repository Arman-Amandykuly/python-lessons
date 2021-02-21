a = [i for i in input().split()]
k = int(input())
k = k%len(a)
if(k>0):
    for i in a[len(a)-k:]:
        print(i,end = ' ')
    for i in a[:len(a)-k]:
        print(i,end = ' ')
else:
    k = -k
    for i in a[k:]:
        print(i,end = ' ')
    for i in a[:k]:
        print(i,end = ' ')