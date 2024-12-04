# NA , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


def longest_subarray_with_sum_less_than_k(arr: list[int], k: int) -> int:
    mx_len = 0

    for i in range(len(arr)):
        sm = 0
        for j in range(i, len(arr)):
            sm += arr[j]
            if sm <= k:
                mx_len = max(mx_len, j - i + 1)
            elif sm > k:
                break

    return mx_len


# Better
# T.C. - O(N+N)
# S.C  - O(1)


def longest_subarray_with_sum_less_than_k(arr: list[int], k: int) -> int:
    mx_len = 0

    l, r = 0, 0
    sm = 0

    while r < len(arr):
        sm += arr[r]

        while sm > k:  # Keep shrinking unitl condition holds
            sm -= arr[l]
            l += 1

        if sm <= k:  # if condition holds check mx_len
            mx_len = max(mx_len, sm)

        r += 1

    return mx_len


# Optimal [Maintain the max window size,dont go below the current window size , 2->3->4]
# T.C. - O(N)
# S.C  - O(1)


def longest_subarray_with_sum_less_than_k(arr: list[int], k: int) -> int:
    mx_len = 0

    l, r = 0, 0
    sm = 0

    while r < len(arr):
        sm += arr[r]

        if sm > k:  # Keep shrinking unitl condition holds
            sm -= arr[l]
            l += 1

        if sm <= k:  # if condition holds check mx_len
            mx_len = max(mx_len, sm)

        r += 1

    return mx_len
