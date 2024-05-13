n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    a = input().split()
    if a[0] == '?':
        temp = arr[int(a[1])-1:int(a[2])]
        k = int(a[3])
        b = int(a[4])
        maximum = max(temp)
        print(min(maximum, k * (arr.index(maximum)+1) + b))
    else:
        temp = arr[int(a[1])-1:int(a[2])]
        x = int(a[3])
        arr[int(a[1])-1:int(a[2])] = list(map(lambda y: y + x, temp))