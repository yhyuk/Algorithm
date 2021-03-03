# 1~9 까지 제곱수 중 마지막 자리 규칙 찾기
# 1 = 1 1 1 1
# 2 = 2 4 8 6
# 3 = 3 9 7 1
# 4 = 4 6 4 6
# 5 = 5 5 5 5
# 6 = 6 6 6 6
# 7 = 7 9 3 1
# 8 = 8 4 2 6
# 9 = 9 1 9 1
# 10 = 0 0 0 0

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6: #1,5,6은 다 똑같은 값 1,5,6
        print(a)
    elif a == 4 or a == 9: #4,9는 홀수는 자기자신, 짝수는 6과 1
        if b % 2 == 1: #홀수 일 때
            print(a)
        else:
            print((a * a) % 10)
    else: # 2,3,4,7은 4개씩 규칙 이므로 나머지 0 이라면 자기 출력
        if b % 4 == 0:
            print((a ** 4) % 10)
        else:
            print((a ** b) % 10)