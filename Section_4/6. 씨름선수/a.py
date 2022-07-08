# 현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습 니다. 현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
# 현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
# “다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자 만 뽑기로 했습니다.”
# 만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니다.
# 첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력하세요.

import sys

sys.stdin = open("in5.txt", 'r')

n = int(input())

player = []

for _ in range(n):
    player.append(list(map(int, input().split())))

player.sort(key=lambda x:-x[0]) # 키 내림차순으로 정렬, player.sort(reverse=True)와 같다

cnt = 0 # 씨름 선수 인원

maxweight = 0 # 몸무게 최대값

for p in player:
    if p[1] > maxweight: # p 선수의 몸무게가 그 전 선수들 몸무게보다 많을 경우
        cnt += 1
        maxweight = p[1] # 몸무게 최대값 갱신

print(cnt)
