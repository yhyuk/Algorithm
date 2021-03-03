# 여러개의 입력 테스트
# 배수, 약수, 아닌 것 총 3가지 출력
# 마지막에는 0 0 이 주어짐

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')