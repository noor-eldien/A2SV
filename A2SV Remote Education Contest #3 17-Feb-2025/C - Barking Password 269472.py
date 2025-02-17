# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

import math,sys,random
from collections import Counter

ps = input()
n = int(input())
lst = []
for i in range(n):
    lst.append(input())
if ps in lst:
    print("YES")
    sys.exit()
for i in range(n):
    for j in range(n):
        if lst[i][1] == ps[0] and lst[j][0] == ps[1]:
            print("YES")
            sys.exit()
print("NO")