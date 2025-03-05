# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst = set(nums)
        ans = list(lst)
        ans = sorted(ans)
        ans = ans[::-1]
        if len(ans)>=3:
            return(ans[2])
        else:
            return(max(ans))