# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        es = 0
        ans = []
        for i in nums:
            if i%2==0:
                es+=i
        for val,idx in queries:
            if nums[idx]%2==0:
                es-=nums[idx]
            nums[idx]+=val
            if nums[idx]%2==0:
                es+=nums[idx]
            ans.append(es)
        return(ans)
        