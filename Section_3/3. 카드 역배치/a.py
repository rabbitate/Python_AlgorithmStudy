# 1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓 여있다. 
# 각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.
# 다음과 같은 규칙으로 카드의 위치를 바꾼다: 구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
# 총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다.

import sys

sys.stdin = open("in4.txt", 'r')

list = list(range(21)) # 편의를 위해 인덱스에 인덱스 숫자로 초기화 [0,1,2,3,...,18,19,20]

for _ in range(10):
    a,b = map(int, input().split())
    dif = b - a
    if dif % 2 == 0: # 구간의 카드 개수가 홀수일 때, 구간의 차는 짝수
        for i in range(dif,0,-2):
            list[a], list[a+i] = list[a+i], list[a]
            a += 1
    else: # 구간의 카드 개수가 짝수일 때, 구간의 차는 홀수
        for i in range(dif,-1,-2):
            list[a], list[a+i] = list[a+i], list[a]
            a += 1

list.remove(0) # 처음에 편의를 위해 넣어줬던 0 제거
print(list)
