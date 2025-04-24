# https://leetcode.com/problems/hand-of-straights , Medium


# Better
# T.C. - O(n) +O(nlog(n)) O(n*k)
# S.C  - O(n)


class Solution:
    def getFirstEntryInMap(self, map: dict[int, int]) -> int:
        return list(map.items())[0]

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq_map = {}

        for num in hand:
            freq_map[num] = 1 + freq_map.get(num, 0)

        freq_map = dict(sorted(freq_map.items(), key=lambda x: x[0]))

        while freq_map:
            k, v = self.getFirstEntryInMap(freq_map)

            for i in range(k, k + groupSize):
                if i not in freq_map:
                    return False

                freq_map[i] -= 1
                if freq_map[i] == 0:
                    del freq_map[i]

        return True


# Optimal
# T.C. - O(n)+O(klog(k))
# S.C  - O(n)+O(n)


import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq_map = {}

        for num in hand:
            freq_map[num] = 1 + freq_map.get(num, 0)

        min_heap = list(freq_map.keys())
        heapq.heapify(min_heap)

        while min_heap:
            min_elem = min_heap[0]

            for i in range(min_elem, min_elem + groupSize):
                if i not in freq_map:
                    return False

                freq_map[i] -= 1
                if freq_map[i] == 0:
                    if min_heap[0] != i:  # Not super intutive requires dry run
                        return False
                    heapq.heappop(min_heap)

        return True
