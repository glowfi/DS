# https://leetcode.com/problems/kth-missing-positive-number/ , Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Convert the original array to set for O(1) lookups
        st = set(arr)

        # Initialize num with 1 and keep incrementing it in the below while loop till we get our result
        num = 1

        while True:
            # Whenever you see a number is not present in the original array decrement k by one
            if num not in st:
                k -= 1

            # When k becomes zero its an indicator that we have reach our kth positive element
            # which is not present in the original array
            if k == 0:
                return num

            num += 1


# Better
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def getMissing(self, idx, arr):
        return arr[idx] - (idx + 1)

    def findKthPositive(self, arr: List[int], k: int) -> int:
        idx = -1
        for i in range(len(arr)):
            if self.getMissing(i, arr) < k:
                idx = i
            else:
                break

        more = k - self.getMissing(idx, arr)
        return arr[idx] + more


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def getMissing(self, idx, arr):
        return arr[idx] - (idx + 1)

    def findKthPositive(self, arr: List[int], k: int) -> int:
        st, en = 0, len(arr) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if self.getMissing(mid, arr) < k:
                st = mid + 1
            else:
                en = mid - 1

        more = k - self.getMissing(en, arr)

        return arr[en] + more
