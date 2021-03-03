# 풀이1
n = int(input())
print(min(map(int,input().split())))

# 풀이2
n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(n):
  if a[i] < ans:
    ans = a[i]
print(ans)