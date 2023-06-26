# https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1, Easy


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def bsAsc(self, st, en, arr, x):
        while st <= en:
            mid = (st + en) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                en = mid - 1
            else:
                st = mid + 1
        return -1

    def bsDesc(self, st, en, arr, x):
        while st <= en:
            mid = (st + en) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                st = mid + 1
            else:
                en = mid - 1
        return -1

    def bitonicPoint(self, arr, n):
        if len(arr) == 1:
            return 0

        st, en = 0, len(arr) - 1

        while st <= en:
            mid = (st + en) // 2

            if mid > 0 and mid < n - 1:
                if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                    return mid

                # Left is Promising
                elif arr[mid - 1] > arr[mid]:
                    en = mid - 1
                # Right is Promising
                else:
                    st = mid + 1

            elif mid == 0:
                if arr[0] > arr[1]:
                    return 0
                return 1

            elif mid == len(arr) - 1:
                if arr[n - 1] > arr[n - 2]:
                    return n - 1
                return n - 2

    def search(self, arr, x):
        findPoint = self.bitonicPoint(arr, len(arr))

        firstHalf = self.bsAsc(0, findPoint - 1, arr, x)
        if firstHalf != -1:
            return firstHalf
        return self.bsDesc(findPoint, len(arr) - 1, arr, x)


ls = [-3, 9, 18, 20, 17, 5, 1]
key = -3
obj = Solution()
print(obj.search(ls, key))
