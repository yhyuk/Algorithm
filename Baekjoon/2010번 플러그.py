# 문제 읽고 이해가 안됬는데 질문에 있는 그림 보고 이해감....
# input : N개의 콘센트
# output : 최대로 연결 가능한 컴퓨터 수

import sys
n = int(sys.stdin.readline())
nsum = 0
for i in range(n):
    nsum += int(sys.stdin.readline())
print(nsum-n+1)