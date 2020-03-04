# 덩치 비교해 순위정하기
People = int(input())
ranks = []
datas = []
for n in range(0, People):
    datas.append(list(map(int, input().split())))
    ranks.append(1)

for n in range(0, People):
    rank = 1
    for it in range(0, People):
        if (it == n):
            continue
        if (datas[n][0] < datas[it][0] and datas[n][1] < datas[it][1]):
            rank += 1
    ranks[n] = rank

for n in range(0, People):
    print(ranks[n], end=" ")
# ranks를 5로 고정시키고 예제만 보고 풀었다... 그래서 삽질했다. 문제를 크게보는 연습을 하자...
