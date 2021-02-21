a = input().split()
a = list(map(int,a))
a = [a[i] for i in range(0,len(a),2)]
for i in a:
    print(i,end=' ')