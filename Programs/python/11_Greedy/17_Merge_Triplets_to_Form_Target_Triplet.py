# <Question Link> , <Difficulty>

# Intuition
# + First filter out all the triplets having values less than the target triplet
# + Now we are sure all the triplets have values less than equal to target triplets
# + Now just check of any of the existing triplets have values in first,second,postion
# + we can combine all the triplets and get our result

# Optimal
# T.C. - O(n)
# S.C  - O(3)


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        st = set()
        for first, second, third in triplets:
            if first > target[0] or second > target[1] or third > target[2]:
                continue

            if first == target[0]:
                st.add(0)
            if second == target[1]:
                st.add(1)
            if third == target[2]:
                st.add(2)

        return len(st) == 3
