# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 
# 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하여 프로그래밍 한다.

import sys

# 숫자를 뒤집어 반환해주는 함수
def reverse(x):
    m = 1 # 자릿수에 곱해주는 숫자
    rnum = 0 # x를 뒤집은 숫자
    for c in x:
        i = int(c)
        rnum += i * m
        m *= 10

    return rnum

# 소수인지 확인하는 함수
def isPrime(x):
    if x == 1: return False
    for i in range(2,x//2 + 1): # x의 절반만 확인하면 소수인지 확인할 수 있다
        if x % i == 0: # 소수가 아니면
            return False
    else: # 소수이면
        return True


sys.stdin = open("in5.txt", 'r')

n = int(input()) # 자연수의 개수
num = input().split() # n개의 자연수 리스트

for x in num:
    if isPrime(reverse(x)): # 뒤집은 자연수가 소수이면
        print(reverse(x), end=' ')
