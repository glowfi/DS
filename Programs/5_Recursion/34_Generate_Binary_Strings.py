# https://practice.geeksforgeeks.org/problems/generate-all-binary-strings/1 , Medium

# Recursive Tree
# https://0x0.st/Htdu.867.png


# Optimal [ans in body]
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, proc, n):
        if idx == n:
            return [proc]

        tmp = []

        # if not first time check no consecutive ones
        if idx > 0:
            # Proceed with zero if last is also one
            if proc[idx - 1] == "1":
                val = self.helper(idx + 1, proc + "0", n)
                for i in val:
                    tmp.append(i)

            # Proceed with zero or one
            else:
                val = self.helper(idx + 1, proc + "0", n)
                for i in val:
                    tmp.append(i)
                val = self.helper(idx + 1, proc + "1", n)
                for j in val:
                    tmp.append(j)

        # If first time or idx==0
        elif idx == 0:
            val = self.helper(idx + 1, proc + "0", n)
            for i in val:
                tmp.append(i)
            val = self.helper(idx + 1, proc + "1", n)
            for j in val:
                tmp.append(j)

        return tmp

    def generateBinaryStrings(self, n):
        return self.helper(0, "", n)
