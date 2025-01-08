from typing import List, Optional
import collections
import heapq
import math

def isPrefixAndSuffix(str1, str2):
    if str2.startswith(str1) and str2.endswith(str1):
        return True
    else:
        return False
    
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]) == True:
                    count += 1
        return count
    
solution = Solution()

# print("Test Case 1:")
# print(solution.countPrefixSuffixPairs(["a","aba","ababa","aa"]))

print("Test Case 2:")
print(solution.countPrefixSuffixPairs(["pa","papa","ma","mama"]))

# print("Test Case 3:")
# print(solution.countPrefixSuffixPairs(["abab","ab"]))