# www.acmicpc.net/problem/2522
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n = int(input())
for i in range(1,n+1):
    print(' ' * (n-i) + '*'*i)
for j in range(1,n):
    print(' ' * j + '*' * (n-j))
