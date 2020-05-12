# 블랙잭 게임
Ncard, limit = [int(x) for x in input("").split()]
cards = [int(x) for x in input().strip().split()]
answer = 0
for i in range(0, Ncard - 2):
    for j in range(i + 1, Ncard - 1):
        for k in range(j + 1, Ncard):
            if (cards[i] + cards[j] + cards[k] <= limit and cards[i] + cards[j] + cards[k] >= answer):
                answer = cards[i] + cards[j] + cards[k]

print(answer)
## 반복문을 이용하는게 부족했다.
## 3개의 수를 순회하는 것인데 for문 3개 중첩으로 for in 구문으로 천천히 했으면 됬을듯... 어쨋든 이 문제에선 3개의 순회하는 방식을 배움.