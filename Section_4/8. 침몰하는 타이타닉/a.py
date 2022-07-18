# 유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고 있습니다. 
# 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있으며, 
# 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
# N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.

import sys

sys.stdin = open("in1.txt", 'r')

n, m = map(int, input().split()) # 승객의 수 n, 보트 하나 무게제한 m

weight = list(map(int, input().split())) # 승객 몸무게 리스트, 50 이상 150 이하

weight.sort(reverse=True) # 내림차순 정렬

start = 0 # start cursor
end = n-1 # end cursor
cnt = 0 # 구명 보트 최소 개수

while start <= end:
    # 가장 무거운 사람과 가장 가벼운 사람을 태웠을 때 가능하다면
    if weight[start] + weight[end] <= m:
        end -= 1
    cnt += 1 # 보트에 태우고
    start += 1 # 다음으로 무거운 사람과 비교

print(cnt)
