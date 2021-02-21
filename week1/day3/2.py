a = input().split()
a = list(map(int,a))
a = [i for i in a if i>0]
print(min(a))