# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        cntr=-1
        row=0
        for i in range(len(mat)):
            if mat[i].count(1) > cntr:
                row = i
                cntr = mat[i].count(1)
        return [row,cntr]