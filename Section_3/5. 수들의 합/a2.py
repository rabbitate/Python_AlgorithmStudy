# N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다. 
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys

sys.stdin = open("in5.txt", 'r')

n,m = map(int, input().split())

a = list(map(int, input().split()))

l = 0 # left cursor
r = 1 # right cursor
count = 0 # 경우의 수
total = a[0] # 수의 합, 0번째 수로 초기화

while True:
    if total < m: # 수의 합이 m보다 작다면
        if r < n: 
            total += a[r] 
            r += 1
        else: break # 수의 합이 m보다 작고, r이 n과 같다면 경우를 다 살펴본 것
    elif total == m: # 수의 합이 m일 때
        count += 1 # 경우의 수 증가
        total -= a[l] # 수의 합에서 l번째 수를 빼준다
        l += 1 # left cursor 이동
    else:
        total -= a[l]
        l += 1 # left cursor 이동

print(count)
