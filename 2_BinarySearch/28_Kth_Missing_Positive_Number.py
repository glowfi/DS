# https://leetcode.com/problems/kth-missing-positive-number/ , Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        st = set(arr)
        num = 1

        while True:
            if num not in st:
                k -= 1

            if k == 0:
                break
            num += 1
        return num


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
