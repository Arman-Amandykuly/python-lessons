a = input()
print('\n'.join([str(sum([1 for i in a if i in "abcdefghijklmnopqrstuvwxyz"])),str(sum([1 for i in a if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']))]))