# https://www.codingninjas.com/studio/problems/count-with-k-different-characters_1214627 , Medium

# Brute
# T.C. -> O(n*n)
# S.C. -> O(n)


def check_Kdiffchar(s, k):
    st = set()

    for i in s:
        if i not in st:
            st.add(i)

        if len(st) > k:
            return False

    if len(st) == k:
        return True
    return False


def countSubStrings(s: str, k: int) -> int:
    c = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if check_Kdiffchar(s[i : j + 1], k):
                c += 1

    return c


# Better
# T.C. -> O(n*n)
# S.C. -> O(n)


def countSubStrings(s: str, k: int) -> int:
    c = 0
    for i in range(len(s)):
        st = set()
        for j in range(i, len(s)):
            st.add(s[j])
            if len(st) == k:
                c += 1
            elif len(st) > k:
                break
    return c
