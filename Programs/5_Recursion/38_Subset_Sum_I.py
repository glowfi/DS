# https://practice.geeksforgeeks.org/problems/subset-sums2234/1 , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def getAns(self, idx, count, arr, ans):
        if idx == len(arr):
            ans.append(count)
            return

        ans.append(count)

        for i in range(idx, len(arr)):
            self.getAns(i + 1, count + arr[i], arr, ans)

    def subsetSums(self, arr, N):
        ans = []
        self.getAns(0, 0, arr, ans)
        return ans


ls = [5, 2, 1]
N = len(ls)
obj = Solution()
print(obj.subsetSums(ls, N))
