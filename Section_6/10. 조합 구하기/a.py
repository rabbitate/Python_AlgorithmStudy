# 1부터 N까지 번호가 적힌 구슬이 있습니다.이 중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.

import sys

def DFS(num,v):
    global n, m, res
    if v == m:
        res += 1
        for c in l:
            print(c, end=" ")
        print()
    else:
        for i in range(num+1,n+1):
            l[v] = i
            DFS(i,v+1)

        
sys.stdin = open("in1.txt", 'r')

n,m = map(int,input().split())

l = [0] * m # 조합 리스트

res = 0 # 조합의 수

DFS(0,0)

print(res)
