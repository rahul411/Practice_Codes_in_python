def isSubsetSum(sumValue, n, arr):
    if sumValue == 0:
        return 1
    if sumValue != 0 and n < 0:
        return 0
    if arr[n] > sumValue:
        return isSubsetSum(sumValue, n - 1, arr)
    return isSubsetSum(sumValue, n - 1, arr) or isSubsetSum(
        sumValue - arr[n], n - 1, arr
    )


def isSubsetSumUsingDp(sumValue, n, arr):
    table = [[0 for i in range(3)] for j in range(sumValue + 1)]
    # print(table)
    for i in range(n + 1):
        for j in range(sumValue + 1):
            if j == 0:
                table[i % 2][j] = 1
            elif i == 0:
                table[i % 2][j] = 0
            elif arr[i - 1] > j:
                table[i % 2][j] = table[(i + 1) % 2][j]
            else:
                table[i % 2][j] = (
                    table[(i + 1) % 2][j] or table[(i + 1) % 2][j - arr[i - 1]]
                )
    return table[n % 2][sumValue]


a = [1, 1, 2]
print(isSubsetSum(2, 2, a))
print(isSubsetSumUsingDp(2, 3, a))
