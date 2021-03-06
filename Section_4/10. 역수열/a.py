# 1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 
# 1부터 n까지 각각의 수 앞 에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.
# 예를 들어 다음과 같은 수열의 경우 4 8 6 2 5 1 3 7
# 1앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고
# 2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
# 3앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개
# 따라서 4 8 6 2 5 1 3 7의 역수열은 5 3 4 0 2 1 1 0이 된다.
# n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출력하는 프로그램을 작성하세요.

import sys

sys.stdin = open("in5.txt", 'r')

n = int(input())
reverse = list(map(int, input().split())) # 역순열
og = [-1 for _ in range(n)] # 원래 순열, 값이 들어 있었나 확인하기 위해 -1로 초기화

for i in range(n):
    cnt = 0 # 자신보다 큰 수의 개수
    for j in range(n):
        if cnt == reverse[i]: break
        if og[j] == -1: cnt += 1 # 값이 없다면 카운트를 증가시킨다
    # 자리를 찾았는데 값이 있다면, 인덱스를 하나씩 추가해가며 자리를 찾는다(이미 삽입된 숫자는 삽입할 숫자보다 작으므로 카운트가 안됨)
    while og[j] != -1:
        j += 1
    og[j] = i+1 # 자리에 i+1 삽입
        
print(og)
