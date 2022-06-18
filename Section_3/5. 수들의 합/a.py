# N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다. 
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys

sys.stdin = open("in2.txt", 'r')

n,m = map(int, input().split())

a = list(map(int, input().split()))

sum = 0 # 수의 합
count = 0 # 경우의 수

for i in range(0,n):
    sum += a[i] 
    # i번째 수가 m일 경우
    if sum == m:
        count += 1
        sum = 0
    else:
        for j in range(m-a[i]):
            if i+j == n-1 or sum > m: break # 수의 합이 m보다 크거나 끝까지 돌았을 경우
            sum += a[i+j+1]
            if sum == m:
                count += 1
                sum = 0
                break
        sum = 0 # 수의 합 0으로 초기화

print(count)
