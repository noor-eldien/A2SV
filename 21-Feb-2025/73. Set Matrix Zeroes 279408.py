# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n= len(matrix),len(matrix[0])
        cntr=0
        idx = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    idx.add(cntr)
                    cntr+=1
                else:
                    cntr+=1
        rs = set()
        cs = set()
        for i in idx:
            rs.add(i//n)
            cs.add(i % n)
        for i in range(m):
            for j in cs:
                matrix[i][j]=0
        for i in range(n):
            for j in rs:
                matrix[j][i]=0