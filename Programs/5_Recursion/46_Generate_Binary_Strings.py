# https://practice.geeksforgeeks.org/problems/generate-all-binary-strings/1 , Medium

# Recursive Tree
# https://0x0.st/Htdu.867.png


# Optimal [ans in body]
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, tmp, n):
        if idx == n:
            return [tmp]

        ans = []

        # Check last element
        if idx > 0:
            if tmp[idx - 1] == "0":
                # can take both 0 and 1
                vals = self.helper(idx + 1, tmp + "0", n)
                for val in vals:
                    ans.append(val)

                vals = self.helper(idx + 1, tmp + "1", n)
                for val in vals:
                    ans.append(val)
            else:
                # Can take only zero
                vals = self.helper(idx + 1, tmp + "0", n)
                for val in vals:
                    ans.append(val)

        elif idx == 0:
            # can take both 0 and 1
            vals = self.helper(idx + 1, tmp + "0", n)
            for val in vals:
                ans.append(val)

            vals = self.helper(idx + 1, tmp + "1", n)
            for val in vals:
                ans.append(val)

        return ans

    def generateBinaryStrings(self, n):
        return self.helper(0, "", n)
