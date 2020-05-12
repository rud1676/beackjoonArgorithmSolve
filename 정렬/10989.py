# 카운팅 정렬로 빠르게 정렬하기
import sys
N = int(input())
counts = [0 for i in range(10001)]
for n in range(0, N):
    counts[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(0, counts[i]):
        print(i)

"""sys.stdin.readline() << 한줄읽어오는 함수인데...
이게 input()보다 빠르다고 한다 시간이 민감한 문제이면 써먹어야할듯
"""
