# 가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 그리고 둘째 줄부터 차례대로 파스칼 의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다. 
# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성하시오. 
# 단, 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.

import sys

sys.stdin = open("in5.txt", 'r')

def DFS(v):
    global n, f
    # 순열이 완성되었을 때
    if v == n:
        sum = 0
        # 순열과 이항계수를 곱하면 파스칼 삼각형 덧셈이 된다
        for i in range(n):
            sum += p[i]*c[i]
        if sum == f:
            for i in p:
              print(i, end=" ")
            sys.exit()
    else:
        for i in range(1,n+1):
            if i in p: continue
            p.append(i)
            DFS(v+1)
            p.pop()

n, f = map(int, input().split())

p = [] # 순열 리스트
c = [1] * n # 이항계수 리스트

# 이항계수 설정
for i in range(1,n):
    c[i] = c[i-1] * (n-i) // i

DFS(0)
