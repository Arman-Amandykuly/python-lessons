a = input().split()
a = list(map(int,a))
for i in range(len(a)-1,-1,-1):
    print(a[i],end = ' ')