# 5명의 참가자
# 각각 평가 점수 1~5점
# 평가 점수가 주어졌을 때 우승자와 그의 합 점수?

# 내 풀이 
# for문을 통해 하나씩 값 넣고 큰 값 출력
num = 0
asum = 0
for i in range(1,6):
    ssum = sum(list(map(int, input().split())))
    if ssum > asum:
        asum = ssum
        num = i
print(num,asum)

# 다른사람 풀이
# 리스트[]에 값 넣고 바로 출력ㄷㄷ
a = []
for i in range(5):
    a.append(sum(map(int, input().split())))
print(a.index(max(a))+1, max(a))