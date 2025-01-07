from typing import List, Optional
import collections
import heapq
import math

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr = 0
        for index, num in enumerate(nums):
            curr += num
            if curr >= total_sum - curr:
                answer += 1
        
        return answer

    
solution = Solution()
print(solution.waysToSplitArray([6,-1,9]))