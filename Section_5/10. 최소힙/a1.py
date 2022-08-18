import sys
import heapq as hq

sys.stdin = open("in1.txt")

h = []

while True:
    i = int(input())

    if i == -1:
        break
    elif i == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(-hq.heappop(h)) # 최대 힙 구현을 위해 pop할 때, 음수 값을 양수로 만들어준다
    else:
        hq.heappush(h, -i) # 최대 힙 구현을 위해 push할 때, 양수 값을 음수로 바꿔준다
