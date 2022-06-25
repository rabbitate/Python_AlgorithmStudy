# 완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.

import sys

# 스도쿠를 정확하게 풀었는지 검사, 정확하면 True 아니라면 False 반환
def check(sudoku):
    # 각 3x3짜리 사각형에 중복없는지 확인
    for i in range(9):
        s = set(sudoku[i]) # 중복되는 수를 제거하는 set 특성을 활용하여
        if len(s) != 9: # set의 길이가 9가 아니라면
            return False

    # 각 행 1부터 9까지의 숫자 중복 검사
    for i in range(0,7,3):
        for j in range(0,7,3):
            ch = []
            for k in range(3):
                for l in range(3):
                    ch.append(sudoku[k+i][l+j])
            s = set(ch)
            if len(s) != 9: # set의 길이가 9가 아니라면
                return False

    # 각 열 1부터 9까지의 숫자 중복 검사
    for i in range(3):
        for j in range(3):
            ch = []
            for k in range(0,7,3):
                for l in range(0,7,3):
                    ch.append(sudoku[k+i][l+j])
            s = set(ch)
            if len(s) != 9: # set의 길이가 9가 아니라면
                return False
    
    return True
    
sys.stdin = open("in3.txt", 'r')

sudoku = [[] for _ in range(9)]
l = [0,1,2]

# 3x3의 정사각형을 리스트 하나로 입력하는 방식
for i in range(9):
    h = list(map(int, input().split()))
    if i == 3 or i == 6: 
        for i in range(3):
            l[i] += 3
    for j in range(9):
        if j % 9 < 3:
            sudoku[l[0]].append(h[j])
        elif 3 <= j % 9 < 6:
            sudoku[l[1]].append(h[j])
        else:
            sudoku[l[2]].append(h[j])

if check(sudoku):
    print("YES")
else:
    print("NO")
