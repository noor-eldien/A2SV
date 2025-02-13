# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ll = len(nums) // 3
        cntr = dict(Counter(nums))
        ans = [key for key, val in cntr.items() if val > ll]
        return (ans)
