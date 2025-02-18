# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
cntr = dict()
for _ in range(n):
    s = input()
    if cntr.get(s,0)>0:
        cntr.pop(s)
        cntr[s]=1
    else:
        cntr[s]=1
st =[]
for k in cntr:
    st.append(k)
for i in st[::-1]:
    print(i)