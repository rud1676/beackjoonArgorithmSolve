import math
import sys
N = int(input())

numSum = 0
average = 0
mode = 0
minNum = -5999
maxNum = -5999

modenum = 0
count = 0

Nums = [0 for i in range(8001)]
for n in range(N):
    Nums[int(sys.stdin.readline())+4000] += 1

for n in range(0, 8000):
    numcount = 0
    for i in range(0, Nums[n]):
        Rn = n-4000
        if (minNum == -5999):
            minNum = Rn
        if (maxNum < Rn):
            maxNum = Rn
        numSum += Rn
        count += 1
        numcount += 1
        if (count == (N + 1) / 2):
            average = Rn
    if (modenum < numcount):
        modenum = numcount

count = 0
for n in range(0, 8000):
    if Nums[n] == modenum:
        mode = n - 4000
        count += 1
    if (count == 2):
        break


print(round(numSum / N))
print(average)
print(mode)
print(maxNum - minNum)
