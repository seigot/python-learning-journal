
memo = {}
def fibonacci_memo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]

print(fibonacci_memo(1)) # 1
print(fibonacci_memo(2)) # 1
print(fibonacci_memo(3)) # 2
print(fibonacci_memo(4)) # 3
print(fibonacci_memo(5)) # 5
print(fibonacci_memo(6)) # 8
print(fibonacci_memo(7)) # 13
print(fibonacci_memo(8)) # 21
print(fibonacci_memo(9)) # 34
print(fibonacci_memo(10)) # 55

print("---")
memo = {}
def fibonacci_tabulation(n):
#    memo = [0] * n
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(fibonacci_tabulation(1)) # 1
print(fibonacci_tabulation(2)) # 1
print(fibonacci_tabulation(3)) # 2
print(fibonacci_tabulation(4)) # 3
print(fibonacci_tabulation(5)) # 5
print(fibonacci_tabulation(6)) # 8
print(fibonacci_tabulation(7)) # 13
print(fibonacci_tabulation(8)) # 21
print(fibonacci_tabulation(9)) # 34
print(fibonacci_tabulation(10)) # 55

