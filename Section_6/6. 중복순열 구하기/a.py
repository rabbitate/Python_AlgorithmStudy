# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력합니다.

import sys

def DFS(count):
    global n,m,total
    # 중복 순열이 완성 됐을 때
    if count == m:
        for i in p:
            print(i, end=" ")
        total += 1
        print()
    else:
        for i in range(1,n+1):
            p[count] = i
            # p.append(i)
            DFS(count+1)
            # p.pop()
    
sys.stdin = open("in5.txt", 'r')

n,m = map(int, input().split())

p = [0] * m # 중복 순열 리스트
total = 0 # 경우의 수

DFS(0)
print(total)
