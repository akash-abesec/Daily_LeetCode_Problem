# Problem :- https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=daily-question&envId=2024-09-11

# Solution :- https://www.youtube.com/watch?v=OOdrmcfZXd8&ab_channel=takeUforward

# 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        return bin(ans).count('1')        
