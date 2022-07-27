# 여러 개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다. 
# 쇠막대기와 레 이저의 배치는 다음 조건을 만족한다.
# • 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
# • 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
# • 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
# 1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반 드시 레이저를 표현한다.
# 2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.
# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.

import sys

sys.stdin = open("in5.txt", 'r')

status = list(input()) # 쇠막대기와 레이저의 배치를 나타내는 괄호 표현

stack = [] # 
sum = 0 # 쇠막대기 총 개수

for i in status:
    if i == '(':
        stack.append(i)
        before = i # stack의 마지막 요소 저장
    else:
        stack.pop()
        # 레이저일 경우
        if before == '(':
            sum += len(stack) # 자른 쇠막대기 개수를 더해준다
        # 쇠막대기가 끝났을 경우
        else:
            sum += 1 # 자르고 남은 쇠막대기 하나를 더해준다
        before = i # stack의 마지막 요소 저장
        
print(sum)
