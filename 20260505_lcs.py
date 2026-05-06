def longest_common_subsequence(str1, str2):
    n = len(str1)
    m = len(str2)

    # DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruction
    i = n
    j = m
    result = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            result.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    result.reverse()
    return dp[n][m], "".join(result)


# Example
#str1 = "abcde"
#str2 = "ace"
str1 = "abcde"
str2 = "eac"

length, sequence = longest_common_subsequence(str1, str2)

print("Length:", length)
print("LCS:", sequence)