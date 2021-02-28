# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([AEIOUaeiou]{2,})[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]",input(),flags = re.I)
print('\n'.join(m or ['-1']))
