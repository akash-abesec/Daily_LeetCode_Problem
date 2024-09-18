# Problem :-  https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18

# Solution :- https://www.youtube.com/watch?v=ZVNE6hJQP5A&ab_channel=devwithcp

# 179. Largest Number

class Solution(object):
    def cmp(self, a, b):
        if a + b > b + a:
            return -1
        return a + b < b + a
    def largestNumber(self, nums):
        all_str = list(map(str, nums))
        
        all_str.sort(key=cmp_to_key(self.cmp))

        if all_str[0] == '0':
            return "0"

        return ''.join(all_str)
