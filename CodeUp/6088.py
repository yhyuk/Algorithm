# 풀이1
a,d,n = map(int, input().split())
for i in range(n-1):
    a+=d
print(a)

# 풀이2
a,d,n = map(int, input().split())
print(a+d*(n-1))
