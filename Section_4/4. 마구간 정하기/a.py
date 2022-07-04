# N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마구간의 좌표가 중복되는 일은 없습니다.
# 현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 
# 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
# C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

import sys

# 말을 배치한 마구간 간격을 최소 interval만큼 떨어트릴 때 배치할 수 있는 말의 수를 리턴해주는 함수
def horse(interval):
    count = 1 # 첫 번째 마구간
    index = 0
    for i in range(1,n):
        if l[i] - l[index] >= interval: # 마구간 간격이 interval보다 크거나 같다면
            count += 1 # index번째 마구간에 말 배치
            index = i # 비교 마구간을 index번째로 설정
    return count

sys.stdin = open("in5.txt", 'r')

n, c = map(int, input().split()) # 마구간, 말의 수

l = [] # 마구간 좌표 리스트

for _ in range(n):
    l.append(int(input()))

lc = 1 # left cursor, 마구간의 좌표가 중복되는 일이 없으므로 간격은 최소 1
rc = max(l) - l[0] # right cursor, 최대 끝좌표-처음좌표

# 이분 탐색
while(lc<=rc):
    mid = (lc+rc)//2
    if horse(mid) >= c: # 간격이 mid일때 배치된 말의 수가 c보다 크거나 같을 때
        lc = mid+1
        res = mid
    else:
        rc = mid-1

print(res)
