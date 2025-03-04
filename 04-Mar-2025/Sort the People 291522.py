# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)
        for i in range(n):
            mn = i
            for j in range(i+1,n):
                if heights[j] <= heights[mn]:
                    mn = j
            heights[i],heights[mn] = heights[mn],heights[i]
            names[i],names[mn] = names[mn],names[i]
        return(names[::-1])