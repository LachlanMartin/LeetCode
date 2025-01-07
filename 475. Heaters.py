from typing import List, Optional
import collections
import heapq
import math


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        pos = 0
        heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[pos]: # We find the first heater that happens occurs to the left of the first house
                pos += 1
            r = min(house - heaters[pos - 1], heaters[pos] - house) # We then simply find the min radius surrounding this house
            ans = max(ans, r) # Keep track of the maximum radius we have so far and we just repeat for each house
        return ans
    
solution = Solution()

print("Test Case 1:")
print(solution.findRadius([1,2,3], [2]))

# print("Test Case 2:")
# print(solution.findRadius([1,2,3,4], [1,4]))

# print("Test Case 3:")
# print(solution.findRadius([1,5], [2]))