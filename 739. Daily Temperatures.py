from typing import List, Optional
import collections
import heapq
import math

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        stack = []
        for i in range(len(temperatures)):
            today_temp = temperatures[i]
            while True:
                i += 1
                stack.append(temperatures[i])
                if temperatures[i] > today_temp:
                    break
            while True:
                
            answer.append(len(stack))
            stack.pop()

        return answer


solution = Solution()

# Test cases
print("Test Case 1:")
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))  # Expected: [1,1,4,2,1,1,0,0]

print("Test Case 2:")
print(solution.dailyTemperatures([30,40,50,60]))  # Expected: [1,1,1,0]

print("Test Case 3:")
print(solution.dailyTemperatures([30,60,90]))  # Expected: [1,1,0]