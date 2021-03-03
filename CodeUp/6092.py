n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(24):
    ans.append(0)
for i in range(n):
    ans[a[i]] += 1
for i in range(1,24):
    print(ans[i],end=' ')
