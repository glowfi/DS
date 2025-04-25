# https://www.geeksforgeeks.org/problems/minimum-rotations-to-unlock-a-circular-lock1001/0 , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Selection criteria : at each step see the min between going clockwise or anticlockwise


class Solution:
    def rotationCount(self, R, D):
        c = 0

        while R:
            initial = R % 10
            target = D % 10
            R //= 10
            D //= 10

            clockwise = abs(target - initial)
            anticlockwise = 10 - abs(target - initial)

            c += min(clockwise, anticlockwise)

        return c
