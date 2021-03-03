# 주어진 입력값을 리스트[]에 append 하기.
# 홀수만 리스트에 저장.
# if~else 문으로 홀수, 짝수 출력값 출력.


ans = []
for a in range(7):
    a = int(input())
    if a % 2 != 0: ans.append(a)
if ans: print(sum(ans));print(min(ans))
else: print(-1)