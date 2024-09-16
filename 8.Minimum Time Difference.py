# Problem :- https://leetcode.com/problems/minimum-time-difference/description/?envType=daily-question&envId=2024-09-16

# Solution :- https://www.youtube.com/watch?v=L35DaWhvheg&ab_channel=devwithcp

# Minimum Time Difference(539)

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Step 1: Convert all time points to minutes and store in a list
        vec = []
        for timePoint in timePoints:
            h, m = map(int, timePoint.split(':'))
            mins = h * 60 + m
            vec.append(mins)
        
        # Step 2: Sort the time points
        vec.sort()
        
        # Step 3: Calculate the minimum difference
        res = float('inf')
        for i in range(1, len(vec)):
            res = min(vec[i] - vec[i - 1], res)
        
        # Step 4: Handle the circular case (difference between the first and last time points)
        return min(res, 1440 + vec[0] - vec[-1])
