#  https://leetcode.com/problems/subarray-sums-divisible-by-k/ , Medium

# https://0x0.st/XkKz.701.png
# + Find the current remainder in the past
# + Take care of negative remainder by adding k
# + For count {0:1} , For Length {0:-1}


# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                if sm % k == 0:
                    c += 1
        return c


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = 0
        sm = 0
        hmap = {0: 1}

        for i in range(len(nums)):
            sm += nums[i]
            rem = sm % k

            if rem < 0:
                rem += k

            if rem in hmap:
                c += hmap[rem]

            if rem in hmap:
                hmap[rem] += 1
            else:
                hmap[rem] = 1

        return c
