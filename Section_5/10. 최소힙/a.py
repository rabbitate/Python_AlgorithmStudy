import sys
import heapq as hq

# sys.stdin = open("in1.txt", 'r')

h = [] # heap

while True:
    i = int(input())

    if i == -1:
        break
    elif i == 0:
        if len(h) == 0: print(-1) # 출력할 데이터가 없다면 -1 출력
        else: print(hq.heappop(h))
    else:
        hq.heappush(h,i)
