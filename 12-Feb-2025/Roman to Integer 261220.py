# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        vals={ "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        cntr=0
        for i in s:
            if i in vals:
                cntr+=vals[i]
        return cntr