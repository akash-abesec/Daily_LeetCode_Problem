# Problem :- https://leetcode.com/problems/shortest-palindrome/description/?envType=daily-question&envId=2024-09-20

# Solution :- https://www.youtube.com/watch?v=niOT-FK1RH8&ab_channel=NeetCodeIO

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i] + s
