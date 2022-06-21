# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다.
# N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 
# 현수는 격자판안의 사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자 안의 사과는 새들을 위해서 남겨놓는다.
# 만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다.

import sys

sys.stdin = open("in2.txt", 'r')

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

total = 0 # 수확한 사과의 개수의 합

# n//2번째까지 
for i in range(n//2+1):
    total += l[i][n//2]
    for j in range(1,i+1):
        total += l[i][n//2-j] + l[i][n//2+j]

# n//2+1번째부터 n-1번째까지
for i in range(n//2+1,n):
    total += l[i][n//2]
    for j in range(1,n-i):
        total += l[i][n//2-j] + l[i][n//2+j]

print(total)
