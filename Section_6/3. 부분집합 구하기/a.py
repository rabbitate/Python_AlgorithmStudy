# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성하세요.

import sys

# sys.stdin = open("in1.txt", 'r')

def DFS(v):
    # 숫자의 범위를 넘었을 경우
    if v == n+1:
        # 사용 처리된 숫자 출력
        for i in range(1,n+1):
            if ch_list[i] == 0:
                print(i, end=" ")
        print()
    else:
        ch_list[v] = 0 # 인덱스에 해당하는 숫자 사용 처리
        DFS(v+1) # v가 사용 처리된 부분집합
        ch_list[v] = -1 # 인덱스에 해당하는 숫자 미사용 처리
        DFS(v+1) # v가 미사용 처리된 부분집합

n = int(input())

ch_list = [-1] * (n+1) # 인덱스(숫자)가 포함되었는지 확인하는 상태 트리, value가 -1일때 미사용 상태

DFS(1)
