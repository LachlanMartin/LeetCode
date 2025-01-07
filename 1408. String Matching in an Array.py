from typing import List, Optional
import collections
import heapq
import math

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = list()
        for word in words:
            copy = words.copy()
            copy.remove(word)
            for c in copy:
                if word in c:
                    result.add(word)
                    break
        
        return result

    
solution = Solution()
print(solution.waysToSplitArray([6,-1,9]))