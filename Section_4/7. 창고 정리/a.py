import sys

sys.stdin = open("in5.txt", 'r')

l = int(input()) # 창고 가로 길이

boxes = list(map(int, input().split())) 

m = int(input()) # 높이 조정 횟수

# m번 만큼 창고 높이 조정
for _ in range(m):
    boxes.sort()
    boxes[0] += 1
    boxes[l-1] -= 1

boxes.sort()

print(boxes[l-1] - boxes[0]) # 가장 높은 곳과 가장 낮은 곳의 차이 출력
