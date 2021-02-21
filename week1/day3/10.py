n = int(input())
a = []
for i in range(n): 
    a.append([i for i in input().split()])
c = input()
for i in a:
    if(c in i):
        print(i[(i.index(c)+1)%2])
        break