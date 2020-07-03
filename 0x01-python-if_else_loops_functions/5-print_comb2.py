#!/usr/bin/python3
num = 0
while(num < 100):
    if num == 99:
        print('{}'.format(num))
        num = num + 1
    else:
        print('{:02d}, '.format(num), end="")
        num = num + 1
