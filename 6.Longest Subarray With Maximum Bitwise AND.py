# Problem:- https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2024-09-14

# Solution :- https://www.youtube.com/watch?v=lvzNrqBzdbg&ab_channel=devwithcp

# 2419. Longest Subarray With Maximum Bitwise AND

class Solution(object):
    def longestSubarray(self, nums):
        ans, cnt = 0, 0
        
        max_element = max(nums)
        for num in nums:
            if num == max_element:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans
