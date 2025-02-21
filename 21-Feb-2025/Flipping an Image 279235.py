# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in image:
            ans.append(list(reversed(i)))
        for i in ans:
            for j in range(len(i)):
                i[j]=1 if i[j]==0 else 0
        return (ans)