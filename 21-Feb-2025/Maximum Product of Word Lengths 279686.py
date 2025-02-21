# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = []
        for x in range(len(words)):
            for y in range(x + 1, len(words)):
                if set(words[x]).isdisjoint(set(words[y])):
                    ans.append(len(words[x])*len(words[y]))
        return (0 if len(ans)==0 else max(ans))