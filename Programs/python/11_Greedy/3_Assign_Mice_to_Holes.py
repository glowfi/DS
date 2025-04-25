# https://www.geeksforgeeks.org/problems/assign-mice-holes3053/0 , Easy


# Optimal
# T.C. - 2*O(nlog(n))
# S.C  - O(1)

# Selection criteria : For a mice at index i always choose the hole nearer/closer to it


class Solution:
    def assignMiceHoles(self, N, M, H):
        M.sort()
        H.sort()

        max_time = float("-inf")

        for idx, mice in enumerate(M):
            max_time = max(max_time, abs(mice - H[idx]))

        return max_time
