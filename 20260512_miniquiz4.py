# Write a program that finds the largest sum you can make using numbers from a list, 
# but you are not allowed to use two numbers that are next to each other.
# For example, given this list: [3, 2, 5, 10, 7] the largest sum would be 3 + 5 + 7 = 15

def solve(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for ii in range(2, len(nums)):
        # either:
        # 1. skip current number
        # 2. take current number + dp[i-2]
        dp[ii] = max(dp[ii-1], dp[ii-2] + nums[ii])
    return dp[-1]

print(solve([3]))
print(solve([3, 2]))
print(solve([3, 2, 5]))
print(solve([3, 2, 5, 10, 7]))      # 15
print(solve([3, 2, 5, 10, 7, 100])) # 113


# dp[n] : the maximum number that safisfy the requirement "you are not allowed to use two numbers that are next to each other" in index n:
#def solve(l):
#  n = len(l)
#  dp = [[0]*2 for _ in range(n+3)]
#  if n <= 2:
#    return max(l)
#
#  dp[0][1] = l[0]
#  dp[1][1] = max(dp[1][0]+l[1], dp[0][0])
#  dp[1][0] = max(dp[1][0], dp[0][1])
#
##  print(dp)
#  for ii in range(2, n):
#    # 2 types of transition
#    # use index ii
#    dp[ii][1] = max(dp[ii-1][0]+l[ii], dp[ii-2][1]+l[ii])
#    # not use index ii
#    dp[ii][0] = max(dp[ii-1][1], dp[ii-1][0])
#
#  ans = max(dp[n-1])
##  print(dp)
#  return ans
#
#print(solve([3]))
#print(solve([3, 2]))
#print(solve([3, 2, 5]))
#print(solve([3, 2, 5, 10, 7]))
#print(solve([3, 2, 5, 10, 7, 100]))

