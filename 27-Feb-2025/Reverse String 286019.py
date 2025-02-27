# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        idx = int(len(s)/2 if len(s)%2==0 else len(s)/2)
        for i in range(0,idx):
            s[i],s[(len(s)-1)-i]  = s[(len(s)-1)-i], s[i]
        return(len(s))
        