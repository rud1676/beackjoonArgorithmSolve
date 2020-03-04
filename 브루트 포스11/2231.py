# 생성자를 구하는 문제
N = int(input())
answer = 0


def sum_digit(number):
    result = 0
    for i in str(number):
        result += int(i)
    return result


for n in range(N - 1, 1, -1):
    if (N == n + sum_digit(n)):
        answer = n

print(answer)
# 정답! 핵심은 입력된 수보다 작은값을 다 해봐야됨! 규칙이 없을 땐 다해보는게맞음!
