# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요

import sys

# 회문 개수를 리턴해주는 함수
def count(l):
    sum = 0 # 회문 개수

    # 행 검사
    for i in range(7):
        for j in range(3):
            for k in range(2): # 5자리기 때문에 두 번의 회문 검사
                if l[i][j+k] != l[i][j+5-k-1]: break # 앞뒤가 다를 경우 break, l[::-1]과 비교하여 회문 검사도 가능
            else: # 반복문이 정상적으로 종료됐다면
                sum += 1 # 회문 개수 증가

    # 열 검사
    for i in range(7):
        for j in range(3):
            for k in range(2):
                if l[j+k][i] != l[j+5-k-1][i]: break # 앞뒤가 다를 경우 break
            else: 
                sum += 1
    
    return sum
        
sys.stdin = open("in5.txt", 'r')

l = [list(map(int, input().split())) for _ in range(7)]

print(count(l))
