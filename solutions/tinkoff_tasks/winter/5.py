n, m, q = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
for i in range(m):
    first, second = map(int, input().split())
    if first in d:
        d[first].append(second)
    else:
        d[first] = [second]
    if second in d:
        d[second].append(first)
    else:
        d[second] = [first]

for i in range(q):
    a = input().split()
    if a[0] == '?':
        print(arr[int(a[1])-1])
    else:
        temp = d[int(a[1])]
        for j in range(len(temp)):
            arr[temp[j]-1] += int(a[2])