# NA, Easy


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)

# ls=[0,0,0,0,.......,1,1,1,.....]
# key=Postion of 1st 1


def bs(st, en, nums, target):
    ans = -1
    while st <= en:
        mid = (st + en) // 2
        if nums[mid] >= target:
            ans = mid
            en = mid - 1
        else:
            st = mid + 1
    return ans


def search(target, nums):
    st, en = 0, 1
    pos = -1

    while True:
        mid = (st + en) // 2

        if nums[mid] == 1:
            pos = mid
            break

        elif nums[mid] < 1:
            st = en
            en *= 2

    # Calcualte Lower Bound
    bs(st, pos, nums, target)
