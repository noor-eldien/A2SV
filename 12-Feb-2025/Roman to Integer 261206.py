# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        civ=s.count("IV")
        cix=s.count("IX")
        cxl=s.count("XL")
        cxc=s.count("XC")
        ccd=s.count("CD")
        ccm=s.count("CM")
        s=s.replace("IV","",civ)
        s=s.replace("IX","",cix)
        s=s.replace("XL","",cxl)
        s=s.replace("XC","",cxc)
        s=s.replace("CD","",ccd)
        s=s.replace("CM","",ccm)
        cntr = civ*4 + cix*9 + cxl*40 + cxc*90 + ccd*400 + ccm*900
        for i in s:
            if i == "M":
                cntr+=1000
            elif i == "D":
                cntr+=500
            elif i=="C":
                cntr+=100
            elif i=="L":
                cntr+=50
            elif i=="X":
                cntr+=10
            elif i=="V":
                cntr+=5
            elif i=="I":
                cntr+=1
        return cntr
