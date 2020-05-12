# 오름차순 정렬문제
N = int(input())
Nums = []
for n in range(0, N):
    Nums.append(int(input()))
Nums.sort()
for n in Nums:
    print(n)
# sort함수를 이용해 간단하게 풀었음! - 삽입,버블,선택은 너무많이 해봐서
# 가장 효율적으로 짜져있는 sort함수로 정렬을 함.
