# 풀이1
a,r,n = map(int, input().split())
for i in range(n-1):
    a = a*r
    print(a)

# 풀이2 등비수열 공식
a,r,n = map(int, input().split())
print(a*r**(n-1))