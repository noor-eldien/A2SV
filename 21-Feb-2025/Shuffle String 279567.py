# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = dict()
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        ans = dict(sorted(ans.items()))
        anss=[val for val in ans.values()]
        return("".join(anss))