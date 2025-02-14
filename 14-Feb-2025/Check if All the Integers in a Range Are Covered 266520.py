# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for i in ranges:
            for x in range(i[0],i[1]+1):
                s.add(x)
        for i in range(left,right+1):
            if i not in s:
                return False
                sys.exit()
        return True