# 지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다. 
# DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지 되어야 한다. 
# 순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다.
# 즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야 한다. 
# 또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
# 지니레코드 입장에서는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에 이 사업에 낭비되는 DVD를 가급적 줄이려고 한다. 
# 고민 끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기로 하였다. 이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 
# 그리고 M개의 DVD는 모두 같은 크기여야 제조원가가 적게 들기 때문에 꼭 같은 크기로 해야 한다.

import sys

# DVD 1개의 용량을 입력 받아 만들 수 있는 DVD 개수를 리턴해주는 함수
def DVD(size):
    cnt = 1 # 마지막 DVD를 카운트하기 위해 1부터 시작
    sum = 0 # DVD 1개가 담는 용량

    for s in song:
        if sum+s <= size: # DVD에 담을 수 있다면
            sum += s
        else: # 1개가 꽉 찼을 때
            cnt += 1 # DVD 개수 증가
            sum = s # 못 담았던 곡의 길이는 새로운 DVD의 용량에 넣는다

    return cnt
    
sys.stdin = open("in5.txt", 'r')

n, m = map(int, input().split()) # 곡 수(n), 저장하려는 DVD 개수(m)

song = list(map(int, input().split())) # 곡 길이 리스트

lc = 1 # left cursor
rc = sum(song) # right cursor

res = 0 # DVD 최소 용량

while(lc<=rc):
    mid = (lc+rc)//2
    if DVD(mid) <= m:
        rc = mid-1
        res = mid
    else: lc = mid+1

print(res)
