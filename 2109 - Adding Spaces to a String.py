from typing import List, Optional
import collections
import heapq
import math

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Create list of substrings using string slicing
        result = []
        prev = 0
        for pos in spaces:
            result.append(s[prev:pos])
            prev = pos
        result.append(s[prev:])  # Add the remaining part
        
        return ' '.join(result)
    
solution = Solution()
print(solution.addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))