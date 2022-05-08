# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 
# 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

import sys
sys.stdin = open("in1.txt", 'r')

test = int(input()) # Test Case 개수

for _ in range(test):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s-1:e] # s번째부터 e번째까지의 수를 넣은 리스트로 변환
    arr.sort() # 오름차순 정렬
    print(arr[k-1]) # k번째 수 출력
