# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

import math,sys,random,copy
from collections import Counter


lst = []
for _ in range(5):
    lst.extend(list(map(int,input().split())))
cntr = 0
for i in lst:
    if i == 1:
        break
    else:
        cntr+=1

r = (cntr//5)+1
c = (cntr%5)+1
print(abs(3-r)+abs(3-c))