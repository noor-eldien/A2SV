# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for i in strs:
             x="".join(sorted(i))
             if x not in mp:
                mp[x]=[]
             mp[x].append(i)
        ans=[]
        for i in mp:
            ans.append(mp[i])
        return ans