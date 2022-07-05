# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들려고 한다. 
# 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 
# 단, 회의는 한번 시작하면 중간에 중 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

import sys

sys.stdin = open("in1.txt", 'r')

n = int(input())

timetable = []

for _ in range(n):
    timetable.append(list(map(int,input().split())))

timetable.sort(key=lambda x:x[1]) # 끝나는 시간을 기준으로 정렬

cnt = 0 # 회의 수
endtime = 0 # 현재 회의의 종료시간

for start,end in timetable:
    if endtime <= start: # 회의 시간이 겹치지 않는다면
        endtime = end 
        cnt += 1

print(cnt)
