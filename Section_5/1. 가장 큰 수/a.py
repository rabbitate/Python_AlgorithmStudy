# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다. 
# 단, 숫자의 순서는 유지해야 합니다
# 만약 5276823이 주어지고 3개의 자릿수를 제거한다면
# 7823이 가장 큰 숫자가 됩니다.

import sys

sys.stdin = open("in5.txt", 'r')

num, m = map(int, input().split()) # 숫자 num, 제거하려는 숫자 개수 m

num = list(map(int, str(num))) # 문자열로 변환 후, 문자 하나씩 int

s = [] # stack
cnt = 0 # pop한 횟수(제거한 횟수)

for i in num:
    while s and s[-1] < i and cnt < m:
        s.pop()
        cnt += 1
    s.append(i) # 스택이 비어있거나, 숫자를 제거할 수 있을 때 마지막 숫자보다 클 경우(더 큰 수를 만들 수 있을 경우)

# 비교를 다 했는데 아직 숫자를 다 제거하지 못한 경우
while cnt < m:
    s.pop()
    cnt += 1

for i in s:
    print(i,end="")
