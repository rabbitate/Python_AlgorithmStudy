# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.

import sys

def DFS(count):
    global n,m, cnt
    # 구슬을 다 뽑았다면
    if count == m:
        for i in p:
            print(i, end=" ")
        print()
        cnt += 1
        return
    else:
        for i in range(1,n+1):
            if i in p: continue # 순열이기 때문에 중복을 허용하지 않는다
            p.append(i) # 순열에 i 추가
            DFS(count+1)
            p.pop()


sys.stdin = open("in5.txt", 'r')

n,m = map(int, input().split())
p = []
cnt = 0 # 경우의 수

DFS(0)
print(cnt)
