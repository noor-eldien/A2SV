# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

import math,sys,random
from collections import Counter


t = int(input())
for i in range(t):
    n = int(input())
    if n==1:
        print(1)
    elif n==2:
        print(-1)
    elif n>=3:
        lst = [val for val in range(1,(n*n+1)) if val%2==0 ]
        lst.extend(val for val in range(1,(n*n+1)) if val%2!=0 )
        for i in range(0, len(lst), n):
            print(*lst[i:i + n])