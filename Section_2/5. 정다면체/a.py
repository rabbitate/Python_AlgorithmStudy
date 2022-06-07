# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

# 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

import sys
sys.stdin = open("in1.txt", 'r')

n, m = map(int, input().split())

cnt = [0] * (n + m + 1) # 주사위 수의 합 개수를 세주는 리스트, 눈의 합이 n+m 이상이 나올 수 없다

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j] += 1

max = 2 # 1+1

for index in range(len(cnt)):
    if max < cnt[index]:
        max = cnt[index] # 최대값 갱신

for index in range(len(cnt)):
    if cnt[index] == max:
        print(index, end=' ')
