#  Problem :- https://leetcode.com/problems/xor-queries-of-a-subarray/description/?envType=daily-question&envId=2024-09-13

#  Solution :- https://www.youtube.com/watch?v=1Q4lxfSlbPs&ab_channel=NeetCodeIO

# 1310. XOR Queries of a Subarray

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        res = []
        for left, right in queries:
            total = arr[right]
            remove = 0 if left == 0 else arr[left - 1]
            res.append(
                total ^ remove
            )
        return res
