# def func(n, m, arr):
#     dp = [0] * (n+1)
#     for i in range(n+1):
#         if arr[i-1] + sum(dp[:i]) < m:
#             dp[i] = arr[i-1]
#         else:
#             dp[i-1] = arr[i-1]
#     if m - sum(dp) > 0:
#         return m - sum(dp)
#     else:
#         return 0
n, m = map(int, input().split())
arr = list(map(int, input().split()))
# print(func(n, m, arr))
##################################################
result = []
for i in range(1,m+1):
    for j in arr:
        if i >= j:
            i = i - j
    result.append(i)
print(max(result))