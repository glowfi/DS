# NA, Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def searchBitonic(self, arr, n, X):
        for i in range(n):
            if arr[i] == X:
                return i
        return -1


# Optimal
# T.C. -> O(log(n))+O(log(n))
# S.C. -> O(1)


class Solution:
    def bsAsc(self, st, en, arr, X):
        while st <= en:
            mid = st + ((en - st) // 2)

            if arr[mid] == X:
                return mid

            elif arr[mid] < X:
                st = mid + 1

            else:
                en = mid - 1

        return -1

    def bsDsc(self, st, en, arr, X):
        while st <= en:
            mid = st + ((en - st) // 2)

            if arr[mid] == X:
                return mid

            elif arr[mid] > X:
                st = mid + 1

            else:
                en = mid - 1

        return -1

    def getBitonic(self, arr, n):
        if arr[0] > arr[1]:
            return 0

        if arr[n - 1] > arr[n - 2]:
            return arr[n - 1]

        st, en = 1, len(arr) - 2
        while st <= en:
            mid = st + ((en - st) // 2)

            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid

            elif arr[mid - 1] > arr[mid] and arr[mid - 1] > arr[mid + 1]:
                en = mid - 1

            else:
                st = mid + 1

    def searchBitonic(self, arr, n, X):
        point = self.getBitonic(arr, n)
        if point:
            k = self.bsAsc(0, point - 1, arr, X)

            if k != -1:
                return k
            return self.bsDsc(point + 1, n - 1, arr, X)
