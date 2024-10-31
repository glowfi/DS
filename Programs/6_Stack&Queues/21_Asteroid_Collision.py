# https://leetcode.com/problems/asteroid-collision , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)

from typing import List


class Solution:
    def isOfSameDirection(self, stackval: int, currval: int):
        if (stackval < 0 and currval > 0) or (stackval > 0 and currval < 0):
            return False
        return True

    def willExplode(self, stackval, currval):
        if stackval > 0 and currval < 0:
            if abs(stackval) > abs(currval):
                return [True, currval]
            elif abs(currval) > abs(stackval):
                return [True, stackval]
            else:
                return [True, 0]
        return [False, 0]

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = [asteroids[0]]

        for i in range(1, len(asteroids)):
            wasGreaterThroughout = True
            encounteredEqualElements = False

            if (
                stk
                and not self.isOfSameDirection(stk[-1], asteroids[i])
                and self.willExplode(stk[-1], asteroids[i])
            ):
                while True:
                    if not stk:
                        break

                    res = self.willExplode(stk[-1], asteroids[i])
                    will_explode = res[0]
                    val_to_explode = res[1]

                    if will_explode:
                        if val_to_explode == stk[-1]:
                            stk.pop(-1)
                        elif val_to_explode == asteroids[i]:
                            wasGreaterThroughout = False
                            break
                        elif val_to_explode == 0:
                            encounteredEqualElements = True
                            stk.pop(-1)
                            break
                    else:
                        break

            if wasGreaterThroughout and not encounteredEqualElements:
                stk.append(asteroids[i])

        return stk
