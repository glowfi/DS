# https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1 , Medium


# Optimal
# T.C. - O(n^2)
# S.C  - O(n)+O(n)


class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp = [1 for _ in range(len(arr))]
        path_map = {idx: idx for idx in range(len(arr))}

        mx_le = 1
        mx_dp_idx = 0
        ans = []

        for idx in range(len(arr)):
            for prevIdx in range(idx):
                if arr[prevIdx] < arr[idx]:
                    if 1 + dp[prevIdx] > dp[idx]:
                        dp[idx] = max(dp[idx], 1 + dp[prevIdx])
                        path_map[idx] = prevIdx
                        if dp[idx] > mx_le:
                            mx_le = dp[idx]
                            mx_dp_idx = idx

        start = mx_dp_idx

        while True:
            if path_map[start] == start:
                ans.append(arr[start])
                break
            ans.append(arr[start])
            start = path_map[start]

        return ans[::-1]


obj = Solution()
arr = [5, 4, 11, 1, 16, 8]
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
arr = [1]
arr = [7, 7, 7, 7, 7, 7]
N = len(arr)
print(obj.longestIncreasingSubsequence(N, arr))
