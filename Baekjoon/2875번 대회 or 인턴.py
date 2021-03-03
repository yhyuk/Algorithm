# 팀 조건 woman 2명 + man 1명
# K명은 반드시 빠짐
# input : w, m, k 
# output : 최대 팀 개수

w, m, k = map(int, input().split())
t = 0
while w >= 2 and m >= 1 and w+m >= k+3:
    t+=1
    w-=2
    m-=1
print(t)