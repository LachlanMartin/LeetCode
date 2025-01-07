from typing import List, Optional
import collections
import heapq
import math

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0

        for index, value in enumerate(s[:-2]):
            count += s[index + 2:].count(value)
        
        return count

    
solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))