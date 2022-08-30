# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용해서 출력해야 합니다.

import sys

sys.stdin = open("in5.txt", 'r')

n = int(input())

def Recursive(n):
    if n >= 2:
        Recursive(n//2)
        print(n%2, end="")
    else:
        print(n, end="")

Recursive(n)
