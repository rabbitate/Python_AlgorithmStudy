# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.

import sys

sys.stdin = open("in5.txt", 'r')

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

# l = []

# for _ in range(n):
#     l.append(list(map(int, input().split())))

sum = 0
largest = 0

# 각 행의 합 추가
for i in range(n):
    sum = 0
    for j in range(n):
        sum += l[i][j]
    if largest < sum:
        largest = sum

# 각 열의 합 추가
for i in range(n):
    sum = 0
    for j in range(n):
        sum += l[j][i]
    if largest < sum:
        largest = sum

# 대각선의 합 1 
for i in range(n):
    sum += l[i][i]
    if largest < sum:
        largest = sum
    sum = 0

# 대각선의 합 2
for i in range(n):
    sum += l[i][n-i-1]
    if largest < sum:
        largest = sum
    sum = 0

print(largest)
