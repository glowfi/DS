# https://leetcode.com/problems/lemonade-change , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total_5 = 0
        total_10 = 0

        for bill in bills:
            if bill == 5:
                total_5 += 1
            elif bill == 10:
                if not total_5:
                    return False
                total_5 -= 1
                total_10 += 1
            elif bill == 20:
                cond1 = (
                    total_5 >= 1 and total_10 >= 1
                )  # Being greedy here by giving change only with 10 and 5
                cond2 = total_5 >= 3

                if cond1:
                    total_5 -= 1
                    total_10 -= 1
                elif cond2:
                    total_5 -= 3
                else:
                    return False

        return True
