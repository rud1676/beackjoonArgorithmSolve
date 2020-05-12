# 종말번호 찾기
N = int(input())
count = 0
num = 0
while 1:
    num += 1
    if (str(num).count("666")):
        count += 1
    if (count == N):
        break

print(num)
