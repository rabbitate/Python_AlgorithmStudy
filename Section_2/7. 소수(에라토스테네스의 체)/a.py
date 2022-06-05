# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초입니다.

import sys

# 1부터 n까지의 소수의 개수 리턴해주는 함수(재귀로 구현)

def Count_decimal(n):
    if n == 2: return 1 # 2일 경우 1 리턴(2는 소수)
    else:
        for i in range(2,n): # 소수인지 검증
            if n % i == 0: # 소수가 아니라면
                return Count_decimal(n-1) # 1을 더해주지 않고 재귀 호출
        else: return 1 + Count_decimal(n-1) # n이 소수라면 개수에 1을 더해주고 재귀 호출

# sys.stdin = open("in5.txt", 'r')

n = int(input())

print(Count_decimal(n))
