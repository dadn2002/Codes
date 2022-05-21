import sys

import Functions

""" Our terminal subprocess starter, keep using your code without losing time with too long computations"""
""" Use it for long run functions like facdifsquare or others """
print("Call.py Begin")

x = sys.argv[1]
y = sys.argv[2]
print(x)
print(y)
list1x = list(x.strip(" "))
del list1x[0]
list2x = ''.join([str(item) for item in list1x])
list1y = list(x.strip(" "))
del list1y[0]
list2y = ''.join([str(item) for item in list1y])

with open("Text/GmailVerify.txt", "w", encoding='utf-8') as f1:
    if list2y == '1':
        f1.write('1')
exec(list2x)
with open("Text/GmailVerify.txt", "w", encoding='utf-8') as f1:
    f1.write('0')

y = input('help')

