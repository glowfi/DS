# NA, Easy


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)

# ls=[1,2,3,4,5,6,7,........]
# key=90


def bs(st, en, nums, target):
    pass


def search(target, nums):
    st, en = 0, 1
    pos = -1

    while True:
        mid = (st + en) // 2

        if nums[mid] > target:
            pos = mid
            break

        elif nums[mid] < target:
            st = en
            en *= 2

    bs(st, pos, nums, target)
