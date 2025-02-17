# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution(object):
    def findWinners(self, matches):
        l = dict()
        for m in matches:
            l[m[0]] = l.get(m[0],0) + 0
            l[m[1]] = l.get(m[1],0) + 1

        ww = [key for key,val in l.items() if val==0 ]
        ll = [key for key,val in l.items() if val==1 ]
        ans = [sorted(ww),sorted(ll)]
        return (ans)
