# 정수 a,b 붙인 수 + 정수 c,d 붙인 수 값?

# 1 내 풀이
# a,b,c,d 입력받고 문자열로 a,b / c,d 붙인 수 구함
# 구한값 더하기
a,b,c,d = map(int, input().split())
ans1,ans2 = str(a)+str(b), str(c)+str(d)
print(int(ans1)+int(ans2))

# 2 다른 사람 풀이
# 한개의 입력값만 주고, []를 이용해서 붙인 수 구함;;
n=input().split()
print(int(n[0]+n[1])+int(n[2]+n[3]))

# 리스트[]를 이용하면 문자열(str)처럼 이용 할 수 있다.
# [10]+[20], [30]+[40] -> 1020 + 3040 = 4060