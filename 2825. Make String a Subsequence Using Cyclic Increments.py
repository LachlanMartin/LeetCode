from typing import List, Optional
import collections
import heapq
import math

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str1_pointer = 0
        str2_pointer = 0
        for c in str2:
            while str1[str1_pointer] != c and chr(ord(str1[str1_pointer]) - 1) != c:
                str1_pointer += 1
                if str1_pointer >= len(str1):
                    return False
            
        return True
    
solution = Solution()
print(solution.canMakeSubsequence("abc", "ad"))