# 10개의 총 가격 주어짐
# 9개의 가격만 알 수 있음.
# 나머지 1개의 가격은?
a = int(input())
asum = []
for i in range(9): 
    i = int(input())
    asum.append(i)
print(a - sum(asum))
