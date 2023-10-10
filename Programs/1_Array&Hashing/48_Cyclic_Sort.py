# NA , Easy


# Whenver it says an array contains element from 0,n or 1,n we use cyclic
# If there are duplicate they move to extereme right like magic
# if array contains elements from 0 to n make inbounds check
# Missing -> index
# Duplicates -> nums[index]

# Optimal
# T.C. - O(n)
# S.C  - O(1)


class cyclicSort:
    """docstring for cyclicSort."""

    def sort(self, arr):
        idx = 0

        while idx < len(arr):
            actualPos = arr[idx] - 1

            # If the number at current index is not in its actual Position
            if arr[actualPos] != arr[idx]:
                arr[actualPos], arr[idx] = arr[idx], arr[actualPos]
            else:
                idx += 1


obj = cyclicSort()
ls = [3, 5, 2, 1, 4]
ls = [7, 5, 1, 2, 3, 6, 4]
# ls = [7, 5, 1, 2, 3, 6, 4, 1, 3, 2, 5]
obj.sort(ls)

print(ls)
