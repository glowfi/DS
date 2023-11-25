# https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1 , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, N, fromm, to, aux):
        if N == 1:
            print(
                "move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to)
            )
            return

        self.helper(N - 1, fromm, aux, to)
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        self.helper(N - 1, aux, to, fromm)

    def toh(self, N, fromm, to, aux):
        self.helper(N, fromm, to, aux)
        return (2**N) - 1
