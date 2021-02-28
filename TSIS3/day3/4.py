a = input().split()
l = len(a)
a = [i for i in a if(i!='0')]
for i in a:
    print(i,end = ' ')
for i in range(l-len(a)):
    print('0',end = ' ')
