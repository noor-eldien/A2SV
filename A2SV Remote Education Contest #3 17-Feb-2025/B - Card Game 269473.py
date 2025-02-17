# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

import math,sys,random
from collections import Counter

n = int(input())
lst = list(map(int, input().split()))
tmp = sorted(lst)
val = tmp[0]+tmp[-1]
for i in range(len(lst)):
    x = val-lst[i]
    if x in lst[i+1:]:
        lst[i] = 0
        print(i+1,lst.index(x)+1)
        lst[lst.index(x)] = 0