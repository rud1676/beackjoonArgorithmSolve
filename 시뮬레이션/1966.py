import copy
result = []
TestCase = int(input(""))

for i in range(TestCase):
    N, M = (int(i) for i in input("").split())
    nums = [int(i) for i in input().split()]
    comp = [0 for i in range(N)]
    comp[M] = 1  # 내가 볼 순서!
    count = 0
    while True:
        if (nums[0] == max(nums)):
            count += 1
            if (comp[0] == 1):
                print(count)
                break
            else:
                del nums[0]  # 필요없는 순서는 지워버리는 것!
                del comp[0]
        else:
            nums.append(nums[0])
            comp.append(comp[0])
            del nums[0]
            del comp[0]
# 입력된 리스트를 다시 저장해 중요도 순서로 저장한다 (comp 비교하기 위해 만듬)
# 원으로 순회하면서 높은 중요도 순서(comp)로 비교해 맞다면 count횟수를 넣어줌
# 11로 시작하는 이유는 중요도가 1~9까지라 겹치지 않게 하기위함 - 찾으면 count값으로 바꿔줌
# 그리고 쭉 순회해 모두 순서를 저장.

# 찝찝한것. 큐라는 것이 명시되어있어
# 그것을 이용해 pop을 이용해 데이터를 끝에넣고 하는 방식으로 했으면 좋았는데...
# 그래서 검색을 했더니 큐를 이용한 방법을 보았다. - 아이디어: 내가 검사할 순서만 봐도됨 나머진 저장할 필요가 없음!
# 배운것: max, 큐로 생각하는 방법..?
