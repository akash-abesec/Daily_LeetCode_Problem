# Problem :- https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09

# Solution :- https://www.youtube.com/watch?v=zRPJvEqsUNo&ab_channel=devwithcp

# 2326. Spiral Matrix IV

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        i, j, curr_dir = 0, 0, 0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        res = np.full((m,n), -1)
        while (head != None):
            res[i][j] = (head.val)
            newi = i + dx[curr_dir]
            newj = j + dy[curr_dir]
            if (min(newi, newj) <0 or newi >= m or newj >= n or res[newi][newj] != -1):
                curr_dir = (curr_dir + 1)%4
            i += dx[curr_dir]
            j += dy[curr_dir]
            head = head.next
        return res
