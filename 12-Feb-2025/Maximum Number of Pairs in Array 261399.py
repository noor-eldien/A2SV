# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        st = set(nums)
        cntr=0
        rem=0
        for i in st:
            cntr += nums.count(i)//2
            if nums.count(i)%2!=0:
                rem+=1
        ans = [cntr,rem]
        return ans