# 1
# 정수 0, 1 의 갯수를 비교해 주어진 문장 출력
# 1이 입력 될 때마다 c값 증가로 0과 1의 갯수 비교
n = int(input())
c = 0
for i in range(n):
    if int(input()) == 1:
        c+=1
if c > n//2: print("Junhee is cute!")
else: print("Junhee is not cute!")


# 2
# 입력값을 리스트[]에 넣고 count 함수를 통해 0,1 의 갯수값 구함
# if문 비교로 주어진 문장 출력
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
ocount = a.count(1)
zcount = a.count(0)

if ocount > zcount: print("Junhee is cute!")
else: print("Junhee is not cute!")