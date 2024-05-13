t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print('Yes')
    else:
        if (n - 1) * 2 == sum(a):
            print('Yes')
        else:
            print('No')