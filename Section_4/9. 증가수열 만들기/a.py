# 1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
# 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열을 만듭니다. 
# 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니다.
# 예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
# 맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4, 왼쪽 끝에서 5를 가져와 
# 2 3 4 5 증가수열을 만들수있습니다.

import sys

# sys.stdin = open("in5.txt", 'r')

n = int(input())
num = list(map(int, input().split()))

start = 0 # start cursor
end = n-1 # end cursor
before = 0 # 비교되는 숫자

newNum = [] # 증가수열을 저장하는 리스트
s = "" # 방향 정보 문자열

tmp = [] # 숫자 삽입을 위한 임시 리스트

while start<=end:
    # start의 숫자가 수열의 마지막 숫자보다 클 경우
    if num[start] > before:
        tmp.append((num[start], 'L'))
    # end의 숫자가 수열의 마지막 숫자보다 클 경우
    if num[end] > before:
        tmp.append((num[start], 'R'))

    # tmp의 크기가 0일 경우 증가수열을 완성한 것
    if len(tmp) == 0: break

    tmp.sort() # 오름차순 정렬
    newNum.append(tmp[0][0]) # tmp에서 가장 작은 값을 증가수열에 추가
    s += tmp[0][1] # 방향 정보 문자열에 추가
    before = tmp[0][0] # 비교되는 숫자 갱신

    # 방향에 따른 커서 변경
    if tmp[0][1] == 'L': start += 1
    else: end -= 1
    
# while start<=end:
#     # start 와 end의 수가 before보다 작다면 증가수열 완성
#     if num[start] < before and num[end] < before:
#         break
#     # start의 수가 증가수열의 마지막 수보다 작다면
#     elif num[start] < before:
#         before = num[end] # end의 수를 비교대상으로 설정하고
#         newNum.append(before) # 증가수열에 end의 수를 추가
#         end -= 1
#         s += "R"
#     # end의 수가 증가수열의 마지막 수보다 작다면
#     elif num[end] < before:
#         before = num[start] # start의 수를 비교대상으로 설정하고
#         newNum.append(before) # 증가수열에 start의 수를 추가
#         start += 1
#         s += "L"
#     # start 와 end의 수가 before보다 크다면  
#     else:
#         if num[start] > num[end]:
#             before = num[end]
#             newNum.append(before)
#             end -= 1
#             s += "R"
#         else:
#             before = num[start]
#             newNum.append(before)
#             start += 1
#             s += "L" 

print(len(newNum))
print(s)
