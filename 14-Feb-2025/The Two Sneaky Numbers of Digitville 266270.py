# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cntr = dict(Counter(nums))
        ans = [key for key,val in cntr.items() if val>1]
        return ans