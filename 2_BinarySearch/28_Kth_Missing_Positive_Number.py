# https://leetcode.com/problems/kth-missing-positive-number/ , Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        st = set(arr)
        for i in range(1, arr[-1] + k + 1):
            if i not in st:
                k -= 1
            if k == 0:
                return i


# Better
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def missingTillCurrIndex(self, arr, idx):
        return arr[idx] - (idx + 1)

    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = -1
        for i in range(len(arr)):
            m = self.missingTillCurrIndex(arr, i)
            if m < k:
                ans = i
            else:
                break
        more = k - self.missingTillCurrIndex(arr, ans)
        return arr[ans] + more


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def missingTillCurrIndex(self, arr, idx):
        return arr[idx] - (idx + 1)

    def findKthPositive(self, arr: List[int], k: int) -> int:
        st, en = 0, len(arr) - 1

        while st <= en:
            mid = st + ((en - st) // 2)

            if self.missingTillCurrIndex(arr, mid) < k:
                st = mid + 1
            else:
                en = mid - 1

        more = k - self.missingTillCurrIndex(arr, en)
        return arr[en] + more
