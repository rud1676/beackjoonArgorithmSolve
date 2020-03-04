# 체스판 문제
board1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
          "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
board2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
          "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", ]


def drawNum(board):
    b1, b2 = 0, 0
    for i in range(0, 8):
        for j in range(0, 8):
            if (board[i][j] != board1[i][j]):
                b1 += 1
            if (board[i][j] != board2[i][j]):
                b2 += 1
    return min([b1, b2])


N, M = list(map(int, input().split()))
checkboard = []
for i in range(0, N):
    checkboard.append(input())

answer = -1
for i in range(0, N - 7):
    for j in range(0, M - 7):
        b = [checkboard[n][j:j+8] for n in range(i, i+8)]
        if(answer < 0):
            answer = drawNum(b)
        elif(answer > drawNum(b)):
            answer = drawNum(b)

print(answer)
# 검사할 가상의 판을 만든다 bw , wb 그래서 8x8판을 뽑아와서 그것을 가상의 판과 비교해 그 횟수가 젤 적은걸 찾는다.
# 다른 풀이법을 보니 더해서 짝수면 b, 홀수면 w이런식으로 접근했음.
