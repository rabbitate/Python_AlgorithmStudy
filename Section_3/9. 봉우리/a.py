# 지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
# 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요. 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
# 만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

import sys

sys.stdin = open("in1.txt", 'r')

n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

cnt = 0 # 봉우리 개수

# 봉우리 계산 편의를 위해 가장자리에 0 추가
for i in range(n+2):
    # 첫 번째 행과 마지막 행에 0 추가
    if i == 0 or i == n+1:
        l.insert(i, [0 for _ in range(n+2)])
    else: # 처음과 끝에 0 추가
        l[i].insert(0,0)
        l[i].insert(n+1,0)

for i in range(1,n+1):
    for j in range(1,n+1):
        # 봉우리일 경우
        if l[i][j] > l[i-1][j] and l[i][j] > l[i][j-1] and l[i][j] > l[i][j+1] and l[i][j] > l[i+1][j]:
            cnt += 1

print(cnt)
