from typing import List, Optional
import collections
import heapq
import math

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currentSubarraySum = nums[0]

        # Loop through the list starting from the second element
        for currentIdx in range(1, len(nums)):
            if nums[currentIdx] <= nums[currentIdx - 1]:
                # If the current element is not greater than the previous one,
                # update maxSum
                maxSum = max(maxSum, currentSubarraySum)
                # Reset the sum for the next ascending subarray
                currentSubarraySum = 0
            currentSubarraySum += nums[currentIdx]

        # Final check after the loop ends to account for the last ascending
        # subarray
        return max(maxSum, currentSubarraySum)
    
solution = Solution()

print("Test Case 1:")
nums = [10,20,30,40,50]
print(solution.maxAscendingSum(nums))

# print("Test Case 2:")
# print(solution.countPrefixSuffixPairs(["pa","papa","ma","mama"]))

# print("Test Case 3:")
# print(solution.countPrefixSuffixPairs(["abab","ab"]))