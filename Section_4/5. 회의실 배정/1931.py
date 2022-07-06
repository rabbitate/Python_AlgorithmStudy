# https://www.acmicpc.net/problem/1931

n = int(input()) # 회의의 수

timetable = []

for _ in range(n):
    timetable.append(list(map(int, input().split())))

timetable.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간을 기준으로 우선 정렬, 후에 시작 시간으로 정렬(시작 시간과 끝나는 시간이 같을 경우를 고려함. ex) 7 7)

res = 0 # 회의 수
endtime = 0

for start,end in timetable:
    if endtime <= start: # 회의 시간이 겹치지 않는다면
        endtime = end
        res += 1
    
print(res)
