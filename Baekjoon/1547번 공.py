# 3개의 컵 1,2,3
# n번 만큼 바꿈
# 1번컵 아래 공을 둔다.
# 바꾼 x,y값을 배열에 저장
# 원하는 공 몇번째 컵인지 값?

n = int(input())
c = [0,1,2,3]
for i in range(n):
    x, y = map(int, input().split())
    c[x],c[y] = c[y],c[x]
print(c.index(1))
