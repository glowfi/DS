# NA , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(fruitsToPick)


def generateAllCombi(idx, tmp, arr, ans, fruitsToPick):
    if fruitsToPick == 0:
        return []
    if len(tmp) == fruitsToPick:
        ans.append(tmp[:])
        return

    for i in range(idx, len(arr)):
        # Remove Duplicates
        # if i > 0 and arr[i] == arr[i - 1]:
        #     continue
        tmp.append(arr[i])
        generateAllCombi(i + 1, tmp, arr, ans, fruitsToPick)
        tmp.pop(-1)


fruits = ["Apple", "Apple", "Pear"]
ans = []
for j in range(len(fruits) + 1):
    generateAllCombi(0, [], fruits, ans, j)
    print(f"Fruits To Pick : {j}   Result: {ans}")
    ans = []
    print()
