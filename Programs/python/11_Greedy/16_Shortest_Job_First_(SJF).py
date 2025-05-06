# https://www.geeksforgeeks.org/problems/shortest-job-first/1 , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# At every step keep track of end time
# total_wt is summation of the end time of previous job for every ith job


class Solution:
    def solve(self, bt):
        bt.sort()
        total_wt = 0
        prev_end_time = 0

        for i in range(len(bt)):
            total_wt += prev_end_time
            prev_end_time = prev_end_time + bt[i]

        return total_wt // len(bt)
