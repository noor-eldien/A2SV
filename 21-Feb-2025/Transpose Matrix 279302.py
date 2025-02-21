# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lst = []
        for j in range(len(matrix[0])):
            ls = []
            for i in range(len(matrix)):
                ls.append(matrix[i][j])
            lst.append(ls)
        return(lst)