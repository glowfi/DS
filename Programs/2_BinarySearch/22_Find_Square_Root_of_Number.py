# https://practice.geeksforgeeks.org/problems/square-root/0 , Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def floorSqrt(self, x):
        ans = 1
        for i in range(1, x):
            # equal to x
            if i * i == x:
                return i
            # less than x
            elif i * i < x:
                ans = i
            # greater than x
            else:
                break
        return ans


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def floorSqrt(self, x):
        st, en = 1, x + 1
        ans = 1

        while st <= en:
            mid = st + (en - st) // 2

            #  equal to x
            if mid * mid == x:
                return mid

            # less than x
            elif mid * mid < x:
                ans = mid
                st = mid + 1

            # greater than x
            else:
                en = mid - 1

        return ans
