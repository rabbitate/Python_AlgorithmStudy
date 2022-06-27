# 이분 탐색

import sys

sys.stdin = open("in2.txt", 'r')

n, m = map(int, input().split()) # 숫자의 개수 n, 찾고자 하는 수 m

nl = list(map(int, input().split()))
nl.sort() # 오름차순 정렬

l = 0 # left cursor
r = n-1 # right cursor

while(l<=r):
    mid = (l+r)//2
    if nl[mid] == m: 
        print(mid+1)
        break
    elif nl[mid] > m:
        r = mid-1
    else:
        l = mid+1
