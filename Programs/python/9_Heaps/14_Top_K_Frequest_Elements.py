# https://leetcode.com/problems/top-k-frequent-elements/ , Medium

# Brute
# T.C. - O(n)+O(nlog(n))+O(k)
# S.C  - O(n)+O(n)+O(k)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        res = []

        for num, freq in freq_map.items():
            res.append([num, freq])

        new_arr = sorted(res, key=lambda x: x[1], reverse=True)[:k]
        final = []

        for num in new_arr:
            final.append(num[0])

        return final


# Better
# T.C. - O(n)+O(nlog(k))+O(k)
# S.C  - O(n)+O(k)

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, [freq, num])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[-1])

        return res


# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Hint
# + Use Bucket Sort
# + initialize an array with size of atmost n+1  the indexs will represent count as
# max no of times an element can occut is n times
# + make the freq map
# + loop through freq map and append it to its count index such as 2 (count) -> [5,6] 5 and 6 occurs 2 times


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        arr = [[] for _ in range(len(nums) + 1)]

        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        for num, freq in freq_map.items():
            arr[freq].append(num)

        ans = []
        for i in range(len(arr) - 1, -1, -1):
            curr_nums = arr[i]

            for num in curr_nums:
                if k == 0:
                    return ans
                ans.append(num)
                k -= 1

        return ans
