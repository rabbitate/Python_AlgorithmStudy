# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.

import sys

sys.stdin = open("in1.txt", 'r')

n = int(input()) # 첫 번째 리스트 크기
a = list(map(int, input().split()))
m = int(input()) # 두 번째 리스트 크기
b = list(map(int, input().split()))

# a = a+b
# a.sort()

# print(a)

# 정렬이 되어있기 때문에 nlog(n)의 sort() 방식보다 n인 방식을 활용한다

sum = [] # 합 리스트

aindex, bindex = 0, 0 # a,b 리스트의 인덱스 변수

while aindex < n and bindex < m: # a 혹은 b 리스트의 끝까지
    if a[aindex] > b[bindex]:
        sum.append(b[bindex])
        bindex += 1
    elif a[aindex] <= b[bindex]:
        sum.append(a[aindex])
        aindex += 1

# 다 옮기지 못한 리스트도 옮겨준다

while aindex != n:
    sum.append(a[aindex])
    aindex += 1

while bindex != m:
    sum.append(b[bindex])
    bindex += 1

print(sum)
