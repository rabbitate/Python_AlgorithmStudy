# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

import sys

# 자릿수의 합을 리턴해주는 재귀 함수

def num_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + num_sum(n//10)

# 자릿수의 합이 최대인 자연수를 리턴해주는 함수

def digit_sum(num):
    max = num[0] # 최댓값을 리스트의 0번째 인덱스의 값으로 초기화

    for n in num:
        if num_sum(max) < num_sum(n): # 합이 최대인 자연수가 있다면
            max = n 

    return max

# sys.stdin = open("in1.txt", 'r')

n = int(input())
num = list(map(int, input().split()))

print(digit_sum(num))
